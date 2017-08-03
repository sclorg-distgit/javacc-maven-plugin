%{?scl:%scl_package javacc-maven-plugin}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}javacc-maven-plugin
Version:        2.6
Release:        23.2%{?dist}
Summary:        JavaCC Maven Plugin
License:        ASL 2.0
URL:            http://mojo.codehaus.org/javacc-maven-plugin/ 
BuildArch:      noarch

#svn export http://svn.codehaus.org/mojo/tags/javacc-maven-plugin-2.6
#tar cjf javacc-maven-plugin-2.6.tar.bz2 javacc-maven-plugin-2.6
Source0:        javacc-maven-plugin-2.6.tar.bz2
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

Patch0:         javacc-maven-plugin-pom.patch

BuildRequires:  %{?scl_prefix}maven-local
BuildRequires:  %{?scl_prefix}mvn(junit:junit)
BuildRequires:  %{?scl_prefix}mvn(net.java.dev.javacc:javacc)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.doxia:doxia-sink-api)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.doxia:doxia-site-renderer)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-model)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-project)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.reporting:maven-reporting-api)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.reporting:maven-reporting-impl)
BuildRequires:  %{?scl_prefix}mvn(org.codehaus.mojo:mojo-parent:pom:)
BuildRequires:  %{?scl_prefix}mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.plugins:maven-plugin-plugin)

%description
Maven Plugin for processing JavaCC grammar files.

%package javadoc
Summary:        Javadoc for %{pkg_name}

%description javadoc
API documentation for %{pkg_name}.

%prep
%setup -n %{pkg_name}-%{version} -q 
%patch0 -b .sav
cp -p %{SOURCE1} .

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE-2.0.txt src/main/resources/NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE-2.0.txt src/main/resources/NOTICE

%changelog
* Thu Jun 22 2017 Michael Simacek <msimacek@redhat.com> - 2.6-23.2
- Mass rebuild 2017-06-22

* Wed Jun 21 2017 Java Maintainers <java-maint@redhat.com> - 2.6-23.1
- Automated package import and SCL-ization

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun 15 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6-22
- Add missing build-requires

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 25 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6-19
- Mavenize requires and build-requires

* Mon Jun  9 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6-18
- Update to current packaging guidelines

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 29 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6-16
- Use .mfiles generated during build

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

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
