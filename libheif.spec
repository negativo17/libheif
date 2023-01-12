Name:           libheif
Version:        1.14.2
Release:        1%{?dist}
Summary:        ISO/IEC 23008-12:2017 HEIF and AVIF file format decoder and encoder
License:        LGPLv3+ and MIT
URL:            https://github.com/strukturag/%{name}

Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(aom)
BuildRequires:  pkgconfig(dav1d)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(libde265)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(rav1e)
%ifarch x86_64
BuildRequires:  pkgconfig(SvtAv1Enc)
%endif
BuildRequires:  pkgconfig(x265)

Requires:   shared-mime-info

%description
libheif is an ISO/IEC 23008-12:2017 HEIF and AVIF (AV1 Image File Format) file
format decoder and encoder.

HEIF and AVIF are new image file formats employing HEVC (h.265) or AV1 image
coding, respectively, for the best compression ratios currently possible.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1
rm -rf third-party/

%build
%cmake \
 -GNinja \
 -DBUILD_SHARED_LIBS=ON \
 -DENABLE_PLUGIN_LOADING=ON \
 -DWITH_AOM_DECODER_PLUGIN=ON \
 -DWITH_AOM_ENCODER_PLUGIN=ON \
 -DWITH_DAV1D_PLUGIN=ON \
 -DWITH_LIBDE265_PLUGIN=ON \
%ifarch x86_64
 -DWITH_SvtEnc_PLUGIN=ON \
%endif
 -DWITH_RAV1E_PLUGIN=ON \
 -DWITH_X265_PLUGIN=ON

%cmake_build

%install
%cmake_install

%{?ldconfig_scriptlets}

%files
%license COPYING
%doc README.md
%{_bindir}/heif-convert
%{_bindir}/heif-enc
%{_bindir}/heif-info
%{_bindir}/heif-thumbnailer
%{_libdir}/%{name}.so.1
%{_libdir}/%{name}.so.%{version}
%{_libdir}/%{name}/%{name}-aomdec.so
%{_libdir}/%{name}/%{name}-aomenc.so
%{_libdir}/%{name}/%{name}-dav1d.so
%{_libdir}/%{name}/%{name}-libde265.so
%{_libdir}/%{name}/%{name}-rav1e.so
%ifarch x86_64
%{_libdir}/%{name}/%{name}-svtenc.so
%endif
%{_libdir}/%{name}/%{name}-x265.so
%{_libdir}/gdk-pixbuf-2.0/*/loaders/libpixbufloader-heif.so
%{_datadir}/mime/packages/avif.xml
%{_datadir}/mime/packages/heif.xml
%{_datadir}/thumbnailers/
%{_mandir}/man1/heif-convert.1*
%{_mandir}/man1/heif-enc.1*
%{_mandir}/man1/heif-info.1*
%{_mandir}/man1/heif-thumbnailer.1*

%files devel
%{_includedir}/%{name}/
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/%{name}.so

%changelog
* Thu Jan 12 2023 Simone Caronni <negativo17@gmail.com> - 1.14.2-1
- First build.
