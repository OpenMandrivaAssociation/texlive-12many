# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/12many
# catalog-date 2008-10-03 01:00:01 +0200
# catalog-license lppl
# catalog-version 0.3
Name:		texlive-12many
Version:	0.3
Release:	1
Summary:	Generalising mathematical index sets
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/12many
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/12many.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/12many.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/12many.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

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
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/12many/12many.sty
%doc %{_texmfdistdir}/doc/latex/12many/12many.pdf
%doc %{_texmfdistdir}/doc/latex/12many/README
#- source
%doc %{_texmfdistdir}/source/latex/12many/12many.dtx
%doc %{_texmfdistdir}/source/latex/12many/12many.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
