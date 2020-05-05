#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
%bcond_with	tests_i18n	# tests with localization (requires some DateTime::Locale language resources)

%define		pdir	DateTime
%define		pnam	Format-Strptime
Summary:	DateTime::Format::Strptime - Parse and format strp and strf time patterns
Summary(pl.UTF-8):	DateTime::Format::Strptime - analiza i formatowanie wzorców czasu strp i strf
Name:		perl-DateTime-Format-Strptime
# fill version to 4 decimal digits to avoid epoch bumps after 1.5000 (drop in >= 2.x if possible)
%define	rver	1.77
Version:	%{rver}00
Release:	1
License:	Artistic v2.0
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/DateTime/DateTime-Format-Strptime-%{rver}.tar.gz
# Source0-md5:	891c38cdbe0a30291ed4afe711a17e3b
URL:		https://metacpan.org/release/DateTime-Format-Strptime
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.31
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-DateTime >= 1:1.00
BuildRequires:	perl-DateTime-Locale >= 1.23
BuildRequires:	perl-DateTime-TimeZone >= 2.09
BuildRequires:	perl-Params-ValidationCompiler
BuildRequires:	perl-Specio >= 0.33
BuildRequires:	perl-Test-Fatal
BuildRequires:	perl-Test-Simple >= 0.96
BuildRequires:	perl-Test-Warnings
BuildRequires:	perl-Try-Tiny
%endif
%if %{with tests_i18n} && "%(ls /usr/share/perl5/vendor_perl/auto/share/dist/DateTime-Locale/{de,en-AU,en-GB,en-US-POSIX,fr,fr-FR,ga,pt,zh}.pl >/dev/null 2>&1 ; echo $?)" != "0"
BuildRequires:	perl-DateTime-Locale(with_locales:de;en-AU;en-GB;en-US;fr;fr-FR;ga;pt;zh)
%endif
Requires:	perl-DateTime >= 1.00
Requires:	perl-DateTime-Locale >= 1.23
Requires:	perl-DateTime-TimeZone >= 2.09
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
%setup -q -n %{pdir}-%{pnam}-%{rver}

%if %{with tests} && %{without tests_i18n}
%{__sed} -i -e "/^\[\(Australian\|UK\|French\)/,/^\[/ d" t/basic.t
%{__sed} -i -e "/locale.*'pt'/ s/'pt'/'en-US'/" t/format-datetime.t
%{__rm} t/format-with-locale.t t/locale-{de,ga,pt,zh}.t
%endif

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
%doc Changes
%{perl_vendorlib}/DateTime/Format/Strptime.pm
%{perl_vendorlib}/DateTime/Format/Strptime
%{_mandir}/man3/DateTime::Format::Strptime.3pm*
%{_mandir}/man3/DateTime::Format::Strptime::Types.3pm*
