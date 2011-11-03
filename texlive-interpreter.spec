# revision 23399
# category Package
# catalog-ctan /macros/luatex/generic/interpreter
# catalog-date 2011-07-12 12:52:39 +0200
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-interpreter
Version:	1.0
Release:	1
Summary:	Translate input files on the fly
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/luatex/generic/interpreter
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/interpreter.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/interpreter.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package preprocesses input files to a Lua(La)TeX run, on
the fly. The user defines Lua regular expressions to search for
patterns and modify input lines (or entire paragraphs)
accordingly, before TeX reads the material. In this way,
documents may be prepared in a non-TeX language (e.g., some
lightweight markup language) and turned into 'proper' TeX for
processing. The source of the documentation is typed in such a
lightweight language and is thus easily readable in a text
editor (the PDF file is also available, of course); the
transformation to TeX syntax via Interpreter's functions is
explained in the documentation itself. Interpreter works for
plain TeX and LaTeX, but not ConTeXt.

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
%{_texmfdistdir}/tex/luatex/interpreter/interpreter.lua
%{_texmfdistdir}/tex/luatex/interpreter/interpreter.sty
%{_texmfdistdir}/tex/luatex/interpreter/interpreter.tex
%doc %{_texmfdistdir}/doc/luatex/interpreter/README
%doc %{_texmfdistdir}/doc/luatex/interpreter/i-doc.lua
%doc %{_texmfdistdir}/doc/luatex/interpreter/interpreter-doc.pdf
%doc %{_texmfdistdir}/doc/luatex/interpreter/interpreter-doc.tex
%doc %{_texmfdistdir}/doc/luatex/interpreter/interpreter-doc.txt
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
