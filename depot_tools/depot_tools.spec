%global rev d629fb40849ddc046a8255f5407ef588f49e32d8

Name:                   depot_tools
Summary:                depot_tools to manage interaction with the Chromium source code repository
License:                GPL
Version:                1.0
Release:                2%{?dist}
Url:			http://www.chromium.org/developers/how-tos/depottools
Source0:                %{name}.tgz
BuildArch:              noarch
BuildRequires:		tar zlib git openssl
Requires:               python

%description
Chromium uses a package of scripts, the depot_tools, to manage interaction with the Chromium source code repository and the Chromium development process.  It contains the following utilities:

    gclient: Meta-checkout tool managing both subversion and git checkouts.
             It is similar to repo tool except that it works on Linux, OS X, 
	     and Windows and supports both svn and git. On the other hand, gclient doesn't integrate any code review functionality.
    gcl: Rietveld code review tool for subversion. The gcl tool runs presubmit scripts.
    git-cl: Rietveld code review tool for git. The git-cl tool runs presubmit scripts.
    hammer: (Obsolete) Wrapper script for building Chromium with the SCons software construction tool.
    drover: Quickly revert svn commits.
    cpplint.py: Checks for C++ style compliance.
    presubmit_support.py: Runs PRESUBMIT.py presubmit checks.
    repo: The repo tool.
    trychange.py: Try server tool. It is wrapped by gcl try and git-try.
    git-try: Try change tool for git users
    wtf: Displays the active git branches in a chromium os checkout.
    weekly: Displays the log of checkins for a particular developer since a particular date for git checkouts.
    git-gs: Wrapper for git grep with relevant source types.
    zsh-goodies: Completion for zsh users.

%prep
%setup -q -n depot_tools
%build
%install
rm -rf %buildroot

mkdir -p %{buildroot}/opt/chromium/%{name}
cp -pr *.* %{buildroot}/opt/chromium/%{name}

#remove .git crap
find %{buildroot}/opt/chromium/%{name} -name "*.git" |xargs -i rm -fv {}

#remove win crap
find %{buildroot}/opt/chromium/%{name} -name "*.bat *.exe" |xargs -i rm -fv {}
%check

%clean
if ! test -f /.buildenv; then
	rm -rf $RPM_BUILD_ROOT
fi


%files
%defattr(-,root,root)
%dir /opt/chromium/%{name}
/opt/chromium/%{name}/*.*


%changelog
* Wed Oct 01 2014 Tomas Hrcka <thrcka@redhat.com> - 1.0-2
- rebuilt


