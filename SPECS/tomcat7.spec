Name: tomcat7
Version: 7.0.50
Release: HT.%{date}
Summary: Open source software implementation of the Java Servlet and JavaServer Pages technologies.
Group: Productivity/Networking/Web/Servers
License: Apache Software License.
Url: http://tomcat.apache.org
Source: apache-tomcat-7.0.50.tar.gz
Requires: jdk
BuildRoot: %{_tmppath}/%{name}-%{version}-build
BuildArch: x86_64

%description
Apache Tomcat is an open source software implementation of the Java Servlet and JavaServer Pages technologies. The Java Servlet and JavaServer Pages specifications are developed under the Java Community Process.

%prep
%setup -c

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/tomcat7
mkdir -p $RPM_BUILD_ROOT/etc/init.d/
rsync -av apache-tomcat-7.0.50/ $RPM_BUILD_ROOT/usr/local/tomcat7/
cp $RPM_SOURCE_DIR/init/tomcat7 $RPM_BUILD_ROOT/etc/init.d

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(0755,tomcat,tomcat)
/usr/local/tomcat7
/etc/init.d/tomcat7

%post
chown -R tomcat.tomcat /usr/local/tomcat7

%changelog
