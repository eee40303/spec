%global use_systemd 0

%if 0%{?fedora} >= 15 || 0%{?rhel} >=7 || 0%{?suse_version} >= 1210 || 0%{?_unitdir:1}
%global use_systemd 1
%else
%global use_systemd 0
%endif

%if 0%{?use_systemd}
%{!?_unitdir: %global _unitdir /usr/lib/systemd/system}
%{?systemd_requires}
%if 0%{?suse_version}
BuildRequires:   systemd-rpm-macros
%else
BuildRequires:   systemd
%endif
%endif


%ifarch armv7h
%global goarch arm
%else
%ifarch aarch64
%global goarch arm64
%else
%ifarch mips64el
%global goarch mips64
%else
%ifarch x86_64
%global goarch amd64
%else
%global goarch %{_arch}
%endif
%endif
%endif
%endif

%global debug_package %{nil}



Name:           v2ray-plugin
Version:        v1.3.2
Release:        1%{?dist}
Summary:        A SIP003 plugin based on v2ray for shadowsocks

License:        MIT License
URL:            https://github.com/shadowsocks/v2ray-plugin
Source0:        dist.zip
Source1:        https://github.com/shadowsocks/v2ray-plugin/releases/download/v1.3.2/v2ray-plugin-linux-386-v1.3.2.tar.gz
Source2:        https://github.com/shadowsocks/v2ray-plugin/releases/download/v1.3.2/v2ray-plugin-linux-amd64-v1.3.2.tar.gz
Source3:        https://github.com/shadowsocks/v2ray-plugin/releases/download/v1.3.2/v2ray-plugin-linux-arm-v1.3.2.tar.gz
Source4:        https://github.com/shadowsocks/v2ray-plugin/releases/download/v1.3.2/v2ray-plugin-linux-arm64-v1.3.2.tar.gz
#Source5:        https://github.com/shadowsocks/v2ray-plugin/releases/download/v1.3.2/v2ray-plugin-linux-mips-v1.3.2.tar.gz
#Source6:        https://github.com/shadowsocks/v2ray-plugin/releases/download/v1.3.2/v2ray-plugin-linux-mips64-v1.3.2.tar.gz


BuildRequires:  rpm
Requires:       rpm

%description
Yet another SIP003 plugin for shadowsocks, based on v2ray
https://github.com/shadowsocks/%{name}/releases/download/%{version}/%{name}-linux-%{goarch}-%{version}.tar.gz


%prep
%autosetup -c

#tar -xf %{_sourcedir}/v2ray-plugin-linux-%{goarch}-%{version}.tar.gz
mkdir -p tmp_extract
tar -xf %{_sourcedir}/v2ray-plugin-linux-%{goarch}-%{version}.tar.gz -C tmp_extract
pwd
find tmp_extract -type f -name "v2ray-plugin*" -exec mv -v {} ./v2ray-plugin \;
rm -rf _tmp_foo


%build


%install
rm -rf $RPM_BUILD_ROOT

mkdir -p %{buildroot}/etc/shadowsocks-libev
install -m 644 %{_builddir}/%{buildsubdir}/dist/etc/config-v2ray-plugin.json %{buildroot}%{_sysconfdir}/shadowsocks-libev/
mkdir -p %{buildroot}%{_bindir}
install -m 755 %{_builddir}/%{buildsubdir}/v2ray-plugin %{buildroot}%{_bindir}/v2ray-plugin

%if ! 0%{?use_systemd}
mkdir -p %{buildroot}%{_initddir}
install -m 755 %{_builddir}/%{buildsubdir}/dist/etc/init.d/shadowsocks-libev %{buildroot}%{_initddir}/shadowsocks-libev
%else
mkdir -p %{buildroot}%{_unitdir}/
install -m 644 %{_builddir}/%{buildsubdir}/dist/systemd/shadowsocks-libev-v2ray-plugin.service %{buildroot}%{_unitdir}/
%endif


%files
%{_bindir}/v2ray-plugin
%{_sysconfdir}/shadowsocks-libev/config-v2ray-plugin.json
%if ! 0%{?use_systemd}
%{_initddir}/*
%else
%{_unitdir}/shadowsocks-libev-v2ray-plugin.service
%endif

#%license add-license-file-here
#%doc add-docs-here



%changelog
* Mon Jan 12 2026 e3
- 
