%global commit0 03158c13aa2fa9e8d3c96ced6dcff61b86418d20
%global date 20230203
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global tag %{version}

Name:       libheif
Epoch:      1
Version:    1.17.5
Release:    1%{?dist}
Summary:    ISO/IEC 23008-12:2017 HEIF and AVIF file format decoder and encoder
License:    LGPLv3+ and MIT
URL:        https://github.com/strukturag/%{name}

%if 0%{?tag:1}
Source0:    %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
%else
Source0:    %{url}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
%endif

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libavcodec-devel
BuildRequires:  ninja-build
BuildRequires:  openjpeg2-devel
BuildRequires:  pkgconfig(aom)
BuildRequires:  pkgconfig(dav1d)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(kvazaar)
BuildRequires:  pkgconfig(libde265)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libsharpyuv)
BuildRequires:  pkgconfig(rav1e)
%ifarch x86_64
BuildRequires:  pkgconfig(SvtAv1Enc)
%endif
BuildRequires:  pkgconfig(x265)

%description
libheif is an ISO/IEC 23008-12:2017 HEIF and AVIF (AV1 Image File Format) file
format decoder and encoder.

HEIF and AVIF are new image file formats employing HEVC (h.265) or AV1 image
coding, respectively, for the best compression ratios currently possible.

%package    devel
Summary:    Development files for %{name}
Requires:   %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%if 0%{?tag:1}
%autosetup -p1
%else
%autosetup -p1 -n %{name}-%{commit0}
%endif

%build
%cmake \
 -GNinja \
 -DBUILD_SHARED_LIBS=ON \
 -DENABLE_PLUGIN_LOADING=ON \
 -DWITH_AOM_DECODER=ON \
 -DWITH_AOM_DECODER_PLUGIN=ON \
 -DWITH_AOM_ENCODER=ON \
 -DWITH_AOM_ENCODER_PLUGIN=ON \
 -DWITH_DAV1D=ON \
 -DWITH_DAV1D_PLUGIN=ON \
 -DWITH_EXAMPLES=ON \
 -DWITH_FFMPEG_DECODER=ON \
 -DWITH_FFMPEG_DECODER_PLUGIN=ON \
 -DWITH_KVAZAAR=ON \
 -DWITH_KVAZAAR_PLUGIN=ON \
 -DWITH_JPEG_DECODER=ON \
 -DWITH_JPEG_DECODER_PLUGIN=ON \
 -DWITH_JPEG_ENCODER=ON \
 -DWITH_JPEG_ENCODER_PLUGIN=ON \
 -DWITH_LIBDE265=ON \
 -DWITH_LIBDE265_PLUGIN=ON \
 -DWITH_LIBSHARPYUV=ON \
 -DWITH_OpenJPEG_ENCODER=ON \
 -DWITH_OpenJPEG_DECODER=ON \
%ifarch x86_64
 -DWITH_SvtEnc=ON \
 -DWITH_SvtEnc_PLUGIN=ON \
%endif
 -DWITH_RAV1E=ON \
 -DWITH_RAV1E_PLUGIN=ON \
 -DWITH_X265=ON \
 -DWITH_X265_PLUGIN=ON

%cmake_build

%install
%cmake_install

%files
%license COPYING
%doc README.md
%{_bindir}/heif-convert
%{_bindir}/heif-enc
%{_bindir}/heif-info
%{_bindir}/heif-thumbnailer
%{_datadir}/thumbnailers/
%{_libdir}/%{name}.so.1
%{_libdir}/%{name}.so.%{version}
%{_libdir}/%{name}/%{name}-aomdec.so
%{_libdir}/%{name}/%{name}-aomenc.so
%{_libdir}/%{name}/%{name}-dav1d.so
%{_libdir}/%{name}/%{name}-ffmpegdec.so
%{_libdir}/%{name}/%{name}-j2kdec.so
%{_libdir}/%{name}/%{name}-j2kenc.so
%{_libdir}/%{name}/%{name}-jpegdec.so
%{_libdir}/%{name}/%{name}-jpegenc.so
%{_libdir}/%{name}/%{name}-kvazaar.so
%{_libdir}/%{name}/%{name}-libde265.so
%{_libdir}/%{name}/%{name}-rav1e.so
%ifarch x86_64
%{_libdir}/%{name}/%{name}-svtenc.so
%endif
%{_libdir}/%{name}/%{name}-x265.so
%{_libdir}/gdk-pixbuf-2.0/*/loaders/libpixbufloader-heif.so
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
* Tue Nov 21 2023 Simone Caronni <negativo17@gmail.com> - 1:1.17.5-1
- Update to 1.17.5.

* Tue Nov 21 2023 Simone Caronni <negativo17@gmail.com> - 1:1.17.4-1
- Update to 1.17.4.

* Fri Nov 10 2023 Simone Caronni <negativo17@gmail.com> - 1:1.17.3-1
- Update to 1.17.3.

* Fri Oct 20 2023 Simone Caronni <negativo17@gmail.com> - 1:1.17.1-1
- Update to 1.17.1.

* Tue Oct 17 2023 Simone Caronni <negativo17@gmail.com> - 1:1.17.0-1
- Update to 1.17.0.
- Enable libsharpyuv and all new plugins.

* Fri Jun 02 2023 Simone Caronni <negativo17@gmail.com> - 1:1.16.2-2
- Rebuild for updated dependencies.

* Tue May 23 2023 Simone Caronni <negativo17@gmail.com> - 1:1.16.2-1
- Update to 1.16.2.

* Fri May 05 2023 Simone Caronni <negativo17@gmail.com> - 1:1.16.1-1
- Update to 1.16.1.

* Mon May 01 2023 Simone Caronni <negativo17@gmail.com> - 1.15.2-1
- Update to 1.15.2.
- Bump Epoch to override Fedora package.

* Tue Mar 14 2023 Simone Caronni <negativo17@gmail.com> - 1.15.1-2
- Rebuild for updated dependencies.

* Fri Feb 24 2023 Simone Caronni <negativo17@gmail.com> - 1.15.1-1
- Update to 1.15.1.

* Mon Feb 06 2023 Simone Caronni <negativo17@gmail.com> - 1.14.2-5.20230203git03158c1
- Update to latest snapshot, drop merged patches.

* Fri Jan 20 2023 Simone Caronni <negativo17@gmail.com> - 1.14.2-4.20230119git96a114f
- Enable SVT-AV1 encoder.

* Fri Jan 20 2023 Simone Caronni <negativo17@gmail.com> - 1.14.2-3.20230119git96a114f
- Rebase to latest snapshot, dynamic plugin linking is fixed.
- Temporarily drop SVT encoder plugin.

* Fri Jan 13 2023 Simone Caronni <negativo17@gmail.com> - 1.14.2-2
- Temporarily disable dynamic plugins due to a bug.

* Thu Jan 12 2023 Simone Caronni <negativo17@gmail.com> - 1.14.2-1
- First build.
