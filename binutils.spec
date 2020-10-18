#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : binutils
Version  : 2.35.1
Release  : 389
URL      : https://mirrors.kernel.org/gnu/binutils/binutils-2.35.1.tar.xz
Source0  : https://mirrors.kernel.org/gnu/binutils/binutils-2.35.1.tar.xz
Summary  : zlib compression library
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0 GPL-3.0+ LGPL-2.0 LGPL-2.1
Requires: binutils-bin = %{version}-%{release}
Requires: binutils-info = %{version}-%{release}
Requires: binutils-lib = %{version}-%{release}
Requires: binutils-locales = %{version}-%{release}
Requires: binutils-man = %{version}-%{release}
BuildRequires : bison
BuildRequires : dejagnu
BuildRequires : expect
BuildRequires : flex
BuildRequires : gettext
BuildRequires : grep
BuildRequires : sed
BuildRequires : texinfo
BuildRequires : zlib-dev
BuildRequires : zlib-staticdev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: binutils-stable-branch.patch
Patch2: binutils-add-LD_AS_NEEDED-global-env.patch

%description
This directory contains various GNU compilers, assemblers, linkers,
debuggers, etc., plus their support routines, definitions, and documentation.

%package bin
Summary: bin components for the binutils package.
Group: Binaries

%description bin
bin components for the binutils package.


%package dev
Summary: dev components for the binutils package.
Group: Development
Requires: binutils-lib = %{version}-%{release}
Requires: binutils-bin = %{version}-%{release}
Provides: binutils-devel = %{version}-%{release}
Requires: binutils = %{version}-%{release}

%description dev
dev components for the binutils package.


%package extras
Summary: extras components for the binutils package.
Group: Default

%description extras
extras components for the binutils package.


%package info
Summary: info components for the binutils package.
Group: Default

%description info
info components for the binutils package.


%package lib
Summary: lib components for the binutils package.
Group: Libraries

%description lib
lib components for the binutils package.


%package locales
Summary: locales components for the binutils package.
Group: Default

%description locales
locales components for the binutils package.


%package man
Summary: man components for the binutils package.
Group: Default

%description man
man components for the binutils package.


%package staticdev
Summary: staticdev components for the binutils package.
Group: Default
Requires: binutils-dev = %{version}-%{release}

%description staticdev
staticdev components for the binutils package.


%prep
%setup -q -n binutils-2.35.1
cd %{_builddir}/binutils-2.35.1
%patch1 -p1
%patch2 -p1

%build
## build_prepend content
rm -rf gdb libdecnumber readline sim
export SOURCE_DATE_EPOCH=1549215809
sed -i -e "s/#define BFD_VERSION_DATE.*/#define BFD_VERSION_DATE 20190203/g" bfd/version.h
## build_prepend end
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1602977673
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
## altflags_pgo content
## pgo generate
export PGO_GEN="-fprofile-generate=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-update=atomic -fprofile-arcs -ftest-coverage --coverage -fprofile-partial-training"
export CFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -flto=16 -fPIC $PGO_GEN"
export FCFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -flto=16 -fPIC $PGO_GEN"
export FFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -flto=16 -fPIC $PGO_GEN"
export CXXFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -fvisibility-inlines-hidden -pipe -ffat-lto-objects -flto=16 -fPIC $PGO_GEN"
export LDFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -flto=16 -fPIC $PGO_GEN"
## pgo use
## -ffat-lto-objects -fno-PIE -fno-PIE -m64 -no-pie -fpic -fvisibility=hidden -flto-partition=none
## gcc: -feliminate-unused-debug-types -fipa-pta -flto=16 -Wno-error -Wp,-D_REENTRANT -fno-common
export PGO_USE="-fprofile-use=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-correction -fprofile-partial-training --coverage"
export CFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC $PGO_USE"
export FCFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC $PGO_USE"
export FFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC $PGO_USE"
export CXXFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC $PGO_USE"
export LDFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC $PGO_USE"
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
#
export MAKEFLAGS=%{?_smp_mflags}
#
%global _lto_cflags 1
#global _lto_cflags %{nil}
#
# export PATH="/usr/lib64/ccache/bin:$PATH"
# export CCACHE_NOHASHDIR=1
# export CCACHE_DIRECT=1
# export CCACHE_SLOPPINESS=pch_defines,locale,time_macros
# export CCACHE_DISABLE=1
## altflags_pgo end
##
%global _lto_cflags 1
##
export CFLAGS="${CFLAGS_GENERATE}"
export CXXFLAGS="${CXXFLAGS_GENERATE}"
export FFLAGS="${FFLAGS_GENERATE}"
export FCFLAGS="${FCFLAGS_GENERATE}"
export LDFLAGS="${LDFLAGS_GENERATE}"
## make_prepend content
# Do not use a macro - breaks toolchain
./configure \
--prefix=/usr \
--libdir=/usr/lib64 \
--includedir=/usr/include \
--with-lib-path=/usr/lib64:/usr/lib32:/usr/lib \
--enable-shared --disable-static \
--target=x86_64-generic-linux \
--build=x86_64-generic-linux \
--enable-targets=i386-linux,x86_64-linux \
--enable-deterministic-archives \
--enable-lto \
--enable-plugins \
--enable-gold \
--enable-secureplt \
--disable-werror \
--enable-64-bit-bfd \
--with-system-zlib \
--without-debuginfod
## make_prepend end
make  %{?_smp_mflags}  tooldir=/usr V=1 VERBOSE=1

make -j1 check tooldir=/usr V=1 VERBOSE=1 || :
make distclean || : 
find . -type f -name 'config.cache' -exec rm {} \;
export CFLAGS="${CFLAGS_USE}"
export CXXFLAGS="${CXXFLAGS_USE}"
export FFLAGS="${FFLAGS_USE}"
export FCFLAGS="${FCFLAGS_USE}"
export LDFLAGS="${LDFLAGS_USE}"
## make_prepend content
# Do not use a macro - breaks toolchain
./configure \
--prefix=/usr \
--libdir=/usr/lib64 \
--includedir=/usr/include \
--with-lib-path=/usr/lib64:/usr/lib32:/usr/lib \
--enable-shared --disable-static \
--target=x86_64-generic-linux \
--build=x86_64-generic-linux \
--enable-targets=i386-linux,x86_64-linux \
--enable-deterministic-archives \
--enable-lto \
--enable-plugins \
--enable-gold \
--enable-secureplt \
--disable-werror \
--enable-64-bit-bfd \
--with-system-zlib \
--without-debuginfod
## make_prepend end
make  %{?_smp_mflags}  tooldir=/usr V=1 VERBOSE=1


%check
export LANG=C.UTF-8
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
make %{?_smp_flags} check tooldir=/usr V=1 VERBOSE=1 || :

%install
export SOURCE_DATE_EPOCH=1602977673
rm -rf %{buildroot}
%make_install tooldir=/usr
%find_lang binutils
%find_lang gprof
%find_lang ld
%find_lang bfd
%find_lang opcodes
%find_lang gas
%find_lang gold
## install_append content
install -d %{buildroot}/usr/include

# Manually install libiberty - can be fixed post glibc/gcc fixups
install -m 0644 libiberty/libiberty.a %{buildroot}/usr/lib64

# Find out who is using these headers and reduce their usage.
install -m 644 include/ansidecl.h %{buildroot}/usr/include/
install -m 644 include/libiberty.h %{buildroot}/usr/include/
install -m 644 include/plugin-api.h %{buildroot}/usr/include/

install -d %{buildroot}/usr/include/libiberty
install -m 644 include/*.h %{buildroot}/usr/include/libiberty/
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/addr2line
/usr/bin/ar
/usr/bin/as
/usr/bin/c++filt
/usr/bin/dwp
/usr/bin/elfedit
/usr/bin/gprof
/usr/bin/ld
/usr/bin/ld.bfd
/usr/bin/nm
/usr/bin/objcopy
/usr/bin/objdump
/usr/bin/ranlib
/usr/bin/readelf
/usr/bin/size
/usr/bin/strings
/usr/bin/strip

%files dev
%defattr(-,root,root,-)
/usr/include/ansidecl.h
/usr/include/bfd.h
/usr/include/bfd_stdint.h
/usr/include/bfdlink.h
/usr/include/ctf-api.h
/usr/include/ctf.h
/usr/include/diagnostics.h
/usr/include/dis-asm.h
/usr/include/libiberty.h
/usr/include/libiberty/alloca-conf.h
/usr/include/libiberty/ansidecl.h
/usr/include/libiberty/bfdlink.h
/usr/include/libiberty/binary-io.h
/usr/include/libiberty/bout.h
/usr/include/libiberty/ctf-api.h
/usr/include/libiberty/ctf.h
/usr/include/libiberty/demangle.h
/usr/include/libiberty/diagnostics.h
/usr/include/libiberty/dis-asm.h
/usr/include/libiberty/dwarf2.h
/usr/include/libiberty/dyn-string.h
/usr/include/libiberty/environ.h
/usr/include/libiberty/fibheap.h
/usr/include/libiberty/filenames.h
/usr/include/libiberty/floatformat.h
/usr/include/libiberty/fnmatch.h
/usr/include/libiberty/fopen-bin.h
/usr/include/libiberty/fopen-same.h
/usr/include/libiberty/fopen-vms.h
/usr/include/libiberty/gcc-c-interface.h
/usr/include/libiberty/gcc-cp-interface.h
/usr/include/libiberty/gcc-interface.h
/usr/include/libiberty/getopt.h
/usr/include/libiberty/hashtab.h
/usr/include/libiberty/hp-symtab.h
/usr/include/libiberty/leb128.h
/usr/include/libiberty/libiberty.h
/usr/include/libiberty/longlong.h
/usr/include/libiberty/lto-symtab.h
/usr/include/libiberty/md5.h
/usr/include/libiberty/oasys.h
/usr/include/libiberty/objalloc.h
/usr/include/libiberty/obstack.h
/usr/include/libiberty/os9k.h
/usr/include/libiberty/partition.h
/usr/include/libiberty/plugin-api.h
/usr/include/libiberty/progress.h
/usr/include/libiberty/safe-ctype.h
/usr/include/libiberty/sha1.h
/usr/include/libiberty/simple-object.h
/usr/include/libiberty/sort.h
/usr/include/libiberty/splay-tree.h
/usr/include/libiberty/symcat.h
/usr/include/libiberty/timeval-utils.h
/usr/include/libiberty/vtv-change-permission.h
/usr/include/libiberty/xregex.h
/usr/include/libiberty/xregex2.h
/usr/include/libiberty/xtensa-config.h
/usr/include/libiberty/xtensa-isa-internal.h
/usr/include/libiberty/xtensa-isa.h
/usr/include/plugin-api.h
/usr/include/symcat.h
/usr/lib/ldscripts/elf32_x86_64.x
/usr/lib/ldscripts/elf32_x86_64.xbn
/usr/lib/ldscripts/elf32_x86_64.xc
/usr/lib/ldscripts/elf32_x86_64.xce
/usr/lib/ldscripts/elf32_x86_64.xd
/usr/lib/ldscripts/elf32_x86_64.xdc
/usr/lib/ldscripts/elf32_x86_64.xdce
/usr/lib/ldscripts/elf32_x86_64.xde
/usr/lib/ldscripts/elf32_x86_64.xdw
/usr/lib/ldscripts/elf32_x86_64.xdwe
/usr/lib/ldscripts/elf32_x86_64.xe
/usr/lib/ldscripts/elf32_x86_64.xn
/usr/lib/ldscripts/elf32_x86_64.xr
/usr/lib/ldscripts/elf32_x86_64.xs
/usr/lib/ldscripts/elf32_x86_64.xsc
/usr/lib/ldscripts/elf32_x86_64.xsce
/usr/lib/ldscripts/elf32_x86_64.xse
/usr/lib/ldscripts/elf32_x86_64.xsw
/usr/lib/ldscripts/elf32_x86_64.xswe
/usr/lib/ldscripts/elf32_x86_64.xu
/usr/lib/ldscripts/elf32_x86_64.xw
/usr/lib/ldscripts/elf32_x86_64.xwe
/usr/lib/ldscripts/elf_i386.x
/usr/lib/ldscripts/elf_i386.xbn
/usr/lib/ldscripts/elf_i386.xc
/usr/lib/ldscripts/elf_i386.xce
/usr/lib/ldscripts/elf_i386.xd
/usr/lib/ldscripts/elf_i386.xdc
/usr/lib/ldscripts/elf_i386.xdce
/usr/lib/ldscripts/elf_i386.xde
/usr/lib/ldscripts/elf_i386.xdw
/usr/lib/ldscripts/elf_i386.xdwe
/usr/lib/ldscripts/elf_i386.xe
/usr/lib/ldscripts/elf_i386.xn
/usr/lib/ldscripts/elf_i386.xr
/usr/lib/ldscripts/elf_i386.xs
/usr/lib/ldscripts/elf_i386.xsc
/usr/lib/ldscripts/elf_i386.xsce
/usr/lib/ldscripts/elf_i386.xse
/usr/lib/ldscripts/elf_i386.xsw
/usr/lib/ldscripts/elf_i386.xswe
/usr/lib/ldscripts/elf_i386.xu
/usr/lib/ldscripts/elf_i386.xw
/usr/lib/ldscripts/elf_i386.xwe
/usr/lib/ldscripts/elf_iamcu.x
/usr/lib/ldscripts/elf_iamcu.xbn
/usr/lib/ldscripts/elf_iamcu.xc
/usr/lib/ldscripts/elf_iamcu.xce
/usr/lib/ldscripts/elf_iamcu.xd
/usr/lib/ldscripts/elf_iamcu.xdc
/usr/lib/ldscripts/elf_iamcu.xdce
/usr/lib/ldscripts/elf_iamcu.xde
/usr/lib/ldscripts/elf_iamcu.xdw
/usr/lib/ldscripts/elf_iamcu.xdwe
/usr/lib/ldscripts/elf_iamcu.xe
/usr/lib/ldscripts/elf_iamcu.xn
/usr/lib/ldscripts/elf_iamcu.xr
/usr/lib/ldscripts/elf_iamcu.xs
/usr/lib/ldscripts/elf_iamcu.xsc
/usr/lib/ldscripts/elf_iamcu.xsce
/usr/lib/ldscripts/elf_iamcu.xse
/usr/lib/ldscripts/elf_iamcu.xsw
/usr/lib/ldscripts/elf_iamcu.xswe
/usr/lib/ldscripts/elf_iamcu.xu
/usr/lib/ldscripts/elf_iamcu.xw
/usr/lib/ldscripts/elf_iamcu.xwe
/usr/lib/ldscripts/elf_k1om.x
/usr/lib/ldscripts/elf_k1om.xbn
/usr/lib/ldscripts/elf_k1om.xc
/usr/lib/ldscripts/elf_k1om.xce
/usr/lib/ldscripts/elf_k1om.xd
/usr/lib/ldscripts/elf_k1om.xdc
/usr/lib/ldscripts/elf_k1om.xdce
/usr/lib/ldscripts/elf_k1om.xde
/usr/lib/ldscripts/elf_k1om.xdw
/usr/lib/ldscripts/elf_k1om.xdwe
/usr/lib/ldscripts/elf_k1om.xe
/usr/lib/ldscripts/elf_k1om.xn
/usr/lib/ldscripts/elf_k1om.xr
/usr/lib/ldscripts/elf_k1om.xs
/usr/lib/ldscripts/elf_k1om.xsc
/usr/lib/ldscripts/elf_k1om.xsce
/usr/lib/ldscripts/elf_k1om.xse
/usr/lib/ldscripts/elf_k1om.xsw
/usr/lib/ldscripts/elf_k1om.xswe
/usr/lib/ldscripts/elf_k1om.xu
/usr/lib/ldscripts/elf_k1om.xw
/usr/lib/ldscripts/elf_k1om.xwe
/usr/lib/ldscripts/elf_l1om.x
/usr/lib/ldscripts/elf_l1om.xbn
/usr/lib/ldscripts/elf_l1om.xc
/usr/lib/ldscripts/elf_l1om.xce
/usr/lib/ldscripts/elf_l1om.xd
/usr/lib/ldscripts/elf_l1om.xdc
/usr/lib/ldscripts/elf_l1om.xdce
/usr/lib/ldscripts/elf_l1om.xde
/usr/lib/ldscripts/elf_l1om.xdw
/usr/lib/ldscripts/elf_l1om.xdwe
/usr/lib/ldscripts/elf_l1om.xe
/usr/lib/ldscripts/elf_l1om.xn
/usr/lib/ldscripts/elf_l1om.xr
/usr/lib/ldscripts/elf_l1om.xs
/usr/lib/ldscripts/elf_l1om.xsc
/usr/lib/ldscripts/elf_l1om.xsce
/usr/lib/ldscripts/elf_l1om.xse
/usr/lib/ldscripts/elf_l1om.xsw
/usr/lib/ldscripts/elf_l1om.xswe
/usr/lib/ldscripts/elf_l1om.xu
/usr/lib/ldscripts/elf_l1om.xw
/usr/lib/ldscripts/elf_l1om.xwe
/usr/lib/ldscripts/elf_x86_64.x
/usr/lib/ldscripts/elf_x86_64.xbn
/usr/lib/ldscripts/elf_x86_64.xc
/usr/lib/ldscripts/elf_x86_64.xce
/usr/lib/ldscripts/elf_x86_64.xd
/usr/lib/ldscripts/elf_x86_64.xdc
/usr/lib/ldscripts/elf_x86_64.xdce
/usr/lib/ldscripts/elf_x86_64.xde
/usr/lib/ldscripts/elf_x86_64.xdw
/usr/lib/ldscripts/elf_x86_64.xdwe
/usr/lib/ldscripts/elf_x86_64.xe
/usr/lib/ldscripts/elf_x86_64.xn
/usr/lib/ldscripts/elf_x86_64.xr
/usr/lib/ldscripts/elf_x86_64.xs
/usr/lib/ldscripts/elf_x86_64.xsc
/usr/lib/ldscripts/elf_x86_64.xsce
/usr/lib/ldscripts/elf_x86_64.xse
/usr/lib/ldscripts/elf_x86_64.xsw
/usr/lib/ldscripts/elf_x86_64.xswe
/usr/lib/ldscripts/elf_x86_64.xu
/usr/lib/ldscripts/elf_x86_64.xw
/usr/lib/ldscripts/elf_x86_64.xwe

%files extras
%defattr(-,root,root,-)
/usr/bin/ld.gold

%files info
%defattr(0644,root,root,0755)
/usr/share/info/as.info
/usr/share/info/bfd.info
/usr/share/info/binutils.info
/usr/share/info/gprof.info
/usr/share/info/ld.info

%files lib
%defattr(-,root,root,-)
/usr/lib64/libbfd-2.35.1.20190203.so
/usr/lib64/libbfd.so
/usr/lib64/libctf-nobfd.so
/usr/lib64/libctf-nobfd.so.0
/usr/lib64/libctf-nobfd.so.0.0.0
/usr/lib64/libctf.so
/usr/lib64/libctf.so.0
/usr/lib64/libctf.so.0.0.0
/usr/lib64/libopcodes-2.35.1.20190203.so
/usr/lib64/libopcodes.so

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/addr2line.1
/usr/share/man/man1/ar.1
/usr/share/man/man1/as.1
/usr/share/man/man1/c++filt.1
/usr/share/man/man1/dlltool.1
/usr/share/man/man1/elfedit.1
/usr/share/man/man1/gprof.1
/usr/share/man/man1/ld.1
/usr/share/man/man1/nm.1
/usr/share/man/man1/objcopy.1
/usr/share/man/man1/objdump.1
/usr/share/man/man1/ranlib.1
/usr/share/man/man1/readelf.1
/usr/share/man/man1/size.1
/usr/share/man/man1/strings.1
/usr/share/man/man1/strip.1
/usr/share/man/man1/windmc.1
/usr/share/man/man1/windres.1

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libiberty.a

%files locales -f binutils.lang -f gprof.lang -f ld.lang -f bfd.lang -f opcodes.lang -f gas.lang -f gold.lang
%defattr(-,root,root,-)

