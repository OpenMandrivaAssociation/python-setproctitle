%define module	setproctitle
%global debug_package %{nil}

Name:		python-%{module}
Version:	1.1.10
Release:	3
Summary:	A library allowing a process to change its title
License:	BSD
Group:		System/Libraries
Url:		https://github.com/dvarrazzo/py-setproctitle/
Source0:	https://pypi.io/packages/source/s/%{module}/%{module}-%{version}.tar.gz

BuildRequires:	pkgconfig(python)
BuildRequires:	python-setuptools

%description
The library allows a process to change its title (as displayed by system tools
such as ps and top).
Changing the title is mostly useful in multi-process systems, for example when
a master process is forked: changing the children's title allows to identify
the task each process is busy with.

%package -n	python2-%{module}
Summary:	A library allowing a process to change its title
Group:		Development/Python

BuildRequires:	pkgconfig(python2)
BuildRequires:	python2-setuptools

%description -n	python2-%{module}
The library allows a process to change its title (as displayed by system tools
such as ps and top).
Changing the title is mostly useful in multi-process systems, for example when
a master process is forked: changing the children's title allows to identify
the task each process is busy with.

This is the Python 2 version of the package.

%prep
%setup -q -n %{module}-%{version}

cp -a . %{py2dir}

%build
python3 setup.py build

pushd %{py2dir}
python2 setup.py build
popd

%install
pushd %{py2dir}
python2 setup.py install --root=%buildroot
popd

python3 setup.py install --root=%buildroot

%files
%doc HISTORY.rst README.rst
%{python_sitearch}/%{module}.cpython-*.so
%{python_sitearch}/%{module}-%{version}-py%{python_version}.egg-info

%files -n python2-%{module}
%doc HISTORY.rst README.rst
%{python2_sitearch}/%{module}.so
%{python2_sitearch}/%{module}-%{version}-py%{python2_version}.egg-info

