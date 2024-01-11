Name: wayland-ivi-extension
Version: 2.2.0
Release: r0
Summary: Wayland IVI Extension
License: Apache-2.0
URL: http://projects.genivi.org/wayland-ivi-extension
Source0: %{name}-%{version}.tar.gz

BuildRequires: cmake weston
BuildRequires: pkgconfig(wayland-scanner)
BuildRequires: pkgconfig(wayland-server)
BuildRequires: pkgconfig(wayland-client)

%description
GENIVI Layer Management API based on Wayland IVI Extension

%prep
%autosetup -n %{name}

%package -n wayland-ivi-extension-dev
Summary: wayland-ivi-extension header files

%description -n wayland-ivi-extension-dev
Header files and shared files of wayland-ivi-extension

%build
%cmake -DWITH_ILM_INPUT=1 -DCMAKE_BUILD_TYPE=Release -DCMAKE_TOOLCHAIN_FILE=$CMAKE_TOOLCHAIN_FILE -DCMAKE_RULE_MESSAGES:BOOL=OFF -DCMAKE_VERBOSE_MAKEFILE:BOOL=$VER -DCMAKE_INSTALL_INCLUDEDIR=%{_includedir} -DCMAKE_INSTALL_LIBDIR=%{_libdir} -DCMAKE_INSTALL_BINDIR=%{_bindir}
%cmake_build

%install
%cmake_install

%files -n wayland-ivi-extension-dev
%dir %{_includedir}/ilm
%{_includedir}/ilm/ilm_client.h
%{_includedir}/ilm/ilm_common.h
%{_includedir}/ilm/ilm_control.h
%{_includedir}/ilm/ilm_input.h
%{_includedir}/ilm/ilm_platform.h
%{_includedir}/ilm/ilm_types.h
%{_includedir}/ilm/ivi-application-client-protocol.h
%dir %{_usr}/share/wayland-ivi-extension/textures/skyscrapers
%{_usr}/share/wayland-ivi-extension/textures/base.bmp
%{_usr}/share/wayland-ivi-extension/textures/car.bmp
%{_usr}/share/wayland-ivi-extension/textures/sources.txt
%{_usr}/share/wayland-ivi-extension/textures/street.bmp
%{_usr}/share/wayland-ivi-extension/textures/skyscrapers/facade00.bmp
%{_usr}/share/wayland-ivi-extension/textures/skyscrapers/facade01.bmp
%{_usr}/share/wayland-ivi-extension/textures/skyscrapers/facade02.bmp
%{_usr}/share/wayland-ivi-extension/textures/skyscrapers/facade03.bmp
%{_usr}/share/wayland-protocols/stable/ivi-application/ivi-application.xml

%files
%{_bindir}/EGLWLInputEventExample
%{_bindir}/EGLWLMockNavigation
%{_bindir}/layer-add-surfaces
%{_bindir}/LayerManagerControl
%{_bindir}/multi-touch-viewer
%{_bindir}/simple-weston-client
%{_libdir}/pkgconfig/ilmCommon.pc
%{_libdir}/pkgconfig/ilmControl.pc
%{_libdir}/pkgconfig/ilmInput.pc
%{_libdir}/pkgconfig/ivi-application.pc
%dir %{_libdir}/weston
%{_libdir}/weston/ivi-controller.so
%{_libdir}/weston/ivi-id-agent.so
%{_libdir}/weston/ivi-input-controller.so
%{_libdir}/libilmClient.so
%{_libdir}/libilmClient.so.2.2.0
%{_libdir}/libilmCommon.so
%{_libdir}/libilmCommon.so.2.2.0
%{_libdir}/libilmControl.so
%{_libdir}/libilmControl.so.2.2.0
%{_libdir}/libilmInput.so
%{_libdir}/libilmInput.so.2.2.0
%{_libdir}/libivi-application.so
%{_libdir}/libivi-application.so.2.2.0
