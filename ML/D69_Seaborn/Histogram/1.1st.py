import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


data=sns.load_dataset("penguins")
print(data)

sns.displot(x="bill_length_mm",data=data)
plt.savefig("3.1st.png")
