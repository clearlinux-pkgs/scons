#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : scons
Version  : 2.3.5
Release  : 7
URL      : https://bitbucket.org/scons/scons/downloads/scons-2.3.5.tar.gz
Source0  : https://bitbucket.org/scons/scons/downloads/scons-2.3.5.tar.gz
Summary  : Open Source next-generation build tool.
Group    : Development/Tools
License  : MIT
Requires: scons-bin
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : setuptools

%description
SCons - a software construction tool
Version 2.3.5
This is SCons, a tool for building software (and other files).  SCons is
implemented in Python, and its "configuration files" are actually Python
scripts, allowing you to use the full power of a real scripting language
to solve build problems.  You do not, however, need to know Python to
use SCons effectively.

%package bin
Summary: bin components for the scons package.
Group: Binaries

%description bin
bin components for the scons package.


%prep
%setup -q -n scons-2.3.5

%build
python2 setup.py build -b py2

%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)
/usr/lib/scons-2.3.5/SCons/Action.py
/usr/lib/scons-2.3.5/SCons/Action.pyc
/usr/lib/scons-2.3.5/SCons/Action.pyo
/usr/lib/scons-2.3.5/SCons/Builder.py
/usr/lib/scons-2.3.5/SCons/Builder.pyc
/usr/lib/scons-2.3.5/SCons/Builder.pyo
/usr/lib/scons-2.3.5/SCons/CacheDir.py
/usr/lib/scons-2.3.5/SCons/CacheDir.pyc
/usr/lib/scons-2.3.5/SCons/CacheDir.pyo
/usr/lib/scons-2.3.5/SCons/Conftest.py
/usr/lib/scons-2.3.5/SCons/Conftest.pyc
/usr/lib/scons-2.3.5/SCons/Conftest.pyo
/usr/lib/scons-2.3.5/SCons/Debug.py
/usr/lib/scons-2.3.5/SCons/Debug.pyc
/usr/lib/scons-2.3.5/SCons/Debug.pyo
/usr/lib/scons-2.3.5/SCons/Defaults.py
/usr/lib/scons-2.3.5/SCons/Defaults.pyc
/usr/lib/scons-2.3.5/SCons/Defaults.pyo
/usr/lib/scons-2.3.5/SCons/Environment.py
/usr/lib/scons-2.3.5/SCons/Environment.pyc
/usr/lib/scons-2.3.5/SCons/Environment.pyo
/usr/lib/scons-2.3.5/SCons/Errors.py
/usr/lib/scons-2.3.5/SCons/Errors.pyc
/usr/lib/scons-2.3.5/SCons/Errors.pyo
/usr/lib/scons-2.3.5/SCons/Executor.py
/usr/lib/scons-2.3.5/SCons/Executor.pyc
/usr/lib/scons-2.3.5/SCons/Executor.pyo
/usr/lib/scons-2.3.5/SCons/Job.py
/usr/lib/scons-2.3.5/SCons/Job.pyc
/usr/lib/scons-2.3.5/SCons/Job.pyo
/usr/lib/scons-2.3.5/SCons/Memoize.py
/usr/lib/scons-2.3.5/SCons/Memoize.pyc
/usr/lib/scons-2.3.5/SCons/Memoize.pyo
/usr/lib/scons-2.3.5/SCons/Node/Alias.py
/usr/lib/scons-2.3.5/SCons/Node/Alias.pyc
/usr/lib/scons-2.3.5/SCons/Node/Alias.pyo
/usr/lib/scons-2.3.5/SCons/Node/FS.py
/usr/lib/scons-2.3.5/SCons/Node/FS.pyc
/usr/lib/scons-2.3.5/SCons/Node/FS.pyo
/usr/lib/scons-2.3.5/SCons/Node/Python.py
/usr/lib/scons-2.3.5/SCons/Node/Python.pyc
/usr/lib/scons-2.3.5/SCons/Node/Python.pyo
/usr/lib/scons-2.3.5/SCons/Node/__init__.py
/usr/lib/scons-2.3.5/SCons/Node/__init__.pyc
/usr/lib/scons-2.3.5/SCons/Node/__init__.pyo
/usr/lib/scons-2.3.5/SCons/Options/BoolOption.py
/usr/lib/scons-2.3.5/SCons/Options/BoolOption.pyc
/usr/lib/scons-2.3.5/SCons/Options/BoolOption.pyo
/usr/lib/scons-2.3.5/SCons/Options/EnumOption.py
/usr/lib/scons-2.3.5/SCons/Options/EnumOption.pyc
/usr/lib/scons-2.3.5/SCons/Options/EnumOption.pyo
/usr/lib/scons-2.3.5/SCons/Options/ListOption.py
/usr/lib/scons-2.3.5/SCons/Options/ListOption.pyc
/usr/lib/scons-2.3.5/SCons/Options/ListOption.pyo
/usr/lib/scons-2.3.5/SCons/Options/PackageOption.py
/usr/lib/scons-2.3.5/SCons/Options/PackageOption.pyc
/usr/lib/scons-2.3.5/SCons/Options/PackageOption.pyo
/usr/lib/scons-2.3.5/SCons/Options/PathOption.py
/usr/lib/scons-2.3.5/SCons/Options/PathOption.pyc
/usr/lib/scons-2.3.5/SCons/Options/PathOption.pyo
/usr/lib/scons-2.3.5/SCons/Options/__init__.py
/usr/lib/scons-2.3.5/SCons/Options/__init__.pyc
/usr/lib/scons-2.3.5/SCons/Options/__init__.pyo
/usr/lib/scons-2.3.5/SCons/PathList.py
/usr/lib/scons-2.3.5/SCons/PathList.pyc
/usr/lib/scons-2.3.5/SCons/PathList.pyo
/usr/lib/scons-2.3.5/SCons/Platform/__init__.py
/usr/lib/scons-2.3.5/SCons/Platform/__init__.pyc
/usr/lib/scons-2.3.5/SCons/Platform/__init__.pyo
/usr/lib/scons-2.3.5/SCons/Platform/aix.py
/usr/lib/scons-2.3.5/SCons/Platform/aix.pyc
/usr/lib/scons-2.3.5/SCons/Platform/aix.pyo
/usr/lib/scons-2.3.5/SCons/Platform/cygwin.py
/usr/lib/scons-2.3.5/SCons/Platform/cygwin.pyc
/usr/lib/scons-2.3.5/SCons/Platform/cygwin.pyo
/usr/lib/scons-2.3.5/SCons/Platform/darwin.py
/usr/lib/scons-2.3.5/SCons/Platform/darwin.pyc
/usr/lib/scons-2.3.5/SCons/Platform/darwin.pyo
/usr/lib/scons-2.3.5/SCons/Platform/hpux.py
/usr/lib/scons-2.3.5/SCons/Platform/hpux.pyc
/usr/lib/scons-2.3.5/SCons/Platform/hpux.pyo
/usr/lib/scons-2.3.5/SCons/Platform/irix.py
/usr/lib/scons-2.3.5/SCons/Platform/irix.pyc
/usr/lib/scons-2.3.5/SCons/Platform/irix.pyo
/usr/lib/scons-2.3.5/SCons/Platform/os2.py
/usr/lib/scons-2.3.5/SCons/Platform/os2.pyc
/usr/lib/scons-2.3.5/SCons/Platform/os2.pyo
/usr/lib/scons-2.3.5/SCons/Platform/posix.py
/usr/lib/scons-2.3.5/SCons/Platform/posix.pyc
/usr/lib/scons-2.3.5/SCons/Platform/posix.pyo
/usr/lib/scons-2.3.5/SCons/Platform/sunos.py
/usr/lib/scons-2.3.5/SCons/Platform/sunos.pyc
/usr/lib/scons-2.3.5/SCons/Platform/sunos.pyo
/usr/lib/scons-2.3.5/SCons/Platform/win32.py
/usr/lib/scons-2.3.5/SCons/Platform/win32.pyc
/usr/lib/scons-2.3.5/SCons/Platform/win32.pyo
/usr/lib/scons-2.3.5/SCons/SConf.py
/usr/lib/scons-2.3.5/SCons/SConf.pyc
/usr/lib/scons-2.3.5/SCons/SConf.pyo
/usr/lib/scons-2.3.5/SCons/SConsign.py
/usr/lib/scons-2.3.5/SCons/SConsign.pyc
/usr/lib/scons-2.3.5/SCons/SConsign.pyo
/usr/lib/scons-2.3.5/SCons/Scanner/C.py
/usr/lib/scons-2.3.5/SCons/Scanner/C.pyc
/usr/lib/scons-2.3.5/SCons/Scanner/C.pyo
/usr/lib/scons-2.3.5/SCons/Scanner/D.py
/usr/lib/scons-2.3.5/SCons/Scanner/D.pyc
/usr/lib/scons-2.3.5/SCons/Scanner/D.pyo
/usr/lib/scons-2.3.5/SCons/Scanner/Dir.py
/usr/lib/scons-2.3.5/SCons/Scanner/Dir.pyc
/usr/lib/scons-2.3.5/SCons/Scanner/Dir.pyo
/usr/lib/scons-2.3.5/SCons/Scanner/Fortran.py
/usr/lib/scons-2.3.5/SCons/Scanner/Fortran.pyc
/usr/lib/scons-2.3.5/SCons/Scanner/Fortran.pyo
/usr/lib/scons-2.3.5/SCons/Scanner/IDL.py
/usr/lib/scons-2.3.5/SCons/Scanner/IDL.pyc
/usr/lib/scons-2.3.5/SCons/Scanner/IDL.pyo
/usr/lib/scons-2.3.5/SCons/Scanner/LaTeX.py
/usr/lib/scons-2.3.5/SCons/Scanner/LaTeX.pyc
/usr/lib/scons-2.3.5/SCons/Scanner/LaTeX.pyo
/usr/lib/scons-2.3.5/SCons/Scanner/Prog.py
/usr/lib/scons-2.3.5/SCons/Scanner/Prog.pyc
/usr/lib/scons-2.3.5/SCons/Scanner/Prog.pyo
/usr/lib/scons-2.3.5/SCons/Scanner/RC.py
/usr/lib/scons-2.3.5/SCons/Scanner/RC.pyc
/usr/lib/scons-2.3.5/SCons/Scanner/RC.pyo
/usr/lib/scons-2.3.5/SCons/Scanner/__init__.py
/usr/lib/scons-2.3.5/SCons/Scanner/__init__.pyc
/usr/lib/scons-2.3.5/SCons/Scanner/__init__.pyo
/usr/lib/scons-2.3.5/SCons/Script/Interactive.py
/usr/lib/scons-2.3.5/SCons/Script/Interactive.pyc
/usr/lib/scons-2.3.5/SCons/Script/Interactive.pyo
/usr/lib/scons-2.3.5/SCons/Script/Main.py
/usr/lib/scons-2.3.5/SCons/Script/Main.pyc
/usr/lib/scons-2.3.5/SCons/Script/Main.pyo
/usr/lib/scons-2.3.5/SCons/Script/SConsOptions.py
/usr/lib/scons-2.3.5/SCons/Script/SConsOptions.pyc
/usr/lib/scons-2.3.5/SCons/Script/SConsOptions.pyo
/usr/lib/scons-2.3.5/SCons/Script/SConscript.py
/usr/lib/scons-2.3.5/SCons/Script/SConscript.pyc
/usr/lib/scons-2.3.5/SCons/Script/SConscript.pyo
/usr/lib/scons-2.3.5/SCons/Script/__init__.py
/usr/lib/scons-2.3.5/SCons/Script/__init__.pyc
/usr/lib/scons-2.3.5/SCons/Script/__init__.pyo
/usr/lib/scons-2.3.5/SCons/Sig.py
/usr/lib/scons-2.3.5/SCons/Sig.pyc
/usr/lib/scons-2.3.5/SCons/Sig.pyo
/usr/lib/scons-2.3.5/SCons/Subst.py
/usr/lib/scons-2.3.5/SCons/Subst.pyc
/usr/lib/scons-2.3.5/SCons/Subst.pyo
/usr/lib/scons-2.3.5/SCons/Taskmaster.py
/usr/lib/scons-2.3.5/SCons/Taskmaster.pyc
/usr/lib/scons-2.3.5/SCons/Taskmaster.pyo
/usr/lib/scons-2.3.5/SCons/Tool/386asm.py
/usr/lib/scons-2.3.5/SCons/Tool/386asm.pyc
/usr/lib/scons-2.3.5/SCons/Tool/386asm.pyo
/usr/lib/scons-2.3.5/SCons/Tool/BitKeeper.py
/usr/lib/scons-2.3.5/SCons/Tool/BitKeeper.pyc
/usr/lib/scons-2.3.5/SCons/Tool/BitKeeper.pyo
/usr/lib/scons-2.3.5/SCons/Tool/CVS.py
/usr/lib/scons-2.3.5/SCons/Tool/CVS.pyc
/usr/lib/scons-2.3.5/SCons/Tool/CVS.pyo
/usr/lib/scons-2.3.5/SCons/Tool/DCommon.py
/usr/lib/scons-2.3.5/SCons/Tool/DCommon.pyc
/usr/lib/scons-2.3.5/SCons/Tool/DCommon.pyo
/usr/lib/scons-2.3.5/SCons/Tool/FortranCommon.py
/usr/lib/scons-2.3.5/SCons/Tool/FortranCommon.pyc
/usr/lib/scons-2.3.5/SCons/Tool/FortranCommon.pyo
/usr/lib/scons-2.3.5/SCons/Tool/GettextCommon.py
/usr/lib/scons-2.3.5/SCons/Tool/GettextCommon.pyc
/usr/lib/scons-2.3.5/SCons/Tool/GettextCommon.pyo
/usr/lib/scons-2.3.5/SCons/Tool/JavaCommon.py
/usr/lib/scons-2.3.5/SCons/Tool/JavaCommon.pyc
/usr/lib/scons-2.3.5/SCons/Tool/JavaCommon.pyo
/usr/lib/scons-2.3.5/SCons/Tool/MSCommon/__init__.py
/usr/lib/scons-2.3.5/SCons/Tool/MSCommon/__init__.pyc
/usr/lib/scons-2.3.5/SCons/Tool/MSCommon/__init__.pyo
/usr/lib/scons-2.3.5/SCons/Tool/MSCommon/arch.py
/usr/lib/scons-2.3.5/SCons/Tool/MSCommon/arch.pyc
/usr/lib/scons-2.3.5/SCons/Tool/MSCommon/arch.pyo
/usr/lib/scons-2.3.5/SCons/Tool/MSCommon/common.py
/usr/lib/scons-2.3.5/SCons/Tool/MSCommon/common.pyc
/usr/lib/scons-2.3.5/SCons/Tool/MSCommon/common.pyo
/usr/lib/scons-2.3.5/SCons/Tool/MSCommon/netframework.py
/usr/lib/scons-2.3.5/SCons/Tool/MSCommon/netframework.pyc
/usr/lib/scons-2.3.5/SCons/Tool/MSCommon/netframework.pyo
/usr/lib/scons-2.3.5/SCons/Tool/MSCommon/sdk.py
/usr/lib/scons-2.3.5/SCons/Tool/MSCommon/sdk.pyc
/usr/lib/scons-2.3.5/SCons/Tool/MSCommon/sdk.pyo
/usr/lib/scons-2.3.5/SCons/Tool/MSCommon/vc.py
/usr/lib/scons-2.3.5/SCons/Tool/MSCommon/vc.pyc
/usr/lib/scons-2.3.5/SCons/Tool/MSCommon/vc.pyo
/usr/lib/scons-2.3.5/SCons/Tool/MSCommon/vs.py
/usr/lib/scons-2.3.5/SCons/Tool/MSCommon/vs.pyc
/usr/lib/scons-2.3.5/SCons/Tool/MSCommon/vs.pyo
/usr/lib/scons-2.3.5/SCons/Tool/Perforce.py
/usr/lib/scons-2.3.5/SCons/Tool/Perforce.pyc
/usr/lib/scons-2.3.5/SCons/Tool/Perforce.pyo
/usr/lib/scons-2.3.5/SCons/Tool/PharLapCommon.py
/usr/lib/scons-2.3.5/SCons/Tool/PharLapCommon.pyc
/usr/lib/scons-2.3.5/SCons/Tool/PharLapCommon.pyo
/usr/lib/scons-2.3.5/SCons/Tool/RCS.py
/usr/lib/scons-2.3.5/SCons/Tool/RCS.pyc
/usr/lib/scons-2.3.5/SCons/Tool/RCS.pyo
/usr/lib/scons-2.3.5/SCons/Tool/SCCS.py
/usr/lib/scons-2.3.5/SCons/Tool/SCCS.pyc
/usr/lib/scons-2.3.5/SCons/Tool/SCCS.pyo
/usr/lib/scons-2.3.5/SCons/Tool/Subversion.py
/usr/lib/scons-2.3.5/SCons/Tool/Subversion.pyc
/usr/lib/scons-2.3.5/SCons/Tool/Subversion.pyo
/usr/lib/scons-2.3.5/SCons/Tool/__init__.py
/usr/lib/scons-2.3.5/SCons/Tool/__init__.pyc
/usr/lib/scons-2.3.5/SCons/Tool/__init__.pyo
/usr/lib/scons-2.3.5/SCons/Tool/aixc++.py
/usr/lib/scons-2.3.5/SCons/Tool/aixc++.pyc
/usr/lib/scons-2.3.5/SCons/Tool/aixc++.pyo
/usr/lib/scons-2.3.5/SCons/Tool/aixcc.py
/usr/lib/scons-2.3.5/SCons/Tool/aixcc.pyc
/usr/lib/scons-2.3.5/SCons/Tool/aixcc.pyo
/usr/lib/scons-2.3.5/SCons/Tool/aixf77.py
/usr/lib/scons-2.3.5/SCons/Tool/aixf77.pyc
/usr/lib/scons-2.3.5/SCons/Tool/aixf77.pyo
/usr/lib/scons-2.3.5/SCons/Tool/aixlink.py
/usr/lib/scons-2.3.5/SCons/Tool/aixlink.pyc
/usr/lib/scons-2.3.5/SCons/Tool/aixlink.pyo
/usr/lib/scons-2.3.5/SCons/Tool/applelink.py
/usr/lib/scons-2.3.5/SCons/Tool/applelink.pyc
/usr/lib/scons-2.3.5/SCons/Tool/applelink.pyo
/usr/lib/scons-2.3.5/SCons/Tool/ar.py
/usr/lib/scons-2.3.5/SCons/Tool/ar.pyc
/usr/lib/scons-2.3.5/SCons/Tool/ar.pyo
/usr/lib/scons-2.3.5/SCons/Tool/as.py
/usr/lib/scons-2.3.5/SCons/Tool/as.pyc
/usr/lib/scons-2.3.5/SCons/Tool/as.pyo
/usr/lib/scons-2.3.5/SCons/Tool/bcc32.py
/usr/lib/scons-2.3.5/SCons/Tool/bcc32.pyc
/usr/lib/scons-2.3.5/SCons/Tool/bcc32.pyo
/usr/lib/scons-2.3.5/SCons/Tool/c++.py
/usr/lib/scons-2.3.5/SCons/Tool/c++.pyc
/usr/lib/scons-2.3.5/SCons/Tool/c++.pyo
/usr/lib/scons-2.3.5/SCons/Tool/cc.py
/usr/lib/scons-2.3.5/SCons/Tool/cc.pyc
/usr/lib/scons-2.3.5/SCons/Tool/cc.pyo
/usr/lib/scons-2.3.5/SCons/Tool/cvf.py
/usr/lib/scons-2.3.5/SCons/Tool/cvf.pyc
/usr/lib/scons-2.3.5/SCons/Tool/cvf.pyo
/usr/lib/scons-2.3.5/SCons/Tool/cyglink.py
/usr/lib/scons-2.3.5/SCons/Tool/cyglink.pyc
/usr/lib/scons-2.3.5/SCons/Tool/cyglink.pyo
/usr/lib/scons-2.3.5/SCons/Tool/default.py
/usr/lib/scons-2.3.5/SCons/Tool/default.pyc
/usr/lib/scons-2.3.5/SCons/Tool/default.pyo
/usr/lib/scons-2.3.5/SCons/Tool/dmd.py
/usr/lib/scons-2.3.5/SCons/Tool/dmd.pyc
/usr/lib/scons-2.3.5/SCons/Tool/dmd.pyo
/usr/lib/scons-2.3.5/SCons/Tool/docbook/__init__.py
/usr/lib/scons-2.3.5/SCons/Tool/docbook/__init__.pyc
/usr/lib/scons-2.3.5/SCons/Tool/docbook/__init__.pyo
/usr/lib/scons-2.3.5/SCons/Tool/dvi.py
/usr/lib/scons-2.3.5/SCons/Tool/dvi.pyc
/usr/lib/scons-2.3.5/SCons/Tool/dvi.pyo
/usr/lib/scons-2.3.5/SCons/Tool/dvipdf.py
/usr/lib/scons-2.3.5/SCons/Tool/dvipdf.pyc
/usr/lib/scons-2.3.5/SCons/Tool/dvipdf.pyo
/usr/lib/scons-2.3.5/SCons/Tool/dvips.py
/usr/lib/scons-2.3.5/SCons/Tool/dvips.pyc
/usr/lib/scons-2.3.5/SCons/Tool/dvips.pyo
/usr/lib/scons-2.3.5/SCons/Tool/f03.py
/usr/lib/scons-2.3.5/SCons/Tool/f03.pyc
/usr/lib/scons-2.3.5/SCons/Tool/f03.pyo
/usr/lib/scons-2.3.5/SCons/Tool/f77.py
/usr/lib/scons-2.3.5/SCons/Tool/f77.pyc
/usr/lib/scons-2.3.5/SCons/Tool/f77.pyo
/usr/lib/scons-2.3.5/SCons/Tool/f90.py
/usr/lib/scons-2.3.5/SCons/Tool/f90.pyc
/usr/lib/scons-2.3.5/SCons/Tool/f90.pyo
/usr/lib/scons-2.3.5/SCons/Tool/f95.py
/usr/lib/scons-2.3.5/SCons/Tool/f95.pyc
/usr/lib/scons-2.3.5/SCons/Tool/f95.pyo
/usr/lib/scons-2.3.5/SCons/Tool/filesystem.py
/usr/lib/scons-2.3.5/SCons/Tool/filesystem.pyc
/usr/lib/scons-2.3.5/SCons/Tool/filesystem.pyo
/usr/lib/scons-2.3.5/SCons/Tool/fortran.py
/usr/lib/scons-2.3.5/SCons/Tool/fortran.pyc
/usr/lib/scons-2.3.5/SCons/Tool/fortran.pyo
/usr/lib/scons-2.3.5/SCons/Tool/g++.py
/usr/lib/scons-2.3.5/SCons/Tool/g++.pyc
/usr/lib/scons-2.3.5/SCons/Tool/g++.pyo
/usr/lib/scons-2.3.5/SCons/Tool/g77.py
/usr/lib/scons-2.3.5/SCons/Tool/g77.pyc
/usr/lib/scons-2.3.5/SCons/Tool/g77.pyo
/usr/lib/scons-2.3.5/SCons/Tool/gas.py
/usr/lib/scons-2.3.5/SCons/Tool/gas.pyc
/usr/lib/scons-2.3.5/SCons/Tool/gas.pyo
/usr/lib/scons-2.3.5/SCons/Tool/gcc.py
/usr/lib/scons-2.3.5/SCons/Tool/gcc.pyc
/usr/lib/scons-2.3.5/SCons/Tool/gcc.pyo
/usr/lib/scons-2.3.5/SCons/Tool/gdc.py
/usr/lib/scons-2.3.5/SCons/Tool/gdc.pyc
/usr/lib/scons-2.3.5/SCons/Tool/gdc.pyo
/usr/lib/scons-2.3.5/SCons/Tool/gettext.py
/usr/lib/scons-2.3.5/SCons/Tool/gettext.pyc
/usr/lib/scons-2.3.5/SCons/Tool/gettext.pyo
/usr/lib/scons-2.3.5/SCons/Tool/gfortran.py
/usr/lib/scons-2.3.5/SCons/Tool/gfortran.pyc
/usr/lib/scons-2.3.5/SCons/Tool/gfortran.pyo
/usr/lib/scons-2.3.5/SCons/Tool/gnulink.py
/usr/lib/scons-2.3.5/SCons/Tool/gnulink.pyc
/usr/lib/scons-2.3.5/SCons/Tool/gnulink.pyo
/usr/lib/scons-2.3.5/SCons/Tool/gs.py
/usr/lib/scons-2.3.5/SCons/Tool/gs.pyc
/usr/lib/scons-2.3.5/SCons/Tool/gs.pyo
/usr/lib/scons-2.3.5/SCons/Tool/hpc++.py
/usr/lib/scons-2.3.5/SCons/Tool/hpc++.pyc
/usr/lib/scons-2.3.5/SCons/Tool/hpc++.pyo
/usr/lib/scons-2.3.5/SCons/Tool/hpcc.py
/usr/lib/scons-2.3.5/SCons/Tool/hpcc.pyc
/usr/lib/scons-2.3.5/SCons/Tool/hpcc.pyo
/usr/lib/scons-2.3.5/SCons/Tool/hplink.py
/usr/lib/scons-2.3.5/SCons/Tool/hplink.pyc
/usr/lib/scons-2.3.5/SCons/Tool/hplink.pyo
/usr/lib/scons-2.3.5/SCons/Tool/icc.py
/usr/lib/scons-2.3.5/SCons/Tool/icc.pyc
/usr/lib/scons-2.3.5/SCons/Tool/icc.pyo
/usr/lib/scons-2.3.5/SCons/Tool/icl.py
/usr/lib/scons-2.3.5/SCons/Tool/icl.pyc
/usr/lib/scons-2.3.5/SCons/Tool/icl.pyo
/usr/lib/scons-2.3.5/SCons/Tool/ifl.py
/usr/lib/scons-2.3.5/SCons/Tool/ifl.pyc
/usr/lib/scons-2.3.5/SCons/Tool/ifl.pyo
/usr/lib/scons-2.3.5/SCons/Tool/ifort.py
/usr/lib/scons-2.3.5/SCons/Tool/ifort.pyc
/usr/lib/scons-2.3.5/SCons/Tool/ifort.pyo
/usr/lib/scons-2.3.5/SCons/Tool/ilink.py
/usr/lib/scons-2.3.5/SCons/Tool/ilink.pyc
/usr/lib/scons-2.3.5/SCons/Tool/ilink.pyo
/usr/lib/scons-2.3.5/SCons/Tool/ilink32.py
/usr/lib/scons-2.3.5/SCons/Tool/ilink32.pyc
/usr/lib/scons-2.3.5/SCons/Tool/ilink32.pyo
/usr/lib/scons-2.3.5/SCons/Tool/install.py
/usr/lib/scons-2.3.5/SCons/Tool/install.pyc
/usr/lib/scons-2.3.5/SCons/Tool/install.pyo
/usr/lib/scons-2.3.5/SCons/Tool/intelc.py
/usr/lib/scons-2.3.5/SCons/Tool/intelc.pyc
/usr/lib/scons-2.3.5/SCons/Tool/intelc.pyo
/usr/lib/scons-2.3.5/SCons/Tool/ipkg.py
/usr/lib/scons-2.3.5/SCons/Tool/ipkg.pyc
/usr/lib/scons-2.3.5/SCons/Tool/ipkg.pyo
/usr/lib/scons-2.3.5/SCons/Tool/jar.py
/usr/lib/scons-2.3.5/SCons/Tool/jar.pyc
/usr/lib/scons-2.3.5/SCons/Tool/jar.pyo
/usr/lib/scons-2.3.5/SCons/Tool/javac.py
/usr/lib/scons-2.3.5/SCons/Tool/javac.pyc
/usr/lib/scons-2.3.5/SCons/Tool/javac.pyo
/usr/lib/scons-2.3.5/SCons/Tool/javah.py
/usr/lib/scons-2.3.5/SCons/Tool/javah.pyc
/usr/lib/scons-2.3.5/SCons/Tool/javah.pyo
/usr/lib/scons-2.3.5/SCons/Tool/latex.py
/usr/lib/scons-2.3.5/SCons/Tool/latex.pyc
/usr/lib/scons-2.3.5/SCons/Tool/latex.pyo
/usr/lib/scons-2.3.5/SCons/Tool/ldc.py
/usr/lib/scons-2.3.5/SCons/Tool/ldc.pyc
/usr/lib/scons-2.3.5/SCons/Tool/ldc.pyo
/usr/lib/scons-2.3.5/SCons/Tool/lex.py
/usr/lib/scons-2.3.5/SCons/Tool/lex.pyc
/usr/lib/scons-2.3.5/SCons/Tool/lex.pyo
/usr/lib/scons-2.3.5/SCons/Tool/link.py
/usr/lib/scons-2.3.5/SCons/Tool/link.pyc
/usr/lib/scons-2.3.5/SCons/Tool/link.pyo
/usr/lib/scons-2.3.5/SCons/Tool/linkloc.py
/usr/lib/scons-2.3.5/SCons/Tool/linkloc.pyc
/usr/lib/scons-2.3.5/SCons/Tool/linkloc.pyo
/usr/lib/scons-2.3.5/SCons/Tool/m4.py
/usr/lib/scons-2.3.5/SCons/Tool/m4.pyc
/usr/lib/scons-2.3.5/SCons/Tool/m4.pyo
/usr/lib/scons-2.3.5/SCons/Tool/masm.py
/usr/lib/scons-2.3.5/SCons/Tool/masm.pyc
/usr/lib/scons-2.3.5/SCons/Tool/masm.pyo
/usr/lib/scons-2.3.5/SCons/Tool/midl.py
/usr/lib/scons-2.3.5/SCons/Tool/midl.pyc
/usr/lib/scons-2.3.5/SCons/Tool/midl.pyo
/usr/lib/scons-2.3.5/SCons/Tool/mingw.py
/usr/lib/scons-2.3.5/SCons/Tool/mingw.pyc
/usr/lib/scons-2.3.5/SCons/Tool/mingw.pyo
/usr/lib/scons-2.3.5/SCons/Tool/msgfmt.py
/usr/lib/scons-2.3.5/SCons/Tool/msgfmt.pyc
/usr/lib/scons-2.3.5/SCons/Tool/msgfmt.pyo
/usr/lib/scons-2.3.5/SCons/Tool/msginit.py
/usr/lib/scons-2.3.5/SCons/Tool/msginit.pyc
/usr/lib/scons-2.3.5/SCons/Tool/msginit.pyo
/usr/lib/scons-2.3.5/SCons/Tool/msgmerge.py
/usr/lib/scons-2.3.5/SCons/Tool/msgmerge.pyc
/usr/lib/scons-2.3.5/SCons/Tool/msgmerge.pyo
/usr/lib/scons-2.3.5/SCons/Tool/mslib.py
/usr/lib/scons-2.3.5/SCons/Tool/mslib.pyc
/usr/lib/scons-2.3.5/SCons/Tool/mslib.pyo
/usr/lib/scons-2.3.5/SCons/Tool/mslink.py
/usr/lib/scons-2.3.5/SCons/Tool/mslink.pyc
/usr/lib/scons-2.3.5/SCons/Tool/mslink.pyo
/usr/lib/scons-2.3.5/SCons/Tool/mssdk.py
/usr/lib/scons-2.3.5/SCons/Tool/mssdk.pyc
/usr/lib/scons-2.3.5/SCons/Tool/mssdk.pyo
/usr/lib/scons-2.3.5/SCons/Tool/msvc.py
/usr/lib/scons-2.3.5/SCons/Tool/msvc.pyc
/usr/lib/scons-2.3.5/SCons/Tool/msvc.pyo
/usr/lib/scons-2.3.5/SCons/Tool/msvs.py
/usr/lib/scons-2.3.5/SCons/Tool/msvs.pyc
/usr/lib/scons-2.3.5/SCons/Tool/msvs.pyo
/usr/lib/scons-2.3.5/SCons/Tool/mwcc.py
/usr/lib/scons-2.3.5/SCons/Tool/mwcc.pyc
/usr/lib/scons-2.3.5/SCons/Tool/mwcc.pyo
/usr/lib/scons-2.3.5/SCons/Tool/mwld.py
/usr/lib/scons-2.3.5/SCons/Tool/mwld.pyc
/usr/lib/scons-2.3.5/SCons/Tool/mwld.pyo
/usr/lib/scons-2.3.5/SCons/Tool/nasm.py
/usr/lib/scons-2.3.5/SCons/Tool/nasm.pyc
/usr/lib/scons-2.3.5/SCons/Tool/nasm.pyo
/usr/lib/scons-2.3.5/SCons/Tool/packaging/__init__.py
/usr/lib/scons-2.3.5/SCons/Tool/packaging/__init__.pyc
/usr/lib/scons-2.3.5/SCons/Tool/packaging/__init__.pyo
/usr/lib/scons-2.3.5/SCons/Tool/packaging/ipk.py
/usr/lib/scons-2.3.5/SCons/Tool/packaging/ipk.pyc
/usr/lib/scons-2.3.5/SCons/Tool/packaging/ipk.pyo
/usr/lib/scons-2.3.5/SCons/Tool/packaging/msi.py
/usr/lib/scons-2.3.5/SCons/Tool/packaging/msi.pyc
/usr/lib/scons-2.3.5/SCons/Tool/packaging/msi.pyo
/usr/lib/scons-2.3.5/SCons/Tool/packaging/rpm.py
/usr/lib/scons-2.3.5/SCons/Tool/packaging/rpm.pyc
/usr/lib/scons-2.3.5/SCons/Tool/packaging/rpm.pyo
/usr/lib/scons-2.3.5/SCons/Tool/packaging/src_tarbz2.py
/usr/lib/scons-2.3.5/SCons/Tool/packaging/src_tarbz2.pyc
/usr/lib/scons-2.3.5/SCons/Tool/packaging/src_tarbz2.pyo
/usr/lib/scons-2.3.5/SCons/Tool/packaging/src_targz.py
/usr/lib/scons-2.3.5/SCons/Tool/packaging/src_targz.pyc
/usr/lib/scons-2.3.5/SCons/Tool/packaging/src_targz.pyo
/usr/lib/scons-2.3.5/SCons/Tool/packaging/src_zip.py
/usr/lib/scons-2.3.5/SCons/Tool/packaging/src_zip.pyc
/usr/lib/scons-2.3.5/SCons/Tool/packaging/src_zip.pyo
/usr/lib/scons-2.3.5/SCons/Tool/packaging/tarbz2.py
/usr/lib/scons-2.3.5/SCons/Tool/packaging/tarbz2.pyc
/usr/lib/scons-2.3.5/SCons/Tool/packaging/tarbz2.pyo
/usr/lib/scons-2.3.5/SCons/Tool/packaging/targz.py
/usr/lib/scons-2.3.5/SCons/Tool/packaging/targz.pyc
/usr/lib/scons-2.3.5/SCons/Tool/packaging/targz.pyo
/usr/lib/scons-2.3.5/SCons/Tool/packaging/zip.py
/usr/lib/scons-2.3.5/SCons/Tool/packaging/zip.pyc
/usr/lib/scons-2.3.5/SCons/Tool/packaging/zip.pyo
/usr/lib/scons-2.3.5/SCons/Tool/pdf.py
/usr/lib/scons-2.3.5/SCons/Tool/pdf.pyc
/usr/lib/scons-2.3.5/SCons/Tool/pdf.pyo
/usr/lib/scons-2.3.5/SCons/Tool/pdflatex.py
/usr/lib/scons-2.3.5/SCons/Tool/pdflatex.pyc
/usr/lib/scons-2.3.5/SCons/Tool/pdflatex.pyo
/usr/lib/scons-2.3.5/SCons/Tool/pdftex.py
/usr/lib/scons-2.3.5/SCons/Tool/pdftex.pyc
/usr/lib/scons-2.3.5/SCons/Tool/pdftex.pyo
/usr/lib/scons-2.3.5/SCons/Tool/qt.py
/usr/lib/scons-2.3.5/SCons/Tool/qt.pyc
/usr/lib/scons-2.3.5/SCons/Tool/qt.pyo
/usr/lib/scons-2.3.5/SCons/Tool/rmic.py
/usr/lib/scons-2.3.5/SCons/Tool/rmic.pyc
/usr/lib/scons-2.3.5/SCons/Tool/rmic.pyo
/usr/lib/scons-2.3.5/SCons/Tool/rpcgen.py
/usr/lib/scons-2.3.5/SCons/Tool/rpcgen.pyc
/usr/lib/scons-2.3.5/SCons/Tool/rpcgen.pyo
/usr/lib/scons-2.3.5/SCons/Tool/rpm.py
/usr/lib/scons-2.3.5/SCons/Tool/rpm.pyc
/usr/lib/scons-2.3.5/SCons/Tool/rpm.pyo
/usr/lib/scons-2.3.5/SCons/Tool/rpmutils.py
/usr/lib/scons-2.3.5/SCons/Tool/rpmutils.pyc
/usr/lib/scons-2.3.5/SCons/Tool/rpmutils.pyo
/usr/lib/scons-2.3.5/SCons/Tool/sgiar.py
/usr/lib/scons-2.3.5/SCons/Tool/sgiar.pyc
/usr/lib/scons-2.3.5/SCons/Tool/sgiar.pyo
/usr/lib/scons-2.3.5/SCons/Tool/sgic++.py
/usr/lib/scons-2.3.5/SCons/Tool/sgic++.pyc
/usr/lib/scons-2.3.5/SCons/Tool/sgic++.pyo
/usr/lib/scons-2.3.5/SCons/Tool/sgicc.py
/usr/lib/scons-2.3.5/SCons/Tool/sgicc.pyc
/usr/lib/scons-2.3.5/SCons/Tool/sgicc.pyo
/usr/lib/scons-2.3.5/SCons/Tool/sgilink.py
/usr/lib/scons-2.3.5/SCons/Tool/sgilink.pyc
/usr/lib/scons-2.3.5/SCons/Tool/sgilink.pyo
/usr/lib/scons-2.3.5/SCons/Tool/sunar.py
/usr/lib/scons-2.3.5/SCons/Tool/sunar.pyc
/usr/lib/scons-2.3.5/SCons/Tool/sunar.pyo
/usr/lib/scons-2.3.5/SCons/Tool/sunc++.py
/usr/lib/scons-2.3.5/SCons/Tool/sunc++.pyc
/usr/lib/scons-2.3.5/SCons/Tool/sunc++.pyo
/usr/lib/scons-2.3.5/SCons/Tool/suncc.py
/usr/lib/scons-2.3.5/SCons/Tool/suncc.pyc
/usr/lib/scons-2.3.5/SCons/Tool/suncc.pyo
/usr/lib/scons-2.3.5/SCons/Tool/sunf77.py
/usr/lib/scons-2.3.5/SCons/Tool/sunf77.pyc
/usr/lib/scons-2.3.5/SCons/Tool/sunf77.pyo
/usr/lib/scons-2.3.5/SCons/Tool/sunf90.py
/usr/lib/scons-2.3.5/SCons/Tool/sunf90.pyc
/usr/lib/scons-2.3.5/SCons/Tool/sunf90.pyo
/usr/lib/scons-2.3.5/SCons/Tool/sunf95.py
/usr/lib/scons-2.3.5/SCons/Tool/sunf95.pyc
/usr/lib/scons-2.3.5/SCons/Tool/sunf95.pyo
/usr/lib/scons-2.3.5/SCons/Tool/sunlink.py
/usr/lib/scons-2.3.5/SCons/Tool/sunlink.pyc
/usr/lib/scons-2.3.5/SCons/Tool/sunlink.pyo
/usr/lib/scons-2.3.5/SCons/Tool/swig.py
/usr/lib/scons-2.3.5/SCons/Tool/swig.pyc
/usr/lib/scons-2.3.5/SCons/Tool/swig.pyo
/usr/lib/scons-2.3.5/SCons/Tool/tar.py
/usr/lib/scons-2.3.5/SCons/Tool/tar.pyc
/usr/lib/scons-2.3.5/SCons/Tool/tar.pyo
/usr/lib/scons-2.3.5/SCons/Tool/tex.py
/usr/lib/scons-2.3.5/SCons/Tool/tex.pyc
/usr/lib/scons-2.3.5/SCons/Tool/tex.pyo
/usr/lib/scons-2.3.5/SCons/Tool/textfile.py
/usr/lib/scons-2.3.5/SCons/Tool/textfile.pyc
/usr/lib/scons-2.3.5/SCons/Tool/textfile.pyo
/usr/lib/scons-2.3.5/SCons/Tool/tlib.py
/usr/lib/scons-2.3.5/SCons/Tool/tlib.pyc
/usr/lib/scons-2.3.5/SCons/Tool/tlib.pyo
/usr/lib/scons-2.3.5/SCons/Tool/wix.py
/usr/lib/scons-2.3.5/SCons/Tool/wix.pyc
/usr/lib/scons-2.3.5/SCons/Tool/wix.pyo
/usr/lib/scons-2.3.5/SCons/Tool/xgettext.py
/usr/lib/scons-2.3.5/SCons/Tool/xgettext.pyc
/usr/lib/scons-2.3.5/SCons/Tool/xgettext.pyo
/usr/lib/scons-2.3.5/SCons/Tool/yacc.py
/usr/lib/scons-2.3.5/SCons/Tool/yacc.pyc
/usr/lib/scons-2.3.5/SCons/Tool/yacc.pyo
/usr/lib/scons-2.3.5/SCons/Tool/zip.py
/usr/lib/scons-2.3.5/SCons/Tool/zip.pyc
/usr/lib/scons-2.3.5/SCons/Tool/zip.pyo
/usr/lib/scons-2.3.5/SCons/Util.py
/usr/lib/scons-2.3.5/SCons/Util.pyc
/usr/lib/scons-2.3.5/SCons/Util.pyo
/usr/lib/scons-2.3.5/SCons/Variables/BoolVariable.py
/usr/lib/scons-2.3.5/SCons/Variables/BoolVariable.pyc
/usr/lib/scons-2.3.5/SCons/Variables/BoolVariable.pyo
/usr/lib/scons-2.3.5/SCons/Variables/EnumVariable.py
/usr/lib/scons-2.3.5/SCons/Variables/EnumVariable.pyc
/usr/lib/scons-2.3.5/SCons/Variables/EnumVariable.pyo
/usr/lib/scons-2.3.5/SCons/Variables/ListVariable.py
/usr/lib/scons-2.3.5/SCons/Variables/ListVariable.pyc
/usr/lib/scons-2.3.5/SCons/Variables/ListVariable.pyo
/usr/lib/scons-2.3.5/SCons/Variables/PackageVariable.py
/usr/lib/scons-2.3.5/SCons/Variables/PackageVariable.pyc
/usr/lib/scons-2.3.5/SCons/Variables/PackageVariable.pyo
/usr/lib/scons-2.3.5/SCons/Variables/PathVariable.py
/usr/lib/scons-2.3.5/SCons/Variables/PathVariable.pyc
/usr/lib/scons-2.3.5/SCons/Variables/PathVariable.pyo
/usr/lib/scons-2.3.5/SCons/Variables/__init__.py
/usr/lib/scons-2.3.5/SCons/Variables/__init__.pyc
/usr/lib/scons-2.3.5/SCons/Variables/__init__.pyo
/usr/lib/scons-2.3.5/SCons/Warnings.py
/usr/lib/scons-2.3.5/SCons/Warnings.pyc
/usr/lib/scons-2.3.5/SCons/Warnings.pyo
/usr/lib/scons-2.3.5/SCons/__init__.py
/usr/lib/scons-2.3.5/SCons/__init__.pyc
/usr/lib/scons-2.3.5/SCons/__init__.pyo
/usr/lib/scons-2.3.5/SCons/compat/__init__.py
/usr/lib/scons-2.3.5/SCons/compat/__init__.pyc
/usr/lib/scons-2.3.5/SCons/compat/__init__.pyo
/usr/lib/scons-2.3.5/SCons/compat/_scons_builtins.py
/usr/lib/scons-2.3.5/SCons/compat/_scons_builtins.pyc
/usr/lib/scons-2.3.5/SCons/compat/_scons_builtins.pyo
/usr/lib/scons-2.3.5/SCons/compat/_scons_collections.py
/usr/lib/scons-2.3.5/SCons/compat/_scons_collections.pyc
/usr/lib/scons-2.3.5/SCons/compat/_scons_collections.pyo
/usr/lib/scons-2.3.5/SCons/compat/_scons_dbm.py
/usr/lib/scons-2.3.5/SCons/compat/_scons_dbm.pyc
/usr/lib/scons-2.3.5/SCons/compat/_scons_dbm.pyo
/usr/lib/scons-2.3.5/SCons/compat/_scons_hashlib.py
/usr/lib/scons-2.3.5/SCons/compat/_scons_hashlib.pyc
/usr/lib/scons-2.3.5/SCons/compat/_scons_hashlib.pyo
/usr/lib/scons-2.3.5/SCons/compat/_scons_io.py
/usr/lib/scons-2.3.5/SCons/compat/_scons_io.pyc
/usr/lib/scons-2.3.5/SCons/compat/_scons_io.pyo
/usr/lib/scons-2.3.5/SCons/compat/_scons_sets.py
/usr/lib/scons-2.3.5/SCons/compat/_scons_sets.pyc
/usr/lib/scons-2.3.5/SCons/compat/_scons_sets.pyo
/usr/lib/scons-2.3.5/SCons/compat/_scons_subprocess.py
/usr/lib/scons-2.3.5/SCons/compat/_scons_subprocess.pyc
/usr/lib/scons-2.3.5/SCons/compat/_scons_subprocess.pyo
/usr/lib/scons-2.3.5/SCons/cpp.py
/usr/lib/scons-2.3.5/SCons/cpp.pyc
/usr/lib/scons-2.3.5/SCons/cpp.pyo
/usr/lib/scons-2.3.5/SCons/dblite.py
/usr/lib/scons-2.3.5/SCons/dblite.pyc
/usr/lib/scons-2.3.5/SCons/dblite.pyo
/usr/lib/scons-2.3.5/SCons/exitfuncs.py
/usr/lib/scons-2.3.5/SCons/exitfuncs.pyc
/usr/lib/scons-2.3.5/SCons/exitfuncs.pyo
/usr/lib/scons-2.3.5/scons-2.3.5-py2.7.egg-info
/usr/man/man1/scons-time.1
/usr/man/man1/scons.1
/usr/man/man1/sconsign.1

%files bin
%defattr(-,root,root,-)
/usr/bin/scons
/usr/bin/scons-2.3.5
/usr/bin/scons-time
/usr/bin/scons-time-2.3.5
/usr/bin/sconsign
/usr/bin/sconsign-2.3.5