%define _dict_dir %{_datadir}/dict/

Summary:	A dictionary of English words for the /usr/dict directory
Name:		words
Version:	3.0
Release:	%mkrel 5
License:	Public Domain
Group:		Text tools
URL:		http://www.dcs.shef.ac.uk/research/ilash/Moby/
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
dos2unix --auto *; chmod a+r *
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
