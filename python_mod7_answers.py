# Module 7
#
# 1. What is the fasta format?
''' FASTA format is a text-based format for representing either nucleotide sequences or peptide sequences, in which base pairs or amino acids are represented using single-letter codes. A sequence in FASTA format begins with a single-line description.'''
# 2. How to open a fasta file with Biopython?
# How to open a fasta file using the open command?
from Bio import SeqIO
inputSeqFile = open(filename, "rU")
SeqDict = SeqIO.to_dict(SeqIO.parse(inputSeqFile, "fasta"))
inputSeqFile.close()
# starting from biopython 1.45, for a single record only
record = SeqIO.read(open("single.fasta"), "fasta")
# 3. How can you open (very) large inputfiles?
# works only with sequential file formats (e.g. "fasta", "gb", "fastq"
records = SeqIO.index("Quality/example.fastq", "fastq")
# 4. How to convert a sequence in a string?
str(my_seq)
# 5. How to convert a string to a sequence (e.g. DNA, RNA)
from Bio.Alphabet import IUPAC
my_seq = Seq.Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC", IUPAC.unambiguous_dna)
# 6. Print the genetic code (standard code and mitochondrial code) using Biopython
from Bio.Data import CodonTable
print CodonTable.unambiguous_dna_by_name["Standard"]
print CodonTable.unambiguous_dna_by_name["Vertebrate Mitochondrial"]
# 7. Create following DNA sequence: AAAAGAGAGATGTCCCTACCCTTT  
my_seq = Seq.Seq("AAAAGAGAGATGTCCCTACCCTTT", IUPAC.unambiguous_dna)
# 1) Find the motif “TACC”
my_seq.find("TACC") # ==> 16
# 2) Produce the complement
my_seq.complement() # ==> Seq('TTTTCTCTCTACAGGGATGGGAAA', IUPACUnambiguousDNA())
# 3) Produce the reverse complement
my_seq.reverse_complement() # ==> Seq('AAAGGGTAGGGACATCTCTCTTTT', IUPACUnambiguousDNA())
# 4) Transcribe the sequence
my_seq.transcribe() # ==> Seq('AAAAGAGAGAUGUCCCUACCCUUU', IUPACUnambiguousRNA())
# 5) Transcribe the reverse complement
my_seq.reverse_complement().transcribe() # ==> Seq('AAAGGGUAGGGACAUCUCUCUUUU', IUPACUnambiguousRNA())
# 6) Translate the sequence using the Standard code
my_seq.translate(table="Standard") # ==> Seq('KREMSLPF', IUPACProtein())
# 8.  What is the difference between Seq and MutableSeq?
# >> Seq objects are immutable and MutableSeq can be changes. MutableSeq obj. con not be used as dict. keys
