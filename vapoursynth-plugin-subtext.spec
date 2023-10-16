Summary:	Subtext plugin for Vapoursynth
Summary(pl.UTF-8):	Wtyczka programu Vapoursynth wyświetlająca podpisy
Name:		vapoursynth-plugin-subtext
Version:	3
Release:	2
# it was vapoursynth.spec subpackage up to 54
Epoch:		1
License:	MIT
Group:		Libraries
Source0:	https://github.com/vapoursynth/subtext/archive/R%{version}/subtext-R%{version}.tar.gz
# Source0-md5:	6483b72d357bafa228d46ab5ded2fe13
URL:		https://github.com/vapoursynth/subtext
BuildRequires:	ffmpeg-devel
BuildRequires:	libass-devel >= 0.12.0
BuildRequires:	libstdc++-devel
BuildRequires:	meson
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	vapoursynth-devel >= 55
Requires:	libass >= 0.12.0
Requires:	vapoursynth >= 55
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Subtext is a subtitle renderer that uses libass and ffmpeg.

%description -l pl.UTF-8
Subtext to wtyczka wyświetlająca podpisy, wykorzystująca biblioteki
libass oraz ffmpeg.

%prep
%setup -q -n subtext-R%{version}

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE docs/subtext.rst
%attr(755,root,root) %{_libdir}/vapoursynth/libsubtext.so
