import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


data=sns.load_dataset("penguins")
print(data)

sns.scatterplot(x='bill_length_mm',y='bill_depth_mm',data=data,hue='sex')
plt.savefig("4.1st.png")