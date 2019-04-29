%global _prefix /usr/local
%global node_version 4.11.0

Name:    node-sass-binding-node-rpm-linux-x64
Version: 64
Release: 1
Summary: Node.js bindings to libsass https://npmjs.org/package/node-sass
Group:   Development Tools
License: ASL 2.0
URL: https://github.com/sass/node-sass/releases/download/v%{node_version}/linux-x64-%{version}_binding.node
Source0: README.md

%description
Node-sass is a library that provides binding for Node.js to LibSass,
the C version of the popular stylesheet preprocessor, Sass.

%prep
curl -L %{url} > linux-x64-%{version}_binding.node

%install
%{__install} -m 0755 -d %{buildroot}/opt/lib/node-sass/linux-x64-%{node_version}/
cp linux-x64-%{version}_binding.node %{buildroot}/opt/lib/node-sass/linux-x64-%{node_version}/

%files
/opt/lib/node-sass/linux-x64-%{node_version}/linux-x64-%{version}_binding.node

