Summary:	fsp library
Summary(pl):	biblioteka fsp
Name:		fsplib
Version:	0.6
Release:	1
License:	see COPYING
Group:		Libraries
Source0:	http://dl.sourceforge.net/fsp/%{name}-%{version}.tar.gz
# Source0-md5:	18f837120b5a185840dd16555728dc30
URL:		http://fsp.sourceforge.net/fsplib.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is C library which support talking with FSP server using FSP v2 protocol
and provides posix-like file manipulation interface.

For more information about FSP protocol see http://fsp.sourceforge.net/
For library and API info see http://fsp.sourceforge.net/fsplib.html

%description -l pl
To jest biblioteka napisana w C, która obs³uguje "rozmowê" z serwerem FSP
u¿ywaj±c wersji 2 protoko³u i dostarcza zgodnego z POSIX interfejsu.

Wiêcej informacji o protokole FSP znajdziesz na http://fsp.sourceforge.net/.
Informacje o bibliotece i API znajduj± siê na
http://fsp.sourceforge.net/fsplib.html.

%package devel
Summary:	Header files for FSP library
Summary(pl):	Pliki nag³ówkowe biblioteki FSP
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for FSP library.

%description devel -l pl
Pliki nag³ówkowe biblioteki FSP.

%package static
Summary:	Static FSP library
Summary(pl):	Statyczna biblioteka FSP
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static FSP library.

%description static -l pl
Statyczna biblioteka FSP.

%prep
%setup -c -q

%build
autoreconf -i
%{__libtoolize}
%{__autoconf}
%{__automake}
%configure \
	--enable-shared
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

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
