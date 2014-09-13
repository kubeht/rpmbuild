Name: activemqconfig
Version: 5.9.0 
Release: HT.1.0.5
Summary: Open source software implementation of AMQP/JMS Broker.
Group: Productivity/Networking/Web/Servers
License: GPLv2.
Requires: activemq 
Source0:   %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-build
BuildArch: x86_64

%description
Configuration for activemq590


%prep
%setup -cT


%install
echo RPM_SOURCE_DIR is $RPM_SOURCE_DIR 
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/opt/activemq/conf/
mkdir -p $RPM_BUILD_ROOT/opt/activemq/bin/linux-x86-64

# beoker configuration
rsync -av $RPM_SOURCE_DIR/conf/activemq.xml.tmpl.v3 $RPM_BUILD_ROOT/opt/activemq/conf/activemq.xml
rsync -av $RPM_SOURCE_DIR/linux-x86-64/wrapper.conf $RPM_BUILD_ROOT/opt/activemq/bin/linux-x86-64/wrapper.conf

%clean 
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

################### package for default ################
%package default
Summary: Package containing default configurtion
Group: Productivity/Networking/Web/Servers

%description default 
Package containing default configurtion 

%files default
%defattr(0600,root,root)
%config /opt/activemq/conf/activemq.xml

%defattr(0755,root,root)
%config /opt/activemq/bin/linux-x86-64/wrapper.conf

%post default

################### package for hsa ################
%package hsa
Summary: Package containing hsa configurtion
Group: Productivity/Networking/Web/Servers

%description hsa 
Package containing hsa configurtion 
Group: Productivity/Networking/Web/Servers

%files hsa
%defattr(0600,root,root)
%config /opt/activemq/conf/activemq.xml

%defattr(0755,root,root)
%config /opt/activemq/bin/linux-x86-64/wrapper.conf

%post hsa
perl -p -i -e 's/((-DmulticastUri)=(.+))/"$2=multicast:\/\/default\?group=hsa"/ge' /opt/activemq/bin/linux-x86-64/wrapper.conf


%changelog
