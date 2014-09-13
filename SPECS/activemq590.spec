Name: activemq
Version: 5.9.0
Release: HT.1.0.2
Summary: Open source software implementation of JMS/AMQP Broker.
Group: Productivity/Networking/Web/Servers
License: Apache Software License.
Url: http://activemq.apache.org
Source: apache-activemq-5.9.0-bin.tar.gz
Source1: wrapper-linux-x86-64-3.5.24.tar.gz 
BuildRoot: %{_tmppath}/%{name}-%{version}-build
BuildArch: x86_64


%description
Open source software implementation of JMS/AMQP Broker, repackaged to facilitate configuration/deployment.


%prep
%setup -c
%setup -T -D -a 1 

%install
echo RPM_SOURCE_DIR is $RPM_SOURCE_DIR 


echo "======> activemq basics"
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/opt/activemq/lib
mkdir -p $RPM_BUILD_ROOT/opt/activemq/webapps
mkdir -p $RPM_BUILD_ROOT/opt/activemq/bin
mkdir -p $RPM_BUILD_ROOT/opt/activemq/bin/linux-x86-64
mkdir -p $RPM_BUILD_ROOT/opt/activemq/data
mkdir -p $RPM_BUILD_ROOT/opt/activemq/conf
mkdir -p $RPM_BUILD_ROOT/opt/activemq/tmp

rsync -av apache-activemq-5.9.0/lib/ $RPM_BUILD_ROOT/opt/activemq/lib/
rsync -av apache-activemq-5.9.0/webapps/ $RPM_BUILD_ROOT/opt/activemq/webapps/

rsync -av apache-activemq-5.9.0/bin/activemq $RPM_BUILD_ROOT/opt/activemq/bin/activemq
rsync -av apache-activemq-5.9.0/bin/activemq.jar $RPM_BUILD_ROOT/opt/activemq/bin/activemq.jar
rsync -av apache-activemq-5.9.0/bin/activemq-admin $RPM_BUILD_ROOT/opt/activemq/bin/activemq-admin
rsync -av apache-activemq-5.9.0/bin/diag $RPM_BUILD_ROOT/opt/activemq/bin/diag
rsync -av apache-activemq-5.9.0/bin/linux-x86-64/activemq $RPM_BUILD_ROOT/opt/activemq/bin/linux-x86-64/activemq

rsync -av \
--exclude activemq.xml \
--exclude credentials.properties \
--exclude jmx.password \
--exclude jetty-realm.properties \
--exclude users.properties \
apache-activemq-5.9.0/conf/ $RPM_BUILD_ROOT/opt/activemq/conf/

# security setup 
rsync -av $RPM_SOURCE_DIR/conf/credentials.properties $RPM_BUILD_ROOT/opt/activemq/conf/credentials.properties
rsync -av $RPM_SOURCE_DIR/conf/jmx.password $RPM_BUILD_ROOT/opt/activemq/conf/jmx.password
rsync -av $RPM_SOURCE_DIR/conf/jetty-realm.properties $RPM_BUILD_ROOT/opt/activemq/conf/jetty-realm.properties
rsync -av $RPM_SOURCE_DIR/conf/users.properties $RPM_BUILD_ROOT/opt/activemq/conf/users.properties


# activemq wrapper
mkdir -p $RPM_BUILD_ROOT/opt/activemq/bin
mkdir -p $RPM_BUILD_ROOT/etc/init.d

rsync -av wrapper-linux-x86-64-3.5.24/lib/libwrapper.so $RPM_BUILD_ROOT/opt/activemq/bin/linux-x86-64/libwrapper.so
rsync -av wrapper-linux-x86-64-3.5.24/bin/wrapper $RPM_BUILD_ROOT/opt/activemq/bin/linux-x86-64/wrapper
rsync -av wrapper-linux-x86-64-3.5.24/lib/wrapper.jar $RPM_BUILD_ROOT/opt/activemq/bin/wrapper.jar
rsync -av $RPM_SOURCE_DIR/init.d/ht-activemq $RPM_BUILD_ROOT/etc/init.d/ht-activemq


%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(0755,root,root)
/opt/activemq/bin/activemq
/opt/activemq/bin/activemq-admin
/opt/activemq/bin/activemq.jar
/opt/activemq/bin/diag
/opt/activemq/lib
/opt/activemq/webapps

%defattr(0644,root,root)
/opt/activemq/data
/opt/activemq/tmp

%defattr(0600,root,root)
%config /opt/activemq/conf

%defattr(0555,root,root)
/opt/activemq/bin/wrapper.jar
/opt/activemq/bin/linux-x86-64/libwrapper.so
/opt/activemq/bin/linux-x86-64/wrapper

%defattr(0755,root,root)
/opt/activemq/bin/linux-x86-64/activemq
/etc/init.d/ht-activemq


%changelog
