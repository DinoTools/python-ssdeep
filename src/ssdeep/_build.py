from typing import Dict, List, Tuple

import cffi


cdef: str = """
    static const long FUZZY_FLAG_ELIMSEQ;
    static const long FUZZY_FLAG_NOTRUNC;
    static const long FUZZY_MAX_RESULT;

    struct fuzzy_state;
    struct fuzzy_state *fuzzy_new(void);

    struct fuzzy_state *fuzzy_clone(
        const struct fuzzy_state *
    );

    int fuzzy_update(
        struct fuzzy_state *,
        const unsigned char *,
        size_t
    );

    int fuzzy_digest(
        const struct fuzzy_state *,
        char *,
        unsigned int
    );
    void fuzzy_free(struct fuzzy_state *);

    int fuzzy_hash_buf(
        const unsigned char *,
        uint32_t,
        char *
    );

    int fuzzy_hash_file(
        FILE *,
        char *
    );

    int fuzzy_hash_stream(
        FILE *,
        char *
    );

    int fuzzy_hash_filename(
        const char *,
        char *
    );

    int fuzzy_compare(
        const char *,
        const char *
    );

    static const long ssdeep_HAS_STATEFUL_HASHING;
"""

source: str = """
    #include "fuzzy.h"

    #ifndef FUZZY_FLAG_ELIMSEQ
    static const long ssdeep_HAS_STATEFUL_HASHING = 0;

    struct fuzzy_state {};
    const long FUZZY_FLAG_ELIMSEQ = 0;
    const long FUZZY_FLAG_NOTRUNC = 0;
    int (*fuzzy_clone)(const struct fuzzy_state *) = NULL;
    int (*fuzzy_digest)(
        const struct fuzzy_state *,
        char *,
        unsigned int
    ) = NULL;
    int (*fuzzy_free)(struct fuzzy_state *) = NULL;
    int (*fuzzy_new)(void) = NULL;
    int (*fuzzy_update)(
        struct fuzzy_state *,
        const unsigned char *,
        size_t
    ) = NULL;

    int (*fuzzy_hash_stream)(
        FILE *,
        char *
    ) = NULL;

    #else

    static const long ssdeep_HAS_STATEFUL_HASHING = 1;

    #endif
"""

CONDITIONAL_NAMES: Dict[str, Tuple] = {
    "ssdeep_HAS_STATEFUL_HASHING": (
        "FUZZY_FLAG_ELIMSEQ",
        "FUZZY_FLAG_NOTRUNC",
        "fuzzy_clone",
        "fuzzy_digest",
        "fuzzy_free",
        "fuzzy_new",
        "fuzzy_update",
        "fuzzy_hash_stream"
    )
}

libraries: List[str] = ["fuzzy"]

ffi: cffi.FFI = cffi.FFI()
ffi.set_source(
    "ssdeep._libfuzzy",
    source,
    libraries=libraries,
)
ffi.cdef(cdef)


if __name__ == '__main__':
    ffi.compile()
