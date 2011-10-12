# croos-arm package initially based on codesourcery now coverted on
# basically a stage1 of the DJ Delorie arm bootstrap scripts at
# http://fedorapeople.org/~djdelorie/
# adapted for the mandriva arm bootstrap setup

# build bootstrap target side libraries and binaries?
%define		build_bootstrap		1

%define		_enable_debug_packages	%{nil}
%define		debug_package		%{nil}
%define		__find_provides		%{SOURCE100}
%define		__find_requires		%{SOURCE100}

%define		arch			arm
%define		target			armv7l-mandriva-linux-gnueabi
%define		prefix			%{_prefix}/%{target}
%define		sysroot			%{prefix}/sysroot
%define 	build_root		%{_builddir}/%{arch}-cross/root
%define		cross_libdir		%{_prefix}/lib
%define		cross_configure		./configure --prefix=%{_prefix} --exec-prefix=%{_prefix} --bindir=%{_bindir} --sbindir=%{_sbindir} --sysconfdir=%{_sysconfdir} --datadir=%{_datadir} --includedir=%{_includedir} --libdir=%{cross_libdir} --libexecdir=%{cross_libdir} --localstatedir=%{_localstatedir} --sharedstatedir=%{_sharedstatedir} --mandir=%{_mandir} --infodir=%{_infodir}
%define		__cross_configure	../%{cross_configure}
%define		build_config		--build=%{_target_platform} --disable-werror --with-build-sysroot=%{build_root}%{sysroot}
%define		target_config		--with-cpu=cortex-a8 --with-tune=cortex-a8 --with-arch=armv7-a --with-mode=thumb --with-float=softfp --with-fpu=vfpv3-d16 --with-abi=aapcs-linux --with-sysroot=%{sysroot} --target=%{target}
%define		host_config		--with-cpu=cortex-a8 --with-tune=cortex-a8 --with-arch=armv7-a --with-mode=thumb --with-float=softfp --with-fpu=vfpv3-d16 --with-abi=aapcs-linux --host=%{target} --target=%{target}

%define		gcc_version		4.6.1
%define		cross_linux		linux-2.6.38
%define		cross_binutils		binutils-2.22.51
%define		cross_gcc		gcc-4.6-20111007
%define		cross_glibc		glibc-2.14-121-g5551a7b
%define		cross_gdb		gdb-7.1
%define		cross_gmp		gmp-5.0.2
%define		cross_mpfr		mpfr-3.1.0
%define		cross_mpc		mpc-0.9
%define		cross_ppl		ppl-0.11
%define		cross_cloog		cloog-parma-0.16.1
%define		cross_zlib		zlib-1.2.5
%define		cross_bash		bash-4.2
%define		cross_make		make-3.82
%define		cross_sed		sed-4.2.1
%define		cross_coreutils		coreutils-8.12
%define		cross_util_linux	util-linux-2.20
%define		cross_tar		tar-1.26
%define		cross_gzip		gzip-1.4
%define		cross_bzip2		bzip2-1.0.6
%define		cross_diffutils		diffutils-3.2
%define		cross_findutils		findutils-4.5.10
%define		cross_gawk		gawk-4.0.0
%define		cross_patch		patch-2.6.1
%define		cross_unzip		unzip60
%define		cross_which		which-2.20
%define		cross_xz		xz-5.1.1alpha
%define		cross_grep		grep-2.9

%define 	build_root		%{_builddir}/cross-%{arch}/root
%define		gccdir			%{prefix}/lib/gcc/%{target}/%{gcc_version}

Name:		cross-arm
Release:	2
Version:	2011.10
License:	GPLv3+
Group:		Development/Other
Summary:	ARM GNU/Linux cross toolchain
URL:		http://fedorapeople.org/~djdelorie/

# revision: 677434
# repsys co kernel; cd kernel; ./build_sources
# mv SOURCES/%{cross_linux}.tar.bz2 ../cross-arm/SOURCES
Source0:	%{cross_linux}.tar.bz2

# revision: 703525
# repsys co binutils; cd binutils
# rpmbuild -bp --define "_topdir `pwd`" --define "_target_cpu arm" SPECS/binutils.spec
# cd BUILD; tar jcf %{cross_binutils}.tar.bz2 %{cross_binutils}; mv %{cross_binutils}.tar.bz2 ../../cross-arm/SOURCES
Source1:	%{cross_binutils}.tar.bz2

# revision: 703958
# repsys co gcc; cd gcc
# rpmbuild -bp --define "_topdir `pwd`" --define "_target_cpu armv7l" SPECS/gcc.spec
# cd BUILD; tar jcf %{cross_gcc}.tar.bz2 %{cross_gcc}; mv %{cross_gcc}.tar.bz2 ../../cross-arm/SOURCES
Source2:	%{cross_gcc}.tar.bz2

# revision: 702438
# repsys co glibc; cd glibc
# rpmbuild -bp --define "_topdir `pwd`" --define "_target_cpu arm" SPECS/glibc.spec
# cd BUILD; tar jcf %{cross_glibc}.tar.bz2 %{cross_glibc}; mv %{cross_glibc}.tar.bz2 ../../cross-arm/SOURCES
Source3:	%{cross_glibc}.tar.bz2

# revision: 682884
# repsys co gdb; cd gdb
# rpmbuild -bp --define "_topdir `pwd`" --define "_target_cpu arm" SPECS/gdb.spec
# cd BUILD; tar jcf %{cross_gdb}.bz2 %{cross_gdb}; mv %{cross_gdb}.tar.bz2 ../../cross-arm/SOURCES
Source4:	%{cross_gdb}.tar.bz2

# revision: 673760
# repsys co gmp; cd gmp
# rpmbuild -bp --define "_topdir `pwd`" --define "_target_cpu arm" SPECS/gmp.spec
# cd BUILD; tar jcf %{cross_gmp}.tar.bz2 %{cross_gmp}; mv %{cross_gmp}.tar.bz2 ../../cross-arm/SOURCES
Source5:	%{cross_gmp}.tar.bz2

# revision: 703197
# repsys co mpfr; cd mpfr
# rpmbuild -bp --define "_topdir `pwd`" --define "_target_cpu arm" SPECS/mpfr.spec
# cd BUILD; tar jcf %{cross_mpfr}.tar.bz2 %{cross_mpfr}; mv %{cross_mpfr}.tar.bz2 ../../cross-arm/SOURCES
Source6:	%{cross_mpfr}.tar.bz2

# revision: 662383
# repsys co libmpc; cd libmpc
# rpmbuild -bp --define "_topdir `pwd`" --define "_target_cpu arm" SPECS/libmpc.spec
# cd BUILD; tar jcf %{cross_mpc}.tar.bz2 %{cross_mpc}; mv %{cross_mpc}.tar.bz2 ../../cross-arm/SOURCES
Source7:	%{cross_mpc}.tar.bz2

# revision: 662383
# repsys co ppl; cd ppl
# rpmbuild -bp --define "_topdir `pwd`" --define "_target_cpu arm" SPECS/ppl.spec
# cd BUILD; tar jcf %{cross_ppl}.tar.bz2 %{cross_ppl}; mv %{cross_ppl}.tar.bz2 ../../cross-arm/SOURCES
Source8:	%{cross_ppl}.tar.bz2

# revision: 652216
# repsys co cloog-ppl; cd cloog-ppl
# rpmbuild -bp --define "_topdir `pwd`" --define "_target_cpu arm" SPECS/cloog.spec
# cd BUILD; tar jcf %{cross_cloog}.tar.bz2 %{cross_cloog}; mv %{cross_cloog}.tar.bz2 ../../cross-arm/SOURCES
Source9:	%{cross_cloog}.tar.bz2

# revision: 703340
# repsys co zlib; cd zlib
# rpmbuild -bp --define "_topdir `pwd`" --define "_target_cpu arm" SPECS/zlib.spec
# cd BUILD; tar jcf %{cross_zlib}.tar.bz2 %{cross_zlib}; mv %{cross_zlib}.tar.bz2 ../../cross-arm/SOURCES
Source10:	%{cross_zlib}.tar.bz2

# revision: 696270
# repsys co bash; cd bash
# rpmbuild -bp --define "_topdir `pwd`" --define "_target_cpu arm" SPECS/bash.spec
# cd BUILD; tar jcf %{cross_bash}.tar.bz2 %{cross_bash}; mv %{cross_bash}.tar.bz2 ../../cross-arm/SOURCES
Source11:	%{cross_bash}.tar.bz2

# revision: 655741
# repsys co make; cd make
# rpmbuild -bp --define "_topdir `pwd`" --define "_target_cpu arm" SPECS/make.spec
# cd BUILD; tar jcf %{cross_make}.tar.bz2 %{cross_make}; mv %{cross_make}.tar.bz2 ../../cross-arm/SOURCES
Source12:	%{cross_make}.tar.bz2

# revision: 669967
# repsys co sed; cd sed
# rpmbuild -bp --define "_topdir `pwd`" --define "_target_cpu arm" SPECS/sed.spec
# cd BUILD; tar jcf %{cross_sed}.tar.bz2 %{cross_sed}; mv %{cross_sed}.tar.bz2 ../../cross-arm/SOURCES
Source13:	%{cross_sed}.tar.bz2

# revision: 692305
# repsys co sed; cd sed
# rpmbuild -bp --define "_topdir `pwd`" --define "_target_cpu arm" SPECS/coreutils.spec
# cd BUILD; tar jcf %{cross_coreutils}.tar.bz2 %{cross_coreutils}; mv %{cross_coreutils}.tar.bz2 ../../cross-arm/SOURCES
Source14:	%{cross_coreutils}.tar.bz2

# revision: 698245
# repsys co util-linux; cd util-linux
# rpmbuild -bp --define "_topdir `pwd`" --define "_target_cpu arm" SPECS/util-linux.spec
# cd BUILD; tar jcf %{cross_util_linux}.tar.bz2 %{cross_util_linux}; mv %{cross_util_linux}.tar.bz2 ../../cross-arm/SOURCES
Source15:	%{cross_util_linux}.tar.bz2

# revision: 692310
# repsys co tar; cd tar
# rpmbuild -bp --define "_topdir `pwd`" --define "_target_cpu arm" SPECS/tar.spec
# cd BUILD; tar jcf %{cross_tar}.tar.bz2 %{cross_tar}; mv %{cross_tar}.tar.bz2 ../../cross-arm/SOURCES
Source16:	%{cross_tar}.tar.bz2

# revision: 664965
# repsys co gzip; cd gzip
# rpmbuild -bp --define "_topdir `pwd`" --define "_target_cpu arm" SPECS/gzip.spec
# cd BUILD; tar jcf %{cross_gzip}.tar.bz2 %{cross_gzip}; mv %{cross_gzip}.tar.bz2 ../../cross-arm/SOURCES
Source17:	%{cross_gzip}.tar.bz2

# revision: 663345
# repsys co bzip2; cd bzip2
# rpmbuild -bp --define "_topdir `pwd`" --define "_target_cpu arm" SPECS/bzip2.spec
# cd BUILD/%{cross_bzip2}; patch -R -p1 < ../../SOURCES/%{cross_bzip2}-makefile.diff; cd ../..
# cd BUILD; tar jcf %{cross_bzip2}.tar.bz2 %{cross_bzip2}; mv %{cross_bzip2}.tar.bz2 ../../cross-arm/SOURCES
Source18:	%{cross_bzip2}.tar.bz2

# revision: 698281
# repsys co diffutils; cd diffutils
# rpmbuild -bp --define "_topdir `pwd`" --define "_target_cpu arm" SPECS/diffutils.spec
# cd BUILD; tar jcf %{cross_diffutils}.tar.bz2 %{cross_diffutils}; mv %{cross_diffutils}.tar.bz2 ../../cross-arm/SOURCES
Source19:	%{cross_diffutils}.tar.bz2

# revision: 674766
# repsys co findutils; cd findutils
# rpmbuild -bp --define "_topdir `pwd`" --define "_target_cpu arm" SPECS/findutils.spec
# cd BUILD; tar jcf %{cross_findutils}.tar.bz2 %{cross_findutils}; mv %{cross_findutils}.tar.bz2 ../../cross-arm/SOURCES
Source20:	%{cross_findutils}.tar.bz2

# revision: 703540
# repsys co gawk; cd gawk
# rpmbuild -bp --define "_topdir `pwd`" --define "_target_cpu arm" SPECS/gawk.spec
# cd BUILD; tar jcf %{cross_gawk}.tar.bz2 %{cross_gawk}; mv %{cross_gawk}.tar.bz2 ../../cross-arm/SOURCES
Source21:	%{cross_gawk}.tar.bz2

# revision: 666991
# repsys co patch; cd patch
# rpmbuild -bp --define "_topdir `pwd`" --define "_target_cpu arm" SPECS/patch.spec
# cd BUILD; tar jcf %{cross_patch}.tar.bz2 %{cross_patch}; mv %{cross_patch}.tar.bz2 ../../cross-arm/SOURCES
Source22:	%{cross_patch}.tar.bz2

# revision: 693305
# repsys co unzip; cd unzip
# rpmbuild -bp --define "_topdir `pwd`" --define "_target_cpu arm" SPECS/unzip.spec
# cd BUILD/%{cross_unzip}; patch -R -p1 < ../../SOURCES/unzip-6.0-libnatspec.patch; cd ../..
# cd BUILD; tar jcf %{cross_unzip}.tar.bz2 %{cross_unzip}; mv %{cross_unzip}.tar.bz2 ../../cross-arm/SOURCES
Source23:	%{cross_unzip}.tar.bz2

# revision: 670807
# repsys co which; cd which
# rpmbuild -bp --define "_topdir `pwd`" --define "_target_cpu arm" SPECS/which.spec
# cd BUILD; tar jcf %{cross_which}.tar.bz2 %{cross_which}; mv %{cross_which}.tar.bz2 ../../cross-arm/SOURCES
Source24:	%{cross_which}.tar.bz2

# revision: 695233
# repsys co xz; cd xz
# rpmbuild -bp --define "_topdir `pwd`" --define "_target_cpu arm" SPECS/xz.spec
# cd BUILD; tar jcf %{cross_xz}.tar.bz2 %{cross_xz}; mv %{cross_xz}.tar.bz2 ../../cross-arm/SOURCES
Source25:	%{cross_xz}.tar.bz2

# revision: 686779
# repsys co grep; cd grep
# rpmbuild -bp --define "_topdir `pwd`" --define "_target_cpu arm" SPECS/grep.spec
# cd BUILD; tar jcf %{cross_grep}.tar.bz2 %{cross_grep}; mv %{cross_grep}.tar.bz2 ../../cross-arm/SOURCES
Source26:	%{cross_grep}.tar.bz2

Source98:	stage2.tar.bz2
Source99:	README
Source100:	find-nothing

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
Requires:	cross-%{arch}-host = %{EVRD}
Requires:	cross-%{arch}-gdb = %{EVRD}

Patch0:		cross-arm-gdb.patch
Patch1:		cross-arm-gcc.patch
Patch2:		cross-arm-util-linux.patch

%description
%{summary}.

%files
%defattr(-,root,root,-)

########################################################################
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

########################################################################
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
%dir %{sysroot}%{cross_libdir}
%{sysroot}%{cross_libdir}/libgcc*
%{sysroot}%{cross_libdir}/libgomp*
%{sysroot}%{cross_libdir}/libmudf*

########################################################################
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
%{sysroot}%{cross_libdir}/libstdc++*
%{sysroot}%{cross_libdir}/libsupc++*
%{sysroot}%{_datadir}/gcc-%{gcc_version}

########################################################################
%package	host
Summary:	ARM GNU/Linux cross toolchain host
Requires:	cross-%{arch}-gcc = %{EVRD}
Provides:	cross-%{arch}-glibc = %{EVRD}

%description	host
%{summary}.

%post		host
    rm -fr %{sysroot}/tmp
    rm -fr %{sysroot}/dev
    mkdir -p %{sysroot}/tmp
    chmod 1777 %{sysroot}/tmp
    mkdir -p %{sysroot}/dev
    pushd %{sysroot}/dev
	mknod null	c   1 3
	mknod zero	c   1 5
	mknod random	c   1 8
	mknod urandom	c   1 9
	mknod tty	c   5 0
	mknod console	c   5 1
	mknod sda	b   8 0
	mknod sda1	b   8 1
	mknod sda2	b   8 2
	mknod sda3	b   8 3
	mknod sda4	b   8 4
	mknod mmcblk0	b 179 0
	mknod mmcblk0p1 b 179 1
	mknod mmcblk0p2 b 179 2
	mknod mmcblk0p3 b 179 3
	mknod mmcblk0p4 b 179 4
	mknod ttyO0	c 253 0
	mknod ttyO1	c 253 1
	mknod ttyO2	c 253 2
	mknod ttyO3	c 253 3
	chmod a+rw null zero
    popd

%postun		host
if [ $1 -eq 0 ]; then
    rm -fr %{sysroot}/tmp
    rm -fr %{sysroot}/dev
fi

%files		host
%defattr(-,root,root,-)
%{sysroot}%{_bindir}
%exclude %{sysroot}%{_bindir}/gdbserver
%{sysroot}%{_sysconfdir}
%{sysroot}%{_includedir}
%{sysroot}/lib
%{sysroot}%{_prefix}/lib
%exclude %{sysroot}%{cross_libdir}/libgcc*
%exclude %{sysroot}%{cross_libdir}/libgomp*
%exclude %{sysroot}%{cross_libdir}/libmudf*
%exclude %{sysroot}%{cross_libdir}/libstdc++*
%exclude %{sysroot}%{cross_libdir}/libsupc++*
%{sysroot}/sbin
%{sysroot}%{_sbindir}
%{sysroot}%{_datadir}
%exclude %{sysroot}%{_datadir}/gcc-%{gcc_version}
%{sysroot}%{_localstatedir}/db
%if %{build_bootstrap}
%{sysroot}%{prefix}
%{sysroot}/bin
%{sysroot}/stage2
%endif

########################################################################
%package	gdb
Summary:	ARM GNU/Linux cross toolchain gdb
Requires:	cross-%{arch}-host = %{EVRD}

%description	gdb
%{summary}.

%files		gdb
%defattr(-,root,root,-)
%{_bindir}/%{target}-gdb
%{_bindir}/%{target}-gdbtui
%{_bindir}/%{target}-gstack
%{prefix}/share/gdb
%{sysroot}%{_bindir}/gdbserver

########################################################################
%prep
%setup -q -c -n cross-%{arch} -T -a 0 -a 1 -a 2 -a 3 -a 4 -a 5 -a 6 -a 7 -a 8 -a 9 -a 10 -a 11 -a 12 -a 13 -a 14 -a 15 -a 16 -a 17 -a 18 -a 19 -a 20 -a 21 -a 22 -a 23 -a 24 -a 25 -a 26

%patch0 -p1

########################################################################
%build
unset CC CXX CFLAGS CXXFLAGS AR LD AS
export PATH=%{build_root}%{_bindir}:$PATH

#-----------------------------------------------------------------------
# host cross-tools

# kernel headers
pushd %{cross_linux}
    %make ARCH=%{arch}						\
	INSTALL_HDR_PATH=%{build_root}%{sysroot}%{_prefix}	\
	headers_install
popd

# binutils
pushd %{cross_binutils}
    %cross_configure						\
	%{build_config}						\
	%{target_config}
    %make
    %make install DESTDIR=%{build_root}
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
mkdir -p %{cross_glibc}/build; pushd %{cross_glibc}/build
    echo libc_cv_forced_unwind=yes > config.cache
    echo libc_cv_c_cleanup=yes >> config.cache
    echo libc_cv_ctors_header=no >> config.cache
    %__cross_configure						\
	%{build_config}						\
	--with-headers=%{build_root}%{sysroot}%{_includedir}	\
	--enable-kernel=2.6.32					\
	--enable-bind-now					\
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
    %make install-target-libgcc DESTDIR=%{build_root}
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
    %make install DESTDIR=%{build_root}
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
    %make install DESTDIR=%{build_root}
popd

# gdbserver
pushd %{cross_gdb}/gdb/gdbserver
    %cross_configure						\
	%{build_config}						\
	--with-bugurl=https://qa.mandriva.com			\
	--host=%{target}
    %make
    %make install DESTDIR=%{build_root}%{sysroot}
popd

#-----------------------------------------------------------------------
# target side libraries
pushd %{build_root}%{prefix}/lib
    mv -f libgcc* libgomp* libmudf* libstdc* libsupc* %{build_root}%{sysroot}%{cross_libdir}
popd
rm -f %{build_root}%{sysroot}%{cross_libdir}/*.la

%if %{build_bootstrap}
# gmp
pushd %{cross_gmp}
    %cross_configure						\
	%{build_config}						\
	--host=%{target}					\
	--enable-cxx						\
	%{target_config}
    %make
    %make install DESTDIR=%{build_root}%{sysroot}
    rm -f %{build_root}%{sysroot}%{cross_libdir}/*.la
popd

# mpfr
pushd %{cross_mpfr}
    %cross_configure						\
	%{build_config}						\
	--host=%{target}					\
	%{target_config}
    %make
    %make install DESTDIR=%{build_root}%{sysroot}
    rm -f %{build_root}%{sysroot}%{cross_libdir}/*.la
popd

# mpc
pushd %{cross_mpc}
    %cross_configure						\
	%{build_config}						\
	--host=%{target}					\
	%{target_config}
    %make
    %make install DESTDIR=%{build_root}%{sysroot}
    rm -f %{build_root}%{sysroot}%{cross_libdir}/*.la
popd

# ppl
pushd %{cross_ppl}
    %cross_configure						\
	%{build_config}						\
	--host=%{target}					\
	--enable-shared						\
	--enable-interfaces="c++ c"				\
	 --with-gmp-prefix=%{build_root}%{sysroot}%{_prefix}	\
	%{target_config}
    %make
    %make install DESTDIR=%{build_root}%{sysroot}
    rm -f %{build_root}%{sysroot}%{cross_libdir}/*.la
popd

# cloog
pushd %{cross_cloog}
    %cross_configure						\
	%{build_config}						\
	--host=%{target}					\
	--with-ppl=system					\
	--disable-static					\
	%{target_config}
    %make
    %make install DESTDIR=%{build_root}%{sysroot}
    rm -f %{build_root}%{sysroot}%{cross_libdir}/*.la
popd

# no libselinux on current mandriva

# zlib
pushd %{cross_zlib}
    CHOST=%{target}						\
    ./configure							\
	 --prefix=%{_prefix}					\
	--libdir=%{cross_libdir}				\
	--includedir=%{_includedir}
    %make
    %make install DESTDIR=%{build_root}%{sysroot}
popd

#-----------------------------------------------------------------------
# target side applications

# target binutils
rm -fr %{cross_binutils}; tar jxf %{_sourcedir}/%{cross_binutils}.tar.bz2
pushd %{cross_binutils}
    %cross_configure						\
	%{build_config}						\
	%{host_config}
    %make
    %make install DESTDIR=%{build_root}%{sysroot}
popd

# target gcc
rm -fr %{cross_gcc}; tar jxf %{_sourcedir}/%{cross_gcc}.tar.bz2
patch -l -p1 < %{PATCH1}
mkdir -p %{cross_gcc}/build; pushd %{cross_gcc}/build
    echo %{vendor} > ../gcc/DEV-PHASE
    sed -i -e 's/4\.6\.2/4.6.1/' ../gcc/BASE-VER
    %__cross_configure						\
	%{build_config}						\
	--enable-languages=c,c++				\
	--disable-libssp					\
	%{host_config}
    %make
    %make install DESTDIR=%{build_root}%{sysroot}
popd

# bash
pushd %{cross_bash}
    cat <<EOF > config.cache
bash_cv_func_ctype_nonascii=yes
bash_cv_opendir_not_robust=no
bash_cv_ulimit_maxfds=yes
bash_cv_func_sigsetjmp=present
bash_cv_printf_a_format=yes
bash_cv_job_control_missing=present
bash_cv_sys_named_pipes=present
bash_cv_unusable_rtsigs=no
EOF
    %cross_configure						\
	%{build_config}						\
	--cache-file=config.cache				\
	%{host_config}
    %make
    %make install DESTDIR=%{build_root}%{sysroot}
    mkdir -p %{build_root}%{sysroot}/bin
    pushd %{build_root}%{sysroot}/bin
	mv ../usr/bin/bash .
	ln -s bash sh
    popd
popd

# make
pushd %{cross_make}
    %cross_configure						\
	%{build_config}						\
	%{host_config}
    %make
    %make install DESTDIR=%{build_root}%{sysroot}
popd

# sed
pushd %{cross_sed}
    %cross_configure						\
	%{build_config}						\
	%{host_config}
    # Touch sed.1 so that it will not be built.
    # The makefile in the sed/doc directory attempts to run the
    # built sed binary in order to extract the --help output, but
    # this fails because the sed binary is a cross-tool.
    touch doc/sed.1
    %make
    %make install DESTDIR=%{build_root}%{sysroot}
popd

# coreutils
pushd %{cross_coreutils}
    %cross_configure						\
	%{build_config}						\
	%{host_config}
    for i in $(cd $PWD//man; echo *.x)
    do
	base=`echo $i | sed 's/\.x//'`
	touch man/$base.1
    done
    %make CFLAGS="$CFLAGS -fpic -fPIC"
    %make install DESTDIR=%{build_root}%{sysroot}
popd

# util-linux
patch -l -p1 < %{PATCH2}
pushd %{cross_util_linux}
    %cross_configure						\
	%{build_config}						\
	--without-ncurses					\
	--disable-wall						\
	%{host_config}
    %make
    %make install DESTDIR=%{build_root}%{sysroot}
popd

# tar
pushd %{cross_tar}
    %cross_configure						\
	%{build_config}						\
	%{host_config}						\
	--bindir=/bin
    %make
    %make install DESTDIR=%{build_root}%{sysroot}
popd

# gzip
pushd %{cross_gzip}
    %cross_configure						\
	%{build_config}						\
	%{host_config}
    %make
    %make install DESTDIR=%{build_root}%{sysroot}
popd

# bzip2
pushd %{cross_bzip2}
    %make							\
	CC=%{target}-gcc					\
	AR=%{target}-ar						\
	RANLIB=%{target}-ranlib					\
	PREFIX=%{_prefix}					\
	CFLAGS="$CFLAGS -fpic -fPIC"				\
	libbz2.a bzip2 bzip2recover
    %make							\
	CC=%{target}-gcc					\
	AR=%{target}-ar						\
	RANLIB=%{target}-ranlib					\
	PREFIX=%{build_root}%{sysroot}%{_prefix}		\
	install
    # the installation makes symbols links with our host's paths
    # in them, we need to redo those.
    pushd %{build_root}%{sysroot}%{_bindir}
	rm bzless;  ln -s bzmore bzless
	rm bzfgrep; ln -s bzgrep bzfgrep
	rm bzcmp;   ln -s bzdiff bzcmp
	rm bzegrep; ln -s bzgrep bzegrep
    popd
popd

# diffutils
pushd %{cross_diffutils}
    %cross_configure						\
	%{build_config}						\
	%{host_config}
    %make
    %make install DESTDIR=%{build_root}%{sysroot}
popd

# findutils
pushd %{cross_findutils}
    %cross_configure						\
	%{build_config}						\
	%{host_config}
    %make
    %make install DESTDIR=%{build_root}%{sysroot}
popd

# gawk
pushd %{cross_gawk}
    %cross_configure						\
	%{build_config}						\
	%{host_config}
    %make
    %make install DESTDIR=%{build_root}%{sysroot}
popd

# patch
pushd %{cross_patch}
    cat <<EOF > config.cache
ac_cv_func_strnlen_working=yes
EOF
    %cross_configure						\
	%{build_config}						\
	--cache-file=config.cache				\
	%{host_config}
    %make
    %make install DESTDIR=%{build_root}%{sysroot}
popd

# unzip
pushd %{cross_unzip}
    %make -f unix/Makefile					\
	CC=%{target}-gcc					\
	AS=%{target}-as						\
	AR=%{target}-ar						\
	STRIP=%{target}-strip					\
	RANLIB=%{target}-ranlib					\
	prefix=%{_prefix}					\
	CFLAGS="$CFLAGS -DUNIX=1" generic
    %make -f unix/Makefile					\
	CC=%{target}-gcc					\
	AS=%{target}-as						\
	AR=%{target}-ar						\
	STRIP=%{target}-strip					\
	RANLIB=%{target}-ranlib					\
	prefix=%{build_root}%{sysroot}%{_prefix}		\
	install 
popd

# which
pushd %{cross_which}
    %cross_configure						\
	%{build_config}						\
	%{host_config}
    %make
    %make install DESTDIR=%{build_root}%{sysroot}
popd

# xz
pushd %{cross_xz}
    %cross_configure						\
	%{build_config}						\
	%{host_config}
    %make
    %make install DESTDIR=%{build_root}%{sysroot}
popd

# grep
pushd %{cross_grep}
    %cross_configure						\
	%{build_config}						\
	%{host_config}
    %make
    %make install DESTDIR=%{build_root}%{sysroot}
popd

# build_bootstrap
%endif

########################################################################
%install
# needed by rpm 4.x
mkdir -p %{buildroot}

cp -fpar %{build_root}/* %{buildroot}

# binutils
rm -f %{buildroot}%{_libdir}/libiberty.a
rm -f %{buildroot}%{prefix}/lib*/libiberty.a

rm -fr %{buildroot}%{_datadir}
rm -fr %{buildroot}%{_includedir}
rm -fr %{buildroot}%{sysroot}%{_mandir}
rm -fr %{buildroot}%{sysroot}%{_prefix}/man
rm -fr %{buildroot}%{sysroot}%{_infodir}
rm -fr %{buildroot}%{sysroot}%{_docdir}

rm -f %{buildroot}%{_bindir}/%{target}-c++
ln -sf %{_bindir}/%{target}-g++ %{buildroot}%{_bindir}/%{target}-c++
rm -f %{buildroot}%{sysroot}/bin/{c++,g++,gcc}
ln -sf %{_bindir}/%{target}-g++ %{buildroot}%{prefix}/bin/c++
ln -sf %{_bindir}/%{target}-g++ %{buildroot}%{prefix}/bin/g++
ln -sf %{_bindir}/%{target}-gcc %{buildroot}%{prefix}/bin/gcc

mkdir -p %{buildroot}%{prefix}/share/gdb/auto-load%{cross_libdir}
mv -f %{buildroot}%{sysroot}%{cross_libdir}/libstdc++.so.*.py		\
	%{buildroot}%{prefix}/share/gdb/auto-load%{cross_libdir}
perl -pi -e 's|%%{_datadir}/gcc-%{gcc_version}/python|%{py_puresitedir}|;' \
    %{buildroot}%{prefix}/share/gdb/auto-load%{cross_libdir}/libstdc++.*.py

find %{buildroot}%{sysroot}%{_includedir}			\
    -name .install -o -name ..install.cmd | xargs rm -f

%if %{build_bootstrap}
tar jxf %{SOURCE98} -C %{buildroot}%{sysroot}
(
    echo TARGET=%{target}
    echo RPMTARGET=%{target}
    echo TCONFIGARGS=\"--prefix=/usr --disable-werror %{host_config} \"	\
	| sed 's/--build=[^ ]*//'					\
	| sed 's/--host=[^ ]*//'					\
	| sed 's/--target=[^ ]*//'
) > %{buildroot}%{sysroot}/stage2/local.conf
mkdir -p %{buildroot}%{sysroot}/stage2/rpmbuild
mkdir -p %{buildroot}%{sysroot}/stage2/builds

cp %{SOURCE99} %{buildroot}%{sysroot}/stage2
%endif
