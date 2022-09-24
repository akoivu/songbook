system("perl -p -e 's/\Q\\\Econtentsline \Q{subsection}{\E//s' output.sng | sort | perl -p -e 's/^/\Q\\\Econtentsline \Q{subsection}{\E/g' > tmp.sng");
system("mv tmp.sng output.sng");
system("cat output.sng");