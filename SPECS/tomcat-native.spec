#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

%define tcnver 1
%define aprver 1

Summary: Tomcat Native Java library
Name: tomcat-native
Version: 1.1.29
Release: 1
License: Apache Software License
Group: System Environment/Libraries
URL: http://apr.apache.org/
Source0: %{name}-%{version}-src.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildPrereq: autoconf, libtool, doxygen, apr-devel >= 0:{version}-{release}, openssl >= 0.9.7

%description
The mission of the Tomcat Native Library (TCN) is to provide a
free library of C data structures and routines.  This library
contains additional utility interfaces for Java.

%package devel
Group: Development/Libraries
Summary: Tomcat Native development kit
Requires: tcnative = %{version}-%{release}, apr-devel >= 0:{version}-{release}, openssl-devel >= 0.9.7

%description devel
The mission of the Tomcat Native Library (TCN) is to provide a
free library of C data structures and routines.  This library
contains additional utility interfaces for Java.

%prep
%setup -q

%build
%configure --with-apr=%{_prefix} \
        --includedir=%{_includedir}/apr-%{aprver} \
        --with-java-home=/usr/java/jdk1.7.0_51 \
        --prefix=/usr/local/tomcat7

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# Unpackaged files
rm -f $RPM_BUILD_ROOT%{_libdir}/tcnative.exp

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/libtcnative-%{tcnver}.so.*
%{_libdir}/libtcnative-%{tcnver}.*a
%{_libdir}/libtcnative-%{tcnver}.so

%files devel
%defattr(-,root,root,-)
%{_libdir}/libtcnative-%{tcnver}.*a
%{_libdir}/libtcnative-%{tcnver}.so
%{_libdir}/pkgconfig/tcnative-%{tcnver}.pc



%changelog
                                                                                
