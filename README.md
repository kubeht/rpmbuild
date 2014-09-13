rpmbuild
========


# Prerequisites
- rpmbuild binary must be installed.  A vagrant file is included which has rpmbuild for Mac and Windows users.

# Usage
## Start the VM
```
vagrant up
```

## install rpmbuild if VM is just created
```
sudo yum install rpm-build
```

## Building a RPM
- Clone this repo.

- Running the make command will show you which RPMs are available to build

```
[vagrant@rpmbuild data]$ make
Probable Targets:

tomcat7
```

- Build a RPM

```
[vagrant@rpmbuild data]$ make tomcat7
...
...
Checking for unpackaged file(s): /usr/lib/rpm/check-files /data/BUILDROOT/apache-tomcat-7.0.50-HT.x86_64
Wrote: /data/RPMS/x86_64/apache-tomcat-7.0.50-HT.x86_64.rpm
Executing(%clean): /bin/sh -e /var/tmp/rpm-tmp.I6MifL
+ umask 022
+ cd /data/BUILD
+ cd apache-tomcat-7.0.50
```

## Add a source and spec to be built
Let's say we're building a package called blah.

- Put 'blah.spec' file in 'SPECS'

- Put the source in 'SOURCES/blah' 

- Run 'make blah'

 
