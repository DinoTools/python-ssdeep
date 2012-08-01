"""
A wrapper for the ssdeep lib to generate fuzzy hashes.
"""
__version__ = "2.9-0.1"
__all__  = ["Error", "compare", "hash", "hash_from_file"]

import sys

cdef extern from "fuzzy.h":
    ctypedef unsigned int uint32_t

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
    pass

if sys.version_info.major == 2:
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
    if sys.version_info.major == 3:
        if type(buf) == str:
            buf = buf.encode("utf-8")

    cdef char result[FUZZY_MAX_RESULT]
    cdef int ret = fuzzy_hash_buf(<unsigned char*?>buf, len(buf), result)
    if ret != 0:
        raise Error("fuzzy_hash_buf failed with code %d" % ret)

    if sys.version_info.major == 2:
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
    if sys.version_info.major == 3:
        if type(filename) == str:
            filename = filename.encode("utf-8")

    cdef char result[FUZZY_MAX_RESULT]
    cdef int ret = fuzzy_hash_filename(filename, result)
    if ret != 0:
        raise Error("fuzzy_hash_buf failed with code %d" % ret)

    if sys.version_info.major == 2:
        return str(result)
    else:
        return result.decode("UTF-8")
