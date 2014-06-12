#!/usr/bin/env python
import glob
import os
import stat
import subprocess
import sys
from distutils.command.build import build
from setuptools import setup, find_packages
from setuptools.command.install import install

base_dir = os.path.dirname(__file__)
use_system_lib = True
if os.environ.get("BUILD_LIB") == "1":
    use_system_lib = False


class CFFIBuild(build):
    def finalize_options(self):
        self.distribution.ext_modules = get_ext_modules()
        build.finalize_options(self)


class CFFIInstall(install):
    def finalize_options(self):
        self.distribution.ext_modules = get_ext_modules()
        install.finalize_options(self)


def build_ssdeep():
    try:
        os.chmod(
            "ssdeep-lib/configure",
            stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO
        )
    except:
        pass

    returncode = subprocess.call(
        "(cd ssdeep-lib && ./configure && make)",
        shell=True
    )
    if returncode == 0:
        return

    print("Failed while building ssdeep lib with configure and make.")
    print("Retry with autoreconf ...")

    returncode = subprocess.call(
        "(cd ssdeep-lib && autoreconf --force && ./configure && make)",
        shell=True
    )
    if returncode != 0:
        sys.exit("Failed while building ssdeep lib.")


def get_ext_modules():
    from ssdeep.binding import Binding
    if use_system_lib:
        binding = Binding()
    else:
        build_ssdeep()
        binding = Binding(
            extra_objects=get_objects(),
            include_dirs=["./ssdeep-lib/"],
            libraries=[]
        )
    binding.verify()
    ext_modules = [
        binding.ffi.verifier.get_extension()
    ]
    return ext_modules


def get_objects():
    objects = glob.glob("ssdeep-lib/.libs/*.o")
    if len(objects) > 0:
        return objects
    return glob.glob("ssdeep-lib/.libs/*.obj")

about = {}
with open(os.path.join(base_dir, "ssdeep", "__about__.py")) as f:
    exec(f.read(), about)

with open(os.path.join(base_dir, "README.rst")) as f:
    long_description = f.read()

setup(
    name=about["__title__"],
    version=about["__version__"],

    description=about["__summary__"],
    long_description=long_description,
    license=about["__license__"],
    url=about["__uri__"],

    zip_safe=False,
    author=about["__author__"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=[
        # ToDo: set min version
        "cffi",
        "six >= 1.4.1"
    ],
    setup_requires=[
        # ToDo: set min version
        "cffi",
        "six >= 1.4.1"
    ],
    packages=find_packages(exclude=["*.tests", "*.tests.*"]),
    include_package_data=True,
    cmdclass={
        "build": CFFIBuild,
        "install": CFFIInstall,
    },
    ext_package="ssdeep",
)
