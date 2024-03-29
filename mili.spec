%define _empty_manifest_terminate_build 0

Name:       mili
Version:    3.1.0
Release:    2
Summary:    Minimalistic text editor made with Python and GTK
Group:      Text/Editors
License:    MIT
URL:        https://gitlab.com/zehkira/mili
Source0:    https://gitlab.com/zehkira/mili/-/archive/v%{version}/mili-v%{version}.tar.bz2
 
BuildRequires:  pkgconfig(python)
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtksourceview-3.0)
BuildRequires:  python3dist(setuptools)

%description
Mili is a simple and lightweight (but highly configurable) text editor written in Python. 
It's based on GTK3 and uses GtkSourceView for most of its text editing functionality.
Some notable features include:

automatic indentation style detection
ability to rebind even basic actions (such as saving the current file)
no CSD (unlike gedit) = no issues with tiling or screen sharing

%prep
%autosetup -n %{name}-v%{version} -p1
 
%build
%py_build

%install
%py_install

%files
%{python_sitelib}/zehkira_mili-*-py*.*.egg-info
%{python_sitelib}/zehkira_mili/
