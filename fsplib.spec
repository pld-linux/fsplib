#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	fsp library
Summary(pl.UTF-8):	Biblioteka fsp
Name:		fsplib
Version:	0.11
Release:	1
License:	BSD-like (see COPYING)
Group:		Libraries
Source0:	http://downloads.sourceforge.net/fsp/%{name}-%{version}.tar.gz
# Source0-md5:	f2f4809159d331baada8135d3977563c
Patch0:		%{name}-scons.patch
URL:		http://fsp.sourceforge.net/fsplib.html
BuildRequires:	scons
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is C library which support talking with FSP server using FSP v2
protocol and provides POSIX-like file manipulation interface.

For more information about FSP protocol see
<http://fsp.sourceforge.net/>.

For library and API info see <http://fsp.sourceforge.net/fsplib.html>.

%description -l pl.UTF-8
To jest biblioteka napisana w C, która obsługuje "rozmowę" z serwerem
FSP przy użyciu wersji 2 protokołu i dostarcza interfejsu operacji na
plikach podobnego do POSIX.

Więcej informacji o protokole FSP można znaleźć na
<http://fsp.sourceforge.net/>.

Informacje o bibliotece i API znajdują się na
<http://fsp.sourceforge.net/fsplib.html>.

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
%setup -q -c
%patch0 -p1

%build
%scons \
	CCFLAGS="%{rpmcflags}" \
	enable-shared=yes

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}}

# we know scons is great :/
install libfsplib.so.0.0.0 $RPM_BUILD_ROOT%{_libdir}
ln -sf libfsplib.so.0.0.0 $RPM_BUILD_ROOT%{_libdir}/libfsplib.so.0
ln -sf libfsplib.so.0.0.0 $RPM_BUILD_ROOT%{_libdir}/libfsplib.so
cp -a libfsplib.a $RPM_BUILD_ROOT%{_libdir}
cp -a fsplib.h $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%attr(755,root,root) %{_libdir}/libfsplib.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libfsplib.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfsplib.so
%{_includedir}/fsplib.h

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libfsplib.a
%endif
