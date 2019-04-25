%global _prefix /usr/local

Name:    node-sass-binding-node-rpm-linux-x64
Release: 1
Summary: Node.js bindings to libsass https://npmjs.org/package/node-sass
Group:   Development Tools
License: ASL 2.0
Source0: https://github.com/sass/node-sass/releases/download/v4.11.0/linux-x64-57_binding.node

%description
Node-sass is a library that provides binding for Node.js to LibSass, the C version of the popular stylesheet preprocessor, Sass.

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/opt/lib/node-sass/linux-x64-57/
%{__install} -m 755 %{SOURCE0} %{buildroot}opt/lib/node-sass/linux-x64-57/binding.node

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/%{name}
