
%global srcname voluptuous

%if 0%{?fedora}
%global with_python3 1
%endif

Name: python-%{srcname}
Version: 0.10.5
Release: 2%{?dist}
Summary: A Python data validation library
License: BSD
Group: Development/Languages
URL: http://github.com/alecthomas/voluptuous
Source0: https://pypi.io/packages/source/v/voluptuous/%{srcname}-%{version}.tar.gz

BuildArch: noarch
BuildRequires: python2-devel
%if 0%{?with_python3}
BuildRequires:  python3-devel
%endif # if with_python3

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

%if 0%{?with_python3}
%package -n python3-%{srcname}
Summary: A Python data validation library
BuildRequires:  python3-devel python3-setuptools
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Voluptuous, despite the name, is a Python data validation library. It is 
primarily intended for validating data coming into Python as JSON, YAML, etc.
%endif # with_python3

%prep
%autosetup -n %{srcname}-%{version}

%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif # with_python3

%install
%py2_install
%if 0%{?with_python3}
%py3_install
%endif # with_python3

%files -n python2-%{srcname}
%doc README.md
%license COPYING
%{python2_sitelib}/*

%if 0%{?with_python3}
%files -n python3-%{srcname}
%doc README.md
%license COPYING
%{python3_sitelib}/*
%endif # with_python3

%changelog
* Mon Jan 15 2018 Alfredo Moralejo <amoralej@redhat.com> - 0.10.5
- Added conditional to disable python3 builds in CentOS imports.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Sergio Pascual <sergiopr@fedoraproject.org> - 0.10.5-1
- New upstream source (0.10.5.1)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.9.3-3
- Rebuild for Python 3.6

* Sun Oct 02 2016 Sergio Pascual <sergiopr@fedoraproject.org> - 0.9.3-2
- New upstream source (0.9.3)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.11-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jul 13 2016 Sergio Pascual <sergiopr@fedoraproject.org> - 0.8.11-1
- New upstream source (0.8.11)

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

