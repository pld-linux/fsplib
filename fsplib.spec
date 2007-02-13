#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	fsp library
Summary(pl.UTF-8):	Biblioteka fsp
Name:		fsplib
Version:	0.8
Release:	1
License:	BSD-like (see COPYING)
Group:		Libraries
Source0:	http://dl.sourceforge.net/fsp/%{name}-%{version}.tar.gz
# Source0-md5:	3e629fb06c22b029c7ec07e0d7cc7def
URL:		http://fsp.sourceforge.net/fsplib.html
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is C library which support talking with FSP server using FSP v2
protocol and provides POSIX-like file manipulation interface.

For more information about FSP protocol see
<http://fsp.sourceforge.net/>.

For library and API info see http://fsp.sourceforge.net/fsplib.html .

%description -l pl.UTF-8
To jest biblioteka napisana w C, która obsługuje "rozmowę" z serwerem
FSP przy użyciu wersji 2 protokołu i dostarcza interfejsu operacji na
plikach podobnego do POSIX.

Więcej informacji o protokole FSP można znaleźć na
<http://fsp.sourceforge.net/>.

Informacje o bibliotece i API znajdują się na
http://fsp.sourceforge.net/fsplib.html .

%package devel
Summary:	Header files for FSP library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki FSP
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for FSP library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki FSP.

%package static
Summary:	Static FSP library
Summary(pl.UTF-8):	Statyczna biblioteka FSP
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static FSP library.

%description static -l pl.UTF-8
Statyczna biblioteka FSP.

%prep
%setup -c -q

%build
autoreconf -i
%{__libtoolize}
%{__autoconf}
%{__automake}
%configure \
	--enable-shared \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%endif
