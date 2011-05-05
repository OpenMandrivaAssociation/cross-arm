%define		_requires_exceptions libc.so.6\\|libgcc_s.so.1

%define		upstream	arm-none-linux-gnueabi
%define		target		arm-mandriva-linux-gnueabi
%define		full_version	2010.09-50
%define		prefix		%{_prefix}/%{target}
%define		sysroot		%{prefix}/sysroot
%define 	build_root	%{_builddir}/arm-%{full_version}-%{upstream}/root
%define		gccdir		%{prefix}/lib/gcc/%{target}/4.5.1

Name:		cross-arm
Release:	2
Version:	2010.09
License:	GPLv3+
Group:		Development/Other
Summary:	ARM GNU/Linux cross toolchain based on Sourcery G++ Lite
URL:		http://www.codesourcery.com/sgpp/lite/arm/
# 841081740c155016364bcd979b5c06e9
Source0:	http://www.codesourcery.com/sgpp/lite/arm/portal/package7850/public/arm-none-linux-gnueabi/arm-2010.09-50-arm-none-linux-gnueabi.src.tar.bz2
Source1:	http://www.codesourcery.com/sgpp/lite/arm/portal/doc9947/getting-started.pdf
Buildroot:	%{_tmppath}/%{name}-%{version}-root

# For now, on purpose building with newer gmp, mpfr, mpc and libelf,
# instead of the certified versions
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
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
BuildRequires:	gettext
BuildRequires:	texinfo
BuildRequires:	texlive
BuildRequires:	zlib-devel

Requires:	cross-arm-binutils = %{version}-%{release}
Requires:	cross-arm-gcc = %{version}-%{release}
Requires:	cross-arm-c++ = %{version}-%{release}
Requires:	cross-arm-glibc = %{version}-%{release}
Requires:	cross-arm-gdb = %{version}-%{release}

# backport minor change required by newer make
Patch0:		cross-arm-glibc.patch

Patch1:		cross-arm-gdb.patch

%description
Sourcery G++ Lite for ARM GNU/Linux is intended for developers working on
embedded GNU/Linux applications. It may also be used for Linux kernel
development and debugging, or to build a GNU/Linux distribution.

%files
%defattr(-,root,root,-)

#-----------------------------------------------------------------------
%package	binutils
Summary:	binutils based on Sourcery G++ Lite for ARM GNU/Linux

%description	binutils
binutils based on Sourcery G++ Lite for ARM GNU/Linux.

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
%dir %{prefix}
%dir %{prefix}/bin
%{prefix}/bin/ar
%{prefix}/bin/as
%{prefix}/bin/ld
%{prefix}/bin/nm
%{prefix}/bin/objcopy
%{prefix}/bin/objdump
%{prefix}/bin/ranlib
%{prefix}/bin/strip
%dir %{prefix}/lib
%{prefix}/lib/ldscripts

#-----------------------------------------------------------------------
%package	gcc
Summary:	gcc based on Sourcery G++ Lite for ARM GNU/Linux
Requires:	cross-arm-binutils = %{version}-%{release}

%description	gcc
gcc based on Sourcery G++ Lite for ARM GNU/Linux.

%files		gcc
%defattr(-,root,root,-)
%{_bindir}/%{target}-cpp
%{_bindir}/%{target}-gcc
%{_bindir}/%{target}-gcc-4.5.1
%{_bindir}/%{target}-gccbug
%{_bindir}/%{target}-gcov
%{prefix}/bin/gcc
%{_mandir}/man1/%{target}-cpp.1*
%{_mandir}/man1/%{target}-gcc.1*
%{_mandir}/man1/%{target}-gcov.1*
%dir %{gccdir}
%{gccdir}/include
%{gccdir}/cc1
%{gccdir}/collect2
%{gccdir}/lto1
%{gccdir}/lto-wrapper
%{gccdir}/crtbegin.o
%{gccdir}/crtbeginS.o
%{gccdir}/crtbeginT.o
%{gccdir}/crtend.o
%{gccdir}/crtendS.o
%{gccdir}/libgcc.a
%{gccdir}/libgcc_eh.a
%{gccdir}/libgcov.a
%dir %{sysroot}%{_prefix}/lib
%{sysroot}%{_prefix}/lib/libgcc*
%{gccdir}/armv4t
%dir %{sysroot}/armv4t%{_prefix}/lib
%{sysroot}/armv4t%{_prefix}/lib/libgcc*
%{gccdir}/thumb2
%dir %{sysroot}/thumb2%{_prefix}/lib
%{sysroot}/thumb2%{_prefix}/lib/libgcc*

#-----------------------------------------------------------------------
%package	c++
Summary:	c++ based on Sourcery G++ Lite for ARM GNU/Linux
Requires:	cross-arm-gcc = %{version}-%{release}
Requires:	cross-arm-glibc = %{version}-%{release}

%description	c++
c++ based on Sourcery G++ Lite for ARM GNU/Linux.

%files		c++
%defattr(-,root,root,-)
%{_bindir}/%{target}-c++
%{_bindir}/%{target}-g++
%{prefix}/bin/c++
%{prefix}/bin/g++
%{gccdir}/cc1plus
%{_mandir}/man1/%{target}-g++.1*
%{prefix}/include
%{sysroot}%{_prefix}/lib/libstdc++*
%{sysroot}%{_prefix}/lib/libsupc++*
%{sysroot}%{_datadir}/gcc*
%{sysroot}/armv4t%{_prefix}/lib/libstdc++*
%{sysroot}/armv4t%{_prefix}/lib/libsupc++*
%{sysroot}/armv4t%{_datadir}/gcc*
%{sysroot}/thumb2%{_prefix}/lib/libstdc++*
%{sysroot}/thumb2%{_prefix}/lib/libsupc++*
%{sysroot}/thumb2%{_datadir}/gcc*

#-----------------------------------------------------------------------
%package	glibc
Summary:	glibc based on Sourcery G++ Lite for ARM GNU/Linux
Requires:	cross-arm-gcc = %{version}-%{release}

%description	glibc
glibc based on Sourcery G++ Lite for ARM GNU/Linux.

%files		glibc
%defattr(-,root,root,-)
%{sysroot}%{_bindir}
%exclude %{sysroot}%{_bindir}/gdbserver
%{sysroot}%{_sysconfdir}
%{sysroot}%{_includedir}
%{sysroot}/lib
%{sysroot}%{_prefix}/lib
%exclude %{sysroot}%{_prefix}/lib/libgcc*
%exclude %{sysroot}%{_prefix}/lib/libstdc++*
%exclude %{sysroot}%{_prefix}/lib/libsupc++*
%{sysroot}/sbin
%{sysroot}%{_sbindir}
%{sysroot}%{_datadir}
%exclude %{sysroot}%{_datadir}/gcc*
%{sysroot}/armv4t%{_bindir}
%exclude %{sysroot}/armv4t%{_bindir}/gdbserver
%{sysroot}/armv4t%{_sysconfdir}
%{sysroot}/armv4t%{_includedir}
%{sysroot}/armv4t/lib
%{sysroot}/armv4t%{_prefix}/lib
%exclude %{sysroot}/armv4t%{_prefix}/lib/libgcc*
%exclude %{sysroot}/armv4t%{_prefix}/lib/libstdc++*
%exclude %{sysroot}/armv4t%{_prefix}/lib/libsupc++*
%{sysroot}/armv4t/sbin
%{sysroot}/armv4t%{_sbindir}
%{sysroot}/armv4t%{_datadir}
%exclude %{sysroot}/armv4t%{_datadir}/gcc*
%{sysroot}/thumb2%{_bindir}
%exclude %{sysroot}/thumb2%{_bindir}/gdbserver
%{sysroot}/thumb2%{_sysconfdir}
%{sysroot}/thumb2%{_includedir}
%{sysroot}/thumb2/lib
%{sysroot}/thumb2%{_prefix}/lib
%exclude %{sysroot}/thumb2%{_prefix}/lib/libgcc*
%exclude %{sysroot}/thumb2%{_prefix}/lib/libstdc++*
%exclude %{sysroot}/thumb2%{_prefix}/lib/libsupc++*
%{sysroot}/thumb2/sbin
%{sysroot}/thumb2%{_sbindir}
%{sysroot}/thumb2%{_datadir}
%exclude %{sysroot}/thumb2%{_datadir}/gcc*

#-----------------------------------------------------------------------
%package	gdb
Summary:	gdb based on Sourcery G++ Lite for ARM GNU/Linux
Requires:	cross-arm-glibc = %{version}-%{release}

%description	gdb
gdb based on Sourcery G++ Lite for ARM GNU/Linux.

%files		gdb
%defattr(-,root,root,-)
%{_bindir}/%{target}-gdb
%{_bindir}/%{target}-gdbtui
%{_mandir}/man1/%{target}-gdb.1*
%{_mandir}/man1/%{target}-gdbtui.1*
%{prefix}/share/gdb
%{sysroot}%{_bindir}/gdbserver
%{sysroot}/armv4t%{_bindir}/gdbserver
%{sysroot}/thumb2%{_bindir}/gdbserver

#-----------------------------------------------------------------------
%prep
%setup -q -n arm-%{full_version}-%{upstream}
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
tar jxf gdb-%{full_version}.tar.bz2
mkdir -p gdb-%{version}/build

%patch0 -p1
%patch1 -p1

#-----------------------------------------------------------------------
%build
export PATH=%{build_root}%{_bindir}:$PATH

# binutils
rm -fr binutils-%{version}/build/*
pushd binutils-%{version}/build
    ../configure						\
	--prefix=%{_prefix}					\
	--disable-nls						\
	--disable-werror					\
	--enable-poison-system-directories			\
	--with-sysroot=%{sysroot}				\
	--with-build-sysroot=%{build_root}%{sysroot}		\
	--target=%{target}
    %make
    DESTDIR=%{build_root} %make install
    rm -fr %{build_root}%{_infodir}
    rm -fr %{build_root}%{_libdir}/libiberty.a
    rm -f %{build_root}%{_mandir}/man1/%{target}-{dlltool,nlmconv,windmc,windres}.1*
popd

# kernel headers
pushd linux-%{version}
    %make ARCH=arm						\
	INSTALL_HDR_PATH=%{build_root}%{sysroot}%{_prefix}	\
	headers_install
popd

# glibc(1) install headers
# this may install some --build headers but good enough to get going
rm -fr glibc-2.11-%{version}/build/*
pushd glibc-2.11-%{version}/build
    ../configure						\
	--prefix=%{_prefix}					\
	--disable-nls						\
	--disable-profile					\
	--enable-shared						\
	--enable-kernel=2.6.16					\
	--enable-add-ons					\
	--without-gd						\
	--with-headers=%{build_root}%{sysroot}%{_includedir}	\
	--target=%{target}
    %make install_root=%{build_root}%{sysroot}			\
	install-bootstrap-headers=yes install-headers
popd

# gcc(1) build static and c only
rm -fr gcc-4.5-%{version}/build/*
pushd gcc-4.5-%{version}/build
    ../configure						\
	--prefix=%{_prefix}					\
	--libdir=%{prefix}/lib					\
	--libexecdir=%{prefix}/lib				\
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
	--disable-plugin					\
	--enable-__cxa_atexit					\
	--enable-extra-sgxxlite-multilibs			\
	--enable-languages="c"					\
	--enable-poison-system-directories			\
	--enable-threads					\
	--enable-symvers=gnu					\
	--with-sysroot=%{sysroot}				\
	--with-build-sysroot=%{build_root}%{sysroot}		\
	--with-build-time-tools=%{build_root}%{sysroot}/bin	\
	--with-bugurl=https://qa.mandriva.com			\
	--with-arch=armv5te					\
	--with-system-zlib					\
	--with-gnu-as						\
	--with-gnu-ld						\
	--with-newlib						\
	--without-headers					\
	--target=%{target}
    for dir in armv4t thumb2; do
	mkdir -p %{target}/$dir/libgcc
	ln -sf %{build_root}/%{sysroot}%{_includedir} %{target}/$dir/libgcc
    done
    mkdir -p %{target}/libgcc
    ln -sf %{build_root}/%{sysroot}%{_includedir} %{target}/libgcc
    %make LDFLAGS_FOR_TARGET=--sysroot=%{build_root}%{sysroot}	\
	 CPPFLAGS_FOR_TARGET=--sysroot=%{build_root}%{sysroot}	\
	 build_tooldir=%{build_root}%{sysroot}
    DESTDIR=%{build_root} %make install
    mv -f %{build_root}%{gccdir}/include-fixed/*.h		\
	  %{build_root}%{gccdir}/include
    rm -fr %{build_root}%{gccdir}/include-fixed
popd

# glibc(2) install proper headers and fake multilib libc.so
mkdir -p %{build_root}%{sysroot}{,/armv4t,/thumb2}%{_prefix}/lib
mkdir -p glibc-2.11-%{version}/build
rm -fr glibc-2.11-%{version}/build/*
export CC=%{build_root}%{_bindir}/%{target}-gcc
pushd glibc-2.11-%{version}/build
    ../configure						\
	--prefix=%{_prefix}					\
	--disable-nls						\
	--disable-profile					\
	--enable-shared						\
	--enable-kernel=2.6.16					\
	--enable-add-ons					\
	--without-gd						\
	--with-headers=%{build_root}%{sysroot}%{_includedir}	\
	--host=%{target}					\
	--target=%{target}
    %make install_root=%{build_root}%{sysroot}			\
	 install-bootstrap-headers=yes				\
	 install-headers
    %make csu/subdir_lib
    #--
    cp csu/crt1.o csu/crti.o csu/crtn.o				\
	%{build_root}%{sysroot}%{_prefix}/lib
    %{build_root}%{_bindir}/%{target}-gcc			\
	-o %{build_root}%{sysroot}%{_prefix}/lib/libc.so	\
	-nostdlib -nostartfiles -shared -x c /dev/null
    #--
    cp csu/crt1.o csu/crti.o csu/crtn.o				\
	%{build_root}%{sysroot}/armv4t%{_prefix}/lib
    %{build_root}%{_bindir}/%{target}-gcc -march=armv4t -o	\
	%{build_root}%{sysroot}/armv4t%{_prefix}/lib/libc.so	\
	-nostdlib -nostartfiles -shared -x c /dev/null
    #--
    cp csu/crt1.o csu/crti.o csu/crtn.o				\
	%{build_root}%{sysroot}/thumb2%{_prefix}/lib
    %{build_root}%{_bindir}/%{target}-gcc -mthumb		\
	-march=armv7-a -o					\
	%{build_root}%{sysroot}/thumb2%{_prefix}/lib/libc.so	\
	-nostdlib -nostartfiles -shared -x c /dev/null
popd
unset CC

# gcc(2) build dynamic and c only
rm -fr gcc-4.5-%{version}/build/*
pushd gcc-4.5-%{version}/build
    ../configure						\
	--prefix=%{_prefix}					\
	--libdir=%{prefix}/lib					\
	--libexecdir=%{prefix}/lib				\
	--disable-nls						\
	--disable-decimal-float					\
	--enable-shared						\
	--disable-threads					\
	--disable-libffi					\
	--disable-libgcj					\
	--disable-libgomp					\
	--disable-libmudflap					\
	--disable-libssp					\
	--disable-libstdcxx-pch					\
	--disable-libunwind-exceptions				\
	--disable-plugin					\
	--enable-__cxa_atexit					\
	--enable-extra-sgxxlite-multilibs			\
	--enable-languages="c"					\
	--enable-poison-system-directories			\
	--enable-threads					\
	--enable-symvers=gnu					\
	--with-sysroot=%{sysroot}				\
	--with-build-sysroot=%{build_root}%{sysroot}		\
	--with-build-time-tools=%{build_root}%{sysroot}/bin	\
	--with-bugurl=https://qa.mandriva.com			\
	--with-arch=armv5te					\
	--with-system-zlib					\
	--with-gnu-as						\
	--with-gnu-ld						\
	--with-newlib						\
	--without-headers					\
	--target=%{target}
    for dir in armv4t thumb2; do
	mkdir -p %{target}/$dir/libgcc
	ln -sf %{build_root}/%{sysroot}%{_includedir} %{target}/$dir/libgcc
    done
    mkdir -p %{target}/libgcc
    ln -sf %{build_root}/%{sysroot}%{_includedir} %{target}/libgcc
    %make LDFLAGS_FOR_TARGET=--sysroot=%{build_root}%{sysroot}	\
	 CPPFLAGS_FOR_TARGET=--sysroot=%{build_root}%{sysroot}	\
	 build_tooldir=%{build_root}%{sysroot}
    DESTDIR=%{build_root} %make install
    mv -f %{build_root}%{gccdir}/include-fixed/*.h		\
	  %{build_root}%{gccdir}/include
    rm -fr %{build_root}%{gccdir}/include-fixed
    rm -fr %{build_root}%{gccdir}/install-tools
popd

# glibc(3) build all default targets
mkdir -p glibc-2.11-%{version}/build-armv4t
rm -fr glibc-2.11-%{version}/build-armv4t/*
export CC="%{build_root}%{_bindir}/%{target}-gcc -march=armv4t"
pushd glibc-2.11-%{version}/build-armv4t
    ../configure						\
	--prefix=%{_prefix}					\
	--libdir=%{_prefix}/lib					\
	--libexecdir=%{_prefix}/lib				\
	--disable-nls						\
	--disable-profile					\
	--enable-shared						\
	--enable-kernel=2.6.16					\
	--enable-add-ons					\
	--without-gd						\
	--with-headers=%{build_root}%{sysroot}%{_includedir}	\
	--host=%{target}					\
	--target=%{target}
    %make
    %make install_root=%{build_root}%{sysroot}/armv4t install
popd
#--
mkdir -p glibc-2.11-%{version}/build-thumb2
rm -fr glibc-2.11-%{version}/build-thumb2/*
export CC="%{build_root}%{_bindir}/%{target}-gcc -mthumb -march=armv7-a"
pushd glibc-2.11-%{version}/build-thumb2
    ../configure						\
	--prefix=%{_prefix}					\
	--libdir=%{_prefix}/lib					\
	--libexecdir=%{_prefix}/lib				\
	--disable-nls						\
	--disable-profile					\
	--enable-shared						\
	--enable-kernel=2.6.16					\
	--enable-add-ons					\
	--without-gd						\
	--with-headers=%{build_root}%{sysroot}%{_includedir}	\
	--host=%{target}					\
	--target=%{target}
    %make
    %make install_root=%{build_root}%{sysroot}/thumb2 install
popd
#--
mkdir -p glibc-2.11-%{version}/build
rm -fr glibc-2.11-%{version}/build/*
export CC=%{build_root}%{_bindir}/%{target}-gcc
pushd glibc-2.11-%{version}/build
    ../configure						\
	--prefix=%{_prefix}					\
	--libdir=%{_prefix}/lib					\
	--libexecdir=%{_prefix}/lib				\
	--disable-nls						\
	--disable-profile					\
	--enable-shared						\
	--enable-kernel=2.6.16					\
	--enable-add-ons					\
	--without-gd						\
	--with-headers=%{build_root}%{sysroot}%{_includedir}	\
	--host=%{target}					\
	--target=%{target}
    %make
    %make install_root=%{build_root}%{sysroot} install
popd
unset CC

# gcc(3) build C and C++
rm -fr gcc-4.5-%{version}/build/*
pushd gcc-4.5-%{version}/build
    ../configure						\
	--prefix=%{_prefix}					\
	--libdir=%{prefix}/lib					\
	--libexecdir=%{prefix}/lib				\
	--disable-nls						\
	--disable-libffi					\
	--disable-libgcj					\
	--disable-libgomp					\
	--disable-libmudflap					\
	--disable-libssp					\
	--disable-libstdcxx-pch					\
	--disable-libunwind-exceptions				\
	--disable-plugin					\
	--enable-__cxa_atexit					\
	--enable-extra-sgxxlite-multilibs			\
	--enable-languages="c,c++"				\
	--enable-lto						\
	--enable-poison-system-directories			\
	--enable-shared						\
	--enable-symvers=gnu					\
	--enable-threads					\
	--with-sysroot=%{sysroot}				\
	--with-build-sysroot=%{build_root}%{sysroot}		\
	--with-bugurl=https://qa.mandriva.com			\
	--with-arch=armv5te					\
	--with-system-zlib					\
	--with-gnu-as						\
	--with-gnu-ld						\
	--without-headers					\
	--target=%{target}
    for dir in armv4t thumb2; do
	mkdir -p %{target}/$dir/libgcc
	ln -sf %{build_root}/%{sysroot}%{_includedir} %{target}/$dir/libgcc
    done
    mkdir -p %{target}/libgcc
    ln -sf %{build_root}/%{sysroot}%{_includedir} %{target}/libgcc
    %make LDFLAGS_FOR_TARGET=--sysroot=%{build_root}%{sysroot}	\
	CPPFLAGS_FOR_TARGET=--sysroot=%{build_root}%{sysroot}	\
	build_tooldir=%{build_root}%{sysroot}
    DESTDIR=%{build_root} %make install
    mv -f %{build_root}%{gccdir}/include-fixed/*.h		\
	  %{build_root}%{gccdir}/include
    rm -fr %{build_root}%{gccdir}/include-fixed
    rm -fr %{build_root}%{gccdir}/install-tools
popd

# gdb
rm -fr gdb-%{version}/build/*
pushd gdb-%{version}/build
    ../configure						\
	--prefix=%{_prefix}					\
	--disable-nls						\
	--disable-sim						\
	--with-bugurl=https://qa.mandriva.com			\
	--with-build-time-tools=%{build_root}%{sysroot}/bin	\
	--with-gdb-datadir=%{prefix}/share/gdb			\
	--with-system-gdbinit=%{prefix}/lib/gdbinit		\
	--target=%{target}
    %make
    DESTDIR=%{build_root} %make install
popd

# gdbserver
mkdir -p gdb-%{version}/gdb/gdbserver/build-armv4t
rm -fr gdb-%{version}/gdb/gdbserver/build-armv4t/*
export CC="%{build_root}%{_bindir}/%{target}-gcc -march=armv4t"
pushd gdb-%{version}/gdb/gdbserver/build-armv4t
    ../configure						\
	--prefix=%{_prefix}					\
	--with-bugurl=https://qa.mandriva.com			\
	--host=%{target}
    %make
    DESTDIR=%{build_root}%{sysroot}/armv4t %make install
popd
#--
mkdir -p gdb-%{version}/gdb/gdbserver/build-thumb2
rm -fr gdb-%{version}/gdb/gdbserver/build-thumb2/*
export CC="%{build_root}%{_bindir}/%{target}-gcc -mthumb -march=armv7-a"
pushd gdb-%{version}/gdb/gdbserver/build-thumb2
    ../configure						\
	--prefix=%{_prefix}					\
	--with-bugurl=https://qa.mandriva.com			\
	--host=%{target}
    %make
    DESTDIR=%{build_root}%{sysroot}/thumb2 %make install
popd
#--
mkdir -p gdb-%{version}/gdb/gdbserver/build
rm -fr gdb-%{version}/gdb/gdbserver/build/*
export CC="%{build_root}%{_bindir}/%{target}-gcc"
pushd gdb-%{version}/gdb/gdbserver/build
    ../configure						\
	--prefix=%{_prefix}					\
	--with-bugurl=https://qa.mandriva.com			\
	--host=%{target}
    %make
    DESTDIR=%{build_root}%{sysroot} %make install
popd
unset CC

#-----------------------------------------------------------------------
%install
cp -fpar %{build_root}/* %{buildroot}

# already on system tools
rm -f %{buildroot}%{_libdir}/libiberty.a
rm -f %{buildroot}%{prefix}/lib*/libiberty.a
rm -fr %{buildroot}%{_infodir}
rm -fr %{buildroot}%{_mandir}/man7

rm -f %{buildroot}%{_mandir}/man1/gdbserver.1*

rm -f %{buildroot}%{_bindir}/%{target}-c++
ln -sf %{_bindir}/%{target}-g++ %{buildroot}%{_bindir}/%{target}-c++
rm -f %{buildroot}%{sysroot}/bin/{c++,g++,gcc}
ln -sf %{_bindir}/%{target}-g++ %{buildroot}%{prefix}/bin/c++
ln -sf %{_bindir}/%{target}-g++ %{buildroot}%{prefix}/bin/g++
ln -sf %{_bindir}/%{target}-gcc %{buildroot}%{prefix}/bin/gcc

ln -sf %{prefix}/include/c++ %{buildroot}%{sysroot}%{_includedir}

rm -fr %{buildroot}%{sysroot}/armv4t%{_includedir}
ln -sf %{sysroot}%{_includedir} %{buildroot}%{sysroot}/armv4t%{_includedir}
rm -fr %{buildroot}%{sysroot}/thumb2%{_includedir}
ln -sf %{sysroot}%{_includedir} %{buildroot}%{sysroot}/thumb2%{_includedir}

# move/copy gcc/g++ files
cp -fpar %{buildroot}%{prefix}/share/gcc-4.5.1 %{buildroot}%{sysroot}/armv4t%{_datadir}
cp -fpar %{buildroot}%{prefix}/share/gcc-4.5.1 %{buildroot}%{sysroot}/thumb2%{_datadir}
mv %{buildroot}%{prefix}/share/gcc-4.5.1 %{buildroot}%{sysroot}%{_datadir}
pushd %{buildroot}%{prefix}/lib
    mv -f libgcc* libstdc* libsupc* %{buildroot}%{sysroot}%{_prefix}/lib
    mv -f armv4t/* %{buildroot}%{sysroot}/armv4t%{_prefix}/lib
    mv -f thumb2/* %{buildroot}%{sysroot}/thumb2%{_prefix}/lib
    rmdir armv4t thumb2
popd

#-----------------------------------------------------------------------
%clean
rm -fr %{buildroot}
