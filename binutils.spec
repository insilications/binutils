#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x13FCEF89DD9E3C4F (nickc@redhat.com)
#
Name     : binutils
Version  : 2.33.1
Release  : 324
URL      : https://mirrors.kernel.org/gnu/binutils/binutils-2.33.1.tar.xz
Source0  : https://mirrors.kernel.org/gnu/binutils/binutils-2.33.1.tar.xz
Source1 : https://mirrors.kernel.org/gnu/binutils/binutils-2.33.1.tar.xz.sig
Summary  : zlib compression library
Group    : Development/Tools
License  : BSL-1.0 GPL-2.0 GPL-3.0 GPL-3.0+ LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: binutils-bin = %{version}-%{release}
Requires: binutils-lib = %{version}-%{release}
Requires: binutils-license = %{version}-%{release}
Requires: binutils-locales = %{version}-%{release}
Requires: binutils-man = %{version}-%{release}
BuildRequires : bison
BuildRequires : dejagnu
BuildRequires : expect
BuildRequires : flex
BuildRequires : gawk
BuildRequires : gettext
BuildRequires : grep
BuildRequires : sed
BuildRequires : texinfo
BuildRequires : util-linux
BuildRequires : zlib-dev
Patch1: binutils-stable-branch.patch
Patch2: binutils-add-LD_AS_NEEDED-global-env.patch
Patch3: CVE-2019-17450.patch
Patch4: CVE-2019-17451.patch
Patch5: 0001-gas-Add-md_cons_worker.patch
Patch6: 0002-gas-Add-md_generic_table_relax_frag.patch
Patch7: 0003-i386-Align-branches-within-a-fixed-boundary.patch
Patch8: 0004-i386-Add-mbranches-within-32B-boundaries.patch

%description
These are the GNU binutils.  These are utilities of use when dealing
with binary files, either object files or executables.  These tools
consist of the linker (ld), the assembler (gas), and the profiler
(gprof) each of which have their own sub-directory named after them.
There is also a collection of other binary tools, including the
disassembler (objdump) in this directory.  These tools make use of a
pair of libraries (bfd and opcodes) and a common set of header files
(include).

%package bin
Summary: bin components for the binutils package.
Group: Binaries
Requires: binutils-license = %{version}-%{release}

%description bin
bin components for the binutils package.


%package dev
Summary: dev components for the binutils package.
Group: Development
Requires: binutils-lib = %{version}-%{release}
Requires: binutils-bin = %{version}-%{release}
Provides: binutils-devel = %{version}-%{release}
Requires: binutils = %{version}-%{release}
Requires: binutils = %{version}-%{release}

%description dev
dev components for the binutils package.


%package doc
Summary: doc components for the binutils package.
Group: Documentation
Requires: binutils-man = %{version}-%{release}

%description doc
doc components for the binutils package.


%package extras
Summary: extras components for the binutils package.
Group: Default

%description extras
extras components for the binutils package.


%package lib
Summary: lib components for the binutils package.
Group: Libraries
Requires: binutils-license = %{version}-%{release}

%description lib
lib components for the binutils package.


%package license
Summary: license components for the binutils package.
Group: Default

%description license
license components for the binutils package.


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
Requires: binutils-dev = %{version}-%{release}

%description staticdev
staticdev components for the binutils package.


%prep
%setup -q -n binutils-2.33.1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

%build
## build_prepend content
rm -rf gdb libdecnumber readline sim
export SOURCE_DATE_EPOCH=1549215809
sed -i -e "s/#define BFD_VERSION_DATE.*/#define BFD_VERSION_DATE 20190203/g" bfd/version.h
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
--with-system-zlib
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1573094690
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fcf-protection=full -ffat-lto-objects -flto=4 -fstack-protector-strong "
export FCFLAGS="$CFLAGS -O3 -fcf-protection=full -ffat-lto-objects -flto=4 -fstack-protector-strong "
export FFLAGS="$CFLAGS -O3 -fcf-protection=full -ffat-lto-objects -flto=4 -fstack-protector-strong "
export CXXFLAGS="$CXXFLAGS -O3 -fcf-protection=full -ffat-lto-objects -flto=4 -fstack-protector-strong "
make  %{?_smp_mflags}  tooldir=/usr


%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_flags} check tooldir=/usr || :

%install
export SOURCE_DATE_EPOCH=1573094690
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/binutils
cp %{_builddir}/binutils-2.33.1/COPYING %{buildroot}/usr/share/package-licenses/binutils/68c94ffc34f8ad2d7bfae3f5a6b996409211c1b1
cp %{_builddir}/binutils-2.33.1/COPYING.LIB %{buildroot}/usr/share/package-licenses/binutils/0e8e850b0580fbaaa0872326cb1b8ad6adda9b0d
cp %{_builddir}/binutils-2.33.1/COPYING3 %{buildroot}/usr/share/package-licenses/binutils/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/binutils-2.33.1/COPYING3.LIB %{buildroot}/usr/share/package-licenses/binutils/e7d563f52bf5295e6dba1d67ac23e9f6a160fab9
cp %{_builddir}/binutils-2.33.1/bfd/COPYING %{buildroot}/usr/share/package-licenses/binutils/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/binutils-2.33.1/gas/COPYING %{buildroot}/usr/share/package-licenses/binutils/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/binutils-2.33.1/include/COPYING %{buildroot}/usr/share/package-licenses/binutils/68c94ffc34f8ad2d7bfae3f5a6b996409211c1b1
cp %{_builddir}/binutils-2.33.1/include/COPYING3 %{buildroot}/usr/share/package-licenses/binutils/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/binutils-2.33.1/libiberty/COPYING.LIB %{buildroot}/usr/share/package-licenses/binutils/597bf5f9c0904bd6c48ac3a3527685818d11246d
cp %{_builddir}/binutils-2.33.1/libiberty/copying-lib.texi %{buildroot}/usr/share/package-licenses/binutils/cdb23577fa4523cc88845280fd5223270ddb645a
cp %{_builddir}/binutils-2.33.1/zlib/contrib/dotzlib/LICENSE_1_0.txt %{buildroot}/usr/share/package-licenses/binutils/892b34f7865d90a6f949f50d95e49625a10bc7f0
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
install -m 0644 libiberty/libiberty.a %{buildroot}/usr/lib64
install -m 644 include/ansidecl.h %{buildroot}/usr/include/
install -m 644 include/libiberty.h %{buildroot}/usr/include/
install -m 644 include/plugin-api.h %{buildroot}/usr/include/
install -d %{buildroot}/usr/include/libiberty
install -m 644 include/*.h %{buildroot}/usr/include/libiberty/
## install_append end

%files
%defattr(-,root,root,-)
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

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/info/*

%files extras
%defattr(-,root,root,-)
/usr/bin/ld.gold

%files lib
%defattr(-,root,root,-)
/usr/lib64/libbfd-2.33.1.20190203.so
/usr/lib64/libbfd.so
/usr/lib64/libopcodes-2.33.1.20190203.so
/usr/lib64/libopcodes.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/binutils/0e8e850b0580fbaaa0872326cb1b8ad6adda9b0d
/usr/share/package-licenses/binutils/597bf5f9c0904bd6c48ac3a3527685818d11246d
/usr/share/package-licenses/binutils/68c94ffc34f8ad2d7bfae3f5a6b996409211c1b1
/usr/share/package-licenses/binutils/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/binutils/892b34f7865d90a6f949f50d95e49625a10bc7f0
/usr/share/package-licenses/binutils/cdb23577fa4523cc88845280fd5223270ddb645a
/usr/share/package-licenses/binutils/e7d563f52bf5295e6dba1d67ac23e9f6a160fab9

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

