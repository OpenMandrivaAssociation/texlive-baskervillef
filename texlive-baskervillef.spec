Name:		texlive-baskervillef
Version:	55475
Release:	2
Summary:	Fry's Baskerville look-alike, with math support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/baskervillef
License:	ofl lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/baskervillef.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/baskervillef.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
BaskervilleF is a fork from the Libre Baskerville fonts (Roman,
Italic, Bold only) released under the OFL by Paolo Impallari
and Rodrigo Fuenzalida. Their fonts are optimized for web
usage, while BaskervilleF is optimized for traditional TeX
usage, normally destined for production of pdf files. A bold
italic style was added and mathematical support is offered as
an option to newtxmath.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/baskervillef
%{_texmfdistdir}/fonts/vf/public/baskervillef
%{_texmfdistdir}/fonts/type1/public/baskervillef
%{_texmfdistdir}/fonts/tfm/public/baskervillef
%{_texmfdistdir}/fonts/opentype/public/baskervillef
%{_texmfdistdir}/fonts/map/dvips/baskervillef
%{_texmfdistdir}/fonts/enc/dvips/baskervillef
%doc %{_texmfdistdir}/doc/fonts/baskervillef

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
