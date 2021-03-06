import re

# open and read the original file
allGene = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
# creat a new file and prepare to write data into it
mitoGene = open('mito_gene.fa', 'x')

# initial setting of some variable used in loop
geneName = ''
geneSeq = ''
geneLength= 0



for line in allGene:
    if line.startswith('>'):  # find the beginning of a gene
# write the data into the new file when the length > 0 (mean that the former gene is what we need)
        if geneLength > 0:
            seqName = '>' + geneName[0] + ' ' + str(geneLength) + '\n'  # combine gene name and length
            mitoGene.write(seqName)
            mitoGene.write(geneSeq + '\n')
            geneSeq = ''  # reset the seq and length
            geneLength = 0
# find Mito gene
        if re.search(r':Mito:', line):
# extract the gene name
            geneName = re.findall(r' gene:(.+?) ', line)
            findIt = True
        else:
            findIt = False
# get the sequence and calculate the length of the gene we need
    elif findIt:
        geneSeq += line[:-1]  # extract gene seq
        geneLength += len(line) - 1  # calculate gene length



# close the files
allGene.close()
mitoGene.close()



# show the mito_gene.fa
mitoGene_test = open('mito_gene.fa')
for line in mitoGene_test:
    print(line[:-1])

mitoGene_test.close()