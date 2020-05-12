# input sequence
seq = 'ATGCGACTACGATCGAGGGCCAT'
# base complementary pairing
baseDict = {'A':'T', 'G':'C', 'C':'G', 'T':'A'}
# initialize the variable of reverse complementary sequence
reCompleSeq = ''
# transfer to complementary sequence and reverse
for i in range(len(seq) - 1, -1, -1):
    compleBase = baseDict[seq[i]]
    reCompleSeq += compleBase

# print the sequence
print(reCompleSeq)