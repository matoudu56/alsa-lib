#
# TODO:
#  - track this bug - alsasink in gstreamer isn't working
#    (Patch1 doesn't solve anything, just removes the assertion)
#    https://bugtrack.alsa-project.org/alsa-bug/bug_view_page.php?bug_id=0000116
#
Summary:	Advanced Linux Sound Architecture (ALSA) - Library
Summary(es):	Biblioteca para ALSA (Advanced Linux Sound Architecture)
Summary(pl):	Advanced Linux Sound Architecture (ALSA) - Biblioteka
Summary(pt_BR):	Biblioteca para o ALSA (Advanced Linux Sound Architecture)
Summary(ru):	���������� API ��� ������ � ��������� ALSA
Summary(uk):	��̦����� API ��� ������ � ��������� ALSA
Name:		alsa-lib
Version:	1.0.4
Release:	1
License:	LGPL
Group:		Libraries
Source0:	ftp://ftp.alsa-project.org/pub/lib/%{name}-%{version}.tar.bz2
# Source0-md5:	5f0967a9e71ffdfb47c41fed9e52d9a5
Patch0:		%{name}-bluezsco.patch
# not present in repo
#Patch1:		%{name}-plug_hw_param.patch
URL:		http://www.alsa-project.org/
BuildRequires:	alsa-driver-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	doxygen
BuildRequires:	flex
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildConflicts:	alsa-lib <= 0.4.0
Obsoletes:	alsa-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc

%description
Advanced Linux Sound Architecture (ALSA) - Library

Features:
- general
  - modularized architecture with support for 2.2
  - support for versioned and exported symbols
  - full proc filesystem support - /proc/sound
- ISA soundcards
  - support for 128k ISA DMA buffer
- mixer
  - new enhanced API for applications
  - support for unlimited number of channels
  - volume can be set in three ways (percentual (0-100), exact and
    decibel)
  - support for mute (and hardware mute if hardware supports it)
  - support for mixer events
    - this allows two or more applications to be synchronized
- digital audio (PCM)
  - new enhanced API for applications
  - full real duplex support
  - full duplex support for SoundBlaster 16/AWE soundcards
  - digital audio data for playback and record should be read back using
    proc filesystem
- OSS/Lite compatibility
  - full mixer compatibity
  - full PCM (/dev/dsp) compatibility

%description -l es
Bibliotecas para el sistema de sonido ALSA. Este paquete se necesita
para ejecutar programas Linux que usan el programa de control de
sonido ALSA.

%description -l pl
Advanced Linux Sound Architecture (ALSA) - Biblioteka

Mo�liwo�ci:
- generalne
  - zmodularyzowana architektura ze wsparciem dla j�der 2.2
  - pe�ne wsparcie dla systemu plik�w proc - /proc/sound
- karty d�wi�kowe ISA
  - obs�uga bufora 128k ISA DMA
- mikser
  - nowe rozszerzone API dla aplikacji
  - obs�uga nielimitowanej liczby kana��w
  - g�o�no�� mo�e by� ustawiana na trzy r�ne sposoby (procentowo
    (0-100), liniowo oraz w skali decybelowej)
  - obs�uga wyciszania (oraz sprz�towego wyciszania)
  - obs�uga zdarze� miksera
    - to pozwala dwum lub wi�kszej liczbie aplikacji si� synchronizowa�
- cyfrowe audio (PCM)
  - nowe rozszerzone API dla aplikacji
  - pe�na, prawdziwa obs�uga trybu duplex
  - pe�na obs�uga trybu duplex dla kart SoundBlaster 16/AWE
  - dane cyfrowego d�wi�ku dla odtwarzania i nagrywania powinny by�
    odczytywane poprzez system plik�w /proc
- kompatybilno�� z OSS/Lite
  - pe�na kompatybilno�� miksera
  - pe�na kompatybilno�� PCM (/dev/dsp)

%description -l pt_BR
Bibliotecas para o ALSA. Esse pacote � necess�rio para rodar programas
Linux queusam o driver de som ALSA.

%description -l ru
���������� API ��� ������ � ��������� ALSA.

%description -l uk
��̦����� API ��� ������ � ��������� ALSA.

%package devel
Summary:	Advanced Linux Sound Architecture (ALSA) - header files
Summary(es):	Archivos de desarrollo de ALSA (Advanced Linux Sound Architecture)
Summary(pl):	Advanced Linux Sound Architecture (ALSA) - pliki nag��wkowe
Summary(pt_BR):	Arquivos de desenvolvimento do ALSA (Advanced Linux Sound Architecture)
Summary(ru):	���������� API ��� ������ � ��������� ALSA - ����� ������������
Summary(uk):	��̦����� API ��� ������ � ��������� ALSA - ����� ������ͦ���
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	alsa-driver-devel
Obsoletes:	alsa-devel
Obsoletes:	alsa-lib-devel-doc

%description devel
Advanced Linux Sound Architecture (ALSA) - header files.

%description devel -l es
Este paquete contiene los archivos necesarios para compilar programas
que usan la biblioteca del sistema ALSA. No es necesario instalarlo si
lo que se desea es solamente ejecutar programas.

%description devel -l pl
Advanced Linux Sound Architecture (ALSA) - pliki nag��wkowe.

%description devel -l pt_BR
Esse pacote cont�m os arquivos necess�rios para compilar programas que
usam a biblioteca do ALSA. N�o � necess�rio instalar esse pacote para
apenas rodar programas.

%description devel -l ru
���������� ������������ � ������ ��� ���������� API ��� ������ �
��������� ALSA.

%description devel -l uk
��̦����� ������ͦ��� �� ������ ��� ¦�̦����� API ��� ������ �
��������� ALSA.

%package static
Summary:	Advanced Linux Sound Architecture (ALSA) - static library
Summary(pl):	Advanced Linux Sound Architecture (ALSA) - biblioteka statyczna
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento com a alsa-lib
Summary(ru):	����������� ���������� API ��� ������ � ��������� ALSA
Summary(uk):	�������� ¦�̦����� API ��� ������ � ��������� ALSA
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Advanced Linux Sound Architecture (ALSA) - static library.

%description static -l pl
Advanced Linux Sound Architecture (ALSA) - biblioteka statyczna.

%description static -l pt_BR
Bibliotecas est�ticas para desenvolvimento com a alsa-lib

%description static -l ru
����������� ���������� API ��� ������ � ��������� ALSA.

%description static -l uk
�������� ¦�̦����� API ��� ������ � ��������� ALSA.

%prep
%setup -q
%patch0 -p1
#%patch1 -p1 

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-static

%{__make}
%{__make} doc

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -D utils/alsa.m4 $RPM_BUILD_ROOT%{_aclocaldir}/alsa.m4

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_datadir}/alsa

%files devel
%defattr(644,root,root,755)
%doc doc/doxygen/html/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_aclocaldir}/alsa.m4
%{_includedir}/sys/*.h
%{_includedir}/alsa
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
