import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

data=np.linspace(1,10,10).reshape(2,5)

# print(data)

# sns.heatmap(data,vmax=10,vmin=1,cmap="magma",annot=True,annot_kws={"fontsize":15,"color":"r"})
# plt.savefig("6.change number details.png")

# sns.heatmap(data,vmax=10,vmin=1,cmap="magma",annot=True,annot_kws={"fontsize":15,"color":"r"},linewidths=3)
# plt.savefig("6.2nd change number details.png") #linewides paramiter differnciate b/W two box

# sns.heatmap(data,vmax=10,vmin=1,cmap="magma",annot=True,annot_kws={"fontsize":15,"color":"r"},linewidths=3,linecolor="g")
# plt.savefig("6.3rd change number details with color of lines.png") #linecolor change the differenciate areas color

# sns.heatmap(data,vmax=10,vmin=1,cmap="magma",annot=True,annot_kws={"fontsize":15,"color":"r"},linewidths=3,linecolor="g",cbar=False)
# plt.savefig("6.4 remove colour bar.png") #cbr is colourbar

# sns.heatmap(data,vmax=10,vmin=1,cmap="magma",annot=True,annot_kws={"fontsize":15,"color":"r"},linewidths=3,linecolor="g",cbar=False,xticklabels=False,yticklabels=False)
# plt.savefig("6.5 remove colour bar with lables.png")#xticklabels=False,yticklabels=False means remove x y  lables

sns.set(font_scale=4)
s=sns.heatmap(data,vmax=10,vmin=1,cmap="magma",annot=True,annot_kws={"fontsize":15,"color":"r"},linewidths=3,linecolor="g",cbar=False,xticklabels=False,yticklabels=False)
s.set(xlabel="AI",ylabel="ML")
plt.savefig("6.6 remove colour bar & add lables.png")