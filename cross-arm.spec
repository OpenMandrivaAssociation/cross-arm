# croos-arm package initially based on codesourcery now coverted on
# basically a stage1 of the DJ Delorie arm bootstrap scripts at
# http://fedorapeople.org/~djdelorie/
# adapted for the mandriva arm bootstrap setup

%define		_enable_debug_packages	%{nil}
%define		debug_package		%{nil}
%define		__find_provides		%{SOURCE10}
%define		__find_requires		%{SOURCE10}

%define		arch			arm
%define		target			armv7l-mandriva-linux-gnueabi
%define		prefix			%{_prefix}/%{target}
%define		sysroot			%{prefix}/sysroot
%define 	build_root		%{_builddir}/%{arch}-cross/root
%define		cross_libdir		%{_prefix}/lib
%define		cross_configure		./configure --prefix=%{_prefix} --exec-prefix=%{_prefix} --bindir=%{_bindir} --sbindir=%{_sbindir} --sysconfdir=%{_sysconfdir} --datadir=%{_datadir} --includedir=%{_includedir} --libdir=%{cross_libdir} --libexecdir=%{cross_libdir} --localstatedir=%{_localstatedir} --sharedstatedir=%{_sharedstatedir} --mandir=%{_mandir} --infodir=%{_infodir}
%define		__cross_configure	../%{cross_configure}
%define		build_config		--disable-werror --with-build-sysroot=%{build_root}%{sysroot}
%define		target_config		--with-cpu=cortex-a8 --with-tune=cortex-a8 --with-arch=armv7-a --with-mode=thumb --with-float=softfp --with-fpu=vfpv3-d16 --with-abi=aapcs-linux --with-sysroot=%{sysroot} --target=%{target}

%define		gcc_version		4.6.1
%define		linux_cross		linux-2.6.38
%define		binutils_cross		binutils-2.22.51
%define		cross_gcc		gcc-4.6-20111007
%define		cross_glibc		glibc-2.14-121-g5551a7b
%define		cross_gdb		gdb-7.1

%define 	build_root		%{_builddir}/cross-%{arch}/root
%define		gccdir			%{prefix}/lib/gcc/%{target}/4.6.1

Name:		cross-arm
Release:	1
Version:	2011.10
License:	GPLv3+
Group:		Development/Other
Summary:	ARM GNU/Linux cross toolchain
URL:		http://fedorapeople.org/~djdelorie/

# revision: 677434
# repsys co kernel; cd kernel; ./build_sources
# mv SOURCES/linux-2.6.38.tar.bz2
Source0:	%{linux_cross}.tar.bz2

# revision: 703525
# repsys co binutils
# rpmbuild -bp --define "_topdir `pwd`" --define "_target_cpu arm" SPECS/binutils.spec
# cd BUILD; tar jcf binutils-2.22.51.tar.bz2 binutils-2.22.51; mv binutils-2.22.51.tar.bz2 ../../cross-arm/SOURCES
Source1:	%{binutils_cross}.tar.bz2

# revision: 703958
# repsys co gcc
# rpmbuild -bp --define "_topdir `pwd`" --define "_target_cpu armv7l" SPECS/gcc.spec
# cd BUILD; tar jcf gcc-4.6-20111007.tar.bz2 gcc-4.6-20111007; mv gcc-4.6-20111007.tar.bz2 ../../cross-arm/SOURCES
Source2:	%{cross_gcc}.tar.bz2

# revision: 702438
# repsys co glibc
# rpmbuild -bp --define "_topdir `pwd`" --define "_target_cpu arm" SPECS/glibc.spec
# cd BUILD; tar jcf glibc-2.14-121-g5551a7b.tar.bz2 glibc-2.14-121-g5551a7b; mv glibc-2.14-121-g5551a7b.tar.bz2 ../../cross-arm/SOURCES
Source3:	%{cross_glibc}.tar.bz2

# revision: 682884
# repsys co gdb
# rpmbuild -bp --define "_topdir `pwd`" --define "_target_cpu arm" SPECS/gdb.spec
# cd BUILD; tar jcf gdb-7.1.bz2 gdb-7.1; mv gdb-7.1.tar.bz2 ../../cross-arm/SOURCES
Source4:	%{cross_gdb}.tar.bz2

Source10:	find-nothing

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
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
BuildRequires:	gettext
BuildRequires:	texinfo
BuildRequires:	texlive
BuildRequires:	zlib-devel

Requires:	cross-%{arch}-binutils = %{EVRD}
Requires:	cross-%{arch}-gcc = %{EVRD}
Requires:	cross-%{arch}-c++ = %{EVRD}
Requires:	cross-%{arch}-glibc = %{EVRD}
Requires:	cross-%{arch}-gdb = %{EVRD}

Patch0:		cross-arm-gdb.patch

%description
%{summary}.

%files
%defattr(-,root,root,-)

#-----------------------------------------------------------------------
%package	binutils
Summary:	ARM GNU/Linux cross toolchain binutils

%description	binutils
%{summary}.

%files		binutils
%defattr(-,root,root,-)
%{_bindir}/%{target}-addr2line
%{_bindir}/%{target}-ar
%{_bindir}/%{target}-as
%{_bindir}/%{target}-c++filt
%{_bindir}/%{target}-elfedit
%{_bindir}/%{target}-gprof
%{_bindir}/%{target}-ld
%{_bindir}/%{target}-ld.bfd
%{_bindir}/%{target}-nm
%{_bindir}/%{target}-objcopy
%{_bindir}/%{target}-objdump
%{_bindir}/%{target}-ranlib
%{_bindir}/%{target}-readelf
%{_bindir}/%{target}-size
%{_bindir}/%{target}-strings
%{_bindir}/%{target}-strip
%dir %{prefix}
%dir %{prefix}/bin
%{prefix}/bin/ar
%{prefix}/bin/as
%{prefix}/bin/ld
%{prefix}/bin/ld.bfd
%{prefix}/bin/nm
%{prefix}/bin/objcopy
%{prefix}/bin/objdump
%{prefix}/bin/ranlib
%{prefix}/bin/strip
%dir %{prefix}/lib
%{prefix}/lib/ldscripts

#-----------------------------------------------------------------------
%package	gcc
Summary:	ARM GNU/Linux cross toolchain gcc
Requires:	cross-%{arch}-binutils = %{EVRD}

%description	gcc
%{summary}.

%files		gcc
%defattr(-,root,root,-)
%{_bindir}/%{target}-cpp
%{_bindir}/%{target}-gcc*
%{_bindir}/%{target}-gcov
%{prefix}/bin/gcc
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
%{gccdir}/liblto_plugin.*
%{gccdir}/plugin
%dir %{sysroot}%{_prefix}/lib
%{sysroot}%{_prefix}/lib/libgcc*
%{sysroot}%{_prefix}/lib/libgomp*
%{sysroot}%{_prefix}/lib/libmudf*

#-----------------------------------------------------------------------
%package	c++
Summary:	ARM GNU/Linux cross toolchain c++
Requires:	cross-%{arch}-gcc = %{EVRD}

%description	c++
%{summary}.

%files		c++
%defattr(-,root,root,-)
%{_bindir}/%{target}-c++
%{_bindir}/%{target}-g++
%{prefix}/bin/c++
%{prefix}/bin/g++
%{gccdir}/cc1plus
%{prefix}/include
%{sysroot}%{_prefix}/lib/libstdc++*
%{sysroot}%{_prefix}/lib/libsupc++*
%{sysroot}%{_datadir}/gcc-%{gcc_version}

#-----------------------------------------------------------------------
%package	glibc
Summary:	ARM GNU/Linux cross toolchain binutils
Requires:	cross-%{arch}-gcc = %{EVRD}

%description	glibc
%{summary}.

%files		glibc
%defattr(-,root,root,-)
%{sysroot}%{_bindir}
%exclude %{sysroot}%{_bindir}/gdbserver
%{sysroot}%{_sysconfdir}
%{sysroot}%{_includedir}
%{sysroot}/lib
%{sysroot}%{_prefix}/lib
%exclude %{sysroot}%{_prefix}/lib/libgcc*
%exclude %{sysroot}%{_prefix}/lib/libgomp*
%exclude %{sysroot}%{_prefix}/lib/libmudf*
%exclude %{sysroot}%{_prefix}/lib/libstdc++*
%exclude %{sysroot}%{_prefix}/lib/libsupc++*
%{sysroot}/sbin
%{sysroot}%{_sbindir}
%{sysroot}%{_datadir}
%exclude %{sysroot}%{_datadir}/gcc-%{gcc_version}
%{sysroot}%{_localstatedir}/db

#-----------------------------------------------------------------------
%package	gdb
Summary:	ARM GNU/Linux cross toolchain gdb
Requires:	cross-%{arch}-glibc = %{EVRD}

%description	gdb
%{summary}

%files		gdb
%defattr(-,root,root,-)
%{_bindir}/%{target}-gdb
%{_bindir}/%{target}-gdbtui
%{_bindir}/%{target}-gstack
%{prefix}/share/gdb
%{sysroot}%{_bindir}/gdbserver

#-----------------------------------------------------------------------
%prep
%setup -q -c -n cross-%{arch} -T -a 0 -a 1 -a 2 -a 3 -a 4

%patch0 -p1

#-----------------------------------------------------------------------
%build
unset CC CXX CFLAGS CXXFLAGS AR LD AS
export PATH=%{build_root}%{_bindir}:$PATH
mkdir -p %{cross_glibc}/build
mkdir -p %{cross_gcc}/build

# kernel headers
pushd %{linux_cross}
    %make ARCH=%{arch}						\
	INSTALL_HDR_PATH=%{build_root}%{sysroot}%{_prefix}	\
	headers_install
popd

# binutils
pushd %{binutils_cross}
    %cross_configure						\
	%{build_config}						\
	%{target_config}
    %make
    DESTDIR=%{build_root} %make install
popd

# gcc host
mkdir -p %{cross_gcc}/build; pushd %{cross_gcc}/build
    echo %{vendor} > ../gcc/DEV-PHASE
    sed -i -e 's/4\.6\.2/4.6.1/' ../gcc/BASE-VER
    %__cross_configure						\
	%{build_config}						\
	--libdir=%{prefix}/lib					\
	--libexecdir=%{prefix}/lib				\
	--enable-languages=c,c++				\
	--disable-libssp					\
	--with-headers=%{build_root}%{sysroot}%{_includedir}	\
	%{target_config}
    %make all-host
    DESTDIR=%{build_root} %make install-host
popd

# glibc headers
pushd %{cross_glibc}/build
    echo libc_cv_forced_unwind=yes > config.cache
    echo libc_cv_c_cleanup=yes >> config.cache
    echo libc_cv_ctors_header=no >> config.cache
    %__cross_configure						\
	%{build_config}						\
	--with-headers=%{build_root}%{sysroot}%{_includedir}	\
	--enable-kernel=2.6.32					\
	--enable-bind-now					\
	--host %{target}					\
	--disable-profile					\
	--cache-file=config.cache				\
	--without-cvs						\
	--with-elf						\
	--without-gd						\
	--enable-add-ons=ports,nptl				\
	--disable-sanity-checks					\
	--with-tls						\
	--with-__thread						\
	--host=%{target}
    %make ARCH=%{arch} cross-compiling=yes install-headers install_root=%{build_root}%{sysroot}
    touch %{build_root}%{sysroot}%{_includedir}/gnu/stubs.h
    touch %{build_root}%{sysroot}/%{_includedir}/bits/stdio_lim.h
    cp ../nptl/sysdeps/pthread/pthread.h %{build_root}%{_includedir}
    pushd %{build_root}%{sysroot}%{_includedir}/bits
	sed '/ifndef.*NO_LONG_DOUBLE/,/#endif/d' < mathdef.h > mathdef.h.new
	mv mathdef.h.new mathdef.h
    popd
    # We also build just enough files to link libgcc.so.  The fake
    # libc.so will never actually get used.
    mkdir -p %{build_root}%{sysroot}%{cross_libdir}
    %make ARCH=%{arch} cross-compiling=yes csu/subdir_lib
    cp csu/crt*.o %{build_root}%{sysroot}%{cross_libdir}
    %{target}-gcc -nostdlib -nostartfiles -shared -x c /dev/null -o %{build_root}%{sysroot}%{cross_libdir}/libc.so
popd

# gcc libgcc
pushd %{cross_gcc}/build
    %make all-target-libgcc
    DESTDIR=%{build_root} %make install-target-libgcc
popd

# glibc
pushd %{cross_glibc}/build
    %make ARCH=%{arch} cross-compiling=yes
    %make ARCH=%{arch} cross-compiling=yes install install_root=%{build_root}%{sysroot}
    pushd %{build_root}%{sysroot}%{_includedir}/bits
	sed '/ifndef.*NO_LONG_DOUBLE/,/#endif/d' < mathdef.h > mathdef.h.new
	mv mathdef.h.new mathdef.h
    popd
popd

# gcc
pushd %{cross_gcc}/build
    %make
    DESTDIR=%{build_root} %make install
    mv -f %{build_root}%{gccdir}/include-fixed/*.h		\
	  %{build_root}%{gccdir}/include
    rm -fr %{build_root}%{gccdir}/include-fixed
    rm -fr %{build_root}%{gccdir}/install-tools
popd

# gdb
pushd %{cross_gdb}
    %cross_configure						\
	%{build_config}						\
	--disable-nls						\
	--disable-sim						\
	--with-bugurl=https://qa.mandriva.com			\
	--with-build-time-tools=%{build_root}%{sysroot}/bin	\
	--with-gdb-datadir=%{prefix}/share/gdb			\
	--with-system-gdbinit=%{libdir}/gdbinit			\
	--target=%{target}
    %make
    DESTDIR=%{build_root} %make install
popd

# gdbserver
pushd %{cross_gdb}/gdb/gdbserver
    %cross_configure						\
	%{build_config}						\
	--with-bugurl=https://qa.mandriva.com			\
	--host=%{target}
    %make
    DESTDIR=%{build_root}%{sysroot} %make install
popd

#-----------------------------------------------------------------------
%install
cp -fpar %{build_root}/* %{buildroot}

rm -f %{buildroot}%{_libdir}/libiberty.a
rm -f %{buildroot}%{prefix}/lib*/libiberty.a
mv %{buildroot}%{_datadir}/gcc-%{gcc_version} %{buildroot}%{sysroot}%{_datadir}
rm -fr %{buildroot}%{_datadir}
rm -fr %{buildroot}%{_includedir}
rm -f %{buildroot}%{_bindir}/%{target}-c++
ln -sf %{_bindir}/%{target}-g++ %{buildroot}%{_bindir}/%{target}-c++
rm -f %{buildroot}%{sysroot}/bin/{c++,g++,gcc}
ln -sf %{_bindir}/%{target}-g++ %{buildroot}%{prefix}/bin/c++
ln -sf %{_bindir}/%{target}-g++ %{buildroot}%{prefix}/bin/g++
ln -sf %{_bindir}/%{target}-gcc %{buildroot}%{prefix}/bin/gcc

mkdir -p %{buildroot}%{sysroot}%{_datadir}/gdb/auto-load%{cross_libdir}
mv -f %{buildroot}%{prefix}/lib/libstdc++.so.*.py		\
	%{buildroot}%{sysroot}%{_datadir}/gdb/auto-load%{cross_libdir}
perl -pi -e 's|%%{_datadir}/gcc-%{gcc_version}/python|%{py_puresitedir}|;' \
    %{buildroot}%{_datadir}/gdb/auto-load%{cross_libdir}/libstdc++.*.py

pushd %{buildroot}%{prefix}/lib
    mv -f libgcc* libgomp* libmudf* libstdc* libsupc* %{buildroot}%{sysroot}%{cross_libdir}
popd
perl -pi -e 's|libdir=/usr/%{_target}/lib|libdir=/usr/lib|;'	\
	%{buildroot}%{sysroot}%{_prefix}/lib/*.la
