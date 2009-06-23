#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	MooseX
%define	pnam	Daemonize
Summary:	MooseX::Daemonize - Role for daemonizing your Moose based application
Summary(pl.UTF-8):	MooseX::Daemonize - narzędzie do tworzenia demonów z aplikacji opartych o Moose
Name:		perl-MooseX-Daemonize
Version:	0.08
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/MooseX/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	24ff349f0e2e09ca89e8ecbc73b0dc65
URL:		http://search.cpan.org/dist/MooseX-Daemonize/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(MooseX::Getopt) >= 0.07
BuildRequires:	perl(MooseX::Types::Path::Class)
BuildRequires:	perl-Moose >= 0.33
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Often you want to write a persistant daemon that has a pid file, and
responds appropriately to Signals. This module provides a set of basic
roles as an infrastructure to do that.

%description -l pl.UTF-8
Często pojawia się potrzeba stworzenia trwałego demona, który posiada
plik pid i odpowiada właściwie na Sygnały. Moduł ten zapewnia zestaw
podstawowych mechanizmów by osiągnąć ten cel.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/MooseX/*.pm
%{perl_vendorlib}/MooseX/Daemonize
%{perl_vendorlib}/Test/MooseX/Daemonize.pm
%{_mandir}/man3/*
