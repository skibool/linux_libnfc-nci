Name:		  libnfc-nci
Version:          R2.1 
Release: 	  1
Group:            System Environment/Libraries
License:          LGPLv3+
Summary:          Linux NFC stack for NCI based NXP NFC Controllers
Source:  	  %{name}-%{version}.tar.gz

BuildRequires:    pcsc-lite-devel
BuildRequires:    libusb-devel
Requires:         systemd
Requires(post):   systemd
Requires(postun): systemd

%description
Linux NFC stack for NCI based NXP NFC Controllers

%package devel
Summary: Development libraries for libnfc-nci
Group: Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig

%description devel
The libnfc-nci-devel package contains header files necessary for
developing programs using libnfc-nci.

%package examples
Summary: Examples using libnfc-nci
Group: Development/Tools
Requires: %{name}%{?_isa} = %{version}-%{release}
%description examples
The libnfc-examples package contains examples demonstrating the functionality
of libnfc.

%prep
%setup -q

%build
./bootstrap
%configure --enable-pn7120
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
find %{buildroot} -type f -name "*.la" -delete


%files devel
%{_libdir}/libnfc_nci_linux-1.so
%{_libdir}/libnfc_nci_linux.*
%{_includedir}/*
%config(noreplace) %{_sysconfdir}/libnfc*

%files examples
%{_sbindir}/*
