#input
gene_lengths=[9410,3944141,4442,105338,19149,76779,126550,36296,842,15981]
#sort the list of gene lengths
gene_lengths_modified=sorted(gene_lengths)
#del the minimal gene length
del gene_lengths_modified[0]
#del the maximal gene length
del gene_lengths_modified[len(gene_lengths_modified)-1]
print(gene_lengths_modified)

#import
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon


fig, axs = plt.subplots()
axs.boxplot(gene_lengths_modified)
axs.set_title('Gene lengths')
axs.set_ylabel('gene length')
plt.show()