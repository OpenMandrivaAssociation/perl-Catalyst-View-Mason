%define module Catalyst-View-Mason
%define name	 perl-%{module}
%define version	 0.16
%define release	 %mkrel 2

Summary:	Mason View Class
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}/
Source:     http://www.cpan.org/modules/by-module/Catalyst/%{module}-%{version}.tar.gz
BuildRequires:	perl-Catalyst >= 5
BuildRequires:	perl(HTML::Mason)
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}

%description
Want to use a Mason component in your views? No problem!
Catalyst::View::Mason comes to the rescue.

%prep
%setup -q -n %{module}-%{version}

%build
%__perl Makefile.PL installdirs=vendor --skipdeps
%make

%check
make test

%install
%{__rm} -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Catalyst
%{_mandir}/*/*

