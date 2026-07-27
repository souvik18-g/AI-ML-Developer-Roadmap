import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

url=" https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/021/299/original/final_vg1_-_final_vg_%281%29.csv?1670840166 "
df = pd.read_csv(url)
df.to_csv("final_vg.csv",index=False)
print(df["Genre"])
print(df["Genre"].unique()) # unique value from genre colume
cat_counts=df["Genre"].value_counts() # its show count genre
print(cat_counts)
x=cat_counts.index
y=cat_counts.values
plt.figure(figsize=(12,8)) # make large size of figure so not to be overlap
plt.plot(x,y)
plt.savefig("1.Genre Data in linechart.png",dpi=350,bbox_inches='tight') #save result with resolution accrding me 

plt.bar(x,y)
plt.savefig("2.Genre Data in barchart.png",dpi=350,bbox_inches='tight') #save result with resolution accrding me 

