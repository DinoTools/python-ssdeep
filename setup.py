#!/usr/bin/env python
import glob
import os
import re
import stat
import subprocess
import sys

from distutils.command import build_ext
from setuptools import Extension, setup

VERSION = re.search("__version__\s*=\s*\"(.*)\"", open('ssdeep.pyx').read(), re.M).group(1)

if sys.version_info[0] == 3:
    CYTHON_OPTS = "-3 -f"
else:
    CYTHON_OPTS = "-2 -f"

ssdeep_extension = Extension(
    include_dirs=["ssdeep"],
    name="ssdeep",
    sources=["ssdeep.c"]
)

class BuildExtension(build_ext.build_ext):
    def build_extension(self, ext):
        self.compile_cython()
        self.build_ssdeep()
        return build_ext.build_ext.build_extension(self, ext)

    def build_ssdeep(self):
        if len(get_objects()) == 0:
            try:
                os.chmod(
                    "ssdeep/configure",
                    stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO
                )
            except:
                pass

            returncode = subprocess.call(
                "(cd ssdeep && ./configure && make)",
                shell=True
            )
            if returncode != 0:
                sys.exit("Failed while running ./configure and make")

        ssdeep_extension.extra_objects = get_objects()
        if len(ssdeep_extension.extra_objects) == 0:
            sys.exit("Can't build ssdeep. No objects found.")

    def compile_cython(self):
        returncode = subprocess.call(
            "cython %s ssdeep.pyx" % CYTHON_OPTS,
            shell=True
        )
        if returncode != 0:
            sys.exit("Error running cython")


def get_objects():
    objects = glob.glob("ssdeep/.libs/*.o")
    if len(objects) > 0:
        return objects
    return glob.glob("ssdeep/.libs/*.obj")


ssdeep_extension.extra_objects = get_objects()

def read(name):
    return open(
        os.path.join(
            os.path.dirname(__file__),
            name
        )
    ).read()

if __name__ == "__main__":
    setup(
        author="Philipp Seidel",
        author_email="",
        classifiers=[
            "Topic :: Software Development :: Libraries :: Python Modules",
            "Intended Audience :: Developers",
            "Development Status :: 4 - Beta"
        ],
        cmdclass={
            "build_ext": BuildExtension
        },
        description="Python wrapper for the ssdeep library",
        long_description=read("README.rst"),
        ext_modules=[ssdeep_extension],
        name="ssdeep",
        url="http://github.com/DinoTools/python-ssdeep",
        version=VERSION
    )
