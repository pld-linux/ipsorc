Summary:	IP Sorcery
Name:		ipsorc
Version:	1.4
Release:	1
License:	GPL
Group:		Applications/Networking
Group(de):	Applikationen/Netzwerkwesen
Group(pl):	Aplikacje/Sieciowe
Source0:	http://www.legions.org/~phric/%{name}-%{version}.tar.gz
Patch0:		%{name}-Makefile.patch
URL:		http://www.legions.org/~phric/ipsorcery.html
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IP Sorcery is a TCP/IP packet generator. It has the ability to send
TCP, UDP, and ICMP packets.

%description -l pl
IP Sorcery to generator pakietów TCP/IP. Umie wysy³aæ pakiety TCP,
UDP, oraz ICMP. Obs³uguje IPv4 i IPv6.

%package gtk
Summary:	IP Sorcery
Group:		X11/Applications/Networking
Group(de):	X11/Applikationen/Netzwerkwesen
Group(pl):	X11/Aplikacje/Sieciowe

%description gtk
IP Sorcery is a TCP/IP packet generator. It has the ability to send
TCP, UDP, and ICMP packets with a GTK+ interface.

%description gtk -l pl
IP Sorcery to generator pakietów TCP/IP. Umie wysy³aæ pakiety TCP,
UDP, oraz ICMP ko¿ystaj±c z graficznego interfejsu GTK+. Obs³uguje
IPv4 i IPv6.

%prep
%setup -q
%patch0 -p1

%build
%{__make} CFLAGS="%{rpmcflags}" CC=%{__cc} con
%{__make} CFLAGS="%{rpmcflags}" CC=%{__cc} gtk

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_prefix}/X11R6/bin}

install ipmagic $RPM_BUILD_ROOT%{_bindir}
install magic $RPM_BUILD_ROOT%{_prefix}/X11R6/bin/gipmagic

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%{_bindir}/*

%files gtk
%defattr(644,root,root,755)
%doc README.gz
%{_prefix}/X11R6/bin/*
