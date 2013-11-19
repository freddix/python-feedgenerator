Summary:	Standalone version of django.utils.feedgenerator
Name:		python-feedgenerator
Version:	1.7
Release:	1
License:	BSD
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/f/feedgenerator/feedgenerator-%{version}.tar.gz
# Source0-md5:	92978492871342ad64e8ae0ccfcf200c
URL:		https://pypi.python.org/pypi/feedgenerator
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Standalone version of django.utils.feedgenerator.

%prep
%setup -qn feedgenerator-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/feedgenerator
%{py_sitescriptdir}/*.egg-info

