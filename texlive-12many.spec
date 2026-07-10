%global tl_name 12many
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.3
Release:	%{tl_revision}.1
Summary:	Generalising mathematical index sets
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/12many
License:	lppl1.3a
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/12many.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/12many.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/12many.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
In the discrete branches of mathematics and the computer sciences, it
will only take some seconds before you're faced with a set like
{1,...,m}. Some people write $1\ldotp\ldotp m$, others $\{j:1\leq j\leq
m\}$, and the journal you're submitting to might want something else
entirely. The 12many package provides an interface that makes changing
from one to another a one-line change.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/12many
%dir %{_datadir}/texmf-dist/source/latex/12many
%dir %{_datadir}/texmf-dist/tex/latex/12many
%doc %{_datadir}/texmf-dist/doc/latex/12many/12many.pdf
%doc %{_datadir}/texmf-dist/doc/latex/12many/README
%doc %{_datadir}/texmf-dist/source/latex/12many/12many.dtx
%doc %{_datadir}/texmf-dist/source/latex/12many/12many.ins
%{_datadir}/texmf-dist/tex/latex/12many/12many.sty
