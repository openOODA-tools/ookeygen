Name:           ookeygen
Version:        0.1.0
Release:        1%{?dist}
Summary:        Generates Ed25519 and ML-KEM post-quantum cryptographic keypairs.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/ookeygen
Source0:        ookeygen-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ookeygen is a sovereign, capability-bounded KEY GENERATOR written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ookeygen
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ookeygen-uninstall

%files
/usr/bin/ookeygen
/usr/bin/ookeygen-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
