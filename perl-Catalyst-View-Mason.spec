%define realname Catalyst-View-Mason
%define name	 perl-%{realname}
%define version	 0.08
%define release	 %mkrel 2

Summary:	Mason View Class
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{realname}/
Source:		http://search.cpan.org/CPAN/authors/id/A/AN/ANK/Catalyst/%{realname}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%else
BuildRequires:	perl
%endif
BuildRequires:	perl-Catalyst >= 5
BuildRequires:	perl(HTML::Mason)
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-root

%description
Want to use a Mason component in your views? No problem!
Catalyst::View::Mason comes to the rescue.

%prep
%setup -q -n %{realname}-%{version}

%build
%__perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
%{__rm} -rf %{buildroot}
./Build install destdir=%buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Catalyst/View/*
%{perl_vendorlib}/Catalyst/Helper/View/*
%{_mandir}/*/*

%clean
rm -rf $RPM_BUILD_ROOT

