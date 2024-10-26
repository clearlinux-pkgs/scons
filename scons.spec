#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
# autospec version: v20
# autospec commit: b2d28bb
#
Name     : scons
Version  : 3.1.2
Release  : 49
URL      : https://sourceforge.net/projects/scons/files/scons/3.1.2/scons-3.1.2.tar.gz
Source0  : https://sourceforge.net/projects/scons/files/scons/3.1.2/scons-3.1.2.tar.gz
Summary  : Open Source next-generation build tool.
Group    : Development/Tools
License  : MIT
Requires: scons-bin = %{version}-%{release}
Requires: scons-license = %{version}-%{release}
Requires: scons-man = %{version}-%{release}
BuildRequires : buildreq-distutils3
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: manpage.patch

%description
Improved, cross-platform substitute for the classic Make
        utility.  In short, SCons is an easier, more reliable
        and faster way to build software.

%package bin
Summary: bin components for the scons package.
Group: Binaries
Requires: scons-license = %{version}-%{release}

%description bin
bin components for the scons package.


%package license
Summary: license components for the scons package.
Group: Default

%description license
license components for the scons package.


%package man
Summary: man components for the scons package.
Group: Default

%description man
man components for the scons package.


%prep
%setup -q -n scons-3.1.2
cd %{_builddir}/scons-3.1.2
%patch -P 1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1729968035
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/scons
cp %{_builddir}/scons-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/scons/7340866649e9d1091a571077d1f8c8632c8a4fc8 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## install_append content
find %{buildroot} -name "*.pyc" | xargs rm
## install_append end

%files
%defattr(-,root,root,-)
/usr/lib/scons/SCons/Action.py
/usr/lib/scons/SCons/Builder.py
/usr/lib/scons/SCons/CacheDir.py
/usr/lib/scons/SCons/Conftest.py
/usr/lib/scons/SCons/Debug.py
/usr/lib/scons/SCons/Defaults.py
/usr/lib/scons/SCons/Environment.py
/usr/lib/scons/SCons/Errors.py
/usr/lib/scons/SCons/Executor.py
/usr/lib/scons/SCons/Job.py
/usr/lib/scons/SCons/Memoize.py
/usr/lib/scons/SCons/Node/Alias.py
/usr/lib/scons/SCons/Node/FS.py
/usr/lib/scons/SCons/Node/Python.py
/usr/lib/scons/SCons/Node/__init__.py
/usr/lib/scons/SCons/PathList.py
/usr/lib/scons/SCons/Platform/__init__.py
/usr/lib/scons/SCons/Platform/aix.py
/usr/lib/scons/SCons/Platform/cygwin.py
/usr/lib/scons/SCons/Platform/darwin.py
/usr/lib/scons/SCons/Platform/hpux.py
/usr/lib/scons/SCons/Platform/irix.py
/usr/lib/scons/SCons/Platform/mingw.py
/usr/lib/scons/SCons/Platform/os2.py
/usr/lib/scons/SCons/Platform/posix.py
/usr/lib/scons/SCons/Platform/sunos.py
/usr/lib/scons/SCons/Platform/virtualenv.py
/usr/lib/scons/SCons/Platform/win32.py
/usr/lib/scons/SCons/SConf.py
/usr/lib/scons/SCons/SConsign.py
/usr/lib/scons/SCons/Scanner/C.py
/usr/lib/scons/SCons/Scanner/D.py
/usr/lib/scons/SCons/Scanner/Dir.py
/usr/lib/scons/SCons/Scanner/Fortran.py
/usr/lib/scons/SCons/Scanner/IDL.py
/usr/lib/scons/SCons/Scanner/LaTeX.py
/usr/lib/scons/SCons/Scanner/Prog.py
/usr/lib/scons/SCons/Scanner/RC.py
/usr/lib/scons/SCons/Scanner/SWIG.py
/usr/lib/scons/SCons/Scanner/__init__.py
/usr/lib/scons/SCons/Script/Interactive.py
/usr/lib/scons/SCons/Script/Main.py
/usr/lib/scons/SCons/Script/SConsOptions.py
/usr/lib/scons/SCons/Script/SConscript.py
/usr/lib/scons/SCons/Script/__init__.py
/usr/lib/scons/SCons/Subst.py
/usr/lib/scons/SCons/Taskmaster.py
/usr/lib/scons/SCons/Tool/386asm.py
/usr/lib/scons/SCons/Tool/DCommon.py
/usr/lib/scons/SCons/Tool/FortranCommon.py
/usr/lib/scons/SCons/Tool/GettextCommon.py
/usr/lib/scons/SCons/Tool/JavaCommon.py
/usr/lib/scons/SCons/Tool/MSCommon/__init__.py
/usr/lib/scons/SCons/Tool/MSCommon/arch.py
/usr/lib/scons/SCons/Tool/MSCommon/common.py
/usr/lib/scons/SCons/Tool/MSCommon/netframework.py
/usr/lib/scons/SCons/Tool/MSCommon/sdk.py
/usr/lib/scons/SCons/Tool/MSCommon/vc.py
/usr/lib/scons/SCons/Tool/MSCommon/vs.py
/usr/lib/scons/SCons/Tool/PharLapCommon.py
/usr/lib/scons/SCons/Tool/__init__.py
/usr/lib/scons/SCons/Tool/aixc++.py
/usr/lib/scons/SCons/Tool/aixcc.py
/usr/lib/scons/SCons/Tool/aixcxx.py
/usr/lib/scons/SCons/Tool/aixf77.py
/usr/lib/scons/SCons/Tool/aixlink.py
/usr/lib/scons/SCons/Tool/applelink.py
/usr/lib/scons/SCons/Tool/ar.py
/usr/lib/scons/SCons/Tool/as.py
/usr/lib/scons/SCons/Tool/bcc32.py
/usr/lib/scons/SCons/Tool/c++.py
/usr/lib/scons/SCons/Tool/cc.py
/usr/lib/scons/SCons/Tool/clang.py
/usr/lib/scons/SCons/Tool/clangCommon/__init__.py
/usr/lib/scons/SCons/Tool/clangxx.py
/usr/lib/scons/SCons/Tool/cvf.py
/usr/lib/scons/SCons/Tool/cxx.py
/usr/lib/scons/SCons/Tool/cyglink.py
/usr/lib/scons/SCons/Tool/default.py
/usr/lib/scons/SCons/Tool/dmd.py
/usr/lib/scons/SCons/Tool/docbook/__init__.py
/usr/lib/scons/SCons/Tool/dvi.py
/usr/lib/scons/SCons/Tool/dvipdf.py
/usr/lib/scons/SCons/Tool/dvips.py
/usr/lib/scons/SCons/Tool/f03.py
/usr/lib/scons/SCons/Tool/f08.py
/usr/lib/scons/SCons/Tool/f77.py
/usr/lib/scons/SCons/Tool/f90.py
/usr/lib/scons/SCons/Tool/f95.py
/usr/lib/scons/SCons/Tool/filesystem.py
/usr/lib/scons/SCons/Tool/fortran.py
/usr/lib/scons/SCons/Tool/g++.py
/usr/lib/scons/SCons/Tool/g77.py
/usr/lib/scons/SCons/Tool/gas.py
/usr/lib/scons/SCons/Tool/gcc.py
/usr/lib/scons/SCons/Tool/gdc.py
/usr/lib/scons/SCons/Tool/gettext_tool.py
/usr/lib/scons/SCons/Tool/gfortran.py
/usr/lib/scons/SCons/Tool/gnulink.py
/usr/lib/scons/SCons/Tool/gs.py
/usr/lib/scons/SCons/Tool/gxx.py
/usr/lib/scons/SCons/Tool/hpc++.py
/usr/lib/scons/SCons/Tool/hpcc.py
/usr/lib/scons/SCons/Tool/hpcxx.py
/usr/lib/scons/SCons/Tool/hplink.py
/usr/lib/scons/SCons/Tool/icc.py
/usr/lib/scons/SCons/Tool/icl.py
/usr/lib/scons/SCons/Tool/ifl.py
/usr/lib/scons/SCons/Tool/ifort.py
/usr/lib/scons/SCons/Tool/ilink.py
/usr/lib/scons/SCons/Tool/ilink32.py
/usr/lib/scons/SCons/Tool/install.py
/usr/lib/scons/SCons/Tool/intelc.py
/usr/lib/scons/SCons/Tool/ipkg.py
/usr/lib/scons/SCons/Tool/jar.py
/usr/lib/scons/SCons/Tool/javac.py
/usr/lib/scons/SCons/Tool/javah.py
/usr/lib/scons/SCons/Tool/latex.py
/usr/lib/scons/SCons/Tool/ldc.py
/usr/lib/scons/SCons/Tool/lex.py
/usr/lib/scons/SCons/Tool/link.py
/usr/lib/scons/SCons/Tool/linkloc.py
/usr/lib/scons/SCons/Tool/m4.py
/usr/lib/scons/SCons/Tool/masm.py
/usr/lib/scons/SCons/Tool/midl.py
/usr/lib/scons/SCons/Tool/mingw.py
/usr/lib/scons/SCons/Tool/msgfmt.py
/usr/lib/scons/SCons/Tool/msginit.py
/usr/lib/scons/SCons/Tool/msgmerge.py
/usr/lib/scons/SCons/Tool/mslib.py
/usr/lib/scons/SCons/Tool/mslink.py
/usr/lib/scons/SCons/Tool/mssdk.py
/usr/lib/scons/SCons/Tool/msvc.py
/usr/lib/scons/SCons/Tool/msvs.py
/usr/lib/scons/SCons/Tool/mwcc.py
/usr/lib/scons/SCons/Tool/mwld.py
/usr/lib/scons/SCons/Tool/nasm.py
/usr/lib/scons/SCons/Tool/packaging/__init__.py
/usr/lib/scons/SCons/Tool/packaging/ipk.py
/usr/lib/scons/SCons/Tool/packaging/msi.py
/usr/lib/scons/SCons/Tool/packaging/rpm.py
/usr/lib/scons/SCons/Tool/packaging/src_tarbz2.py
/usr/lib/scons/SCons/Tool/packaging/src_targz.py
/usr/lib/scons/SCons/Tool/packaging/src_tarxz.py
/usr/lib/scons/SCons/Tool/packaging/src_zip.py
/usr/lib/scons/SCons/Tool/packaging/tarbz2.py
/usr/lib/scons/SCons/Tool/packaging/targz.py
/usr/lib/scons/SCons/Tool/packaging/tarxz.py
/usr/lib/scons/SCons/Tool/packaging/zip.py
/usr/lib/scons/SCons/Tool/pdf.py
/usr/lib/scons/SCons/Tool/pdflatex.py
/usr/lib/scons/SCons/Tool/pdftex.py
/usr/lib/scons/SCons/Tool/qt.py
/usr/lib/scons/SCons/Tool/rmic.py
/usr/lib/scons/SCons/Tool/rpcgen.py
/usr/lib/scons/SCons/Tool/rpm.py
/usr/lib/scons/SCons/Tool/rpmutils.py
/usr/lib/scons/SCons/Tool/sgiar.py
/usr/lib/scons/SCons/Tool/sgic++.py
/usr/lib/scons/SCons/Tool/sgicc.py
/usr/lib/scons/SCons/Tool/sgicxx.py
/usr/lib/scons/SCons/Tool/sgilink.py
/usr/lib/scons/SCons/Tool/sunar.py
/usr/lib/scons/SCons/Tool/sunc++.py
/usr/lib/scons/SCons/Tool/suncc.py
/usr/lib/scons/SCons/Tool/suncxx.py
/usr/lib/scons/SCons/Tool/sunf77.py
/usr/lib/scons/SCons/Tool/sunf90.py
/usr/lib/scons/SCons/Tool/sunf95.py
/usr/lib/scons/SCons/Tool/sunlink.py
/usr/lib/scons/SCons/Tool/swig.py
/usr/lib/scons/SCons/Tool/tar.py
/usr/lib/scons/SCons/Tool/tex.py
/usr/lib/scons/SCons/Tool/textfile.py
/usr/lib/scons/SCons/Tool/tlib.py
/usr/lib/scons/SCons/Tool/wix.py
/usr/lib/scons/SCons/Tool/xgettext.py
/usr/lib/scons/SCons/Tool/yacc.py
/usr/lib/scons/SCons/Tool/zip.py
/usr/lib/scons/SCons/Util.py
/usr/lib/scons/SCons/Variables/BoolVariable.py
/usr/lib/scons/SCons/Variables/EnumVariable.py
/usr/lib/scons/SCons/Variables/ListVariable.py
/usr/lib/scons/SCons/Variables/PackageVariable.py
/usr/lib/scons/SCons/Variables/PathVariable.py
/usr/lib/scons/SCons/Variables/__init__.py
/usr/lib/scons/SCons/Warnings.py
/usr/lib/scons/SCons/__init__.py
/usr/lib/scons/SCons/__main__.py
/usr/lib/scons/SCons/compat/__init__.py
/usr/lib/scons/SCons/compat/_scons_dbm.py
/usr/lib/scons/SCons/cpp.py
/usr/lib/scons/SCons/dblite.py
/usr/lib/scons/SCons/exitfuncs.py
/usr/lib/scons/scons-3.1.2-py3.13.egg-info/PKG-INFO
/usr/lib/scons/scons-3.1.2-py3.13.egg-info/SOURCES.txt
/usr/lib/scons/scons-3.1.2-py3.13.egg-info/dependency_links.txt
/usr/lib/scons/scons-3.1.2-py3.13.egg-info/top_level.txt

%files bin
%defattr(-,root,root,-)
/usr/bin/scons
/usr/bin/scons-3.1.2
/usr/bin/scons-3.1.2.bat
/usr/bin/scons-configure-cache
/usr/bin/scons-configure-cache-3.1.2
/usr/bin/scons-time
/usr/bin/scons-time-3.1.2
/usr/bin/scons.bat
/usr/bin/sconsign
/usr/bin/sconsign-3.1.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/scons/7340866649e9d1091a571077d1f8c8632c8a4fc8

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/scons-time.1
/usr/share/man/man1/scons.1
/usr/share/man/man1/sconsign.1
