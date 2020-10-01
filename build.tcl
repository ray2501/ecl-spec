#!/usr/bin/tclsh

set arch "x86_64"
set base "ecl-20.4.24"
set fileurl "https://common-lisp.net/project/ecl/static/files/release/ecl-20.4.24.tgz"

set var [list wget $fileurl -O $base.tgz]
exec >@stdout 2>@stderr {*}$var

if {[file exists build]} {
    file delete -force build
}

file mkdir build/BUILD build/RPMS build/SOURCES build/SPECS build/SRPMS
file copy -force $base.tgz build/SOURCES

set buildit [list rpmbuild --target $arch --define "_topdir [pwd]/build" -bb ecl.spec]
exec >@stdout 2>@stderr {*}$buildit

# Remove our source code
file delete -force $base.tgz

