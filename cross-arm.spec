%define		_requires_exceptions libc.so.6\\|libgcc_s.so.1

%define		target		arm-none-linux-gnueabi
%define		full_version	2010.09-50
%define		prefix		%{_prefix}/%{target}
%define 	sysroot		%{_builddir}/arm-%{full_version}-%{target}/sysroot
%define		gccdir		%{_libdir}/gcc/%{target}/4.5.1

Name:		cross-arm
Release:	1
Version:	2010.09
License:	GPLv3+
Group:		Development/Other
Summary:	Sourcery G++ Lite for ARM GNU/Linux
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
BuildRequires:	gettext
BuildRequires:	texinfo
BuildRequires:	texlive

Requires:	cross-arm-binutils = %{version}-%{release}
Requires:	cross-arm-gcc = %{version}-%{release}
Requires:	cross-arm-c++ = %{version}-%{release}
Requires:	cross-arm-glibc = %{version}-%{release}

# backport minor change required by newer make
Patch0:		cross-arm-glibc.patch

%description
Sourcery G++ Lite for ARM GNU/Linux is intended for developers working on
embedded GNU/Linux applications. It may also be used for Linux kernel
development and debugging, or to build a GNU/Linux distribution.

%files
%defattr(-,root,root,-)

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
%dir %{prefix}/bin
%dir %{prefix}/lib
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
Requires:	cross-arm-binutils = %{version}-%{release}

%description	gcc
gcc Sourcery G++ Lite for ARM GNU/Linux.

%files		gcc
%defattr(-,root,root,-)
%{_bindir}/%{target}-cpp
%{_bindir}/%{target}-gcc
%{_bindir}/%{target}-gcc-4.5.1
%{_bindir}/%{target}-gccbug
%{_bindir}/%{target}-gcov
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
%{gccdir}/armv4t/crtbegin.o
%{gccdir}/armv4t/crtbeginS.o
%{gccdir}/armv4t/crtbeginT.o
%{gccdir}/armv4t/crtend.o
%{gccdir}/armv4t/crtendS.o
%{gccdir}/armv4t/libgcc.a
%{gccdir}/armv4t/libgcc_eh.a
%{gccdir}/armv4t/libgcov.a
%{gccdir}/thumb2/crtbegin.o
%{gccdir}/thumb2/crtbeginS.o
%{gccdir}/thumb2/crtbeginT.o
%{gccdir}/thumb2/crtend.o
%{gccdir}/thumb2/crtendS.o
%{gccdir}/thumb2/libgcc.a
%{gccdir}/thumb2/libgcc_eh.a
%{gccdir}/thumb2/libgcov.a
%{prefix}/bin/gcc
# could be in a libgcc package
%{prefix}/lib/libgcc*
%dir %{prefix}/lib/armv4t
%{prefix}/lib/armv4t/libgcc*
%dir %{prefix}/lib/thumb2
%{prefix}/lib/thumb2/libgcc*
%{_mandir}/man1/%{target}-cpp.1*
%{_mandir}/man1/%{target}-gcc.1*
%{_mandir}/man1/%{target}-gcov.1*

#-----------------------------------------------------------------------
%package	c++
Summary:	c++ Sourcery G++ Lite for ARM GNU/Linux
Requires:	cross-arm-gcc = %{version}-%{release}
Requires:	cross-arm-glibc = %{version}-%{release}

%description	c++
c++ Sourcery G++ Lite for ARM GNU/Linux.

%files		c++
%defattr(-,root,root,-)
%{_bindir}/%{target}-c++
%{_bindir}/%{target}-g++
%{prefix}/bin/c++
%{prefix}/bin/g++
%{gccdir}/cc1plus
# could be in a libstdc++ package
%{prefix}/include/c++
%{prefix}/lib/libstdc++*
%{prefix}/lib/libsupc++*
%{prefix}/lib/armv4t/libstdc++*
%{prefix}/lib/armv4t/libsupc++*
%{prefix}/lib/thumb2/libstdc++*
%{prefix}/lib/thumb2/libsupc++*
%{prefix}/share/gcc*
%{_mandir}/man1/%{target}-g++.1*

#-----------------------------------------------------------------------
%package	glibc
Summary:	glibc Sourcery G++ Lite for ARM GNU/Linux
Requires:	cross-arm-gcc = %{version}-%{release}

%description	glibc
glibc Sourcery G++ Lite for ARM GNU/Linux.

%files		glibc
%defattr(-,root,root,-)
%{prefix}/bin/catchsegv
%{prefix}/bin/gencat
%{prefix}/bin/getconf
%{prefix}/bin/getent
%{prefix}/bin/iconv
%{prefix}/bin/ldd
%{prefix}/bin/locale
%{prefix}/bin/localedef
%{prefix}/bin/mtrace
%{prefix}/bin/pcprofiledump
%{prefix}/bin/rpcgen
%{prefix}/bin/sprof
%{prefix}/bin/tzselect
%{prefix}/bin/xtrace
%{prefix}/etc
%{prefix}/include
%exclude %{prefix}/include/c++
%{prefix}/lib/*
%exclude %dir %{prefix}/lib/armv4t
%exclude %dir %{prefix}/lib/thumb2
%exclude %{prefix}/lib/ldscripts
%exclude %{prefix}/lib/libgcc*
%exclude %{prefix}/lib/armv4t/libgcc*
%exclude %{prefix}/lib/thumb2/libgcc*
%exclude %{prefix}/lib/libstdc++*
%exclude %{prefix}/lib/libsupc++*
%exclude %{prefix}/lib/armv4t/libstdc++*
%exclude %{prefix}/lib/armv4t/libsupc++*
%exclude %{prefix}/lib/thumb2/libstdc++*
%exclude %{prefix}/lib/thumb2/libsupc++*
%{prefix}/sbin
%{prefix}/share
%exclude %{prefix}/share/gcc*

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

#-----------------------------------------------------------------------
%build
export PATH=%{sysroot}%{_bindir}:$PATH
mkdir -p %{sysroot}%{prefix}/include
mkdir -p %{sysroot}%{prefix}/lib/{armv4t,thumb2}

# binutils
rm -fr binutils-%{version}/build/*
pushd binutils-%{version}/build
    ../configure						\
	--prefix=%{_prefix}					\
	--disable-nls						\
	--disable-werror					\
	--with-sysroot=/					\
	--with-build-sysroot=%{sysroot}				\
	--target=%{target}
    make
    DESTDIR=%{sysroot} make installdirs install-host install-target
    rm -fr %{sysroot}%{_infodir}
    rm -fr %{sysroot}%{_libdir}/libiberty.a
    rm -f %{sysroot}%{_mandir}/man1/%{target}-{dlltool,nlmconv,windmc,windres}.1*
popd

# kernel headers
pushd linux-%{version}
    make ARCH=arm INSTALL_HDR_PATH=%{sysroot}%{prefix}		\
	 headers_install
popd

# glibc(1) install headers
# this may install some --build headers but good enough to get going
rm -fr glibc-2.11-%{version}/build/*
pushd glibc-2.11-%{version}/build
    ../configure						\
	--prefix=%{prefix}					\
	--disable-nls						\
	--disable-profile					\
	--enable-shared						\
	--enable-kernel=2.6.16					\
	--enable-add-ons					\
	--without-gd						\
	--with-headers=%{sysroot}%{prefix}/include		\
	--target=%{target}
    make install_root=%{sysroot}				\
	install-bootstrap-headers=yes install-headers
popd
ln -sf %{sysroot}/%{prefix}/include %{sysroot}/%{prefix}/bin
ln -sf %{sysroot}/%{prefix}/lib %{sysroot}/%{prefix}/bin

# gcc(1) build static and c only
rm -fr gcc-4.5-%{version}/build/*
pushd gcc-4.5-%{version}/build
    ../configure						\
	--prefix=%{_prefix}					\
	--libdir=%{_libdir}					\
	--libexecdir=%{_libdir}					\
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
	--enable-languages="c"					\
	--enable-poison-system-directories			\
	--enable-threads					\
	--enable-symvers=gnu					\
	--with-build-sysroot=%{sysroot}				\
	--with-build-time-tools=%{sysroot}%{prefix}/bin		\
	--with-bugurl=https://qa.mandriva.com			\
	--with-arch=armv5te					\
	--with-gnu-as						\
	--with-gnu-ld						\
	--with-newlib						\
	--without-headers					\
	--target=%{target}
    for dir in armv4t thumb2; do
	mkdir -p %{target}/$dir/libgcc
	ln -sf %{sysroot}/%{prefix}/include %{target}/$dir/libgcc
    done
    mkdir -p %{target}/libgcc
    ln -sf %{sysroot}/%{prefix}/include %{target}/libgcc
    make LDFLAGS_FOR_TARGET=--sysroot=%{sysroot}		\
	 CPPFLAGS_FOR_TARGET=--sysroot=%{sysroot}		\
	 build_tooldir=%{sysroot}%{prefix}
    DESTDIR=%{sysroot} make install
    mv -f %{sysroot}%{gccdir}/include-fixed/*.h			\
	  %{sysroot}%{gccdir}/include
    rm -fr %{sysroot}%{gccdir}/include-fixed
popd

# glibc(2) install proper headers and fake multilib libc.so
mkdir -p glibc-2.11-%{version}/build
rm -fr glibc-2.11-%{version}/build/*
export CC=%{sysroot}%{_bindir}/%{target}-gcc
pushd glibc-2.11-%{version}/build
    ../configure						\
	--prefix=%{prefix}					\
	--disable-nls						\
	--disable-profile					\
	--enable-shared						\
	--enable-kernel=2.6.16					\
	--enable-add-ons					\
	--without-gd						\
	--with-headers=%{sysroot}%{prefix}/include		\
	--host=%{target}					\
	--target=%{target}
    make install_root=%{sysroot}				\
	 install-bootstrap-headers=yes				\
	 install-headers
    make csu/subdir_lib
    #--
    cp csu/crt1.o csu/crti.o csu/crtn.o				\
	%{sysroot}%{prefix}/lib
    %{sysroot}%{_bindir}/%{target}-gcc				\
	-o %{sysroot}%{prefix}/lib/libc.so			\
	-nostdlib -nostartfiles -shared -x c /dev/null
    #--
    cp csu/crt1.o csu/crti.o csu/crtn.o				\
	%{sysroot}%{prefix}/lib/armv4t
    %{sysroot}%{_bindir}/%{target}-gcc -march=armv4t		\
	-o %{sysroot}%{prefix}/lib/armv4t/libc.so		\
	-nostdlib -nostartfiles -shared -x c /dev/null
    #--
    cp csu/crt1.o csu/crti.o csu/crtn.o				\
	%{sysroot}%{prefix}/lib/thumb2
    %{sysroot}%{_bindir}/%{target}-gcc -mthumb			\
	-march=armv7-a						\
	-o %{sysroot}%{prefix}/lib/thumb2/libc.so		\
	-nostdlib -nostartfiles -shared -x c /dev/null
popd
unset CC

# gcc(2) build dynamic and c only
rm -fr gcc-4.5-%{version}/build/*
pushd gcc-4.5-%{version}/build
    ../configure						\
	--prefix=%{_prefix}					\
	--libdir=%{_libdir}					\
	--libexecdir=%{_libdir}					\
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
	--enable-__cxa_atexit					\
	--enable-extra-sgxxlite-multilibs			\
	--enable-languages="c"					\
	--enable-poison-system-directories			\
	--enable-threads					\
	--enable-symvers=gnu					\
	--with-build-sysroot=%{sysroot}				\
	--with-build-time-tools=%{sysroot}%{prefix}/bin		\
	--with-bugurl=https://qa.mandriva.com			\
	--with-arch=armv5te					\
	--with-gnu-as						\
	--with-gnu-ld						\
	--with-newlib						\
	--without-headers					\
	--target=%{target}
    for dir in armv4t thumb2; do
	mkdir -p %{target}/$dir/libgcc
	ln -sf %{sysroot}/%{prefix}/include %{target}/$dir/libgcc
    done
    mkdir -p %{target}/libgcc
    ln -sf %{sysroot}/%{prefix}/include %{target}/libgcc
    make LDFLAGS_FOR_TARGET=--sysroot=%{sysroot}		\
	 CPPFLAGS_FOR_TARGET=--sysroot=%{sysroot}		\
	 build_tooldir=%{sysroot}%{prefix}
    DESTDIR=%{sysroot} make install
    mv -f %{sysroot}%{gccdir}/include-fixed/*.h			\
	  %{sysroot}%{gccdir}/include
    rm -fr %{sysroot}%{gccdir}/include-fixed
    rm -fr %{sysroot}%{gccdir}/install-tools
popd

# glibc(3) build all default targets
mkdir -p glibc-2.11-%{version}/build
rm -fr glibc-2.11-%{version}/build/*
export CC="%{sysroot}%{_bindir}/%{target}-gcc -march=armv4t"
pushd glibc-2.11-%{version}/build
    ../configure						\
	--prefix=%{prefix}					\
	--libdir=%{prefix}/lib/armv4t				\
	--libexecdir=%{prefix}/lib/armv4t			\
	--disable-nls						\
	--disable-profile					\
	--enable-shared						\
	--enable-kernel=2.6.16					\
	--enable-add-ons					\
	--without-gd						\
	--with-headers=%{sysroot}%{prefix}/include		\
	--host=%{target}					\
	--target=%{target}
    make
    make install_root=%{sysroot} install
popd
#--
rm -fr glibc-2.11-%{version}/build/*
export CC="%{sysroot}%{_bindir}/%{target}-gcc -mthumb -march=armv7-a"
pushd glibc-2.11-%{version}/build
    ../configure						\
	--prefix=%{prefix}					\
	--libdir=%{prefix}/lib/thumb2				\
	--libexecdir=%{prefix}/lib/thumb2			\
	--disable-nls						\
	--disable-profile					\
	--enable-shared						\
	--enable-kernel=2.6.16					\
	--enable-add-ons					\
	--without-gd						\
	--with-headers=%{sysroot}%{prefix}/include		\
	--host=%{target}					\
	--target=%{target}
    make
    make install_root=%{sysroot} install
popd
#--
rm -fr glibc-2.11-%{version}/build/*
export CC=%{sysroot}%{_bindir}/%{target}-gcc
pushd glibc-2.11-%{version}/build
    ../configure						\
	--prefix=%{prefix}					\
	--libdir=%{prefix}/lib					\
	--libexecdir=%{prefix}/lib				\
	--disable-nls						\
	--disable-profile					\
	--enable-shared						\
	--enable-kernel=2.6.16					\
	--enable-add-ons					\
	--without-gd						\
	--with-headers=%{sysroot}%{prefix}/include		\
	--host=%{target}					\
	--target=%{target}
    make
    make install_root=%{sysroot} install
popd
unset CC

for dir in lib include; do
    [ -d %{sysroot}%{_prefix}/$dir ] &&
	rm -fr %{sysroot}%{_prefix}/$dir
    [ -e %{sysroot}%{_prefix}/$dir ] ||
	ln -sf %{sysroot}%{prefix}/$dir %{sysroot}%{_prefix}/$dir
done

# Rewrite linker scripts to use relative paths
#--
cat > %{sysroot}%{prefix}/lib/libc.so << EOF
/* GNU ld script
   Use the shared library, but some functions are only in
   the static library, so try that secondarily.  */
OUTPUT_FORMAT(elf32-littlearm)
GROUP ( libc.so.6 libc_nonshared.a  AS_NEEDED ( ld-linux.so.3 ) )
EOF
cat > %{sysroot}%{prefix}/lib/libpthread.so << EOF
/* GNU ld script
   Use the shared library, but some functions are only in
   the static library, so try that secondarily.  */
OUTPUT_FORMAT(elf32-littlearm)
GROUP ( libpthread.so.0 libpthread_nonshared.a )
EOF

#--
cat > %{sysroot}%{prefix}/lib/armv4t/libc.so << EOF
/* GNU ld script
   Use the shared library, but some functions are only in
   the static library, so try that secondarily.  */
OUTPUT_FORMAT(elf32-littlearm)
GROUP ( libc.so.6 libc_nonshared.a  AS_NEEDED ( ../ld-linux.so.3 ) )
EOF
cat > %{sysroot}%{prefix}/lib/armv4t/libpthread.so << EOF
/* GNU ld script
   Use the shared library, but some functions are only in
   the static library, so try that secondarily.  */
OUTPUT_FORMAT(elf32-littlearm)
GROUP ( libpthread.so.0 libpthread_nonshared.a )
EOF

#--
cat > %{sysroot}%{prefix}/lib/thumb2/libc.so << EOF
/* GNU ld script
   Use the shared library, but some functions are only in
   the static library, so try that secondarily.  */
OUTPUT_FORMAT(elf32-littlearm)
GROUP ( libc.so.6 libc_nonshared.a  AS_NEEDED ( ../ld-linux.so.3 ) )
EOF
cat > %{sysroot}%{prefix}/lib/thumb2/libpthread.so << EOF
/* GNU ld script
   Use the shared library, but some functions are only in
   the static library, so try that secondarily.  */
OUTPUT_FORMAT(elf32-littlearm)
GROUP ( libpthread.so.0 libpthread_nonshared.a )
EOF

# gcc(3) build C and C++
rm -fr gcc-4.5-%{version}/build/*
pushd gcc-4.5-%{version}/build
    ../configure						\
	--prefix=%{_prefix}					\
	--libdir=%{_libdir}					\
	--libexecdir=%{_libdir}					\
	--disable-nls						\
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
	--enable-lto						\
	--enable-poison-system-directories			\
	--enable-shared						\
	--enable-symvers=gnu					\
	--enable-threads					\
	--with-build-sysroot=%{sysroot}				\
	--with-bugurl=https://qa.mandriva.com			\
	--with-arch=armv5te					\
	--with-gnu-as						\
	--with-gnu-ld						\
	--without-headers					\
	--target=%{target}
    for dir in armv4t thumb2; do
	mkdir -p %{target}/$dir/libgcc
	ln -sf %{sysroot}/%{prefix}/include %{target}/$dir/libgcc
    done
    mkdir -p %{target}/libgcc
    ln -sf %{sysroot}/%{prefix}/include %{target}/libgcc
    make LDFLAGS_FOR_TARGET=--sysroot=%{sysroot}		\
	CPPFLAGS_FOR_TARGET=--sysroot=%{sysroot}		\
	build_tooldir=%{sysroot}%{prefix}
    DESTDIR=%{sysroot} make install
    mv -f %{sysroot}%{gccdir}/include-fixed/*.h			\
	  %{sysroot}%{gccdir}/include
    rm -fr %{sysroot}%{gccdir}/include-fixed
    rm -fr %{sysroot}%{gccdir}/install-tools
popd

#-----------------------------------------------------------------------
%install
cp -fpar %{sysroot}/* %{buildroot}

# symlinks
rm -f %{buildroot}%{_includedir}
%ifarch x86_64
rm -f %{buildroot}%{_prefix}/lib
%endif
rm %{buildroot}%{prefix}/bin/include
rm %{buildroot}%{prefix}/bin/lib

# already on system tools
rm -f %{buildroot}%{_libdir}/libiberty.a
rm -fr %{buildroot}%{_infodir}
rm -fr %{buildroot}%{_mandir}/man7

#-----------------------------------------------------------------------
%clean
rm -fr %{buildroot}
