#!/usr/bin/env python
import sys
import os
import glob
import re
from os.path import join, dirname

if sys.argv[1:] == ['test']:
    import doctest
    doctest.testfile('README.rst')
    sys.exit()

try:
    from setuptools import Extension, setup
except ImportError:
    from distutils.core import Extension, setup
from distutils.command import build_ext

VERSION = re.search("__version__\s*=\s*'(.*)'", open('ssdeep.pyx').read(), re.M).group(1)
assert VERSION
SOURCE = 'ssdeep.pyx'

class my_build_ext(build_ext.build_ext):

    def compile_cython(self):
        if os.path.exists('ssdeep.c'):
            c_mtime = os.stat('ssdeep.c').st_mtime
            source_mtime = os.stat(SOURCE).st_mtime
            if source_mtime - c_mtime < 1:
                return
        print >> sys.stderr, 'Running cython'
        cython_result = os.system('cython ssdeep.pyx')
        if cython_result:
            if os.system('cython -V 2> %s' % os.devnull):
                # there's no cython in the system
                print >> sys.stderr, 'No cython found, cannot rebuild ssdeep.c'
                return
            sys.exit(1)

    def make_ssdeep(self):
        if not get_objects():
            result = os.system('cd ssdeep && ./configure && make')
            if result:
                sys.exit(result)
        SSDEEP_EXT.extra_objects = get_objects()
        if not SSDEEP_EXT.extra_objects:
            sys.exit('failed to build ssdeep')

    def build_extension(self, ext):
        self.compile_cython()
        self.make_ssdeep()
        return build_ext.build_ext.build_extension(self, ext)

SSDEEP_EXT = Extension(name='ssdeep',
                       sources=['ssdeep.c'],
                       include_dirs=['ssdeep'])

def get_objects():
    objects = set(glob.glob('ssdeep/*.o')) - set(['ssdeep/main.o'])
    if not objects:
        objects = set(glob.glob('ssdeep/*.obj')) - set(['ssdeep/main.obj'])
    return objects

SSDEEP_EXT.extra_objects = get_objects()

def read(name):
    return open(join(dirname(__file__), name)).read()

if __name__ == '__main__':
    setup(
        name='ssdeep',
        version=VERSION,
        description='Python wrapper for ssdeep library',
        long_description=read('README.rst'),
        author='Denis Bilenko',
        author_email='denis.bilenko@gmail.com',
        url='http://bitbucket.org/denis/ssdeep',
        ext_modules=[SSDEEP_EXT],
        cmdclass={'build_ext': my_build_ext},
        classifiers=[
        "License :: OSI Approved :: GPLv2",
        "Programming Language :: Python",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Intended Audience :: Developers",
        "Development Status :: 4 - Beta"])
