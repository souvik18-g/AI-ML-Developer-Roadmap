import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


data=sns.load_dataset("penguins")
print(data)

#sns.barplot(x='island',y='bill_length_mm',data=data,hue='sex',order=['Dream','Biscoe','Torgersen'],hue_order=['Female','Male'],ci=50,n_boot=2)
 # here we can write it sns.barplot(x=data.island,y=data.bill_length_mm)
 #hue =diffrenciate,#order=bars order,#hue_order=here male female bar order,#ci=the line of the bars top which 0 to 100
 #n_boot= n no of data from data set choose n time & make another set this is value 1 if we do this n time the n_boot=n
sns.barplot(x='island',y='bill_length_mm',data=data,hue='sex',order=['Dream','Biscoe','Torgersen'],hue_order=['Female','Male'],saturation=.5,errcolor="b",errwidth=.2,capsize=.1)
plt.savefig('1.2nd barplot.png',dpi=1000)                     #saturation control the color saturation,errcolor= error color ,error wide
#capsize is the line of on the errorline 