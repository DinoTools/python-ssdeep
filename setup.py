#!/usr/bin/env python
import os
from distutils.command.build import build
from setuptools import setup, find_packages
from setuptools.command.install import install

base_dir = os.path.dirname(__file__)


class CFFIBuild(build):
    def finalize_options(self):
        self.distribution.ext_modules = get_ext_modules()
        build.finalize_options(self)


class CFFIInstall(install):
    def finalize_options(self):
        self.distribution.ext_modules = get_ext_modules()
        install.finalize_options(self)


def get_ext_modules():
    import ssdeep
    ext_modules = [
        ssdeep.ffi.verifier.get_extension()
    ]
    return ext_modules

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

# ToDo: build and include ssdeep lib?
# import glob
# import os
# import subprocess
#
# def build_ssdeep():
#     try:
#         os.chmod(
#             "ssdeep/configure",
#             stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO
#         )
#     except:
#         pass
#
#     returncode = subprocess.call(
#         "(cd ssdeep && ./configure && make)",
#         shell=True
#     )
#     if returncode != 0:
#         sys.exit("Failed while running ./configure and make")
#
# def get_objects():
#     objects = glob.glob("ssdeep/.libs/*.o")
#     if len(objects) > 0:
#         return objects
#     return glob.glob("ssdeep/.libs/*.obj")
