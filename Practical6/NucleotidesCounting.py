#import matplotlip.pyplot and use a simple "plt" to represent it
import matplotlib.pyplot as plt
#input
A = 6
C = 4
G = 5
T = 6
#found a dictionary
FrequencyOfNucleotides = {'A':6, 'C':4, 'G':5, 'T':6}
#set the argument of the plot
labels = FrequencyOfNucleotides.keys()
sizes = FrequencyOfNucleotides.values()
explode = (0, 0, 0, 0)
#draw the plot
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode, labels, autopct='%1.1f%%')
plt.show()