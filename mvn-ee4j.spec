#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-ee4j
Version  : 1.0.4
Release  : 1
URL      : https://github.com/eclipse-ee4j/ee4j/archive/1.0.4.tar.gz
Source0  : https://github.com/eclipse-ee4j/ee4j/archive/1.0.4.tar.gz
Source1  : https://repo1.maven.org/maven2/org/eclipse/ee4j/project/1.0.4/project-1.0.4.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : EPL-2.0 GPL-2.0
Requires: mvn-ee4j-data = %{version}-%{release}
BuildRequires : apache-maven
BuildRequires : buildreq-mvn

%description
# Eclipse Enterprise for Java (EE4J)
Eclipse Enterprise for Java (EE4J) is an open source initiative to create standard APIs, implementations of those APIs, and technology compatibility kits for Java runtimes that enable development, deployment, and management of server-side and cloud-native applications.  EE4J is based on the Java™ Platform, Enterprise Edition (Java EE) standards, and uses Java EE 8 as the baseline for creating new standards.

%package data
Summary: data components for the mvn-ee4j package.
Group: Data

%description data
data components for the mvn-ee4j package.


%prep
%setup -q -n ee4j-1.0.4

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/eclipse/ee4j/project/1.0.4
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/eclipse/ee4j/project/1.0.4/project-1.0.4.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/eclipse/ee4j/project/1.0.4/project-1.0.4.pom
