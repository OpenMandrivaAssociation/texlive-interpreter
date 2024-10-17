Name:		texlive-interpreter
Version:	27232
Release:	2
Summary:	Translate input files on the fly
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/generic/interpreter
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/interpreter.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/interpreter.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

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
explained in the documentation itself. Interpreter is
implemented using the author's gates (lua version), and works
for plain TeX and LaTeX, but not ConTeXt.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
