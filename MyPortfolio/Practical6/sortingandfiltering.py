# import
import matplotlib.pyplot as plt
import numpy as np

# input
gene_lengths=[9410,3944141,4442,105338,19149,76779,126550,36296,842,15981]
# sort the list of gene lengths
gene_lengths_modified=sorted(gene_lengths)
# del the minimal gene length
del gene_lengths_modified[0]
# del the maximal gene length
del gene_lengths_modified[len(gene_lengths_modified)-1]
# print the list of gene lengths
print('Sorted gene lengths (from short to long):', gene_lengths_modified)


# change the type from list to array
gene_lengths_modified_arr = np.array(gene_lengths_modified)

# draw the box plot
plt.boxplot(gene_lengths_modified_arr,
            patch_artist = True)
# name title and label
plt.title('Gene lengths')
plt.ylabel('number')
plt.show()