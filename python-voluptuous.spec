
%global upname voluptuous

Name: python-%{upname}
Version: 0.8.5
Release: 2%{?dist}
Summary: A Python data validation library
License: BSD
Group: Development/Languages
URL: http://github.com/alecthomas/voluptuous
# The tarball from pypi has missing files (COPYING)
# Use the tarball from github instead
#Source0: http://pypi.python.org/packages/source/v/voluptuous/%{upname}-%{version}.tar.gz
Source0: http://github.com/alecthomas/voluptuous/archive/%{version}.tar.gz#/%{upname}-%{version}.tar.gz
BuildRequires: python2-devel python-setuptools

BuildArch: noarch
%if 0%{?with_python3}
BuildRequires:  python3-devel python3-setuptools
%endif # if with_python3

%description
Voluptuous, despite the name, is a Python data validation library. It is 
primarily intended for validating data coming into Python as JSON, YAML, etc.

%if 0%{?with_python3}
%package -n python3-%{upname}
Summary: A Python data validation library

%description -n python3-%{upname}
Voluptuous, despite the name, is a Python data validation library. It is 
primarily intended for validating data coming into Python as JSON, YAML, etc.

%endif # with_python3

%prep
%setup -q -n %{upname}-%{version}
rm -rf %{upname}.egg-info

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
find %{py3dir} -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'
%endif # with_python3

find -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python2}|'

%build
%{__python2} setup.py build

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif # with_python3

%install

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install -O1 --skip-build --root  %{buildroot}
popd
%endif # with_python3

%{__python2} setup.py install -O1 --skip-build --root  %{buildroot}

%files
%doc README.md COPYING
%{python2_sitelib}/*

%if 0%{?with_python3}
%files -n python3-%{upname}
%doc README.md COPYING
%{python3_sitelib}/*
%endif # with_python3

%changelog
* Tue Jul 22 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.8.5-2
- Use tarball from github
- Add COPYING to doc

* Mon Mar 17 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.8.5-1
- Initial spec file

