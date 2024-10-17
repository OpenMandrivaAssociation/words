%define _dict_dir %{_datadir}/dict/

Summary:	A dictionary of English words for the /usr/dict directory
Name:		words
Version:	3.0
Release:	21
License:	Public Domain
Group:		Text tools
URL:		https://www.dcs.shef.ac.uk/research/ilash/Moby/
Source:		http://www.dcs.shef.ac.uk/research/ilash/Moby/mwords.tar.bz2
BuildArch:	noarch
BuildRequires:	dos2unix
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
The words file is a dictionary of English words for the
/usr/share/dict directory. Some programs use this database of
words to check spelling. Password checkers use it to look for bad
passwords.

%prep
%setup -q -c

%build
cd mwords
dos2unix *; chmod a+r *
cat [1-9]*.??? | egrep  "^[[:alnum:]'&!,./-]+$" | sort --ignore-case --dictionary-order | uniq > moby

cat <<EOF >license.txt
On June 1, 1996 Grady Ward announced that the fruits of
the Moby project were being placed in the public domain:

The Moby lexicon project is complete and has
been place into the public domain. Use, sell,
rework, excerpt and use in any way on any platform.
    
Placing this material on internal or public servers is
also encouraged. The compiler is not aware of any
export restrictions so freely distribute world-wide.
    
You can verify the public domain status by contacting
   
Grady Ward
3449 Martha Ct.
Arcata, CA  95521-4884
    
daedal@myrealbox.com
EOF

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_datadir}/dict
install -m644 mwords/moby %{buildroot}%{_datadir}/dict/linux.words
ln -sf linux.words %{buildroot}%{_datadir}/dict/words

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc mwords/readme.txt mwords/license.txt
%{_dict_dir}linux.words
%{_dict_dir}words


%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 3.0-9mdv2011.0
+ Revision: 670814
- mass rebuild

* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 3.0-8mdv2011.0
+ Revision: 608172
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 3.0-7mdv2010.1
+ Revision: 524355
- rebuilt for 2010.1

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 3.0-6mdv2009.1
+ Revision: 351433
- rebuild

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 3.0-5mdv2009.0
+ Revision: 265778
- rebuild early 2009.0 package (before pixel changes)

* Wed Apr 30 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 3.0-4mdv2009.0
+ Revision: 199351
- spec file clean

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 3.0-3mdv2008.1
+ Revision: 179679
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Jan 10 2007 Warly <warly@mandriva.com> 3.0-2mdv2007.0
+ Revision: 106995
- sort dictionnary with --dictionnary-order to fix bug 13611
- Import words

* Mon Dec 06 2004 Warly <warly@mandrakesoft.com> 3.0-1mdk
- update in the same way Adrian Havill did for fedora
- replace word list with much better Moby Project words list
- revise %%description; ispell/aspell no longer uses words

* Fri Feb 06 2004 David Baudens <baudens@mandrakesoft.com> 2-20mdk
- Rebuild

