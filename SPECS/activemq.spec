Name: activemq
Version: 5.9.1
Release: HT
Summary: Open source software implementation of AMQP Broker.
Group: Productivity/Networking/Web/Servers
License: Apache Software License.
Url: http://activemq.apache.org
Source: apache-activemq-5.9.1-bin.tar.gz
Requires: jdk
BuildRoot: %{_tmppath}/%{name}-%{version}-build
BuildArch: x86_64

%description
Apache Tomcat is an open source software implementation of the Java Servlet and JavaServer Pages technologies. The Java Servlet and JavaServer Pages specifications are developed under the Java Community Process.

%prep
%setup -c

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/activemq
rsync -av apache-activemq-5.9.1/ $RPM_BUILD_ROOT/usr/local/activemq/

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(0755,root,root)
/usr/local/activemq

%changelog
- Inital add, check git log for updates
