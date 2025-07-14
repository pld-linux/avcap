Summary:	Cross-platform, API-independent C++ video capture library 
Summary(pl.UTF-8):	Wieloplatformowa, niezależna od API biblioteka C++ do przechwytywania obrazu
Name:		avcap
Version:	0.1.9
Release:	1
License:	GPL v3+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libavcap/%{name}-%{version}.tar.gz
# Source0-md5:	7e7ba375c68ab37b984b91ae23d0f164
Patch0:		%{name}-v4l2.patch
Patch1:		%{name}-c++.patch
Patch2:		%{name}-install.patch
URL:		http://libavcap.sourceforge.net/
BuildRequires:	autoconf >= 2.56
BuildRequires:	automake
BuildRequires:	libavc1394-devel
BuildRequires:	libdv-devel
BuildRequires:	libiec61883-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The avcap-library (avcap: a video capture library) is a cross-API,
cross-platform simple and easy to use C++ video capture library. Its
aim is to provide a unified API for Linux, Windows and Mac OS X to
capture video from appropriate hardware. It hides the system specific
quirks and issues of different API's used on different systems to
access video capture hardware and hopefully helps to write portable
capture-applications.

%description -l pl.UTF-8
Biblioteka avcap (biblioteka do przechwytywania obrazu) to
wieloplatformowa, niezależna od lokalnego API, łatwa w użyciu
biblioteka C++ do przechwytywania obrazu. Jej celem jest zapewnienie
jednolitego API dla Linuksa, Windows i Mac OS X, służącego do
przechwytywania obrazu z odpowiedniego sprzętu. Ukrywa zależne od
systemu szczegóły związane z różnymi API służącymi do dostępu do
urządzeń przechwytywania obrazu i ułatwia pisanie przenośnych
aplikacji.

%package devel
Summary:	Header files for avcap library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki avcap
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libavc1394-devel
Requires:	libdv-devel
Requires:	libiec61883-devel
Requires:	libstdc++-devel

%description devel
Header files for avcap library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki avcap.

%package static
Summary:	Static avcap library
Summary(pl.UTF-8):	Statyczna biblioteka avcap
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static avcap library.

%description static -l pl.UTF-8
Statyczna biblioteka avcap.

%package apidocs
Summary:	avcap API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki avcap
Group:		Documentation

%description apidocs
avcap API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki avcap.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

# keep AX_PREFIX_CONFIG_H, kill libtool macros
head -n 87 acinclude.m4 > acinclude.m4.tmp
%{__mv} acinclude.m4.tmp acinclude.m4

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# .la kept, *.private dependencies are missing in .pc

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/captest
%attr(755,root,root) %{_libdir}/libavcap.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libavcap.so.6

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libavcap.so
%{_libdir}/libavcap.la
%{_includedir}/avcap
%{_pkgconfigdir}/avcap.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libavcap.a

%files apidocs
%defattr(644,root,root,755)
%doc doc/html/*
