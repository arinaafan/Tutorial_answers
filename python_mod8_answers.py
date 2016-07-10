# Module 8
#
# 1. Create two lists, one for each species, containing the first gene identifiers of each line (the so called seed orthologs)
import re
specie1 = []
specie2 = []
my_file = open("Inparanoid_table.txt", 'r') 
header_line = my_file.readline()
for line in my_file.readlines():
    specie1.append(re.findall(r'ENSTGUP\w+', line)[0])
    specie2.append(re.findall(r'ENSGALP\w+', line)[0])
# 2. Create a dictionary “homologs” with the keys of the seed ortholog of species 1. Each entry should contain the seed ortholog of species 2 such as
homologs = {}
for i in range(len(specie1)):
  homologs[specie1[i]] = specie2[i] 
  
