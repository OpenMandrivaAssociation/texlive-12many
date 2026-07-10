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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
In the discrete branches of mathematics and the computer sciences, it
will only take some seconds before you're faced with a set like
{1,...,m}. Some people write $1\ldotp\ldotp m$, others $\{j:1\leq j\leq
m\}$, and the journal you're submitting to might want something else
entirely. The 12many package provides an interface that makes changing
from one to another a one-line change.

