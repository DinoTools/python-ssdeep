Build Instructions for Centos
=============================

- Download source tar.gz from github and copy it to rpmbuild/SOURCES directory
- Copy python-ssdeep.spec to your rpmbuild/SPEC directory
- Build using ```rpmbuild -bb python-ssdeep.spec```
- .rpm should be created in architecture specific rpmbuild/RPMS/ subdirectory
- Install running ```rpm -i python-ssdeep-*.rpm```

