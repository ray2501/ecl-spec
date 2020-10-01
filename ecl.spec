#
# spec file for package ecl
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%global major 20
%global minor 4
%global revision 24

Name:           ecl
Version:        %{major}.%{minor}.%{revision}
Release:        0
Summary:        Embeddable Common-Lisp
License:        LGPL-2.1+
Group:          Development/Languages/Other
Url:            https://common-lisp.net/project/%{name}/
Source:         %{name}-%{version}.tgz
BuildRequires:	m4
BuildRequires:	gmp-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
ECL (Embeddable Common-Lisp) is an interpreter of the Common-Lisp language as
described in the X3J13 Ansi specification, featuring CLOS (Common-Lisp Object
System), conditions, loops, etc, plus a translator to C, which can produce
standalone executables.

ECL supports the operating systems Linux, FreeBSD, NetBSD, OpenBSD, OS X,
Solaris and Windows, running on top of the Intel, Sparc, Alpha, PowerPC and ARM
processors.

%package -n lib%{name}%{major}_%{minor}
Group:			System/Libraries
Summary:		Embeddable Common-Lisp -- shared library

%description -n lib%{name}%{major}_%{minor}
This package contains the ECL shared library.

%package devel
Group:			Development/Libraries/C and C++
Summary:		Embeddable Common-Lisp -- development files
Requires:		lib%{name}%{major}_%{minor} == %{version}
Requires:		gmp-devel

%description devel
ECL (Embeddable Common-Lisp) is an interpreter of the Common-Lisp language as
described in the X3J13 Ansi specification, featuring CLOS (Common-Lisp Object
System), conditions, loops, etc, plus a translator to C, which can produce
standalone executables.

ECL supports the operating systems Linux, FreeBSD, NetBSD, OpenBSD, OS X,
Solaris and Windows, running on top of the Intel, Sparc, Alpha, PowerPC and ARM
processors.

This package contains development files for ECL.

%prep
%setup -q -n %{name}-%{version}

%build
%configure
make %{?_smp_mflags}

%install
%make_install
%{__rm} -f %{buildroot}%{_libdir}/%{name}-%{version}/*.a
%{__rm} -f %{buildroot}%{_infodir}/dir

%post -n lib%{name}%{major}_%{minor} -p /sbin/ldconfig
%postun -n lib%{name}%{major}_%{minor} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_libdir}/%{name}-%{version}/
%{_mandir}/man1/*
%doc README.md CHANGELOG
%license COPYING

%files -n lib%{name}%{major}_%{minor}
%{_libdir}/lib%{name}.so.%{version}

%files devel
%defattr(-,root,root)
%{_bindir}/%{name}-config
%{_libdir}/lib%{name}.so
%{_libdir}/lib%{name}.so.%{major}
%{_libdir}/lib%{name}.so.%{major}.%{minor}
%{_includedir}/%{name}/

%changelog

