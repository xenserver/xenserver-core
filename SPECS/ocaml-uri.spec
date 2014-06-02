%global debug_package %{nil}

Name:           ocaml-uri
Version:        1.3.8
Release:        2%{?dist}
Summary:        A URI library for OCaml
License:        ISC
URL:            https://github.com/mirage/ocaml-uri
Source0:        https://github.com/mirage/%{name}/archive/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml >= 4.00
BuildRequires:  ocaml-compiler-libs
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-ounit-devel
BuildRequires:  ocaml-re-devel

%description
A URI library for OCaml.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-re-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

%build
ocaml setup.ml -configure --destdir %{buildroot}/%{_libdir}/ocaml
make

%install
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
make install

%files
%doc CHANGES
%doc README.md 
%{_libdir}/ocaml/uri
%exclude %{_libdir}/ocaml/uri/*.a
%exclude %{_libdir}/ocaml/uri/*.cmxa
%exclude %{_libdir}/ocaml/uri/*.cmx
%exclude %{_libdir}/ocaml/uri/*.mli

%files devel
%doc uri.docdir/*
%exclude %{_libdir}/ocaml/usr/local/share/doc/uri/
%exclude /usr/share/doc/%{name}-%{version}/
%{_libdir}/ocaml/uri/*.a
%{_libdir}/ocaml/uri/*.cmx
%{_libdir}/ocaml/uri/*.cmxa
%{_libdir}/ocaml/uri/*.mli

%changelog
* Mon Jun 02 2014 David Scott <dave.scott@eu.citrix.com> - 1.3.8-2
- Split files correctly between base and devel packages

* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com> - 1.3.8-1
- Initial package

