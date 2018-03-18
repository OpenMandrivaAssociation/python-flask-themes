# Created by pyp2rpm-2.0.0
%global pypi_name Flask-Sphinx-Themes
%global pyrpm_name flask-sphinx-themes
%global with_python2 1
%define version 1.0.2

Name:           python-%{pyrpm_name}
Version:        %{version}
Release:        1
Group:          Development/Python
Summary:        Sphinx themes for Flask and related projects

License:        BSD
URL:            https://github.com/pallets/flask-sphinx-themes
Source0:        https://pypi.python.org/packages/ae/66/5e84bfe3168295c9c806d87eebf65f4cfc07d9c2d4f27d80e026c69046e6/Flask-Sphinx-Themes-1.0.2.tar.gz
BuildArch:      noarch
 
BuildRequires:  python-devel
BuildRequires:  python-setuptools
 
%if %{?with_python2}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%endif # if with_python2
 
Requires:       python-sphinx
Requires:       python-setuptools

%description
Sphinx themes for Flask and related projects.

%if 0%{?with_python2}
%package -n     python2-%{pyrpm_name}
Summary:        Sphinx themes for Flask and related projects
 
Requires:       python2-Sphinx
Requires:       python2-setuptools

%description -n python2-%{pyrpm_name}
Sphinx themes for Flask and related projects.
%endif # with_python2


%prep
%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%if 0%{?with_python2}
rm -rf %{py2dir}
cp -a . %{py2dir}
find %{py2dir} -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python2}|'

%endif # with_python2


%build
%{__python3} setup.py build

%if 0%{?with_python2}
pushd %{py2dir}
%{__python2} setup.py build
popd
%endif # with_python2

%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install (and we want the python2 version
# to be the default for now).
%if 0%{?with_python2}
pushd %{py2dir}
printf "%s\n" "We are here"
%{__python2} setup.py install --skip-build --root %{buildroot}
popd
%endif # with_python2
printf "%s\n" "And now we are here"
%{__python3} setup.py install --skip-build --root %{buildroot}


%files
%doc README.rst LICENSE
%{python3_sitelib}/flask_sphinx_themes
%{python3_sitelib}/Flask_Sphinx_Themes-%{version}-py?.?.egg-info
%if 0%{?with_python2}
%files -n python2-%{pyrpm_name}
%doc README.rst LICENSE
%{python2_sitelib}/flask_sphinx_themes
%{python2_sitelib}/Flask_Sphinx_Themes-%{version}-py?.?.egg-info
%endif # with_python2

