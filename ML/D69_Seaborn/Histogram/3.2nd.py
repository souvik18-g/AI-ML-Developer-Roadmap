import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


data=sns.load_dataset("penguins")
print(data)

sns.displot(x='bill_depth_mm',data=data,bins=[10,12,14,16,18,20,22,24,26],kde=True,rug=True,color="g")
#bins is the evry column range ,       #kdg true mens the curve,    #rug true means in bottom the values line 
plt.savefig('3.2nd.png')