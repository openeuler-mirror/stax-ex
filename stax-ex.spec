Name:                stax-ex
Version:             1.8
Release:             2
Summary:             StAX API extensions
License:             CDDL-1.1 or GPLv2
Url:                 https://stax-ex.dev.java.net
Source0:             https://github.com/javaee/metro-stax-ex/archive/%{version}.tar.gz
Source1:             xmvn-reactor
Patch0:              0001-fix-maven-compiler-plugin-release-flag.patch
BuildRequires:       maven java-1.8.0-openjdk-devel dos2unix maven-local
Requires:            javapackages-tools java-1.8.0-openjdk
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
%autosetup -n metro-stax-ex-%{version} -p1
find . -name '*.jar' -print -delete
find . -name '*.class' -print -delete
pushd %{name}
cp %{SOURCE1} ./.xmvn-reactor
echo `pwd` > absolute_prefix.log
sed -i 's/\//\\\//g' absolute_prefix.log
absolute_prefix=`head -n 1 absolute_prefix.log`
sed -i 's/absolute-prefix/'"$absolute_prefix"'/g' .xmvn-reactor
rm -rf src/java/module-info.java
mv LICENSE.txt LICENSE.txt.tmp
iconv -f ISO-8859-1 -t UTF-8 LICENSE.txt.tmp > LICENSE.txt
dos2unix LICENSE.txt
%mvn_file :stax-ex stax-ex
popd

%build
pushd %{name}
mvn -Dproject.build.sourceEncoding=UTF-8 -DskipTests -DskipIT package
popd

%install
pushd %{name}
%mvn_install
popd
install -d -m 0755 %{buildroot}/%{_javadocdir}/%{name}
install -m 0755 %{name}/target/stax-ex-1.8-javadoc.jar %{buildroot}/%{_javadocdir}/%{name}

%files -f %{name}/.mfiles
%license LICENSE

%files help 
%license LICENSE
%{_javadocdir}/%{name}

%changelog
* Tue Jul 5 2022 Chenyx <chenyixiong3@huawei.com> - 1.8-2
- License compliance rectification

* Tue Apr 19 2022 wangkai <wangkai385@h-partners.com> - 1.8-1
- Update to version 1.8

* Fri Jul 30 2021 chenyanpanHW <chenyanpan@huawei.com> - 1.7.7-12
- DESC: delete -S git from %autosetup, and delete BuildRequires git

* Mon May 31 2021 huanghaitao <huanghaitao8@huawei.com> - 1.7.7-11
- Completing build dependencies to fix git commands missing error

* Thu Apr 30 2020 Jeffery.Gao <gaojianxing@huawei.com> - 1.7.7-10
- Package init
