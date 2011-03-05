#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	DateTime
%define	pnam	Format-Strptime
Summary:	DateTime::Format::Strptime - Parse and format strp and strf time patterns
Summary(pl.UTF-8):	DateTime::Format::Strptime - analiza i formatowanie wzorców czasu strp i strf
Name:		perl-DateTime-Format-Strptime
Version:	1.5000
Release:	1
# same as perl
License:	Artistic 2.0
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/DateTime/DROLSKY/DateTime-Format-Strptime-%{version}.tar.gz
# Source0-md5:	ccd7e8fe4276c258e325e0bbce3f8e74
URL:		http://search.cpan.org/dist/DateTime-Format-Strptime/
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.31
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-DateTime >= 1:0.43_04
BuildRequires:	perl-DateTime-Locale >= 0.45
BuildRequires:	perl-DateTime-TimeZone >= 0.79
BuildRequires:	perl-Params-Validate >= 0.64
BuildRequires:	perl-Test-Simple >= 0.88
%endif
Requires:	perl-DateTime >= 0.28-2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements most of strptime(3), the POSIX function that is
the reverse of strftime(3), for DateTime. While strftime takes a
DateTime and a pattern and returns a string, strptime takes a string
and a pattern and returns the DateTime object associated.

%description -l pl.UTF-8
Ten moduł implementuje większość strptime(3) - funkcji POSIX będącej
odwrotną dla strftime(3), dla DateTime. O ile strftime przyjmuje
DateTime i wzorzec, a zwraca łańcuch, to strptime przyjmuje łańcuch i
wzorzec, a zwraca powiązany obiekt DateTime.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/DateTime/Format/Strptime.pm
%{_mandir}/man3/DateTime::Format::Strptime.3pm*
