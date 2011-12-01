%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%define     alphaver    a4

Name:           python-repoze-tm2
Version:        1.0
Release:        0.5.%{alphaver}%{?dist}
Summary:        Zope-like transaction manager via WSGI middleware

Group:          Development/Languages
License:        BSD
URL:            http://pypi.python.org/pypi/repoze.tm2
Source0:        http://pypi.python.org/packages/source/r/repoze.tm2/repoze.tm2-%{version}%{alphaver}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  python-devel python-setuptools-devel
Requires:       python-transaction

%description
The ZODB transaction manager is a completely generic transaction manager.  It
can be used independently of the actual "object database" part of ZODB.  One
of the purposes of creating repoze.tm was to allow for systems other than
Zope to make use of two-phase commit transactions in a WSGI context.


%prep
%setup -q -n repoze.tm2-%{version}%{alphaver}


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README.txt COPYRIGHT.txt LICENSE.txt
%{python_sitelib}/*



%changelog
* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.5.a4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 01 2009 Luke Macken <lmacken@redhat.com> - 1.0-0.4.a4
- Update to 1.0a4

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.3.a3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.0-0.2.a3
- Rebuild for Python 2.6

* Tue Oct 21 2008 Luke Macken <lmacken@redhat.com> - 1.0-0.1.a2
- Initial package
