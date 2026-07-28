import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

data=np.linspace(1,10,10).reshape(2,5)

# print(data)
arr=np.array([["a0","a1","a2","a3","a4"],
             ["b0","b1","b2","b3","b4"]])
sns.heatmap(data,vmax=10,vmin=1,cmap="magma",annot=arr,fmt="")#fmt=format of array value here string so "",for other datatype they have sepate fmt
plt.savefig("5.1st change value .png")
# plt.show()
