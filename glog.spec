%define major 1
%define libglog %mklibname glog
%define libglog_devel %mklibname glog -d

Name:      glog
Version:   0.7.0
Release:   1

License:   BSD
URL:       https://github.com/google/glog
Source0:   https://github.com/google/glog/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz

Summary: Logging library for C++
Group:   Development/C++

BuildRequires:	cmake
BuildRequires:	ninja

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
%{_libdir}/libglog.so.*

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
%{_libdir}/cmake/glog

%prep
%autosetup -p1
%cmake -DWITH_PKGCONFIG:BOOL=ON \
       -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
