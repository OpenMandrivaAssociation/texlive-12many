Name:		texlive-12many
Version:	0.3
Release:	1
Summary:	Generalising mathematical index sets
Group:		Publishing
URL:		http://www.ctan.org/tex-archive//macros/latex/contrib/12many
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/12many.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
In the discrete branches of mathematics and the computer
sciences, it will only take some seconds before you're faced
with a set like {1,...,m}. Some people write $1\ldotp\ldotp m$,
others $\{j:1\leq j\leq m\}$, and that journal you're
submitting to might want something else entirely. The 12many
package provides an interface that makes changing from one to
another a one-line change.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
    fi

%files
%{_texmfdistdir}/tex/latex/12many/12many.sty

%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}
