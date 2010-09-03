__version__ = '2.5'
__all__  = ['Error', 'hash', 'hash_from_file', 'compare']

cdef extern from "fuzzy.h":
    ctypedef unsigned int uint32_t

    int fuzzy_hash_buf(unsigned char *buf, uint32_t buf_len, char *result)
    int fuzzy_hash_filename(char * filename, char* result)
    int fuzzy_compare(char *sig1, char *sig2)

# this are copied from fuzzy.h
DEF SPAMSUM_LENGTH = 64
DEF FUZZY_MAX_RESULT = 116

class Error(Exception):
    pass


def hash(object string):
    """This function computes the fuzzy hash of the buffer 'buf' and returns the result as a string."""
    cdef char result[FUZZY_MAX_RESULT]
    cdef int ret = fuzzy_hash_buf(<unsigned char*?>string, len(string), result)
    if ret == 0:
        return str(result)
    else:
        raise Error('fuzzy_hash_buf failed with code %r' % ret)


def hash_from_file(char* filename):
    """This function computes the fuzzy hash of the file and returns the result as a string."""
    cdef char result[FUZZY_MAX_RESULT]
    cdef int ret = fuzzy_hash_filename(filename, result)
    if ret == 0:
        return str(result)
    else:
        raise Error('fuzzy_hash_filename failed with code %r' % ret)


def compare(char* sig1, char* sig2):
    """This function returns a value from 0 to 100 indicating the match 
       score of the two signatures. A match score of zero indicates the
       sigantures did not match."""
    return fuzzy_compare(sig1, sig2)

