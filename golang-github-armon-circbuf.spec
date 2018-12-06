# https://github.com/armon/circbuf
%global goipath         github.com/armon/circbuf
%global commit          bbbad097214e2918d8543d5201d12bfd7bca254d

%gometa

Name:           %{goname}
Version:        0
Release:        0.17%{?dist}
Summary:        Golang circular (ring) buffer
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.lock
Source2:        glide.yaml

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%forgesetup
cp %{SOURCE1} %{SOURCE2} .

%install
%goinstall glide.lock glide.yaml
chmod -x LICENSE

%check
%gochecks

%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Mon Nov 12 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.17.20180608gitbbbad09
- SPEC refresh

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.16.git.gitbbbad09
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.15.git.gitbbbad09
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 08 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.14.git.gitbbbad09
- Update to spec 3.0
  Upload glide.lock and glide.yaml

* Mon Feb 26 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.13.20150827gitbbbad09
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.gitbbbad09
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.gitbbbad09
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.gitbbbad09
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.gitbbbad09
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.8.gitbbbad09
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.gitbbbad09
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.gitbbbad09
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 12 2016 jchaloup <jchaloup@redhat.com> - 0-0.5.gitbbbad09
- Built with devel subpackage
  related: #1248497

* Wed Jan 06 2016 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.4.gitbbbad09
- Bump to upstream bbbad097214e2918d8543d5201d12bfd7bca254d
  related: #1248497

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 0-0.3.gitf092b4f
- Update to spec-2.1
  related: #1248497

* Thu Jul 30 2015 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.2.gitf092b4f
- Update of spec file to spec-2.0
  resolves: #1248497

* Wed Apr 15 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.gitf092b4f
- First package for Fedora
  resolves: #1211985
