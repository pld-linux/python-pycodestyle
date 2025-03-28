#
# Conditional build:
%bcond_without	doc	# API documentation
%bcond_without	tests	# unit tests

Summary:	Python style guide checker
Summary(pl.UTF-8):	Sprawdzanie zgodności z poradnikiem stylu kodowania w Pythonie
Name:		python-pycodestyle
# NOTE: before upgrading to >=2.8.0 check for python2-compatible flake8 release supporting new pycodestyle
Version:	2.7.0
Release:	6
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pycodestyle/
Source0:	https://files.pythonhosted.org/packages/source/p/pycodestyle/pycodestyle-%{version}.tar.gz
# Source0-md5:	b6d333b5ef185b73b54ec0e9292d7d9e
URL:		https://pycodestyle.readthedocs.io/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%{?with_doc:BuildRequires:	sphinx-pdg}
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pycodestyle is a tool to check your Python code against some of the
style conventions in PEP 8. This module was formerly called pep8.

%description -l pl.UTF-8
pycodestyle to narzędzie do sprawdzania kodu w Pythonie względem
niektórych konwencji stylistycznych opisanych w PEP 8. Ten moduł
wcześniej nazywał się pep8.

%package apidocs
Summary:	API documentation for pycodestyle module
Summary(pl.UTF-8):	Dokumentacja API modułu pycodestyle
Group:		Documentation

%description apidocs
API documentation for pycodestyle module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu pycodestyle.

%prep
%setup -q -n pycodestyle-%{version}

%build
%py_build

%if %{with tests}
%{__python} -m testsuite.test_all
%endif

%if %{with doc}
%{__make} -C docs html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%{__mv} $RPM_BUILD_ROOT%{_bindir}/pycodestyle{,-2}

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.txt LICENSE README.rst
%attr(755,root,root) %{_bindir}/pycodestyle-2
%{py_sitescriptdir}/pycodestyle.py[co]
%{py_sitescriptdir}/pycodestyle-%{version}-py*.egg-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_modules,_static,*.html,*.js}
%endif
