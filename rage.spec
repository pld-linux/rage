Summary:	Rage - media center based on EFL
Summary(pl.UTF-8):	Rage - centrum multimedialne oparte na EFL
Name:		rage
Version:	0.3.0.042
Release:	1
License:	BSD
Group:		X11/Applications/Multimedia
Source0:	http://download.enlightenment.org/snapshots/2008-01-25/%{name}-%{version}.tar.bz2
# Source0-md5:	123bab800a7be6e0c7c8dc6beb8c6368
URL:		http://enlightenment.org/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1.6
# ecore-con ecore-evas ecore-file ecore-ipc ecore-job ecore-txt
BuildRequires:	ecore-devel
BuildRequires:	edje
BuildRequires:	edje-devel
BuildRequires:	eet-devel
BuildRequires:	emotion-devel
BuildRequires:	evas-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rage is a media center designed mostly for use on a television hooked
up to your PC via a remote control.

%description -l pl.UTF-8
Rage to centrum multimedialne zaprojektowane głównie do używania na
telewizorze podłączonym do komputera przy użyciu pilota.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING COPYING-PLAIN README TODO
%attr(755,root,root) %{_bindir}/rage
%attr(755,root,root) %{_bindir}/raged
%attr(755,root,root) %{_bindir}/rage_thumb
%{_datadir}/rage
