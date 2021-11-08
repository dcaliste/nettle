Name:           nettle
Version:        3.7.3
Release:        1
Summary:        A low-level cryptographic library

License:        LGPLv3+ or GPLv2+
URL:            http://www.lysator.liu.se/~nisse/nettle/
Source0:        http://www.lysator.liu.se/~nisse/archive/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  gmp-devel, m4
BuildRequires:	libtool, automake, autoconf, gettext-devel

%package devel
Summary:        Development headers for a low-level cryptographic library
Requires:       %{name} = %{version}-%{release}
Requires:       gmp-devel

%description
Nettle is a cryptographic library that is designed to fit easily in more
or less any context: In crypto toolkits for object-oriented languages
(C++, Python, Pike, ...), in applications like LSH or GNUPG, or even in
kernel space.

%description devel
Nettle is a cryptographic library that is designed to fit easily in more
or less any context: In crypto toolkits for object-oriented languages
(C++, Python, Pike, ...), in applications like LSH or GNUPG, or even in
kernel space.  This package contains the files needed for developing 
applications with nettle.


%prep
%setup -q -n %{name}-%{version}/upstream

%build
autoreconf -ifv
%configure --disable-static --enable-fat --disable-documentation
%make_build

%install

%make_install
make install-shared DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
rm -f $RPM_BUILD_ROOT%{_bindir}/nettle-lfib-stream
rm -f $RPM_BUILD_ROOT%{_bindir}/pkcs1-conv
rm -f $RPM_BUILD_ROOT%{_bindir}/sexp-conv
rm -f $RPM_BUILD_ROOT%{_bindir}/nettle-hash
rm -f $RPM_BUILD_ROOT%{_bindir}/nettle-pbkdf2

chmod 0755 $RPM_BUILD_ROOT%{_libdir}/libnettle.so.*.*
chmod 0755 $RPM_BUILD_ROOT%{_libdir}/libhogweed.so.*.*

%files
%doc AUTHORS NEWS README
%license COPYINGv2 COPYING.LESSERv3
%{_libdir}/libnettle.so.*
%{_libdir}/libhogweed.so.*

%files devel
%{_includedir}/nettle
%{_libdir}/libnettle.so
%{_libdir}/libhogweed.so
%{_libdir}/pkgconfig/hogweed.pc
%{_libdir}/pkgconfig/nettle.pc
