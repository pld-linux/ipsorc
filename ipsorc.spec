Summary:	IP Sorcery
Summary(pl.UTF-8):   Generator pakietów IP
Name:		ipsorc
Version:	1.5
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://www.legions.org/~phric/%{name}-%{version}.tar.gz
# Source0-md5:	923149398a7e9caf894c4dfa2f982baa
Patch0:		%{name}-Makefile.patch
URL:		http://www.legions.org/~phric/ipsorcery.html
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IP Sorcery is a TCP/IP packet generator. It has the ability to send
TCP, UDP, and ICMP packets.

%description -l pl.UTF-8
IP Sorcery to generator pakietów TCP/IP. Umie wysyłać pakiety TCP,
UDP, oraz ICMP. Obsługuje IPv4 i IPv6.

%package gtk
Summary:	IP Sorcery
Summary(pl.UTF-8):   Generator pakietów IP
Group:		X11/Applications/Networking

%description gtk
IP Sorcery is a TCP/IP packet generator. It has the ability to send
TCP, UDP, and ICMP packets with a GTK+ interface.

%description gtk -l pl.UTF-8
IP Sorcery to generator pakietów TCP/IP. Umie wysyłać pakiety TCP,
UDP, oraz ICMP korzystając z graficznego interfejsu GTK+. Obsługuje
IPv4 i IPv6.

%prep
%setup -q
%patch0 -p1

%build
%{__make} CFLAGS="%{rpmcflags}" CC="%{__cc}" con
%{__make} CFLAGS="%{rpmcflags}" CC="%{__cc}" gtk

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install ipmagic $RPM_BUILD_ROOT%{_bindir}
install magic $RPM_BUILD_ROOT%{_bindir}/gipmagic

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/ipmagic

%files gtk
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/gipmagic
