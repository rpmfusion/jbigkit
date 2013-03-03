Name:           jbigkit
Version:        2.0
Release:        5%{?dist}
Summary:        JBIG1 lossless image compression tools

Group:          Applications/Multimedia
License:        GPL
URL:            http://www.cl.cam.ac.uk/~mgk25/jbigkit/
Source0:        http://www.cl.cam.ac.uk/~mgk25/download/%{name}-%{version}.tar.gz
Patch0:         jbigkit-2.0-shlib.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%package libs
Summary:        JBIG1 lossless image compression library
Group:          Applications/Multimedia

%package devel
Summary:        JBIG1 lossless image compression library -- development files
Group:          Applications/Multimedia
Requires:       jbigkit-libs = %{version}-%{release}

%description libs
JBIG-KIT provides a portable library of compression and decompression
functions with a documented interface that you can include very easily
into your image or document processing software. In addition, JBIG-KIT
provides ready-to-use compression and decompression programs with a
simple command line interface (similar to the converters found in
netpbm).

JBIG-KIT implements the specification:
    ISO/IEC 11544:1993 and ITU-T Recommendation T.82(1993):
     Information technology — Coded representation of picture and audio
     information — Progressive bi-level image compression 

which is commonly referred to as the “JBIG1 standard”

%description devel
The jbigkit-devel package contains files needed for development using 
the JBIG-KIT image compression library.

%description
The jbigkit package contains tools for converting between PBM and JBIG1
formats.


%prep
%setup -q -n jbigkit
%patch0 -p1 -b .shlib

%build
make %{?_smp_mflags} CCFLAGS="$RPM_OPT_FLAGS"


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{_includedir}
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1

install -p -m0755 libjbig/libjbig.so.%{version} $RPM_BUILD_ROOT/%{_libdir}
install -p -m0755 libjbig/libjbig85.so.%{version} $RPM_BUILD_ROOT/%{_libdir}
ln -sf libjbig.so.%{version} $RPM_BUILD_ROOT/%{_libdir}/libjbig.so
ln -sf libjbig85.so.%{version} $RPM_BUILD_ROOT/%{_libdir}/libjbig85.so

install -p -m0644 libjbig/jbig.h $RPM_BUILD_ROOT%{_includedir}
install -p -m0644 libjbig/jbig85.h $RPM_BUILD_ROOT%{_includedir}
install -p -m0644 libjbig/jbig_ar.h $RPM_BUILD_ROOT%{_includedir}

install -p -m0755 pbmtools/???to??? $RPM_BUILD_ROOT%{_bindir}
install -p -m0755 pbmtools/???to???85 $RPM_BUILD_ROOT%{_bindir}
install -p -m0644 pbmtools/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%check
make test

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_bindir}/???to*
%{_mandir}/man1/*

%files libs
%{_libdir}/libjbig*.so.%{version}
%doc COPYING ANNOUNCE TODO INSTALL CHANGES

%files devel
%{_libdir}/libjbig*.so
%{_includedir}/jbig*.h

# Don't obfuscate email addresses here, please.
%changelog
* Sun Mar 03 2013 Nicolas Chauvet <kwizart@gmail.com> - 2.0-5
- Mass rebuilt for Fedora 19 Features

* Wed Feb 08 2012 Nicolas Chauvet <kwizart@gmail.com> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 2.0-3
- rebuild for new F11 features

* Fri Sep 05 2008 David Woodhouse <dwmw2@infradead.org> 2.0-2
- Add missing jbig_ar.h

* Wed Sep 03 2008 David Woodhouse <dwmw2@infradead.org> 2.0-1
- Update to 2.0

* Sun Aug 03 2008 Thorsten Leemhuis <fedora@leemhuis.info> - 1.6-3
- rebuild

* Sun Oct  1 2006 David Woodhouse <dwmw2@infradead.org> 1.6-2
- Review fixes

* Tue Sep 12 2006 David Woodhouse <dwmw2@infradead.org> 1.6-1
- Initial version
