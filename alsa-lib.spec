Summary:	Advanced Linux Sound Architecture (ALSA) - Library
Summary(pl):	Advanced Linux Sound Architecture (ALSA) - Biblioteka
Name:		alsa-lib
Version:	0.3.1
Release:	1
Copyright:	GPL
Group:		System/Libraries
Group(pl):	System/Biblioteki
Source:		ftp://ftp.alsa-project.org/pub/lib/%{name}-%{version}.tar.gz
URL:		http://www.alsa-project.org/
BuildRequires:	alsa-driver-devel >= %{version}
Requires:       alsa-driver
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Advanced Linux Sound Architecture (ALSA) - Library

Features
========
* general
  - modularized architecture with support for 2.0 and latest 2.1 kernels
  - support for versioned and exported symbols
  - full proc filesystem support - /proc/sound
* ISA soundcards
  - support for 128k ISA DMA buffer
* mixer
  - new enhanced API for applications
  - support for unlimited number of channels
  - volume can be set in three ways (percentual (0-100), exact and decibel)
  - support for mute (and hardware mute if hardware supports it)
  - support for mixer events
    - this allows two or more applications to be synchronized
* digital audio (PCM)
  - new enhanced API for applications
  - full real duplex support
  - full duplex support for SoundBlaster 16/AWE soundcards
  - digital audio data for playback and record should be read back using
    proc filesystem
* OSS/Lite compatibility
  - full mixer compatibity
  - full PCM (/dev/dsp) compatibility

%description -l pl
Advanced Linux Sound Architecture (ALSA) - Biblioteka

Nowinki
=======
* generalne
  - zmodularyzowana architektura ze wsparciem dla kerneli 2.0 jak i 2.1
  - pe�ne wsparcie dla systemu plik�w proc - /proc/sound
* karty d�wi�kowe ISA
  - wsparcie dla buforu 128k ISA DMA
* mikser
  - nowe rozszerzone API dla aplikacji
  - wsparcie dla nielimitowanej liczby kana��w
  - g�o�no�� mo�e by� ustawiana na trzy r�ne sposoby (procentowo (0-100),
    liniowo oraz w skali decybelowej)
  - wsparcie dla mute (oraz dla sprz�towego mute)
  - wsparcie dla zdarze� miksera
    - to pozwala dwum lub wi�kszej liczbie aplikacji si� synchronizowac
* cyfrowe audio (PCM)
  - nowe rozszerzone API dla aplikacji
  - pe�ne realne wsparcie dla trybu duplex
  - dane cyfrowego d�wi�ku dla odtwarzania i nagrywania powinny by� odczytywane
    poprzez system plik�w /proc
* kompatybilno�� z OSS/Lite
  - pe�na kompatybilno�� miksera
  - pe�na kompatybilno�� PCM (/dev/dsp)

%package devel
Summary:	Header files fo ALSA library
Summary(pl):	Pliki nag�owkowe do biblioteki ALSA
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files fo ALSA library.

%description -l pl devel
Pliki nag�owkowe do biblioteki ALSA.

%package static
Summary:	Advanced Linux Sound Architecture (ALSA) - Static library
Summary(pl):	Advanced Linux Sound Architecture (ALSA) - Biblioteka statyczna
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Advanced Linux Sound Architecture (ALSA) - Static library.

%description -l pl static
Advanced Linux Sound Architecture (ALSA) - Biblioteka statyczna.

%prep
%setup -q 

%build
LDFLAGS="-s"; export LDFLAGS
%configure
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

gzip -9nf ChangeLog doc/*.txt

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc *.gz doc/*.gz

%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_datadir}/aclocal/alsa.m4
%{_includedir}/sys/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
