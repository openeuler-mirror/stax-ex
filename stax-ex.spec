Name:                stax-ex
Version:             1.7.7
Release:             12
Summary:             StAX API extensions
License:             CDDL or GPLv2
Url:                 https://stax-ex.dev.java.net
Source0:             https://github.com/javaee/metro-stax-ex/archive/stax-ex-%{version}.tar.gz
BuildRequires:       dos2unix maven-local mvn(javax.xml.stream:stax-api) mvn(junit:junit)
BuildRequires:       mvn(net.java:jvnet-parent:pom:) mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:       mvn(org.apache.maven.plugins:maven-enforcer-plugin) 
BuildArch:           noarch

%description
The package provides a few extensions API for cpmplement JSR-173,as following area
In het high-performance enviroment like JAX-WS and JAXB, enbale parse instance reuse.
Improve the behavier of reading form not-text infoset, such as FastInfoset.
Improve for namespace support.

%package help
Summary:             Javadoc for stax-ex
Provides:            stax-ex-javadoc = %{version}-%{release}
Obsoletes:           stax-ex-javadoc < %{version}-%{release}

%description help
The package provides javadoc for stax-ex.

%prep
%autosetup -n metro-stax-ex-stax-ex-%{version} -p1
%pom_remove_dep javax.activation:activation
%pom_remove_plugin org.codehaus.mojo:buildnumber-maven-plugin
%pom_remove_plugin org.codehaus.mojo:findbugs-maven-plugin
%pom_remove_plugin org.glassfish.copyright:glassfish-copyright-maven-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-deploy-plugin
mv LICENSE.txt LICENSE.txt.tmp
iconv -f ISO-8859-1 -t UTF-8 LICENSE.txt.tmp > LICENSE.txt
dos2unix LICENSE.txt
%mvn_file :stax-ex stax-ex

%build
%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt

%files help -f .mfiles-javadoc
%license LICENSE.txt

%changelog
* Fri Jul 30 2021 chenyanpanHW <chenyanpan@huawei.com> - 1.7.7-12
- DESC: delete -S git from %autosetup, and delete BuildRequires git

* Mon May 31 2021 huanghaitao <huanghaitao8@huawei.com> - 1.7.7-11
- Completing build dependencies to fix git commands missing error

* Thu Apr 30 2020 Jeffery.Gao <gaojianxing@huawei.com> - 1.7.7-10
- Package init
