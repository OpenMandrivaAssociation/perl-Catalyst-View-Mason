%define upstream_name    Catalyst-View-Mason
%define upstream_version 0.18

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Mason View Class
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Catalyst)
BuildRequires:	perl(HTML::Mason)
BuildRequires:	perl(MRO::Compat)
BuildArch:	noarch

%description
Want to use a Mason component in your views? No problem!
Catalyst::View::Mason comes to the rescue.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL installdirs=vendor --skipdeps
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Catalyst
%{_mandir}/*/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.180.0-2mdv2011.0
+ Revision: 680769
- mass rebuild

* Mon Aug 24 2009 Jérôme Quelin <jquelin@mandriva.org> 0.180.0-1mdv2010.0
+ Revision: 420277
- update to 0.18

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.170.0-1mdv2010.0
+ Revision: 406311
- rebuild using %%perl_convert_version

* Mon May 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.17-1mdv2010.0
+ Revision: 371663
- update to new version 0.17

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.16-2mdv2009.0
+ Revision: 268397
- rebuild early 2009.0 package (before pixel changes)

* Thu May 29 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.16-1mdv2009.0
+ Revision: 212924
- update to new version 0.16

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Nov 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.15-1mdv2008.1
+ Revision: 104517
- update to new version 0.15

* Sun Sep 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.13-1mdv2008.0
+ Revision: 78126
- new version


* Fri Mar 24 2006 Scott Karns <scott@karnstech.com> 0.08-2mdk
- Cleaned SPEC file

* Thu Dec 29 2005 Scott Karns <scott@karnstech.com> 0.08-1mdk
- Initial Mdv RPM

