%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/melodic/.*$
%global __requires_exclude_from ^/opt/ros/melodic/.*$

Name:           ros-melodic-code-coverage
Version:        0.3.0
Release:        1%{?dist}
Summary:        ROS code_coverage package

License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       lcov
BuildRequires:  lcov
BuildRequires:  ros-melodic-catkin

%description
CMake configuration to run coverage

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_LIBDIR="lib" \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/melodic

%changelog
* Tue Nov 19 2019 Michael Ferguson <mike@vanadiumlabs.com> - 0.3.0-1
- Autogenerated by Bloom

* Thu Jul 18 2019 Michael Ferguson <mike@vanadiumlabs.com> - 0.2.4-1
- Autogenerated by Bloom

* Fri Aug 24 2018 Michael Ferguson <mike@vanadiumlabs.com> - 0.2.3-0
- Autogenerated by Bloom

* Tue Aug 21 2018 Michael Ferguson <mike@vanadiumlabs.com> - 0.2.2-0
- Autogenerated by Bloom

* Mon Aug 13 2018 Michael Ferguson <mike@vanadiumlabs.com> - 0.2.1-0
- Autogenerated by Bloom

* Wed Aug 01 2018 Michael Ferguson <mike@vanadiumlabs.com> - 0.2.0-0
- Autogenerated by Bloom

