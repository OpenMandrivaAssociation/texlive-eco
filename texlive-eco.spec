# revision 15878
# category Package
# catalog-ctan /fonts/eco
# catalog-date 2007-09-25 20:45:33 +0200
# catalog-license gpl
# catalog-version 1.3
Name:		texlive-eco
Version:	1.3
Release:	2
Summary:	Oldstyle numerals using EC fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/eco
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eco.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eco.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eco.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A set of font metric files and virtual fonts for using the EC
fonts with oldstyle numerals. These files can only be used
together with the standard ec fonts. The style file eco.sty is
sufficient to use the eco fonts but if you intend to use other
font families as well, e.g., PostScript fonts, try altfont.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/tfm/public/eco/ecobi0500.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecobi0600.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecobi0700.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecobi0800.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecobi0900.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecobi1000.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecobi1095.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecobi1200.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecobi1440.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecobi1728.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecobi2074.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecobi2488.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecobi2986.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecobi3583.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecobl0500.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecobl0600.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecobl0700.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecobl0800.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecobl0900.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecobl1000.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecobl1095.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecobl1200.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecobl1440.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecobl1728.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecobl2074.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecobl2488.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecobl2986.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecobl3583.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecobx0500.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecobx0600.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecobx0700.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecobx0800.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecobx0900.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecobx1000.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecobx1095.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecobx1200.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecobx1440.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecobx1728.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecobx2074.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecobx2488.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecobx2986.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecobx3583.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecodh0500.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecodh0600.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecodh0700.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecodh0800.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecodh0900.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecodh1000.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecodh1095.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecodh1200.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecodh1440.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecodh1728.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecodh2074.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecodh2488.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecodh2986.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecodh3583.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoit0600.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoit0700.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoit0800.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoit0900.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoit1000.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoit1095.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoit1200.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoit1440.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoit1728.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoit2074.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoit2488.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoit2986.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoit3583.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecorb0500.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecorb0600.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecorb0700.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecorb0800.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecorb0900.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecorb1000.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecorb1095.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecorb1200.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecorb1440.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecorb1728.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecorb2074.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecorb2488.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecorb2986.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecorb3583.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecorm0500.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecorm0600.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecorm0700.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecorm0800.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecorm0900.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecorm1000.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecorm1095.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecorm1200.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecorm1440.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecorm1728.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecorm2074.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecorm2488.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecorm2986.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecorm3583.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecosi0500.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecosi0600.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecosi0700.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecosi0800.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecosi0900.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecosi1000.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecosi1095.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecosi1200.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecosi1440.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecosi1728.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecosi2074.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecosi2488.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecosi2986.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecosi3583.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecosl0500.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecosl0600.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecosl0700.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecosl0800.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecosl0900.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecosl1000.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecosl1095.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecosl1200.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecosl1440.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecosl1728.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecosl2074.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecosl2488.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecosl2986.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecosl3583.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoso0500.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoso0600.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoso0700.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoso0800.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoso0900.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoso1000.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoso1095.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoso1200.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoso1440.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoso1728.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoso2074.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoso2488.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoso2986.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoso3583.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoss0500.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoss0600.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoss0700.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoss0800.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoss0900.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoss1000.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoss1095.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoss1200.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoss1440.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoss1728.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoss2074.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoss2488.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoss2986.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoss3583.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecost0600.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecost0700.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecost0800.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecost0900.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecost1000.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecost1095.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecost1200.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecost1440.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecost1728.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecost2074.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecost2488.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecost2986.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecost3583.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecosx0500.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecosx0600.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecosx0700.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecosx0800.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecosx0900.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecosx1000.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecosx1095.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecosx1200.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecosx1440.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecosx1728.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecosx2074.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecosx2488.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecosx2986.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecosx3583.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoti0500.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoti0600.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoti0700.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoti0800.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoti0900.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoti1000.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoti1095.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoti1200.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoti1440.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoti1728.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoti2074.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoti2488.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoti2986.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoti3583.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecott0600.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecott0700.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecott0800.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecott0900.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecott1000.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecott1095.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecott1200.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecott1440.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecott1728.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecott2074.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecott2488.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecott2986.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecott3583.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoui0500.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoui0600.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoui0700.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoui0800.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoui0900.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoui1000.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoui1095.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoui1200.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoui1440.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoui1728.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoui2074.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoui2488.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoui2986.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecoui3583.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecovi0600.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecovi0700.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecovi0800.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecovi0900.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecovi1000.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecovi1095.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecovi1200.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecovi1440.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecovi1728.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecovi2074.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecovi2488.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecovi2986.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecovi3583.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecovt0600.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecovt0700.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecovt0800.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecovt0900.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecovt1000.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecovt1095.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecovt1200.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecovt1440.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecovt1728.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecovt2074.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecovt2488.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecovt2986.tfm
%{_texmfdistdir}/fonts/tfm/public/eco/ecovt3583.tfm
%{_texmfdistdir}/fonts/vf/public/eco/ecobi0500.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecobi0600.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecobi0700.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecobi0800.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecobi0900.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecobi1000.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecobi1095.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecobi1200.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecobi1440.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecobi1728.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecobi2074.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecobi2488.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecobi2986.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecobi3583.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecobl0500.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecobl0600.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecobl0700.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecobl0800.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecobl0900.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecobl1000.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecobl1095.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecobl1200.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecobl1440.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecobl1728.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecobl2074.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecobl2488.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecobl2986.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecobl3583.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecobx0500.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecobx0600.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecobx0700.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecobx0800.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecobx0900.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecobx1000.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecobx1095.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecobx1200.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecobx1440.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecobx1728.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecobx2074.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecobx2488.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecobx2986.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecobx3583.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecodh0500.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecodh0600.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecodh0700.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecodh0800.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecodh0900.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecodh1000.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecodh1095.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecodh1200.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecodh1440.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecodh1728.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecodh2074.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecodh2488.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecodh2986.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecodh3583.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoit0600.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoit0700.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoit0800.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoit0900.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoit1000.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoit1095.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoit1200.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoit1440.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoit1728.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoit2074.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoit2488.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoit2986.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoit3583.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecorb0500.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecorb0600.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecorb0700.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecorb0800.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecorb0900.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecorb1000.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecorb1095.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecorb1200.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecorb1440.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecorb1728.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecorb2074.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecorb2488.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecorb2986.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecorb3583.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecorm0500.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecorm0600.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecorm0700.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecorm0800.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecorm0900.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecorm1000.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecorm1095.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecorm1200.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecorm1440.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecorm1728.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecorm2074.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecorm2488.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecorm2986.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecorm3583.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecosi0500.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecosi0600.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecosi0700.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecosi0800.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecosi0900.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecosi1000.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecosi1095.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecosi1200.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecosi1440.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecosi1728.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecosi2074.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecosi2488.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecosi2986.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecosi3583.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecosl0500.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecosl0600.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecosl0700.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecosl0800.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecosl0900.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecosl1000.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecosl1095.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecosl1200.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecosl1440.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecosl1728.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecosl2074.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecosl2488.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecosl2986.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecosl3583.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoso0500.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoso0600.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoso0700.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoso0800.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoso0900.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoso1000.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoso1095.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoso1200.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoso1440.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoso1728.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoso2074.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoso2488.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoso2986.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoso3583.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoss0500.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoss0600.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoss0700.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoss0800.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoss0900.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoss1000.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoss1095.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoss1200.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoss1440.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoss1728.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoss2074.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoss2488.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoss2986.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoss3583.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecost0600.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecost0700.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecost0800.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecost0900.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecost1000.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecost1095.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecost1200.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecost1440.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecost1728.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecost2074.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecost2488.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecost2986.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecost3583.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecosx0500.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecosx0600.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecosx0700.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecosx0800.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecosx0900.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecosx1000.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecosx1095.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecosx1200.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecosx1440.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecosx1728.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecosx2074.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecosx2488.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecosx2986.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecosx3583.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoti0500.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoti0600.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoti0700.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoti0800.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoti0900.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoti1000.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoti1095.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoti1200.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoti1440.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoti1728.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoti2074.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoti2488.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoti2986.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoti3583.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecott0600.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecott0700.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecott0800.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecott0900.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecott1000.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecott1095.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecott1200.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecott1440.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecott1728.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecott2074.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecott2488.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecott2986.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecott3583.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoui0500.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoui0600.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoui0700.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoui0800.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoui0900.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoui1000.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoui1095.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoui1200.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoui1440.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoui1728.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoui2074.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoui2488.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoui2986.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecoui3583.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecovi0600.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecovi0700.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecovi0800.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecovi0900.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecovi1000.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecovi1095.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecovi1200.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecovi1440.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecovi1728.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecovi2074.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecovi2488.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecovi2986.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecovi3583.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecovt0600.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecovt0700.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecovt0800.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecovt0900.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecovt1000.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecovt1095.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecovt1200.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecovt1440.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecovt1728.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecovt2074.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecovt2488.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecovt2986.vf
%{_texmfdistdir}/fonts/vf/public/eco/ecovt3583.vf
%{_texmfdistdir}/tex/latex/eco/T1cmodh.fd
%{_texmfdistdir}/tex/latex/eco/T1cmor.fd
%{_texmfdistdir}/tex/latex/eco/T1cmoss.fd
%{_texmfdistdir}/tex/latex/eco/T1cmott.fd
%{_texmfdistdir}/tex/latex/eco/T1cmovt.fd
%{_texmfdistdir}/tex/latex/eco/eco.sty
%doc %{_texmfdistdir}/doc/fonts/eco/CHANGES
%doc %{_texmfdistdir}/doc/fonts/eco/COPYING
%doc %{_texmfdistdir}/doc/fonts/eco/INSTALL
%doc %{_texmfdistdir}/doc/fonts/eco/README
%doc %{_texmfdistdir}/doc/fonts/eco/VERSION
#- source
%doc %{_texmfdistdir}/source/fonts/eco/TS1.etx
%doc %{_texmfdistdir}/source/fonts/eco/create.sh
%doc %{_texmfdistdir}/source/fonts/eco/dostretch.mtx
%doc %{_texmfdistdir}/source/fonts/eco/ecodh.tex
%doc %{_texmfdistdir}/source/fonts/eco/ecor.tex
%doc %{_texmfdistdir}/source/fonts/eco/ecori.tex
%doc %{_texmfdistdir}/source/fonts/eco/ecoss.tex
%doc %{_texmfdistdir}/source/fonts/eco/ecott.tex
%doc %{_texmfdistdir}/source/fonts/eco/ecovt.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.3-2
+ Revision: 751320
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.3-1
+ Revision: 718302
- texlive-eco
- texlive-eco
- texlive-eco
- texlive-eco

