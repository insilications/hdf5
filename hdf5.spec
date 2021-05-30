#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : hdf5
Version  : 1.13.0.rc5
Release  : 301
URL      : file:///aot/build/clearlinux/packages/hdf5/hdf5-v1_13_0-rc5.tar.gz
Source0  : file:///aot/build/clearlinux/packages/hdf5/hdf5-v1_13_0-rc5.tar.gz
Summary  : HDF5 (Hierarchical Data Format 5) Software Library
Group    : Development/Tools
License  : GPL-2.0
Requires: hdf5-bin = %{version}-%{release}
Requires: hdf5-data = %{version}-%{release}
Requires: hdf5-lib = %{version}-%{release}
Requires: hdf5-openmpi = %{version}-%{release}
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : binutils-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-configure
BuildRequires : doxygen
BuildRequires : elfutils-dev
BuildRequires : gcc
BuildRequires : gcc-dev
BuildRequires : gcc-libs-math
BuildRequires : gcc-libstdc++32
BuildRequires : gcc-libubsan
BuildRequires : gcc-locale
BuildRequires : glibc-dev
BuildRequires : glibc-staticdev
BuildRequires : libedit
BuildRequires : libedit-dev
BuildRequires : libffi-dev
BuildRequires : libffi-staticdev
BuildRequires : libgcc1
BuildRequires : libstdc++
BuildRequires : libxml2-dev
BuildRequires : libxml2-staticdev
BuildRequires : m4
BuildRequires : modules
BuildRequires : ncurses-dev
BuildRequires : openmpi-dev
BuildRequires : openssh
BuildRequires : python3-dev
BuildRequires : python3-staticdev
BuildRequires : qtbase
BuildRequires : qtbase-dev
BuildRequires : qtdeclarative
BuildRequires : qtdeclarative-dev
BuildRequires : qtlocation
BuildRequires : qtlocation-dev
BuildRequires : qtsvg
BuildRequires : qtsvg-dev
BuildRequires : qtwebchannel
BuildRequires : qtwebchannel-dev
BuildRequires : qtwebengine
BuildRequires : qtwebengine-dev
BuildRequires : xz-dev
BuildRequires : xz-staticdev
BuildRequires : zlib-dev
BuildRequires : zlib-staticdev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: deflate_limit.h5repack_layout.patch

%description
===================================
===================================
This directory contains Fortran APIs for HDF5 Library functionality.
A complete list of implemented Fortran subroutines can be found in the HDF5
Reference Manual.

%package bin
Summary: bin components for the hdf5 package.
Group: Binaries
Requires: hdf5-data = %{version}-%{release}

%description bin
bin components for the hdf5 package.


%package data
Summary: data components for the hdf5 package.
Group: Data

%description data
data components for the hdf5 package.


%package dev
Summary: dev components for the hdf5 package.
Group: Development
Requires: hdf5-lib = %{version}-%{release}
Requires: hdf5-bin = %{version}-%{release}
Requires: hdf5-data = %{version}-%{release}
Requires: hdf5-openmpi = %{version}-%{release}
Provides: hdf5-devel = %{version}-%{release}
Requires: hdf5 = %{version}-%{release}

%description dev
dev components for the hdf5 package.


%package lib
Summary: lib components for the hdf5 package.
Group: Libraries
Requires: hdf5-data = %{version}-%{release}

%description lib
lib components for the hdf5 package.


%package openmpi
Summary: openmpi components for the hdf5 package.
Group: Default

%description openmpi
openmpi components for the hdf5 package.


%package staticdev
Summary: staticdev components for the hdf5 package.
Group: Default
Requires: hdf5-dev = %{version}-%{release}

%description staticdev
staticdev components for the hdf5 package.


%prep
%setup -q -n hdf5
cd %{_builddir}/hdf5
%patch1 -p1
pushd ..
cp -a hdf5 build-openmpi
popd

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1622337922
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
## altflags1 content
export CFLAGS="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -flto=16 -fno-plt -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
# -ffat-lto-objects -fno-PIE -fno-PIE -m64 -no-pie -fPIC -Wl,-z,max-page-size=0x1000 -fvisibility=hidden -flto-partition=none
# gcc: -feliminate-unused-debug-types -flto=16 -Wno-error -Wp,-D_REENTRANT -fno-common -funroll-loops
export CXXFLAGS="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -flto=16 -fno-plt -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
#
export FCFLAGS="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -flto=16 -fno-plt -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
export FFLAGS="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -flto=16 -fno-plt -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -Wl,--build-id=sha1"
export CFFLAGS="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -flto=16 -fno-plt -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
#
export LDFLAGS="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -flto=16 -fno-plt -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -lpthread -Wl,--build-id=sha1"
#
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
#
export MAKEFLAGS=%{?_smp_mflags}
#
%global _lto_cflags 1
#global _lto_cflags %{nil}
%global _disable_maintainer_mode 1
#%global _disable_maintainer_mode %{nil}
#
export CCACHE_DISABLE=true
export PATH="/usr/lib64/ccache/bin:$PATH"
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,file_stat_matches,file_stat_matches_ctime,include_file_ctime,include_file_mtime,modules,system_headers,clang_index_store,file_macro
#export CCACHE_SLOPPINESS=modules,include_file_mtime,include_file_ctime,time_macros,pch_defines,file_stat_matches,clang_index_store,system_headers,locale
#export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,clang_index_store,file_macro
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
#export CCACHE_LOGFILE=/var/tmp/ccache/cache.debug
#export CCACHE_DEBUG=true
#export CCACHE_NODIRECT=true
## altflags1 end
./autogen.sh
./configure --build=x86_64-generic-linux-gnu --host=x86_64-generic-linux-gnu --target=x86_64-clr-linux-gnu --program-prefix= --prefix=/usr --exec-prefix=/usr --bindir=/usr/bin --sbindir=/usr/bin --sysconfdir=/etc --datadir=/usr/share --includedir=/usr/include --libdir=/usr/lib64 --libexecdir=/usr/libexec --localstatedir=/var --sharedstatedir=/usr/com --mandir=/usr/share/man --infodir=/usr/share/info --disable-maintainer-mode --enable-cxx --enable-fortran --enable-static --enable-shared --enable-optimization=high --enable-static-exec --enable-build-mode=production --enable-tools --enable-tests=no --disable-tests
make  %{?_smp_mflags}    V=1 VERBOSE=1

pushd ../build-openmpi/
. /usr/share/defaults/etc/profile.d/modules.sh
module load openmpi
export CFLAGS="-g -O3 -march=native -mtune=native -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fno-lto -fno-plt -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
# -ffat-lto-objects -fno-PIE -fno-PIE -m64 -no-pie -fPIC -Wl,-z,max-page-size=0x1000 -fvisibility=hidden -flto-partition=none
# gcc: -feliminate-unused-debug-types -fno-lto -Wno-error -Wp,-D_REENTRANT -fno-common -funroll-loops
export CXXFLAGS="-g -O3 -march=native -mtune=native -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fno-lto -fno-plt -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
#
export FCFLAGS="-g -O3 -march=native -mtune=native -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fno-lto -fno-plt -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
export FFLAGS="-g -O3 -march=native -mtune=native -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fno-lto -fno-plt -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -Wl,--build-id=sha1"
export CFFLAGS="-g -O3 -march=native -mtune=native -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fno-lto -fno-plt -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
#
export LDFLAGS="-g -O3 -march=native -mtune=native -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fno-lto -fno-plt -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -lpthread -Wl,--build-id=sha1"
#
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
#
export MAKEFLAGS=%{?_smp_mflags}
#
%global _lto_cflags 1
#global _lto_cflags %{nil}
%global _disable_maintainer_mode 1
#
./autogen.sh
./configure --program-prefix=  --exec-prefix=$MPI_ROOT --libdir=$MPI_LIB --bindir=$MPI_BIN --sbindir=$MPI_BIN --includedir=$MPI_INCLUDE --datarootdir=$MPI_ROOT/share --mandir=$MPI_MAN -exec-prefix=$MPI_ROOT --sysconfdir=$MPI_SYSCONFIG --build=x86_64-generic-linux-gnu --host=x86_64-generic-linux-gnu --target=x86_64-clr-linux-gnu --disable-static RUNPARALLEL='mpiexec -x LD_LIBRARY_PATH -n $${NPROCS:=6}' --enable-fortran --enable-parallel --with-szlib --enable-tests=no --disable-tests
make  %{?_smp_mflags}    V=1 VERBOSE=1
module unload openmpi
popd

%install
export SOURCE_DATE_EPOCH=1622337922
rm -rf %{buildroot}
pushd ../build-openmpi/
module load openmpi
%make_install_openmpi
module unload openmpi
popd
%make_install
## install_append content
install -dm 0755 %{buildroot}/usr/lib64/haswell/ || :
cp --archive %{buildroot}/usr/lib64/lib*.so* %{buildroot}/usr/lib64/haswell/ || :
## install_append end

%files
%defattr(-,root,root,-)
/usr/lib64/libhdf5.settings

%files bin
%defattr(-,root,root,-)
/usr/bin/gif2h5
/usr/bin/h52gif
/usr/bin/h5c++
/usr/bin/h5cc
/usr/bin/h5clear
/usr/bin/h5copy
/usr/bin/h5debug
/usr/bin/h5delete
/usr/bin/h5diff
/usr/bin/h5dump
/usr/bin/h5fc
/usr/bin/h5format_convert
/usr/bin/h5import
/usr/bin/h5jam
/usr/bin/h5ls
/usr/bin/h5mkgrp
/usr/bin/h5redeploy
/usr/bin/h5repack
/usr/bin/h5repart
/usr/bin/h5stat
/usr/bin/h5unjam
/usr/bin/h5watch
/usr/bin/mirror_server
/usr/bin/mirror_server_stop

%files data
%defattr(-,root,root,-)
/usr/share/hdf5_examples/README
/usr/share/hdf5_examples/c++/chunks.cpp
/usr/share/hdf5_examples/c++/compound.cpp
/usr/share/hdf5_examples/c++/create.cpp
/usr/share/hdf5_examples/c++/extend_ds.cpp
/usr/share/hdf5_examples/c++/h5group.cpp
/usr/share/hdf5_examples/c++/h5tutr_cmprss.cpp
/usr/share/hdf5_examples/c++/h5tutr_crtatt.cpp
/usr/share/hdf5_examples/c++/h5tutr_crtdat.cpp
/usr/share/hdf5_examples/c++/h5tutr_crtgrp.cpp
/usr/share/hdf5_examples/c++/h5tutr_crtgrpar.cpp
/usr/share/hdf5_examples/c++/h5tutr_crtgrpd.cpp
/usr/share/hdf5_examples/c++/h5tutr_extend.cpp
/usr/share/hdf5_examples/c++/h5tutr_rdwt.cpp
/usr/share/hdf5_examples/c++/h5tutr_subset.cpp
/usr/share/hdf5_examples/c++/readdata.cpp
/usr/share/hdf5_examples/c++/run-c++-ex.sh
/usr/share/hdf5_examples/c++/writedata.cpp
/usr/share/hdf5_examples/c/h5_attribute.c
/usr/share/hdf5_examples/c/h5_chunk_read.c
/usr/share/hdf5_examples/c/h5_cmprss.c
/usr/share/hdf5_examples/c/h5_compound.c
/usr/share/hdf5_examples/c/h5_crtatt.c
/usr/share/hdf5_examples/c/h5_crtdat.c
/usr/share/hdf5_examples/c/h5_crtgrp.c
/usr/share/hdf5_examples/c/h5_crtgrpar.c
/usr/share/hdf5_examples/c/h5_crtgrpd.c
/usr/share/hdf5_examples/c/h5_debug_trace.c
/usr/share/hdf5_examples/c/h5_drivers.c
/usr/share/hdf5_examples/c/h5_elink_unix2win.c
/usr/share/hdf5_examples/c/h5_extend.c
/usr/share/hdf5_examples/c/h5_extend_write.c
/usr/share/hdf5_examples/c/h5_extlink.c
/usr/share/hdf5_examples/c/h5_group.c
/usr/share/hdf5_examples/c/h5_mount.c
/usr/share/hdf5_examples/c/h5_rdwt.c
/usr/share/hdf5_examples/c/h5_read.c
/usr/share/hdf5_examples/c/h5_ref2reg_deprec.c
/usr/share/hdf5_examples/c/h5_ref_compat.c
/usr/share/hdf5_examples/c/h5_ref_extern.c
/usr/share/hdf5_examples/c/h5_reference_deprec.c
/usr/share/hdf5_examples/c/h5_select.c
/usr/share/hdf5_examples/c/h5_shared_mesg.c
/usr/share/hdf5_examples/c/h5_subset.c
/usr/share/hdf5_examples/c/h5_vds-eiger.c
/usr/share/hdf5_examples/c/h5_vds-exc.c
/usr/share/hdf5_examples/c/h5_vds-exclim.c
/usr/share/hdf5_examples/c/h5_vds-percival-unlim-maxmin.c
/usr/share/hdf5_examples/c/h5_vds-percival-unlim.c
/usr/share/hdf5_examples/c/h5_vds-percival.c
/usr/share/hdf5_examples/c/h5_vds-simpleIO.c
/usr/share/hdf5_examples/c/h5_vds.c
/usr/share/hdf5_examples/c/h5_write.c
/usr/share/hdf5_examples/c/ph5example.c
/usr/share/hdf5_examples/c/run-c-ex.sh
/usr/share/hdf5_examples/fortran/compound.f90
/usr/share/hdf5_examples/fortran/compound_complex_fortran2003.f90
/usr/share/hdf5_examples/fortran/compound_fortran2003.f90
/usr/share/hdf5_examples/fortran/h5_cmprss.f90
/usr/share/hdf5_examples/fortran/h5_crtatt.f90
/usr/share/hdf5_examples/fortran/h5_crtdat.f90
/usr/share/hdf5_examples/fortran/h5_crtgrp.f90
/usr/share/hdf5_examples/fortran/h5_crtgrpar.f90
/usr/share/hdf5_examples/fortran/h5_crtgrpd.f90
/usr/share/hdf5_examples/fortran/h5_extend.f90
/usr/share/hdf5_examples/fortran/h5_rdwt.f90
/usr/share/hdf5_examples/fortran/h5_subset.f90
/usr/share/hdf5_examples/fortran/hyperslab.f90
/usr/share/hdf5_examples/fortran/mountexample.f90
/usr/share/hdf5_examples/fortran/nested_derived_type.f90
/usr/share/hdf5_examples/fortran/ph5example.f90
/usr/share/hdf5_examples/fortran/refobjexample.f90
/usr/share/hdf5_examples/fortran/refregexample.f90
/usr/share/hdf5_examples/fortran/run-fortran-ex.sh
/usr/share/hdf5_examples/fortran/rwdset_fortran2003.f90
/usr/share/hdf5_examples/fortran/selectele.f90
/usr/share/hdf5_examples/hl/c++/ptExampleFL.cpp
/usr/share/hdf5_examples/hl/c++/run-hlc++-ex.sh
/usr/share/hdf5_examples/hl/c/ex_ds1.c
/usr/share/hdf5_examples/hl/c/ex_image1.c
/usr/share/hdf5_examples/hl/c/ex_image2.c
/usr/share/hdf5_examples/hl/c/ex_lite1.c
/usr/share/hdf5_examples/hl/c/ex_lite2.c
/usr/share/hdf5_examples/hl/c/ex_lite3.c
/usr/share/hdf5_examples/hl/c/ex_table_01.c
/usr/share/hdf5_examples/hl/c/ex_table_02.c
/usr/share/hdf5_examples/hl/c/ex_table_03.c
/usr/share/hdf5_examples/hl/c/ex_table_04.c
/usr/share/hdf5_examples/hl/c/ex_table_05.c
/usr/share/hdf5_examples/hl/c/ex_table_06.c
/usr/share/hdf5_examples/hl/c/ex_table_07.c
/usr/share/hdf5_examples/hl/c/ex_table_08.c
/usr/share/hdf5_examples/hl/c/ex_table_09.c
/usr/share/hdf5_examples/hl/c/ex_table_10.c
/usr/share/hdf5_examples/hl/c/ex_table_11.c
/usr/share/hdf5_examples/hl/c/ex_table_12.c
/usr/share/hdf5_examples/hl/c/image24pixel.txt
/usr/share/hdf5_examples/hl/c/image8.txt
/usr/share/hdf5_examples/hl/c/pal_rgb.h
/usr/share/hdf5_examples/hl/c/ptExampleFL.c
/usr/share/hdf5_examples/hl/c/run-hlc-ex.sh
/usr/share/hdf5_examples/hl/fortran/ex_ds1.f90
/usr/share/hdf5_examples/hl/fortran/exlite.f90
/usr/share/hdf5_examples/hl/fortran/run-hlfortran-ex.sh
/usr/share/hdf5_examples/hl/run-hl-ex.sh
/usr/share/hdf5_examples/run-all-ex.sh

%files dev
%defattr(-,root,root,-)
/usr/include/H5ACpublic.h
/usr/include/H5AbstractDs.h
/usr/include/H5Apublic.h
/usr/include/H5ArrayType.h
/usr/include/H5AtomType.h
/usr/include/H5Attribute.h
/usr/include/H5Classes.h
/usr/include/H5CommonFG.h
/usr/include/H5CompType.h
/usr/include/H5Cpp.h
/usr/include/H5CppDoc.h
/usr/include/H5Cpublic.h
/usr/include/H5DOpublic.h
/usr/include/H5DSpublic.h
/usr/include/H5DaccProp.h
/usr/include/H5DataSet.h
/usr/include/H5DataSpace.h
/usr/include/H5DataType.h
/usr/include/H5DcreatProp.h
/usr/include/H5Dpublic.h
/usr/include/H5DxferProp.h
/usr/include/H5ESpublic.h
/usr/include/H5EnumType.h
/usr/include/H5Epubgen.h
/usr/include/H5Epublic.h
/usr/include/H5Exception.h
/usr/include/H5FDcore.h
/usr/include/H5FDdirect.h
/usr/include/H5FDfamily.h
/usr/include/H5FDhdfs.h
/usr/include/H5FDlog.h
/usr/include/H5FDmirror.h
/usr/include/H5FDmpi.h
/usr/include/H5FDmpio.h
/usr/include/H5FDmulti.h
/usr/include/H5FDpublic.h
/usr/include/H5FDros3.h
/usr/include/H5FDsec2.h
/usr/include/H5FDsplitter.h
/usr/include/H5FDstdio.h
/usr/include/H5FDwindows.h
/usr/include/H5FaccProp.h
/usr/include/H5FcreatProp.h
/usr/include/H5File.h
/usr/include/H5FloatType.h
/usr/include/H5Fpublic.h
/usr/include/H5Gpublic.h
/usr/include/H5Group.h
/usr/include/H5IMpublic.h
/usr/include/H5IdComponent.h
/usr/include/H5Include.h
/usr/include/H5IntType.h
/usr/include/H5Ipublic.h
/usr/include/H5LDpublic.h
/usr/include/H5LTpublic.h
/usr/include/H5LaccProp.h
/usr/include/H5LcreatProp.h
/usr/include/H5Library.h
/usr/include/H5Location.h
/usr/include/H5Lpublic.h
/usr/include/H5MMpublic.h
/usr/include/H5Mpublic.h
/usr/include/H5Object.h
/usr/include/H5OcreatProp.h
/usr/include/H5Opublic.h
/usr/include/H5PLextern.h
/usr/include/H5PLpublic.h
/usr/include/H5PTpublic.h
/usr/include/H5PacketTable.h
/usr/include/H5Ppublic.h
/usr/include/H5PredType.h
/usr/include/H5PropList.h
/usr/include/H5Rpublic.h
/usr/include/H5Spublic.h
/usr/include/H5StrType.h
/usr/include/H5TBpublic.h
/usr/include/H5TSpublic.h
/usr/include/H5Tpublic.h
/usr/include/H5VLconnector.h
/usr/include/H5VLconnector_passthru.h
/usr/include/H5VLnative.h
/usr/include/H5VLpassthru.h
/usr/include/H5VLpublic.h
/usr/include/H5VarLenType.h
/usr/include/H5Zpublic.h
/usr/include/H5api_adpt.h
/usr/include/H5f90i.h
/usr/include/H5f90i_gen.h
/usr/include/H5overflow.h
/usr/include/H5pubconf.h
/usr/include/H5public.h
/usr/include/H5version.h
/usr/include/h5_gen.mod
/usr/include/h5a.mod
/usr/include/h5d.mod
/usr/include/h5ds.mod
/usr/include/h5e.mod
/usr/include/h5f.mod
/usr/include/h5fortkit.mod
/usr/include/h5fortran_types.mod
/usr/include/h5g.mod
/usr/include/h5global.mod
/usr/include/h5i.mod
/usr/include/h5im.mod
/usr/include/h5l.mod
/usr/include/h5lib.mod
/usr/include/h5lt.mod
/usr/include/h5lt_const.mod
/usr/include/h5o.mod
/usr/include/h5p.mod
/usr/include/h5r.mod
/usr/include/h5s.mod
/usr/include/h5t.mod
/usr/include/h5tb.mod
/usr/include/h5tb_const.mod
/usr/include/h5vl.mod
/usr/include/h5z.mod
/usr/include/hdf5.h
/usr/include/hdf5.mod
/usr/include/hdf5_hl.h
/usr/lib64/haswell/libhdf5.so
/usr/lib64/haswell/libhdf5_fortran.so
/usr/lib64/haswell/libhdf5_hl.so
/usr/lib64/haswell/libhdf5_hl_fortran.so
/usr/lib64/haswell/libhdf5hl_fortran.so
/usr/lib64/libhdf5.so
/usr/lib64/libhdf5_cpp.so
/usr/lib64/libhdf5_fortran.so
/usr/lib64/libhdf5_hl.so
/usr/lib64/libhdf5_hl_cpp.so
/usr/lib64/libhdf5_hl_fortran.so
/usr/lib64/libhdf5hl_fortran.so
/usr/lib64/openmpi/include/H5ACpublic.h
/usr/lib64/openmpi/include/H5Apublic.h
/usr/lib64/openmpi/include/H5Cpublic.h
/usr/lib64/openmpi/include/H5DOpublic.h
/usr/lib64/openmpi/include/H5DSpublic.h
/usr/lib64/openmpi/include/H5Dpublic.h
/usr/lib64/openmpi/include/H5ESpublic.h
/usr/lib64/openmpi/include/H5Epubgen.h
/usr/lib64/openmpi/include/H5Epublic.h
/usr/lib64/openmpi/include/H5FDcore.h
/usr/lib64/openmpi/include/H5FDdirect.h
/usr/lib64/openmpi/include/H5FDfamily.h
/usr/lib64/openmpi/include/H5FDhdfs.h
/usr/lib64/openmpi/include/H5FDlog.h
/usr/lib64/openmpi/include/H5FDmirror.h
/usr/lib64/openmpi/include/H5FDmpi.h
/usr/lib64/openmpi/include/H5FDmpio.h
/usr/lib64/openmpi/include/H5FDmulti.h
/usr/lib64/openmpi/include/H5FDpublic.h
/usr/lib64/openmpi/include/H5FDros3.h
/usr/lib64/openmpi/include/H5FDsec2.h
/usr/lib64/openmpi/include/H5FDsplitter.h
/usr/lib64/openmpi/include/H5FDstdio.h
/usr/lib64/openmpi/include/H5FDwindows.h
/usr/lib64/openmpi/include/H5Fpublic.h
/usr/lib64/openmpi/include/H5Gpublic.h
/usr/lib64/openmpi/include/H5IMpublic.h
/usr/lib64/openmpi/include/H5Ipublic.h
/usr/lib64/openmpi/include/H5LDpublic.h
/usr/lib64/openmpi/include/H5LTpublic.h
/usr/lib64/openmpi/include/H5Lpublic.h
/usr/lib64/openmpi/include/H5MMpublic.h
/usr/lib64/openmpi/include/H5Mpublic.h
/usr/lib64/openmpi/include/H5Opublic.h
/usr/lib64/openmpi/include/H5PLextern.h
/usr/lib64/openmpi/include/H5PLpublic.h
/usr/lib64/openmpi/include/H5PTpublic.h
/usr/lib64/openmpi/include/H5Ppublic.h
/usr/lib64/openmpi/include/H5Rpublic.h
/usr/lib64/openmpi/include/H5Spublic.h
/usr/lib64/openmpi/include/H5TBpublic.h
/usr/lib64/openmpi/include/H5TSpublic.h
/usr/lib64/openmpi/include/H5Tpublic.h
/usr/lib64/openmpi/include/H5VLconnector.h
/usr/lib64/openmpi/include/H5VLconnector_passthru.h
/usr/lib64/openmpi/include/H5VLnative.h
/usr/lib64/openmpi/include/H5VLpassthru.h
/usr/lib64/openmpi/include/H5VLpublic.h
/usr/lib64/openmpi/include/H5Zpublic.h
/usr/lib64/openmpi/include/H5api_adpt.h
/usr/lib64/openmpi/include/H5f90i.h
/usr/lib64/openmpi/include/H5f90i_gen.h
/usr/lib64/openmpi/include/H5overflow.h
/usr/lib64/openmpi/include/H5pubconf.h
/usr/lib64/openmpi/include/H5public.h
/usr/lib64/openmpi/include/H5version.h
/usr/lib64/openmpi/include/h5_gen.mod
/usr/lib64/openmpi/include/h5a.mod
/usr/lib64/openmpi/include/h5d.mod
/usr/lib64/openmpi/include/h5ds.mod
/usr/lib64/openmpi/include/h5e.mod
/usr/lib64/openmpi/include/h5f.mod
/usr/lib64/openmpi/include/h5fortkit.mod
/usr/lib64/openmpi/include/h5fortran_types.mod
/usr/lib64/openmpi/include/h5g.mod
/usr/lib64/openmpi/include/h5global.mod
/usr/lib64/openmpi/include/h5i.mod
/usr/lib64/openmpi/include/h5im.mod
/usr/lib64/openmpi/include/h5l.mod
/usr/lib64/openmpi/include/h5lib.mod
/usr/lib64/openmpi/include/h5lt.mod
/usr/lib64/openmpi/include/h5lt_const.mod
/usr/lib64/openmpi/include/h5o.mod
/usr/lib64/openmpi/include/h5p.mod
/usr/lib64/openmpi/include/h5r.mod
/usr/lib64/openmpi/include/h5s.mod
/usr/lib64/openmpi/include/h5t.mod
/usr/lib64/openmpi/include/h5tb.mod
/usr/lib64/openmpi/include/h5tb_const.mod
/usr/lib64/openmpi/include/h5vl.mod
/usr/lib64/openmpi/include/h5z.mod
/usr/lib64/openmpi/include/hdf5.h
/usr/lib64/openmpi/include/hdf5.mod
/usr/lib64/openmpi/include/hdf5_hl.h
/usr/lib64/openmpi/lib/libhdf5.settings
/usr/lib64/openmpi/lib/libhdf5.so
/usr/lib64/openmpi/lib/libhdf5_fortran.so
/usr/lib64/openmpi/lib/libhdf5_hl.so
/usr/lib64/openmpi/lib/libhdf5_hl_fortran.so
/usr/lib64/openmpi/lib/libhdf5hl_fortran.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/haswell/libhdf5.so.1000
/usr/lib64/haswell/libhdf5.so.1000.0.0
/usr/lib64/haswell/libhdf5_fortran.so.1000
/usr/lib64/haswell/libhdf5_fortran.so.1000.0.0
/usr/lib64/haswell/libhdf5_hl.so.1000
/usr/lib64/haswell/libhdf5_hl.so.1000.0.0
/usr/lib64/haswell/libhdf5hl_fortran.so.1000
/usr/lib64/haswell/libhdf5hl_fortran.so.1000.0.0
/usr/lib64/libhdf5.so.1000
/usr/lib64/libhdf5.so.1000.0.0
/usr/lib64/libhdf5_cpp.so.1000
/usr/lib64/libhdf5_cpp.so.1000.0.0
/usr/lib64/libhdf5_fortran.so.1000
/usr/lib64/libhdf5_fortran.so.1000.0.0
/usr/lib64/libhdf5_hl.so.1000
/usr/lib64/libhdf5_hl.so.1000.0.0
/usr/lib64/libhdf5_hl_cpp.so.1000
/usr/lib64/libhdf5_hl_cpp.so.1000.0.0
/usr/lib64/libhdf5hl_fortran.so.1000
/usr/lib64/libhdf5hl_fortran.so.1000.0.0

%files openmpi
%defattr(-,root,root,-)
/usr/lib64/openmpi/bin/gif2h5
/usr/lib64/openmpi/bin/h52gif
/usr/lib64/openmpi/bin/h5clear
/usr/lib64/openmpi/bin/h5copy
/usr/lib64/openmpi/bin/h5debug
/usr/lib64/openmpi/bin/h5delete
/usr/lib64/openmpi/bin/h5diff
/usr/lib64/openmpi/bin/h5dump
/usr/lib64/openmpi/bin/h5format_convert
/usr/lib64/openmpi/bin/h5import
/usr/lib64/openmpi/bin/h5jam
/usr/lib64/openmpi/bin/h5ls
/usr/lib64/openmpi/bin/h5mkgrp
/usr/lib64/openmpi/bin/h5pcc
/usr/lib64/openmpi/bin/h5pfc
/usr/lib64/openmpi/bin/h5redeploy
/usr/lib64/openmpi/bin/h5repack
/usr/lib64/openmpi/bin/h5repart
/usr/lib64/openmpi/bin/h5stat
/usr/lib64/openmpi/bin/h5unjam
/usr/lib64/openmpi/bin/h5watch
/usr/lib64/openmpi/bin/mirror_server
/usr/lib64/openmpi/bin/mirror_server_stop
/usr/lib64/openmpi/bin/ph5diff
/usr/lib64/openmpi/lib/libhdf5.so.1000
/usr/lib64/openmpi/lib/libhdf5.so.1000.0.0
/usr/lib64/openmpi/lib/libhdf5_fortran.so.1000
/usr/lib64/openmpi/lib/libhdf5_fortran.so.1000.0.0
/usr/lib64/openmpi/lib/libhdf5_hl.so.1000
/usr/lib64/openmpi/lib/libhdf5_hl.so.1000.0.0
/usr/lib64/openmpi/lib/libhdf5hl_fortran.so.1000
/usr/lib64/openmpi/lib/libhdf5hl_fortran.so.1000.0.0
/usr/lib64/openmpi/share/hdf5_examples/README
/usr/lib64/openmpi/share/hdf5_examples/c/h5_attribute.c
/usr/lib64/openmpi/share/hdf5_examples/c/h5_chunk_read.c
/usr/lib64/openmpi/share/hdf5_examples/c/h5_cmprss.c
/usr/lib64/openmpi/share/hdf5_examples/c/h5_compound.c
/usr/lib64/openmpi/share/hdf5_examples/c/h5_crtatt.c
/usr/lib64/openmpi/share/hdf5_examples/c/h5_crtdat.c
/usr/lib64/openmpi/share/hdf5_examples/c/h5_crtgrp.c
/usr/lib64/openmpi/share/hdf5_examples/c/h5_crtgrpar.c
/usr/lib64/openmpi/share/hdf5_examples/c/h5_crtgrpd.c
/usr/lib64/openmpi/share/hdf5_examples/c/h5_debug_trace.c
/usr/lib64/openmpi/share/hdf5_examples/c/h5_drivers.c
/usr/lib64/openmpi/share/hdf5_examples/c/h5_elink_unix2win.c
/usr/lib64/openmpi/share/hdf5_examples/c/h5_extend.c
/usr/lib64/openmpi/share/hdf5_examples/c/h5_extend_write.c
/usr/lib64/openmpi/share/hdf5_examples/c/h5_extlink.c
/usr/lib64/openmpi/share/hdf5_examples/c/h5_group.c
/usr/lib64/openmpi/share/hdf5_examples/c/h5_mount.c
/usr/lib64/openmpi/share/hdf5_examples/c/h5_rdwt.c
/usr/lib64/openmpi/share/hdf5_examples/c/h5_read.c
/usr/lib64/openmpi/share/hdf5_examples/c/h5_ref2reg_deprec.c
/usr/lib64/openmpi/share/hdf5_examples/c/h5_ref_compat.c
/usr/lib64/openmpi/share/hdf5_examples/c/h5_ref_extern.c
/usr/lib64/openmpi/share/hdf5_examples/c/h5_reference_deprec.c
/usr/lib64/openmpi/share/hdf5_examples/c/h5_select.c
/usr/lib64/openmpi/share/hdf5_examples/c/h5_shared_mesg.c
/usr/lib64/openmpi/share/hdf5_examples/c/h5_subset.c
/usr/lib64/openmpi/share/hdf5_examples/c/h5_vds-eiger.c
/usr/lib64/openmpi/share/hdf5_examples/c/h5_vds-exc.c
/usr/lib64/openmpi/share/hdf5_examples/c/h5_vds-exclim.c
/usr/lib64/openmpi/share/hdf5_examples/c/h5_vds-percival-unlim-maxmin.c
/usr/lib64/openmpi/share/hdf5_examples/c/h5_vds-percival-unlim.c
/usr/lib64/openmpi/share/hdf5_examples/c/h5_vds-percival.c
/usr/lib64/openmpi/share/hdf5_examples/c/h5_vds-simpleIO.c
/usr/lib64/openmpi/share/hdf5_examples/c/h5_vds.c
/usr/lib64/openmpi/share/hdf5_examples/c/h5_write.c
/usr/lib64/openmpi/share/hdf5_examples/c/ph5example.c
/usr/lib64/openmpi/share/hdf5_examples/c/run-c-ex.sh
/usr/lib64/openmpi/share/hdf5_examples/fortran/compound.f90
/usr/lib64/openmpi/share/hdf5_examples/fortran/compound_complex_fortran2003.f90
/usr/lib64/openmpi/share/hdf5_examples/fortran/compound_fortran2003.f90
/usr/lib64/openmpi/share/hdf5_examples/fortran/h5_cmprss.f90
/usr/lib64/openmpi/share/hdf5_examples/fortran/h5_crtatt.f90
/usr/lib64/openmpi/share/hdf5_examples/fortran/h5_crtdat.f90
/usr/lib64/openmpi/share/hdf5_examples/fortran/h5_crtgrp.f90
/usr/lib64/openmpi/share/hdf5_examples/fortran/h5_crtgrpar.f90
/usr/lib64/openmpi/share/hdf5_examples/fortran/h5_crtgrpd.f90
/usr/lib64/openmpi/share/hdf5_examples/fortran/h5_extend.f90
/usr/lib64/openmpi/share/hdf5_examples/fortran/h5_rdwt.f90
/usr/lib64/openmpi/share/hdf5_examples/fortran/h5_subset.f90
/usr/lib64/openmpi/share/hdf5_examples/fortran/hyperslab.f90
/usr/lib64/openmpi/share/hdf5_examples/fortran/mountexample.f90
/usr/lib64/openmpi/share/hdf5_examples/fortran/nested_derived_type.f90
/usr/lib64/openmpi/share/hdf5_examples/fortran/ph5example.f90
/usr/lib64/openmpi/share/hdf5_examples/fortran/refobjexample.f90
/usr/lib64/openmpi/share/hdf5_examples/fortran/refregexample.f90
/usr/lib64/openmpi/share/hdf5_examples/fortran/run-fortran-ex.sh
/usr/lib64/openmpi/share/hdf5_examples/fortran/rwdset_fortran2003.f90
/usr/lib64/openmpi/share/hdf5_examples/fortran/selectele.f90
/usr/lib64/openmpi/share/hdf5_examples/hl/c/ex_ds1.c
/usr/lib64/openmpi/share/hdf5_examples/hl/c/ex_image1.c
/usr/lib64/openmpi/share/hdf5_examples/hl/c/ex_image2.c
/usr/lib64/openmpi/share/hdf5_examples/hl/c/ex_lite1.c
/usr/lib64/openmpi/share/hdf5_examples/hl/c/ex_lite2.c
/usr/lib64/openmpi/share/hdf5_examples/hl/c/ex_lite3.c
/usr/lib64/openmpi/share/hdf5_examples/hl/c/ex_table_01.c
/usr/lib64/openmpi/share/hdf5_examples/hl/c/ex_table_02.c
/usr/lib64/openmpi/share/hdf5_examples/hl/c/ex_table_03.c
/usr/lib64/openmpi/share/hdf5_examples/hl/c/ex_table_04.c
/usr/lib64/openmpi/share/hdf5_examples/hl/c/ex_table_05.c
/usr/lib64/openmpi/share/hdf5_examples/hl/c/ex_table_06.c
/usr/lib64/openmpi/share/hdf5_examples/hl/c/ex_table_07.c
/usr/lib64/openmpi/share/hdf5_examples/hl/c/ex_table_08.c
/usr/lib64/openmpi/share/hdf5_examples/hl/c/ex_table_09.c
/usr/lib64/openmpi/share/hdf5_examples/hl/c/ex_table_10.c
/usr/lib64/openmpi/share/hdf5_examples/hl/c/ex_table_11.c
/usr/lib64/openmpi/share/hdf5_examples/hl/c/ex_table_12.c
/usr/lib64/openmpi/share/hdf5_examples/hl/c/image24pixel.txt
/usr/lib64/openmpi/share/hdf5_examples/hl/c/image8.txt
/usr/lib64/openmpi/share/hdf5_examples/hl/c/pal_rgb.h
/usr/lib64/openmpi/share/hdf5_examples/hl/c/ptExampleFL.c
/usr/lib64/openmpi/share/hdf5_examples/hl/c/run-hlc-ex.sh
/usr/lib64/openmpi/share/hdf5_examples/hl/fortran/ex_ds1.f90
/usr/lib64/openmpi/share/hdf5_examples/hl/fortran/exlite.f90
/usr/lib64/openmpi/share/hdf5_examples/hl/fortran/run-hlfortran-ex.sh
/usr/lib64/openmpi/share/hdf5_examples/hl/run-hl-ex.sh
/usr/lib64/openmpi/share/hdf5_examples/run-all-ex.sh

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libhdf5.a
/usr/lib64/libhdf5_cpp.a
/usr/lib64/libhdf5_fortran.a
/usr/lib64/libhdf5_hl.a
/usr/lib64/libhdf5_hl_cpp.a
/usr/lib64/libhdf5_hl_fortran.a
/usr/lib64/libhdf5hl_fortran.a
