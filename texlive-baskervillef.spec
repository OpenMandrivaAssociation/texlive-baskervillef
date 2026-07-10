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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
BaskervilleF is a fork from the Libre Baskerville fonts (Roman, Italic,
Bold only) released under the OFL by Paolo Impallari and Rodrigo
Fuenzalida. Their fonts are optimized for web usage, while BaskervilleF
is optimized for traditional TeX usage, normally destined for production
of pdf files. A bold italic style was added and mathematical support is
offered as an option to newtxmath.

%prep
%setup -q -c -a1
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
%dir %{_datadir}/texmf-dist/fonts
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/fonts
%dir %{_datadir}/texmf-dist/fonts/enc
%dir %{_datadir}/texmf-dist/fonts/map
%dir %{_datadir}/texmf-dist/fonts/opentype
%dir %{_datadir}/texmf-dist/fonts/tfm
%dir %{_datadir}/texmf-dist/fonts/type1
%dir %{_datadir}/texmf-dist/fonts/vf
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/fonts/baskervillef
%dir %{_datadir}/texmf-dist/fonts/enc/dvips
%dir %{_datadir}/texmf-dist/fonts/map/dvips
%dir %{_datadir}/texmf-dist/fonts/opentype/public
%dir %{_datadir}/texmf-dist/fonts/tfm/public
%dir %{_datadir}/texmf-dist/fonts/type1/public
%dir %{_datadir}/texmf-dist/fonts/vf/public
%dir %{_datadir}/texmf-dist/tex/latex/baskervillef
%dir %{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef
%dir %{_datadir}/texmf-dist/fonts/map/dvips/baskervillef
%dir %{_datadir}/texmf-dist/fonts/opentype/public/baskervillef
%dir %{_datadir}/texmf-dist/fonts/tfm/public/baskervillef
%dir %{_datadir}/texmf-dist/fonts/type1/public/baskervillef
%dir %{_datadir}/texmf-dist/fonts/vf/public/baskervillef
%doc %{_datadir}/texmf-dist/doc/fonts/baskervillef/FONTLOG.txt
%doc %{_datadir}/texmf-dist/doc/fonts/baskervillef/OFL-FAQ.txt
%doc %{_datadir}/texmf-dist/doc/fonts/baskervillef/OFL.txt
%doc %{_datadir}/texmf-dist/doc/fonts/baskervillef/README
%doc %{_datadir}/texmf-dist/doc/fonts/baskervillef/baskervillef-doc.pdf
%doc %{_datadir}/texmf-dist/doc/fonts/baskervillef/baskervillef-doc.tex
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_23ismr.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_2hmbf5.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_2j2bbt.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_2vxxim.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_336dgv.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_3a6nlu.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_3kjwvw.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_4hfcgk.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_523v7l.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_532cq4.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_5cwn7d.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_5k66dt.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_5oqvu4.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_6vkpq5.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_734fzj.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_73mseb.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_7cypa5.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_7qcgfh.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_a3asoq.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_a73a6q.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_aqsbza.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_arki3d.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_art6xf.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_b5bk2y.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_bnjopg.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_cjo72v.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_ck2hfy.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_cvjygd.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_e3xw3x.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_e5ewsu.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_etzx2k.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_fcs4fj.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_gliky3.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_gmq6ah.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_hwnpjr.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_hykkzd.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_ihgygy.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_iy3fha.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_jjbdnj.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_kodzea.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_lfhy4n.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_lfjjhs.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_lh5uiy.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_lkeymy.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_m7qm6t.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_mby7uf.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_ogu2yp.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_oxcsv2.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_pxbj3a.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_qiwnw4.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_qvggep.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_rqjco3.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_rtk6yp.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_skajg2.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_srcuqk.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_t3ys54.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_th2k46.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_to6jjw.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_twn2qn.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_typa7y.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_ueebfa.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_uf5aa7.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_uf7ozb.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_ugitcp.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_uqoays.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_uutbpy.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_ve4agh.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_vydigt.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_w4i4io.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_w54rd4.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_wbekxi.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_wn2rfu.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_wxljbs.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_wybx5h.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_wyngyv.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_x7qzb2.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_xpcegd.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_y3x75k.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_y7xbvf.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_ymdv6d.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_zkzy6d.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_zpc5ms.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_zvejcx.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervillef/zba_zygn7r.enc
%{_datadir}/texmf-dist/fonts/map/dvips/baskervillef/BaskervilleF.map
%{_datadir}/texmf-dist/fonts/opentype/public/baskervillef/BaskervilleF-Bold.otf
%{_datadir}/texmf-dist/fonts/opentype/public/baskervillef/BaskervilleF-BoldItalic.otf
%{_datadir}/texmf-dist/fonts/opentype/public/baskervillef/BaskervilleF-Italic.otf
%{_datadir}/texmf-dist/fonts/opentype/public/baskervillef/BaskervilleF-Regular.otf
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Bold-lf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Bold-lf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Bold-lf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Bold-lf-sc-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Bold-lf-sc-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Bold-lf-sc-ot1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Bold-lf-sc-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Bold-lf-sc-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Bold-lf-sc-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Bold-lf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Bold-lf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Bold-lf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Bold-lf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Bold-osf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Bold-osf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Bold-osf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Bold-osf-sc-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Bold-osf-sc-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Bold-osf-sc-ot1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Bold-osf-sc-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Bold-osf-sc-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Bold-osf-sc-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Bold-osf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Bold-osf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Bold-osf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Bold-osf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Bold-osf.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Bold-sup-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Bold-sup-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Bold-sup-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Bold-sup-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Bold-sup-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tlf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tlf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tlf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tlf-ot1G.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tlf-sc-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tlf-sc-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tlf-sc-ot1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tlf-sc-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tlf-sc-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tlf-sc-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tlf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tlf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tlf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tlf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tosf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tosf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tosf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tosf-sc-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tosf-sc-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tosf-sc-ot1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tosf-sc-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tosf-sc-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tosf-sc-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tosf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tosf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tosf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tosf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Bold.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-alph.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-lf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-lf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-lf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-lf-sc-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-lf-sc-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-lf-sc-ot1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-lf-sc-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-lf-sc-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-lf-sc-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-lf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-lf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-lf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-lf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-osf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-osf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-osf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-osf-sc-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-osf-sc-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-osf-sc-ot1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-osf-sc-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-osf-sc-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-osf-sc-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-osf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-osf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-osf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-osf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-osf.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-sup-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-sup-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-sup-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-sup-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-sup-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tlf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tlf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tlf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tlf-ot1G.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tlf-sc-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tlf-sc-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tlf-sc-ot1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tlf-sc-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tlf-sc-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tlf-sc-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tlf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tlf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tlf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tlf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tosf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tosf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tosf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tosf-sc-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tosf-sc-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tosf-sc-ot1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tosf-sc-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tosf-sc-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tosf-sc-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tosf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tosf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tosf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tosf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-alph.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-dnom-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-dnom-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-dnom-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-dnom-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-dnom-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-lf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-lf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-lf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-lf-sc-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-lf-sc-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-lf-sc-ot1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-lf-sc-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-lf-sc-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-lf-sc-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-lf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-lf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-lf-th-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-lf-th-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-lf-th-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-lf-th-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-lf-th-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-lf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-lf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-osf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-osf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-osf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-osf-sc-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-osf-sc-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-osf-sc-ot1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-osf-sc-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-osf-sc-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-osf-sc-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-osf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-osf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-osf-th-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-osf-th-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-osf-th-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-osf-th-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-osf-th-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-osf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-osf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-osf.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-sup-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-sup-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-sup-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-sup-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-sup-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tlf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tlf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tlf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tlf-ot1G.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tlf-sc-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tlf-sc-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tlf-sc-ot1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tlf-sc-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tlf-sc-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tlf-sc-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tlf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tlf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tlf-th-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tlf-th-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tlf-th-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tlf-th-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tlf-th-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tlf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tlf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tosf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tosf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tosf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tosf-sc-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tosf-sc-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tosf-sc-ot1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tosf-sc-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tosf-sc-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tosf-sc-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tosf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tosf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tosf-th-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tosf-th-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tosf-th-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tosf-th-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tosf-th-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tosf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tosf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Italic.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-dnom-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-dnom-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-dnom-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-dnom-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-dnom-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-lf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-lf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-lf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-lf-sc-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-lf-sc-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-lf-sc-ot1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-lf-sc-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-lf-sc-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-lf-sc-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-lf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-lf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-lf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-lf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-osf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-osf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-osf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-osf-sc-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-osf-sc-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-osf-sc-ot1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-osf-sc-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-osf-sc-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-osf-sc-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-osf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-osf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-osf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-osf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-osf.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-sup-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-sup-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-sup-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-sup-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-sup-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tlf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tlf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tlf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tlf-ot1G.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tlf-sc-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tlf-sc-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tlf-sc-ot1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tlf-sc-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tlf-sc-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tlf-sc-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tlf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tlf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tlf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tlf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tosf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tosf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tosf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tosf-sc-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tosf-sc-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tosf-sc-ot1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tosf-sc-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tosf-sc-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tosf-sc-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tosf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tosf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tosf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tosf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/BaskervilleF-Regular.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/zbabmi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervillef/zbami.tfm
%{_datadir}/texmf-dist/fonts/type1/public/baskervillef/BaskervilleF-Bold.pfb
%{_datadir}/texmf-dist/fonts/type1/public/baskervillef/BaskervilleF-BoldItalic.pfb
%{_datadir}/texmf-dist/fonts/type1/public/baskervillef/BaskervilleF-Italic.pfb
%{_datadir}/texmf-dist/fonts/type1/public/baskervillef/BaskervilleF-Regular.pfb
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Bold-lf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Bold-lf-sc-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Bold-lf-sc-ot1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Bold-lf-sc-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Bold-lf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Bold-lf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Bold-osf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Bold-osf-sc-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Bold-osf-sc-ot1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Bold-osf-sc-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Bold-osf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Bold-osf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Bold-sup-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Bold-sup-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Bold-tlf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Bold-tlf-ot1G.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Bold-tlf-sc-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Bold-tlf-sc-ot1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Bold-tlf-sc-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Bold-tlf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Bold-tlf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Bold-tosf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Bold-tosf-sc-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Bold-tosf-sc-ot1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Bold-tosf-sc-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Bold-tosf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Bold-tosf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-BoldItalic-lf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-BoldItalic-lf-sc-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-BoldItalic-lf-sc-ot1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-BoldItalic-lf-sc-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-BoldItalic-lf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-BoldItalic-lf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-BoldItalic-osf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-BoldItalic-osf-sc-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-BoldItalic-osf-sc-ot1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-BoldItalic-osf-sc-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-BoldItalic-osf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-BoldItalic-osf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-BoldItalic-sup-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-BoldItalic-sup-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-BoldItalic-tlf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-BoldItalic-tlf-ot1G.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-BoldItalic-tlf-sc-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-BoldItalic-tlf-sc-ot1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-BoldItalic-tlf-sc-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-BoldItalic-tlf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-BoldItalic-tlf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-BoldItalic-tosf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-BoldItalic-tosf-sc-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-BoldItalic-tosf-sc-ot1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-BoldItalic-tosf-sc-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-BoldItalic-tosf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-BoldItalic-tosf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Italic-dnom-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Italic-dnom-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Italic-lf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Italic-lf-sc-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Italic-lf-sc-ot1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Italic-lf-sc-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Italic-lf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Italic-lf-th-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Italic-lf-th-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Italic-lf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Italic-osf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Italic-osf-sc-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Italic-osf-sc-ot1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Italic-osf-sc-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Italic-osf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Italic-osf-th-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Italic-osf-th-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Italic-osf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Italic-sup-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Italic-sup-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Italic-tlf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Italic-tlf-ot1G.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Italic-tlf-sc-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Italic-tlf-sc-ot1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Italic-tlf-sc-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Italic-tlf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Italic-tlf-th-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Italic-tlf-th-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Italic-tlf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Italic-tosf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Italic-tosf-sc-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Italic-tosf-sc-ot1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Italic-tosf-sc-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Italic-tosf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Italic-tosf-th-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Italic-tosf-th-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Italic-tosf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Regular-dnom-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Regular-dnom-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Regular-lf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Regular-lf-sc-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Regular-lf-sc-ot1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Regular-lf-sc-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Regular-lf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Regular-lf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Regular-osf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Regular-osf-sc-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Regular-osf-sc-ot1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Regular-osf-sc-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Regular-osf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Regular-osf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Regular-sup-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Regular-sup-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Regular-tlf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Regular-tlf-ot1G.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Regular-tlf-sc-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Regular-tlf-sc-ot1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Regular-tlf-sc-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Regular-tlf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Regular-tlf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Regular-tosf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Regular-tosf-sc-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Regular-tosf-sc-ot1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Regular-tosf-sc-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Regular-tosf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/BaskervilleF-Regular-tosf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/zbabmi.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervillef/zbami.vf
%{_datadir}/texmf-dist/tex/latex/baskervillef/LY1BaskervilleF-Dnom.fd
%{_datadir}/texmf-dist/tex/latex/baskervillef/LY1BaskervilleF-LF.fd
%{_datadir}/texmf-dist/tex/latex/baskervillef/LY1BaskervilleF-OsF.fd
%{_datadir}/texmf-dist/tex/latex/baskervillef/LY1BaskervilleF-Sup.fd
%{_datadir}/texmf-dist/tex/latex/baskervillef/LY1BaskervilleF-TLF.fd
%{_datadir}/texmf-dist/tex/latex/baskervillef/LY1BaskervilleF-TOsF.fd
%{_datadir}/texmf-dist/tex/latex/baskervillef/OT1BaskervilleF-Dnom.fd
%{_datadir}/texmf-dist/tex/latex/baskervillef/OT1BaskervilleF-LF.fd
%{_datadir}/texmf-dist/tex/latex/baskervillef/OT1BaskervilleF-OsF.fd
%{_datadir}/texmf-dist/tex/latex/baskervillef/OT1BaskervilleF-Sup.fd
%{_datadir}/texmf-dist/tex/latex/baskervillef/OT1BaskervilleF-TLF.fd
%{_datadir}/texmf-dist/tex/latex/baskervillef/OT1BaskervilleF-TOsF.fd
%{_datadir}/texmf-dist/tex/latex/baskervillef/T1BaskervilleF-Dnom.fd
%{_datadir}/texmf-dist/tex/latex/baskervillef/T1BaskervilleF-LF.fd
%{_datadir}/texmf-dist/tex/latex/baskervillef/T1BaskervilleF-OsF.fd
%{_datadir}/texmf-dist/tex/latex/baskervillef/T1BaskervilleF-Sup.fd
%{_datadir}/texmf-dist/tex/latex/baskervillef/T1BaskervilleF-TLF.fd
%{_datadir}/texmf-dist/tex/latex/baskervillef/T1BaskervilleF-TOsF.fd
%{_datadir}/texmf-dist/tex/latex/baskervillef/TS1BaskervilleF-LF.fd
%{_datadir}/texmf-dist/tex/latex/baskervillef/TS1BaskervilleF-OsF.fd
%{_datadir}/texmf-dist/tex/latex/baskervillef/TS1BaskervilleF-TLF.fd
%{_datadir}/texmf-dist/tex/latex/baskervillef/TS1BaskervilleF-TOsF.fd
%{_datadir}/texmf-dist/tex/latex/baskervillef/baskervillef.fontspec
%{_datadir}/texmf-dist/tex/latex/baskervillef/baskervillef.sty
%{_datadir}/texmf-dist/tex/latex/baskervillef/ly1minbaskervillef.fd
%{_datadir}/texmf-dist/tex/latex/baskervillef/omlzbami.fd
%{_datadir}/texmf-dist/tex/latex/baskervillef/ot1minbaskervillef.fd
%{_datadir}/texmf-dist/tex/latex/baskervillef/t1minbaskervillef.fd
