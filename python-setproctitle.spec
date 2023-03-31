%define module	setproctitle
%global debug_package %{nil}

Name:		python-%{module}
Version:	1.3.2
Release:	2
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

%prep
%autosetup -n %{module}-%{version} -p1


%build
python3 setup.py build

%install

python3 setup.py install --root=%buildroot

%files
%doc HISTORY.rst README.rst
%{python_sitearch}/%{module}-%{version}-py%{python_version}.egg-info
%{python_sitearch}/setproctitle/
