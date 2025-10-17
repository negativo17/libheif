Name:       libheif
Epoch:      1
Version:    1.20.2
Release:    1%{?dist}
Summary:    ISO/IEC 23008-12:2017 HEIF and AVIF file format decoder and encoder
License:    LGPLv3+ and MIT
URL:        https://github.com/strukturag/%{name}

Source0:    %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:     %{name}-vvdec3.patch

BuildRequires:  cmake
BuildRequires:  doxygen
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
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libvvdec) >= 3.0.0
BuildRequires:  pkgconfig(libvvenc) >= 1.12.0
BuildRequires:  pkgconfig(openh264)
BuildRequires:  pkgconfig(openjph) >= 0.18.0
BuildRequires:  pkgconfig(rav1e)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(SvtAv1Enc)
BuildRequires:  pkgconfig(uvg266)
BuildRequires:  pkgconfig(x265)
# Requires the "vvdecapp" and "vvencapp" binaries:
BuildRequires:  vvdec
BuildRequires:  vvenc

Requires:       shared-mime-info
Obsoletes:      heif-pixbuf-loader < %{version}-%{release}

%description
libheif is an ISO/IEC 23008-12:2017 HEIF and AVIF (AV1 Image File Format) file
format decoder and encoder.

HEIF and AVIF are new image file formats employing HEVC (h.265) or AV1 image
coding, respectively, for the best compression ratios currently possible.

%package        tools
Summary:        Tools for manipulating HEIF files
License:        MIT
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description    tools
This package provides tools for manipulating HEIF files.

%package    devel
Summary:    Development files for %{name}
Requires:   %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
%cmake \
  -GNinja \
  -DBUILD_SHARED_LIBS=ON \
  -DBUILD_TESTING=ON \
  -DCMAKE_COMPILE_WARNING_AS_ERROR=OFF \
  -DENABLE_PLUGIN_LOADING=ON \
  -DWITH_AOM_DECODER=ON \
  -DWITH_AOM_DECODER_PLUGIN=ON \
  -DWITH_AOM_ENCODER=ON \
  -DWITH_AOM_ENCODER_PLUGIN=ON \
  -DWITH_DAV1D=ON \
  -DWITH_DAV1D_PLUGIN=ON \
  -DWITH_DEFLATE_HEADER_COMPRESSION=ON \
  -DWITH_EXAMPLES=ON \
  -DWITH_FFMPEG_DECODER=ON \
  -DWITH_FFMPEG_DECODER_PLUGIN=ON \
  -DWITH_GDK_PIXBUF=OFF \
  -DWITH_KVAZAAR=ON \
  -DWITH_KVAZAAR_PLUGIN=ON \
  -DWITH_JPEG_DECODER=ON \
  -DWITH_JPEG_DECODER_PLUGIN=ON \
  -DWITH_JPEG_ENCODER=ON \
  -DWITH_JPEG_ENCODER_PLUGIN=ON \
  -DWITH_LIBDE265=ON \
  -DWITH_LIBDE265_PLUGIN=ON \
  -DWITH_LIBSHARPYUV=ON \
  -DWITH_LIBSHARPYUV_PLUGIN=ON \
  -DWITH_OpenH264_DECODER=ON \
  -DWITH_OpenH264_DECODER_PLUGIN=ON \
  -DWITH_OpenJPEG_ENCODER=ON \
  -DWITH_OpenJPEG_ENCODER_PLUGIN=ON \
  -DWITH_OpenJPEG_DECODER=ON \
  -DWITH_OpenJPEG_DECODER_PLUGIN=ON \
  -DWITH_OPENJPH_ENCODER=ON \
  -DWITH_OPENJPH_ENCODER_PLUGIN=ON \
  -DWITH_SvtEnc=ON \
  -DWITH_SvtEnc_PLUGIN=ON \
  -DWITH_RAV1E=ON \
  -DWITH_RAV1E_PLUGIN=ON \
  -DWITH_REDUCED_VISIBILITY=ON \
  -DWITH_UNCOMPRESSED_CODEC=ON \
  -DWITH_UVG266=ON \
  -DWITH_UVG266_PLUGIN=ON \
  -DWITH_VVDEC=ON \
  -DWITH_VVDEC_PLUGIN=ON \
  -DWITH_VVENC=ON \
  -DWITH_VVENC_PLUGIN=ON \
  -DWITH_X265=ON \
  -DWITH_X265_PLUGIN=ON

%cmake_build

%install
%cmake_install

cp -frv %{_vpath_builddir}/apidoc/man/man3 %{buildroot}%{_mandir}/
rm -f %{buildroot}%{_mandir}/man3/_builddir_build_BUILD_libheif*

%check
%ctest

%files
%license COPYING
%doc README.md
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
%{_libdir}/%{name}/%{name}-jphenc.so
%{_libdir}/%{name}/%{name}-kvazaar.so
%{_libdir}/%{name}/%{name}-libde265.so
%{_libdir}/%{name}/%{name}-openh264dec.so
%{_libdir}/%{name}/%{name}-rav1e.so
%{_libdir}/%{name}/%{name}-svtenc.so
%{_libdir}/%{name}/%{name}-uvg266.so
%{_libdir}/%{name}/%{name}-vvdec.so
%{_libdir}/%{name}/%{name}-vvenc.so
%{_libdir}/%{name}/%{name}-x265.so

%files tools
%{_bindir}/heif-convert
%{_bindir}/heif-dec
%{_bindir}/heif-enc
%{_bindir}/heif-info
%{_bindir}/heif-thumbnailer
%{_bindir}/heif-view
%{_mandir}/man1/heif-dec.1*
%{_mandir}/man1/heif-enc.1*
%{_mandir}/man1/heif-info.1*
%{_mandir}/man1/heif-thumbnailer.1*

%files devel
%doc %{_vpath_builddir}/apidoc/html
%{_includedir}/%{name}/
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/%{name}.so
%{_mandir}/man3/heif.h.3*
%{_mandir}/man3/heif_items.h.3*
%{_mandir}/man3/heif_regions.h.3*

%changelog
* Fri Oct 17 2025 Simone Caronni <negativo17@gmail.com> - 1:1.20.2-1
- Update to 1.20.2.
- Remove obsolete pixbuf loader.

* Tue Apr 29 2025 Simone Caronni <negativo17@gmail.com> - 1:1.19.8-1
- Update to 1.19.8.

* Tue Mar 25 2025 Simone Caronni <negativo17@gmail.com> - 1:1.19.7-2
- Update VVdeC/VVenC requirements.
- Enable testing.
- Fix changelog.

* Mon Mar 17 2025 Simone Caronni <negativo17@gmail.com> - 1:1.19.7-1
- Update to 1.19.7.

* Thu Dec 12 2024 Simone Caronni <negativo17@gmail.com> - 1:1.19.5-1
- Update to 1.19.5.

* Tue Dec 10 2024 Simone Caronni <negativo17@gmail.com> - 1:1.19.3-1
- Update to 1.19.3.
- Fix build on Fedora:
  https://github.com/strukturag/libheif/issues/1360#issuecomment-2452007818
- Enable OpenH264 decoding.
- Re-enable OpenJPH (0.18.0).

* Wed Dec 04 2024 Simone Caronni <negativo17@gmail.com> - 1:1.18.2-5
- Rebuilt for updated dependencies.

* Tue Nov 12 2024 Simone Caronni <negativo17@gmail.com> - 1:1.18.2-4
- Re-enable OpenJPH.

* Thu Sep 12 2024 Simone Caronni <negativo17@gmail.com> - 1:1.18.2-3
- Momentarily disable OpenJPH plugin.

* Tue Sep 10 2024 Simone Caronni <negativo17@gmail.com> - 1:1.18.2-2
- Rebuild for updated depdendencies.
- Adjust snapshot version to recent packaging guidelines.

* Thu Aug 22 2024 Simone Caronni <negativo17@gmail.com> - 1:1.18.2-1
- Update to 1.18.2.
- Enable VVdec/VVenc/uvg266/OpenJPH plugins.
- Split GTK loader in a separate subpackage.

* Sun Jun 16 2024 Simone Caronni <negativo17@gmail.com> - 1:1.17.6-3.20240612git77e9adb
- Update to latest snapshot.
- Enable development documentation.

* Tue Jun 04 2024 Simone Caronni <negativo17@gmail.com> - 1:1.17.6-2.20240525gitf0c1a86
- Update to latest snapshot to fix memory leaks and allow building with SVT-AV1 2.x.
- Adjust plugins and build options, enable SVT-AV1 for aarch64.

* Thu Dec 21 2023 Simone Caronni <negativo17@gmail.com> - 1:1.17.6-1
- Update to 1.17.6.

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
