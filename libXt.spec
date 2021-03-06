# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.23
# 
# >> macros
# << macros

Name:       libXt
Summary:    X.Org X11 libXt runtime library
Version:    1.1.3
Release:    1
Group:      System/Libraries
License:    MIT
URL:        http://www.x.org
Source0:    http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.bz2
Source100:  libXt.yaml
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(kbproto)


%description
%{summary}.



%package devel
Summary:    X.Org X11 libXt development package
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
%{summary}.



%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%configure --disable-static \
    --with-xfile-search-path="%{_sysconfdir}/X11/%%L/%%T/%%N%%C%%S:%{_sysconfdir}/X11/%%l/%%T/\%%N%%C%%S:%{_sysconfdir}/X11/%%T/%%N%%C%%S:%{_sysconfdir}/X11/%%L/%%T/%%N%%S:%{_sysconfdir}/X\11/%%l/%%T/%%N%%S:%{_sysconfdir}/X11/%%T/%%N%%S:%{_datadir}/X11/%%L/%%T/%%N%%C%%S:%{_datadir}/X1\1/%%l/%%T/%%N%%C%%S:%{_datadir}/X11/%%T/%%N%%C%%S:%{_datadir}/X11/%%L/%%T/%%N%%S:%{_datadir}/X11/%%\l/%%T/%%N%%S:%{_datadir}/X11/%%T/%%N%%S"

make %{?jobs:-j%jobs}

# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# << install post



%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig





%files
%defattr(-,root,root,-)
# >> files
%doc COPYING ChangeLog
%{_libdir}/libXt.so.6
%{_libdir}/libXt.so.6.0.0
# << files


%files devel
%defattr(-,root,root,-)
# >> files devel
%dir %{_includedir}/X11
%{_includedir}/X11/CallbackI.h
%{_includedir}/X11/Composite.h
%{_includedir}/X11/CompositeP.h
%{_includedir}/X11/ConstrainP.h
%{_includedir}/X11/Constraint.h
%{_includedir}/X11/ConvertI.h
%{_includedir}/X11/Core.h
%{_includedir}/X11/CoreP.h
%{_includedir}/X11/CreateI.h
%{_includedir}/X11/EventI.h
%{_includedir}/X11/HookObjI.h
%{_includedir}/X11/InitialI.h
%{_includedir}/X11/Intrinsic.h
%{_includedir}/X11/IntrinsicI.h
%{_includedir}/X11/IntrinsicP.h
%{_includedir}/X11/Object.h
%{_includedir}/X11/ObjectP.h
%{_includedir}/X11/PassivGraI.h
%{_includedir}/X11/RectObj.h
%{_includedir}/X11/RectObjP.h
%{_includedir}/X11/ResConfigP.h
%{_includedir}/X11/ResourceI.h
%{_includedir}/X11/SelectionI.h
%{_includedir}/X11/Shell.h
%{_includedir}/X11/ShellI.h
%{_includedir}/X11/ShellP.h
%{_includedir}/X11/StringDefs.h
%{_includedir}/X11/ThreadsI.h
%{_includedir}/X11/TranslateI.h
%{_includedir}/X11/VarargsI.h
%{_includedir}/X11/Vendor.h
%{_includedir}/X11/VendorP.h
%{_includedir}/X11/Xtos.h
%{_libdir}/libXt.so
%{_libdir}/pkgconfig/xt.pc
%doc %{_mandir}/man3/*.3*
%{_datadir}/doc/libXt/*.xml
# << files devel

