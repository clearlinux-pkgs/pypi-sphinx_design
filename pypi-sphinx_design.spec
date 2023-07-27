#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-sphinx_design
Version  : 0.5.0
Release  : 18
URL      : https://files.pythonhosted.org/packages/fd/d0/62a7cee178d30f7217c4badea17eeca020801c0053773098d9ff65636a60/sphinx_design-0.5.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/fd/d0/62a7cee178d30f7217c4badea17eeca020801c0053773098d9ff65636a60/sphinx_design-0.5.0.tar.gz
Summary  : A sphinx extension for designing beautiful, view size responsive web components.
Group    : Development/Tools
License  : Apache-2.0 MIT
Requires: pypi-sphinx_design-license = %{version}-%{release}
Requires: pypi-sphinx_design-python = %{version}-%{release}
Requires: pypi-sphinx_design-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(flit_core)
BuildRequires : pypi(py)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# sphinx-design
[![Github-CI][github-ci]][github-link]
[![Coverage Status][codecov-badge]][codecov-link]
[![PyPI][pypi-badge]][pypi-link]

%package license
Summary: license components for the pypi-sphinx_design package.
Group: Default

%description license
license components for the pypi-sphinx_design package.


%package python
Summary: python components for the pypi-sphinx_design package.
Group: Default
Requires: pypi-sphinx_design-python3 = %{version}-%{release}

%description python
python components for the pypi-sphinx_design package.


%package python3
Summary: python3 components for the pypi-sphinx_design package.
Group: Default
Requires: python3-core
Provides: pypi(sphinx_design)
Requires: pypi(sphinx)

%description python3
python3 components for the pypi-sphinx_design package.


%prep
%setup -q -n sphinx_design-0.5.0
cd %{_builddir}/sphinx_design-0.5.0
pushd ..
cp -a sphinx_design-0.5.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1690471977
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . sphinx
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pypi-dep-fix.py . sphinx
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-sphinx_design
cp %{_builddir}/sphinx_design-%{version}/sphinx_design/compiled/material-icons_LICENSE %{buildroot}/usr/share/package-licenses/pypi-sphinx_design/dfda1f5b7ba837492d7fbf2b731edc313edd0c5e || :
cp %{_builddir}/sphinx_design-%{version}/sphinx_design/compiled/octicon_LICENSE %{buildroot}/usr/share/package-licenses/pypi-sphinx_design/5c0e418ff5750461e481972fdc40ecb88ce84b26 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
pypi-dep-fix.py %{buildroot} sphinx
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-sphinx_design/5c0e418ff5750461e481972fdc40ecb88ce84b26
/usr/share/package-licenses/pypi-sphinx_design/dfda1f5b7ba837492d7fbf2b731edc313edd0c5e

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
