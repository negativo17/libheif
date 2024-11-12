%global commit0 77e9adb9af8ac69e89eb44089151c11726a56f62
%global date 20240612
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global tag %{version}

Name:       libheif
Epoch:      1
Version:    1.18.2%{!?tag:^%{date}git%{shortcommit0}}
Release:    4%{?dist}
Summary:    ISO/IEC 23008-12:2017 HEIF and AVIF file format decoder and encoder
License:    LGPLv3+ and MIT
URL:        https://github.com/strukturag/%{name}

%if 0%{?tag:1}
Source0:    %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
%else
Source0:    %{url}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
%endif

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
BuildRequires:  pkgconfig(openjph)
BuildRequires:  pkgconfig(libvvdec)
BuildRequires:  pkgconfig(libvvenc)
BuildRequires:  pkgconfig(rav1e)
BuildRequires:  pkgconfig(SvtAv1Enc)
BuildRequires:  pkgconfig(uvg266)
BuildRequires:  pkgconfig(x265)
BuildRequires:  vvdec

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

%package -n     heif-pixbuf-loader
Summary:        HEIF image loader for GTK+ applications
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
Requires:       gdk-pixbuf2%{?_isa}

%description -n heif-pixbuf-loader
This package provides a plugin to load HEIF files in GTK+ applications.

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
  -DWITH_DEFLATE_HEADER_COMPRESSION=ON \
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
  -DWITH_LIBSHARPYUV_PLUGIN=ON \
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

%files
%license COPYING
%doc README.md
%{_bindir}/heif-convert
%{_bindir}/heif-dec
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
%{_libdir}/%{name}/%{name}-jphenc.so
%{_libdir}/%{name}/%{name}-kvazaar.so
%{_libdir}/%{name}/%{name}-libde265.so
%{_libdir}/%{name}/%{name}-rav1e.so
%{_libdir}/%{name}/%{name}-svtenc.so
%{_libdir}/%{name}/%{name}-uvg266.so
%{_libdir}/%{name}/%{name}-vvdec.so
%{_libdir}/%{name}/%{name}-vvenc.so
%{_libdir}/%{name}/%{name}-x265.so
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
%{_mandir}/man3/heif_regions.h.3*
%{_mandir}/man3/heif_camera_intrinsic_matrix.3.gz
%{_mandir}/man3/heif_color_conversion_options.3*
%{_mandir}/man3/heif_color_profile_nclx.3*
%{_mandir}/man3/heif_content_light_level.3*
%{_mandir}/man3/heif_decoded_mastering_display_colour_volume.3*
%{_mandir}/man3/heif_decoding_options.3*
%{_mandir}/man3/heif_depth_representation_info.3*
%{_mandir}/man3/heif_encoding_options.3*
%{_mandir}/man3/heif_error.3*
%{_mandir}/man3/heif_init_params.3*
%{_mandir}/man3/heif_items.h.3.gz
%{_mandir}/man3/heif_mastering_display_colour_volume.3*
%{_mandir}/man3/heif_plugin_info.3*
%{_mandir}/man3/heif_reader.3*
%{_mandir}/man3/heif_writer.3*

%files -n heif-pixbuf-loader
%{_libdir}/gdk-pixbuf-2.0/*/loaders/libpixbufloader-heif.so

%changelog
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
