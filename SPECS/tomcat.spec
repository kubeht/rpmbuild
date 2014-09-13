Name: apache-tomcat
Version: 7.0.50
Release: HT
Summary: Open source software implementation of the Java Servlet and JavaServer Pages technologies.
Group: Productivity/Networking/Web/Servers
License: Apache Software License.
Url: http://tomcat.apache.org
Source: %{name}-%{version}.tar.gz
Requires: jdk
BuildRoot: %{_tmppath}/%{name}-%{version}-build
BuildArch: x86_64

%description
Apache Tomcat is an open source software implementation of the Java Servlet and JavaServer Pages technologies. The Java Servlet and JavaServer Pages specifications are developed under the Java Community Process.

%prep
%setup -c

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/tomcat
rsync -av . $RPM_BUILD_ROOT/usr/local/tomcat

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(0755,root,root)
/usr/local/tomcat

%changelog
- Inital add, check git log for updates
