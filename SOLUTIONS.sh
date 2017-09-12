### QUESTION 1 ###
sed 's/[().?!/:;,|&-]/ /g ; s/'\''/ /g ; s/\[/ /g ; s/\]/ /g'  shakespeare.txt | tr "[A-Z]" "[a-z]" | tr "\t" " " | sed 's/  */ /g' | tr ' ' '\n' | sed '/^$/d' | sort | uniq -c | sort -n -r | head

### QUESTION 2 ###
tr "[A-Z]" "[a-z]" < dict > dict1
sed 's/[().?!/:;,|&-]/ /g ; s/'\''/ /g ; s/\[/ /g ; s/\]/ /g'  shakespeare.txt | tr "[A-Z]" "[a-z]" | tr "\t" " " | sed 's/  */ /g' | tr ' ' '\n' | sed '/^$/d' | sort | uniq> shakespeare1 #hey bitch
comm -23 shakespeare1 dict1 > comparison
wc -l < comparison

### MAKE YOUR OWN 1 ###
sed /^$/d password | sed s/HE/R/ |sed s/LUNE/6/g | sed s/6/X/ | sed '8i\
G'| tr -d '\n' | sed s/6489// |sed 's/[a-z]//g'

### MAKE YOUR OWN 2 ###

awk -F":" '$0 !~ /^#/ { print $3"\t"$4"\t"$1 }' passwd | sort -n -k 1,2
