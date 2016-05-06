Name:           ros-kinetic-rtabmap
Version:        0.11.4
Release:        1%{?dist}
Summary:        ROS rtabmap package

Group:          Development/Libraries
License:        BSD
URL:            http://introlab.github.io/rtabmap
Source0:        %{name}-%{version}.tar.gz

Requires:       libfreenect-devel
Requires:       libsq3-devel
Requires:       openni-devel
Requires:       pcl-devel
Requires:       ros-kinetic-cv-bridge
Requires:       zlib-devel
BuildRequires:  cmake
BuildRequires:  libfreenect-devel
BuildRequires:  libsq3-devel
BuildRequires:  openni-devel
BuildRequires:  pcl-devel
BuildRequires:  proj-devel
BuildRequires:  ros-kinetic-cv-bridge
BuildRequires:  zlib-devel

%description
RTAB-Map's standalone library. RTAB-Map is a RGB-D SLAM approach with real-time
constraints.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Fri May 06 2016 Mathieu Labbe <matlabbe@gmail.com> - 0.11.4-1
- Autogenerated by Bloom

* Fri May 06 2016 Mathieu Labbe <matlabbe@gmail.com> - 0.11.4-0
- Autogenerated by Bloom

