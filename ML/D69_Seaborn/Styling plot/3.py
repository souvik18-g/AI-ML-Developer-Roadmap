import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


data=sns.load_dataset("tips")
sns.set_context("poster",font_scale=.5) # in context we can write also paper,notebook,talk,poster
sns.barplot(x="day",y="total_bill",data=data)

plt.savefig("3.change fonts.png")