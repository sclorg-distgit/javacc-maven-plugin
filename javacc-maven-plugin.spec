%global pkg_name javacc-maven-plugin
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

Name:           %{?scl_prefix}%{pkg_name}
Version:        2.6
Release:        17.11%{?dist}
Summary:        JavaCC Maven Plugin

License:        ASL 2.0
URL:            http://mojo.codehaus.org/javacc-maven-plugin/
#svn export http://svn.codehaus.org/mojo/tags/javacc-maven-plugin-2.6
#tar cjf javacc-maven-plugin-2.6.tar.bz2 javacc-maven-plugin-2.6
Source0:        javacc-maven-plugin-2.6.tar.bz2
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

BuildArch: noarch

BuildRequires: %{?scl_prefix}maven-local
BuildRequires: %{?scl_prefix}javacc >= 5.0
BuildRequires: %{?scl_prefix}plexus-utils
BuildRequires: %{?scl_prefix}maven-doxia-sink-api
BuildRequires: %{?scl_prefix}maven-doxia-sitetools
BuildRequires: %{?scl_prefix}maven-invoker-plugin
BuildRequires: %{?scl_prefix}maven-enforcer-plugin
BuildRequires: %{?scl_prefix}maven-plugin-plugin
BuildRequires: %{?scl_prefix}maven-resources-plugin
BuildRequires: %{?scl_prefix}mojo-parent
BuildRequires: %{?scl_prefix}plexus-containers-component-javadoc
BuildRequires: %{?scl_prefix_java_common}junit

%description
Maven Plugin for processing JavaCC grammar files.

%package javadoc
Summary:        Javadoc for %{pkg_name}

%description javadoc
API documentation for %{pkg_name}.

%prep
%setup -q -n %{pkg_name}-%{version}
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x

%pom_remove_dep edu.ucla.cs.compilers:jtb
%pom_xpath_remove pom:profiles

cp -p %{SOURCE1} .
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%dir %{_mavenpomdir}/%{pkg_name}
%dir %{_javadir}/%{pkg_name}
%doc LICENSE-2.0.txt src/main/resources/NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE-2.0.txt src/main/resources/NOTICE

%changelog
* Mon Feb 08 2016 Michal Srb <msrb@redhat.com> - 2.6-17.11
- Fix BR on maven-local & co.

* Mon Jan 11 2016 Michal Srb <msrb@redhat.com> - 2.6-17.10
- maven33 rebuild #2

* Sat Jan 09 2016 Michal Srb <msrb@redhat.com> - 2.6-17.9
- maven33 rebuild

* Thu Jan 15 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6-17.8
- Add directory ownership on %%{_mavenpomdir} subdir

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 2.6-17.7
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 2.6-17.6
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6-17.5
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6-17.4
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6-17.3
- Mass rebuild 2014-02-18

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6-17.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6-17.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 2.6-17
- Mass rebuild 2013-12-27

* Fri Aug 16 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.6-16
- Migrate away from mvn-rpmbuild (#996663)

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6-15
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Fri Feb 08 2013 Michal Srb <msrb@redhat.com> - 2.6-14
- Migrate from maven-doxia to doxia subpackages (Resolves: #909835)

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2.6-13
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Mon Nov 26 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6-12
- Copy LICENSE-2.0.txt to builddir

* Fri Nov 23 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6-11
- Install license files
- Resolves: rhbz#880189

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 24 2011 Alexander Kurtakov <akurtako@redhat.com> 2.6-8
- Build with maven 3.
- Adapt to current guidelines.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 6 2010 Orion Poplawski <orion@cora.nwra.com> 2.6-6
- Require mojo-parent.

* Thu Sep 16 2010 Alexander Kurtakov <akurtako@redhat.com> 2.6-5
- BR mojo-parent.

* Wed Mar 24 2010 Alexander Kurtakov <akurtako@redhat.com> 2.6-4
- Fix BRs.

* Wed Mar 24 2010 Alexander Kurtakov <akurtako@redhat.com> 2.6-3
- Fix plugin metadata build.

* Wed Mar 17 2010 Alexander Kurtakov <akurtako@redhat.com> 2.6-2
- Fix Requires.

* Mon Mar 15 2010 Alexander Kurtakov <akurtako@redhat.com> 2.6-1
- Initial package.
