# Module 10
#
# 1. Run another python script from within python
import os
os.system("python /home/arina/other_script.py")
# 2. Create a new file with the “>” pipe command
os.system("python /home/arina/other_script.py > logfile")
# 3. Run the program “codeml” (in the subfolder paml). It requires an inputfile, 
# which you can copy or explicitly define as argument
from Bio.Phylo.PAML import codeml
cml = codeml.Codeml(alignment = "/home/arina/codeml/alignment.phylip", tree = "/home/arina/codeml/species.tree", out_file = "results.out", working_dir = "/home/arina/codeml/")
results = cml.run()
''' >> Now here I stuck! :( I am getting an error - OSError: [Errno 2] No such file or directory
 and when trying to indicate path to codeml explicitly 
 results = cml.run(command="/usr/local/lib/python2.7/dist-packages/Bio/Phylo/PAML/codeml.py")
 getting error - OSError: [Errno 13] Permission denied '''

# 4. Obtain the likelihood of the output file of codeml (file codeml_output, 
# it's indicated on the line with lnL = ) using a script that prints the likelihood
# >> I suppose, it should be something like that:
results = codeml.read("results.out")
print(results.get("lnL max"))
