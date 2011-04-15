# functions with printf format attribute but with special parser and also
# receiving non constant format strings
%define		Werror_cflags			%{nil}

# avoid failures when testing if compiler used to build gcc can generate
# shared objects (regardless of unresolved symbols)
%define		_disable_ld_no_undefined	1

# avoid build failure due to configure built with different autoconf version
%define		_disable_libtoolize		1

#-----------------------------------------------------------------------
%define		cross			arm
%define 	target			%{cross}-linux
%define 	binutils_version	2.21.51.0.6
%define 	gcc_version		4.6.0
%define 	kernel_version		2.6.38.1
%define 	glibc_version		2.13
%define 	sysroot			%{_builddir}/cross-%{target}-1.0/sysroot
%define		prefix			%{_prefix}/%{target}

Name:		cross-%{target}
Version:	1.0
Release:	1
License:	GPLv3+
Group:		Development/Other
Summary:	Cross platform utilities for %{target}
URL:            http://www.gnu.org/software
Source0:	http://ftp.kernel.org/pub/linux/devel/binutils/binutils-%{binutils_version}.tar.bz2
# from linux-userspace-headers package
Source1:	kernel-headers-%{kernel_version}.tar.xz
Source2:	ftp://gcc.gnu.org/pub/gcc/releases/gcc-%{gcc_version}/gcc-core-%{gcc_version}.tar.bz2
Source3:	ftp://gcc.gnu.org/pub/gcc/releases/gcc-%{gcc_version}/gcc-g++-%{gcc_version}.tar.bz2
Source4:	ftp://ftp.gnu.org/gnu/glibc/glibc-%{glibc_version}.tar.xz
Source5:	ftp://ftp.gnu.org/gnu/glibc/glibc-ports-%{glibc_version}.tar.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}-root

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gcc
BuildRequires:	gettext
BuildRequires:	texinfo

%description
Cross platform utilities for %{target}.

#-----------------------------------------------------------------------
%package	-n cross-%{cross}-binutils
License:	GPLv3+
Summary:        Cross Compiling GNU binutils targeted at %{target}
Group:		Development/Other
Version:	%{binutils_version}

%description	-n cross-%{cross}-binutils
This is a Cross Compiling version of GNU binutils, which can be used to
assemble and link binaries for the %{target} platform, instead of for the
native %{_arch} platform.

%files		-n cross-%{cross}-binutils
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
%{prefix}/bin/ld.bfd
%{prefix}/bin/nm
%{prefix}/bin/objcopy
%{prefix}/bin/objdump
%{prefix}/bin/ranlib
%{prefix}/bin/strip
%{prefix}/lib/ldscripts

#-----------------------------------------------------------------------
%package	-n cross-%{cross}-glibc
License:	GPLv3+
Summary:        Cross Compiled GNU C Library targeted at %{target}
Group:		Development/Other
Version:	%{glibc_version}

%description	-n cross-%{cross}-glibc
This is a Cross Compiled version of the GNU C Library, which can be used to
compile and link binaries for the %{target} platform, instead of for the
native %{_arch} platform.

%files		-n cross-%{cross}-glibc
%defattr(-,root,root,-)

#-----------------------------------------------------------------------
%prep
%setup -q -c -a1 -a2 -a3 -a4 -a5

#-----------------------------------------------------------------------
%build
OPT_FLAGS=`echo %{optflags} |					\
	sed	-e 's/\(-Wp,\)\?-D_FORTIFY_SOURCE=[12]//g'	\
		-e 's/-m\(31\|32\|64\)//g'			\
		-e 's/-fstack-protector//g'			\
		-e 's/--param=ssp-buffer-size=4//'		\
		-e 's/-pipe//g'`
OPT_FLAGS=`echo "$OPT_FLAGS" | sed -e 's/[[:blank:]]\+/ /g'`

mkdir -p %{sysroot}%{prefix}/include

mkdir -p binutils-%{binutils_version}/build
pushd binutils-%{binutils_version}/build
    CFLAGS="$OPT_FLAGS" 					\
    CXXFLAGS="$OPT_FLAGS"					\
    CONFIGURE_TOP=..
    %configure2_5x						\
	--disable-nls						\
	--disable-werror					\
	--target=%{target}
    %make
    make install DESTDIR=%{sysroot}
popd

# headers to bootstrap gcc
pushd kernel-headers-%{kernel_version}
    TARGET=%{cross} ./create_asm_headers.sh
    ./make_versionh.sh
    rm -fr drm
    rm -f create_asm_headers.sh make_versionh.sh
popd
mv -f kernel-headers-%{kernel_version}/* %{sysroot}%{prefix}/include

cp -far glibc-ports-%{glibc_version}/* glibc-%{glibc_version}

mkdir -p glibc-%{glibc_version}/build
pushd glibc-%{glibc_version}/build
    ../configure						\
	--prefix=%{sysroot}%{prefix}				\
	--with-headers=%{sysroot}%{prefix}/include		\
	--without-fp						\
	--without-selinux					\
	--target=%{target}
    # workaround "consistency check"
    ln -sf %{sysroot}%{prefix}/include %{sysroot}%{_includedir}
    # ignore error rebuilding rpcgen
    make -k install-headers || :
    # missing gnu/stubs.h required by libgcc
    cp -far ../include/gnu %{sysroot}%{prefix}/include
    # missing stdio_lim.h required by libgcc
    cp -far bits/stdio_lim.h %{sysroot}%{prefix}/include/bits
popd

# "bootstrap" gcc
mkdir -p gcc-%{gcc_version}/build
pushd gcc-%{gcc_version}/build
    CC=%{__cc}							\
    CFLAGS="$OPT_FLAGS" 					\
    CXXFLAGS="$OPT_FLAGS"					\
    ../configure						\
	--prefix=%{sysroot}%{_prefix}				\
	--libdir=%{sysroot}%{_prefix}/lib			\
	--libexecdir=%{sysroot}%{_prefix}/lib			\
	--disable-libgcj					\
	--disable-libffi					\
	--disable-libgomp					\
	--disable-libquadmath					\
	--disable-libquadmath-support				\
	--disable-libmudflap					\
	--disable-libssp					\
	--enable-long-long					\
	--disable-werror					\
	--enable-__cxa_atexit					\
	--disable-bootstrap					\
	--enable-checking=release				\
	--enable-gnu-unique-object				\
	--enable-languages="c"					\
	--enable-linker-build-id				\
	--disable-plugin					\
	--enable-threads=posix					\
	--with-system-zlib					\
	--with-bugurl=https://qa.mandriva.com/			\
	--with-build-sysroot=%{sysroot}				\
	--with-headers						\
	--disable-multilib					\
	--disable-nls						\
	--disable-shared					\
	--with-float=soft					\
	--target=%{target}
    mkdir -p %{target}/libgcc
    ln -sf %{sysroot}%{prefix}/include %{target}/libgcc/include
    %make
    make install
popd

# build glibc
rm -fr glibc-%{glibc_version}/build/*
pushd glibc-%{glibc_version}/build
    CONFIGURE_TOP=..						\
    CC=%{target}-gcc						\
    PATH=%{sysroot}%{prefix}/bin:%{sysroot}%{_bindir}:$PATH	\
    %configure2_5x						\
	--without-fp						\
	--without-selinux					\
	--disable-profile					\
	--host=%{target}					\
	--target=%{target}
    make install DESTDIR=%{sysroot}
popd

# build gcc
rm -fr gcc-%{gcc_version}/build/*
pushd gcc-%{gcc_version}/build
    CONFIGURE_TOP=..						\
    CC=%{__cc}							\
    CFLAGS="$OPT_FLAGS" 					\
    CXXFLAGS="$OPT_FLAGS"					\
    %configure2_5x						\
	--disable-libgcj					\
	--disable-libffi					\
	--disable-libgomp					\
	--disable-libquadmath					\
	--disable-libquadmath-support				\
	--disable-libmudflap					\
	--disable-libssp					\
	--enable-long-long					\
	--disable-werror					\
	--enable-__cxa_atexit					\
	--disable-bootstrap					\
	--enable-checking=release				\
	--enable-gnu-unique-object				\
	--enable-languages="c,c++"				\
	--enable-linker-build-id				\
	--disable-plugin					\
	--enable-threads=posix					\
	--with-system-zlib					\
	--with-bugurl=https://qa.mandriva.com/			\
	--with-build-sysroot=%{sysroot}				\
	--with-headers						\
	--disable-multilib					\
	--disable-nls						\
	--disable-shared					\
	--with-float=soft					\
	--target=%{target}
    mkdir -p %{target}/libgcc
    ln -sf %{sysroot}%{prefix}/include %{target}/libgcc/include
    %make
popd

#-----------------------------------------------------------------------
%install
pushd binutils-%{binutils_version}/build
    %makeinstall_std
    rm -fr %{buildroot}%{_infodir}
    rm -fr %{buildroot}%{_libdir}/libiberty.a
    rm -f %{buildroot}%{_mandir}/man1/{dlltool,nlmconv,windmc,windres}.1*
    rm -f %{buildroot}%{_mandir}/man1/wind*
popd

pushd glibc-%{glibc_version}/build
    %makeinstall_std
popd

pushd gcc-%{gcc_version}/build
    %makeinstall_std
popd

#-----------------------------------------------------------------------
%clean
rm -fr %{buildroot}
