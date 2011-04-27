# functions with printf format attribute but with special parser and also
# receiving non constant format strings
%define		Werror_cflags			%{nil}

# avoid failures when testing if compiler used to build gcc can generate
# shared objects (regardless of unresolved symbols)
%define		_disable_ld_no_undefined	1

# avoid build failure due to configure built with different autoconf version
%define		_disable_libtoolize		1

#-----------------------------------------------------------------------
%define		target		arm-none-linux-gnueabi
%define		full_version	2010.09-50
%define		prefix		%{_prefix}/%{target}
%define 	build_sysroot	%{_builddir}/arm-%{full_version}-%{target}/sysroot
%define 	sysroot		%{_prefix}/arm-%{full_version}-%{target}
%define		gccdir		%{_libdir}/gcc/%{target}/4.5.1

Name:		cross-arm
Release:	1
Version:	2010.09
License:	GPLv3+
Group:		Development/Other
Summary:	Sourcery G++ Lite for ARM GNU/Linux
# 841081740c155016364bcd979b5c06e9
Source0:	http://www.codesourcery.com/sgpp/lite/arm/portal/package7850/public/arm-none-linux-gnueabi/arm-2010.09-50-arm-none-linux-gnueabi.src.tar.bz2
Source1:	http://www.codesourcery.com/sgpp/lite/arm/portal/doc9947/getting-started.pdf
Buildroot:	%{_tmppath}/%{name}-%{version}-root

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	binutils-devel
BuildRequires:	bison
BuildRequires:	elfutils-devel
BuildRequires:	flex
BuildRequires:	gcc
BuildRequires:	gmp-devel
BuildRequires:	mpfr-devel
BuildRequires:	libmpc-devel
BuildRequires:	gettext
BuildRequires:	texinfo
BuildRequires:	texlive

Patch0:		cross-arm-glibc.patch
Patch1:		cross-arm-libgcc.patch

%description
Sourcery G++ Lite for ARM GNU/Linux is intended for developers working on
embedded GNU/Linux applications. It may also be used for Linux kernel
development and debugging, or to build a GNU/Linux distribution.

#-----------------------------------------------------------------------
%package	binutils
Summary:	binutils Sourcery G++ Lite for ARM GNU/Linux

%description	binutils
binutils Sourcery G++ Lite for ARM GNU/Linux.

%files		binutils
%defattr(-,root,root,-)
%{_bindir}/%{target}-addr2line
%{_bindir}/%{target}-ar
%{_bindir}/%{target}-as
%{_bindir}/%{target}-c++filt
%{_bindir}/%{target}-elfedit
%{_bindir}/%{target}-gprof
%{_bindir}/%{target}-ld
%{_bindir}/%{target}-nm
%{_bindir}/%{target}-objcopy
%{_bindir}/%{target}-objdump
%{_bindir}/%{target}-ranlib
%{_bindir}/%{target}-readelf
%{_bindir}/%{target}-size
%{_bindir}/%{target}-strings
%{_bindir}/%{target}-strip
%{_mandir}/man1/%{target}-addr2line.1*
%{_mandir}/man1/%{target}-ar.1*
%{_mandir}/man1/%{target}-as.1*
%{_mandir}/man1/%{target}-c++filt.1*
%{_mandir}/man1/%{target}-elfedit.1*
%{_mandir}/man1/%{target}-gprof.1*
%{_mandir}/man1/%{target}-ld.1*
%{_mandir}/man1/%{target}-nm.1*
%{_mandir}/man1/%{target}-objcopy.1*
%{_mandir}/man1/%{target}-objdump.1*
%{_mandir}/man1/%{target}-ranlib.1*
%{_mandir}/man1/%{target}-readelf.1*
%{_mandir}/man1/%{target}-size.1*
%{_mandir}/man1/%{target}-strings.1*
%{_mandir}/man1/%{target}-strip.1*
%{prefix}/bin/ar
%{prefix}/bin/as
%{prefix}/bin/ld
%{prefix}/bin/nm
%{prefix}/bin/objcopy
%{prefix}/bin/objdump
%{prefix}/bin/ranlib
%{prefix}/bin/strip
%{prefix}/lib/ldscripts

#-----------------------------------------------------------------------
%package	gcc
Summary:	gcc Sourcery G++ Lite for ARM GNU/Linux

%description	gcc
gcc Sourcery G++ Lite for ARM GNU/Linux.

%files		gcc
%defattr(-,root,root,-)
%{_bindir}/%{target}-cpp
%{_bindir}/%{target}-gcc
%{_bindir}/%{target}-gcc-4.5.1
%{_bindir}/%{target}-gccbug
%{_bindir}/%{target}-gcov
%{gccdir}/armv4t/crtbegin.o
%{gccdir}/armv4t/crtbeginS.o
%{gccdir}/armv4t/crtbeginT.o
%{gccdir}/armv4t/crtend.o
%{gccdir}/armv4t/crtendS.o
%{gccdir}/armv4t/libgcc.a
%{gccdir}/armv4t/libgcov.a
%{gccdir}/cc1
%{gccdir}/collect2
%{gccdir}/crtbegin.o
%{gccdir}/crtbeginS.o
%{gccdir}/crtbeginT.o
%{gccdir}/crtend.o
%{gccdir}/crtendS.o
%{gccdir}/include/arm_neon.h
%{gccdir}/include/float.h
%{gccdir}/include/iso646.h
%{gccdir}/include/limits.h
%{gccdir}/include/mmintrin.h
%{gccdir}/include/stdarg.h
%{gccdir}/include/stdbool.h
%{gccdir}/include/stddef.h
%{gccdir}/include/stdfix.h
%{gccdir}/include/stdint-gcc.h
%{gccdir}/include/stdint.h
%{gccdir}/include/syslimits.h
%{gccdir}/include/unwind.h
%{gccdir}/include/varargs.h
%{gccdir}/libgcc.a
%{gccdir}/libgcov.a
%{gccdir}/lto1
%{gccdir}/thumb2/crtbegin.o
%{gccdir}/thumb2/crtbeginS.o
%{gccdir}/thumb2/crtbeginT.o
%{gccdir}/thumb2/crtend.o
%{gccdir}/thumb2/crtendS.o
%{gccdir}/thumb2/libgcc.a
%{gccdir}/thumb2/libgcov.a
%{prefix}/bin/gcc

#-----------------------------------------------------------------------
%package	glibc
Summary:	glibc Sourcery G++ Lite for ARM GNU/Linux

%description	glibc
glibc Sourcery G++ Lite for ARM GNU/Linux.

%files		glibc
%defattr(-,root,root,-)
%{prefix}/include
%{prefix}/lib

#-----------------------------------------------------------------------
%prep
%setup -q -n arm-%{full_version}-%{target}
tar jxf binutils-%{full_version}.tar.bz2
mkdir -p binutils-%{version}/build
tar jxf linux-%{full_version}.tar.bz2
tar jxf glibc-%{full_version}.tar.bz2
mkdir -p glibc-2.11-%{version}/build
tar jxf glibc_ports-%{full_version}.tar.bz2
mkdir -p glibc-2.11-%{version}/ports
cp -far glibc-ports-2.11-%{version}/* glibc-2.11-%{version}/ports
tar jxf gcc-%{full_version}.tar.bz2
mkdir -p gcc-4.5-%{version}/build

%patch0 -p1
%patch1 -p1

#-----------------------------------------------------------------------
%build
export PATH=%{build_sysroot}%{_bindir}:$PATH
mkdir -p %{build_sysroot}%{prefix}/include
mkdir -p %{build_sysroot}%{prefix}/lib

%if 0
pushd binutils-%{version}/build
    CONFIGURE_TOP=..						\
    %configure2_5x						\
	--disable-nls						\
	--disable-werror					\
	--target=%{target}
    %make
    DESTDIR=%{build_sysroot} make installdirs install-host install-target
    rm -fr %{build_sysroot}%{_infodir}
    rm -fr %{build_sysroot}%{_libdir}/libiberty.a
    rm -f %{build_sysroot}%{_mandir}/man1/%{target}-{dlltool,nlmconv,windmc,windres}.1*
popd

pushd linux-%{version}
    make ARCH=arm INSTALL_HDR_PATH=%{build_sysroot}%{prefix}	\
	 headers_install
popd

rm -fr glibc-2.11-%{version}/build/*
pushd glibc-2.11-%{version}/build
    ../configure						\
	--prefix=%{build_sysroot}%{prefix}			\
	--disable-nls						\
	--disable-profile					\
	--disable-shared					\
	--enable-kernel=2.6.16					\
	--without-gd						\
	--with-headers=%{build_sysroot}%{prefix}/include	\
	--target=%{target}
    make install-bootstrap-headers=yes				\
	 install-headers
popd
%endif

rm -fr gcc-4.5-%{version}/build/*
pushd gcc-4.5-%{version}/build
    ../configure						\
	--prefix=%{build_sysroot}%{_prefix}			\
	--libdir=%{build_sysroot}%{_libdir}			\
	--libexecdir=%{build_sysroot}%{_libdir}			\
	--disable-nls						\
	--disable-decimal-float					\
	--disable-shared					\
	--disable-threads					\
	--disable-libffi					\
	--disable-libgcj					\
	--disable-libgomp					\
	--disable-libmudflap					\
	--disable-libssp					\
	--disable-libstdcxx-pch					\
	--disable-libunwind-exceptions				\
	--enable-__cxa_atexit					\
	--enable-extra-sgxxlite-multilibs			\
	--enable-languages="c,c++"				\
	--enable-poison-system-directories			\
	--enable-threads					\
	--enable-symvers=gnu					\
	--with-build-sysroot=%{build_sysroot}			\
	--with-build-time-tools=%{build_sysroot}%{prefix}/bin	\
	--with-bugurl=https://qa.mandriva.com			\
	--with-arch=armv5te					\
	--with-gnu-as						\
	--with-gnu-ld						\
	--with-newlib						\
	--without-headers					\
	--target=%{target}
    for dir in armv4t thumb2; do
	mkdir -p %{target}/$dir/libgcc
	ln -sf %{build_sysroot}/%{prefix}/include %{target}/$dir/libgcc
    done
    ln -sf %{build_sysroot}/%{prefix}/include %{target}/libgcc
    make LDFLAGS_FOR_TARGET=--sysroot=%{sysroot}		\
	 CPPFLAGS_FOR_TARGET=--sysroot=%{sysroot}		\
	 build_tooldir=%{build_sysroot}%{prefix}/bin
    make installdirs install-target
    make -C gcc install-common install-cpp install-driver	\
		install-headers
    mv -f %{build_sysroot}%{gccdir}/include-fixed/*.h		\
	  %{build_sysroot}%{gccdir}/include
    rm -fr %{build_sysroot}%{gccdir}/include-fixed
popd

mkdir -p glibc-2.11-%{version}/build
rm -fr glibc-2.11-%{version}/build/*
export CC=%{build_sysroot}%{_bindir}/%{target}-gcc
pushd glibc-2.11-%{version}/build
    ../configure						\
	--prefix=%{prefix}					\
	--disable-nls						\
	--disable-profile					\
	--disable-shared					\
	--enable-kernel=2.6.16					\
	--without-gd						\
	--with-headers=%{build_sysroot}%{prefix}/include	\
	--host=%{target}					\
	--target=%{target}
    make install_root=%{build_sysroot}				\
	 install-bootstrap-headers=yes				\
	 install-headers
    make csu/subdir_lib
    cp csu/crt1.o csu/crti.o csu/crtn.o				\
	%{build_sysroot}%{prefix}/lib
    %{build_sysroot}%{_bindir}/%{target}-gcc -o			\
	%{build_sysroot}%{prefix}/lib/libc.so			\
	-nostdlib -nostartfiles -shared -x c /dev/null
popd
unset CC

#-----------------------------------------------------------------------
%install
cp -fpar %{build_sysroot}/* %{buildroot}

#-----------------------------------------------------------------------
%clean
rm -fr %{buildroot}
