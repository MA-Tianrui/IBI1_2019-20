# input sequence
seq = 'ATGCGACTACGATCGAGGGCCAT'

# a dict about base complementary pairing
baseDict = {'A':'T', 'G':'C', 'C':'G', 'T':'A'}

# initialize the variable of reverse complementary sequence
reCompleSeq = ''

# transfer to complementary sequence and reverse
for i in range(len(seq) - 1, -1, -1):  # reverse order
    compleBase = baseDict[seq[i]]
    reCompleSeq += compleBase  # put the complementary base together

# print the sequence
print('Reverse complementary sequence:', reCompleSeq)