Name: tomcat7-UTF8conf 
Version: 7.0.50
Release: HT
Summary: Open source software implementation of the Java Servlet and JavaServer Pages technologies.
Group: Productivity/Networking/Web/Servers
License: Apache Software License.
Source0:   %{name}-%{version}.tar.gz
Requires: tomcat7
BuildRoot: %{_tmppath}/%{name}-%{version}-build
BuildArch: x86_64

%description
Replacement for server.xml containing UTF8 URIEncoding

%prep
%setup -cT

%install
echo RPM_SOURCE_DIR is $RPM_SOURCE_DIR
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/tomcat7/conf

# encoding configuration
rsync -av $RPM_SOURCE_DIR/conf/server.xml $RPM_BUILD_ROOT/usr/local/tomcat7/conf/server.xml

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files 
%defattr(0755,root,root)
%config /usr/local/tomcat7/conf/server.xml

%post

%changelog

