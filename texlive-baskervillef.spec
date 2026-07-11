%global tl_name baskervillef
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.052
Release:	%{tl_revision}.1
Summary:	Frys Baskerville look-alike, with math support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/baskervillef
License:	ofl lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/baskervillef.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/baskervillef.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
BaskervilleF is a fork from the Libre Baskerville fonts (Roman, Italic,
Bold only) released under the OFL by Paolo Impallari and Rodrigo
Fuenzalida. Their fonts are optimized for web usage, while BaskervilleF
is optimized for traditional TeX usage, normally destined for production
of pdf files. A bold italic style was added and mathematical support is
offered as an option to newtxmath.

