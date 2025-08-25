Summary:	Rage - media center based on EFL
Summary(pl.UTF-8):	Rage - centrum multimedialne oparte na EFL
Name:		rage
Version:	0.4.0
Release:	1
License:	BSD
Group:		X11/Applications/Multimedia
Source0:	https://download.enlightenment.org/rel/apps/rage/%{name}-%{version}.tar.xz
# Source0-md5:	e2fed81e9e3ef604cdb685d6822348e5
URL:		https://www.enlightenment.org/about-rage
BuildRequires:	efl-devel
BuildRequires:	meson
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 2.042
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
%meson

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README TODO
%attr(755,root,root) %{_bindir}/rage
%dir %{_libdir}/rage
%dir %{_libdir}/rage/utils
%attr(755,root,root) %{_libdir}/rage/utils/rage_thumb
%{_datadir}/rage
%{_desktopdir}/rage.desktop
%{_iconsdir}/hicolor/*x*/apps/rage.png
