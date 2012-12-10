%define major 0
%define libglog %mklibname glog %major
%define libglog_devel %mklibname glog -d
%define libglog_static_devel %mklibname glog -d -s

Name:      glog
Version:   0.3.2
Release:   1

License:   BSD
URL:       http://code.google.com/p/google-glog/

Source0:   http://google-glog.googlecode.com/files/%{name}-%{version}.tar.gz

#------------------------------------------------------------------------------#

# package glog

Summary: Logging library for C++
Group:   Development/C++

%description
The glog library implements application-level logging. This library provides
logging APIs based on C++-style streams and various helper macros.

#------------------------------------------------------------------------------#

%package -n %{libglog}

Summary: Logging library for C++
Group:   Development/C++

Provides: %{name} = %{version}

%description -n %{libglog}
The glog library implements application-level logging. This library provides
logging APIs based on C++-style streams and various helper macros.

%files -n %{libglog}
%{_libdir}/libglog.so.%{major}
%{_libdir}/libglog.so.%{major}.*

#------------------------------------------------------------------------------#

%package -n %{libglog_devel}

Summary: Development files for %{libglog}
Group:   Development/C++

Requires: %{libglog} = %{version}
Provides: lib%{name}-devel = %{version}-%{release}

%description -n %{libglog_devel}
Development files for %{libglog}

%files -n %{libglog_devel}
%{_libdir}/libglog.so
%{_libdir}/pkgconfig/libglog.pc
%{_includedir}/glog
%{_datadir}/doc/%{name}-%{version}

#------------------------------------------------------------------------------#

%package -n %{libglog_static_devel}

Summary: Static development files for %{libglog}
Group:   Development/C++

Requires: %{libglog_devel} = %{version}
Provides: lib%{name}-static-devel = %{version}-%{release}

%description -n %{libglog_static_devel}
Static development files for %{libglog}

%files -n %{libglog_static_devel}
%{_libdir}/libglog.a

#------------------------------------------------------------------------------#

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std



%changelog
* Mon Jul 16 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.3.2-1
+ Revision: 809798
- version update 0.3.2

* Tue Feb 22 2011 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 0.3.1-1
+ Revision: 639254
- imported package glog

