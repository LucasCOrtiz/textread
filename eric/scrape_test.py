#!/home/lucas/anaconda3/envs/py3e/bin/python
import nltk
from nltk.tag.stanford import StanfordNERTagger
st = StanfordNERTagger('stanford-ner/all.3class.distsim.crf.ser.gz', 'stanford-ner/stanford-ner.jar')

infile = "alice.txt"
outfile = "cleaned_file.txt"
print('Start clean up text file')
delete_list = ["Alice"] # The words to be removed
fin = open(infile)
fout = open(outfile, "w+")
for line in fin:
    for word in delete_list:
        line = line.replace(word, "")
    fout.write(line)
fin.close()
fout.close()
print('Finishing clean up text file')
