%global _prefix /usr/local

Name:    node-sass-binding-node-rpm-linux-x64
Version: 4.11_57
Release: 1
Summary: Node.js bindings to libsass https://npmjs.org/package/node-sass
Group:   Development Tools
License: ASL 2.0

%description
Node-sass is a library that provides binding for Node.js to LibSass, the C version of the popular stylesheet preprocessor, Sass.

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/opt/lib/node-sass/linux-x64-%{version}/
curl -sL https://github.com/sass/node-sass/releases/download/v4.11.0/linux-x64-57_binding.node -o %{buildroot}/opt/lib/node-sass/linux-x64-%{version}/node-sass-binding-%{version}.node

%clean
rm -rf $RPM_BUILD_ROOT

%files
/opt/lib/node-sass/linux-x64-%{version}/node-sass-binding-%{version}.node
