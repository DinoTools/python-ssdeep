"""
A wrapper for the ssdeep lib to generate fuzzy hashes.
"""
__version__ = "2.9-0.3"
__all__  = ["Error", "Hash", "compare", "hash", "hash_from_file"]

cimport libc.errno
import errno
import os
import sys

cdef extern from "fuzzy.h":
    struct fuzzy_state
    cdef enum:
        FUZZY_FLAG_ELIMSEQ
        FUZZY_FLAG_NOTRUNC
        FUZZY_MAX_RESULT
    ctypedef unsigned int uint32_t

    cdef extern fuzzy_state *fuzzy_new() nogil
    cdef extern int fuzzy_update(fuzzy_state *, unsigned char *, size_t) nogil
    cdef extern int fuzzy_digest(fuzzy_state *, char *, unsigned int flags) nogil
    cdef extern void fuzzy_free(fuzzy_state *) nogil
    int fuzzy_compare(char *sig1, char *sig2)
    int fuzzy_hash_buf(unsigned char *buf, uint32_t buf_len, char *result)
    int fuzzy_hash_filename(char * filename, char* result)

# from fuzzy.h
#/// The longest possible length for a fuzzy hash signature (without the filename)
##define FUZZY_MAX_RESULT    (SPAMSUM_LENGTH + (SPAMSUM_LENGTH/2 + 20))
#/// Length of an individual fuzzy hash signature component
##define SPAMSUM_LENGTH 64

DEF FUZZY_MAX_RESULT = 116

class Error(Exception):
    def __init__(self, errno=None):
        self.errno = errno

    def __str__(self):
        return "Error: %s" % os.strerror(self.errno)

    def __repr__(self):
        try:
            return "Error(errno.%s)" % errno.errorcode[self.errno]
        except KeyError:
            return "Error(%d)" % self.errno

cdef class Hash:
    cdef fuzzy_state *state

    def __cinit__(self):
        self.state = fuzzy_new()
        if self.state == NULL:
            raise Error(libc.errno.errno)

    def update(self, object buff):
        if sys.version_info[0] == 3:
            if type(buff) == str:
                buff = buff.encode("utf-8")

        if self.state == NULL:
            raise Error(libc.errno.EINVAL)
        if fuzzy_update(self.state, buff, len(buff)) != 0:
            fuzzy_free(self.state)
            self.state = NULL
            raise Error(libc.errno.errno)

    def digest(self, elimseq=False, notrunc=False):
        if self.state == NULL:
            raise Error(libc.errno.EINVAL)
        cdef char result[FUZZY_MAX_RESULT]
        flags = (FUZZY_FLAG_ELIMSEQ if elimseq else 0) | \
                (FUZZY_FLAG_NOTRUNC if notrunc else 0)
        if fuzzy_digest(self.state, result, flags) != 0:
            raise Error(libc.errno.errno)

        if sys.version_info[0] == 2:
            return str(result)
        return result.decode("UTF-8")

    def __dealloc__(self):
        if self.state != NULL:
            fuzzy_free(self.state)

if sys.version_info[0] == 2:
    def compare(char* sig1, char* sig2):
        """
        Compute the match score between two fuzzy hash signatures.

        :param Str sig1: The fist signature
        :param Str sig2: The second signature
        :return: A value from 0 to 100.
        """
        return fuzzy_compare(sig1, sig2)

else:
    def compare(unicode hash1, unicode hash2):
        """
        Compute the match score between two fuzzy hash signatures.

        :param Str sig1: The fist signature
        :param Str sig2: The second signature
        :return: A value from 0 to 100.
        """
        cdef bytes sig1 = hash1.encode("UTF-8")
        cdef bytes sig2 = hash2.encode("UTF-8")

        return fuzzy_compare(sig1, sig2)

def hash(object buf):
    """
    Compute the fuzzy hash of a buffer. Returns the hash as string.

    :param Bytes buf: The data to be fuzzy hashed
    :return: The fuzzy hash as string
    """
    if sys.version_info[0] == 3:
        if type(buf) == str:
            buf = buf.encode("utf-8")

    cdef char result[FUZZY_MAX_RESULT]
    cdef int ret = fuzzy_hash_buf(<unsigned char*?>buf, len(buf), result)
    if ret != 0:
        raise Error("fuzzy_hash_buf failed with code %d" % ret)

    if sys.version_info[0] == 2:
        return str(result)
    else:
        return result.decode("UTF-8")


def hash_from_file(object filename):
    """
    Hashes the content of the file with the given name 'filename' and returns it
    as string.

    :param Str filename: Name of the file to be hashed
    :return: The fuzzy hash of the file content
    """
    if sys.version_info[0] == 3:
        if type(filename) == str:
            filename = filename.encode("utf-8")

    cdef char result[FUZZY_MAX_RESULT]
    cdef int ret = fuzzy_hash_filename(filename, result)
    if ret != 0:
        raise Error("fuzzy_hash_buf failed with code %d" % ret)

    if sys.version_info[0] == 2:
        return str(result)
    else:
        return result.decode("UTF-8")
