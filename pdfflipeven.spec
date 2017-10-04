%define debug_package %{nil}

%define mybuildnumber %{?build_number}%{?!build_number:1}

Name:           pdfflipeven
Version:        0.0.1
Release:        %{mybuildnumber}%{?dist}
Summary:        Rotate (flip upside-down) even pages of a PDF
BuildArch:      noarch

License:        GPLv3+
URL:            https://github.com/Rudd-O/pdfflipeven
Source0:	https://github.com/Rudd-O/%{name}/archive/{%version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  sed
Requires: gawk
Requires: grep
Requires: poppler-utils
Requires: pdf-stapler
Requires: bash

%description
This program rotates the even pages of input PDF files and writes them to output PDF files.

%prep
%setup -q

%build
true

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT BINDIR=%{_bindir}

%files
%attr(0755, root, root) %{_bindir}/%{name}
%doc README.md

%changelog
* Wed Oct 04 2017 Manuel Amador (Rudd-O) <rudd-o@rudd-o.com>
- Initial release.
