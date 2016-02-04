
%global srcname voluptuous

Name: python-%{srcname}
Version: 0.8.8
Release: 2%{?dist}
Summary: A Python data validation library
License: BSD
Group: Development/Languages
URL: http://github.com/alecthomas/voluptuous
Source0: http://pypi.python.org/packages/source/v/voluptuous/%{srcname}-%{version}.tar.gz

BuildArch: noarch
BuildRequires: python2-devel python3-devel

%description
Voluptuous, despite the name, is a Python data validation library. It is 
primarily intended for validating data coming into Python as JSON, YAML, etc.


%package -n python2-%{srcname}
Summary: A Python data validation library
BuildRequires:  python2-devel python-setuptools
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
Voluptuous, despite the name, is a Python data validation library. It is 
primarily intended for validating data coming into Python as JSON, YAML, etc.

%package -n python3-%{srcname}
Summary: A Python data validation library
BuildRequires:  python3-devel python3-setuptools
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Voluptuous, despite the name, is a Python data validation library. It is 
primarily intended for validating data coming into Python as JSON, YAML, etc.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%files -n python2-%{srcname}
%doc README.md
%license COPYING
%{python2_sitelib}/*

%files -n python3-%{srcname}
%doc README.md
%license COPYING
%{python3_sitelib}/*

%changelog
* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 21 2015 Sergio Pascual <sergiopr@fedoraproject.org> - 0.8.8-1
- New upstream source
- Use new python macros
- Enable python3, fixes bz #1292616

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jul 22 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.8.5-2
- Use tarball from github
- Add COPYING to doc

* Mon Mar 17 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.8.5-1
- Initial spec file

