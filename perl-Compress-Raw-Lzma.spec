%define	upstream_name		Compress-Raw-Lzma
%define upstream_version 2.064

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Low-Level Interface to the liblzma compression library
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/P/PM/PMQS/Compress-Raw-Lzma-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	pkgconfig(liblzma)

%description
Low-Level Interface to the liblzma compression library.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes
%{_mandir}/*/*
%{perl_vendorarch}/Compress
%{perl_vendorarch}/auto/Compress



%changelog
* Tue Mar 13 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.49.0-1
+ Revision: 784856
- imported package perl-Compress-Raw-Lzma


* Mon Mar 13 2012 Per Øyvind Karlsen <pkarlsen@mandriva.com> 2.49.0-1
- initial release




