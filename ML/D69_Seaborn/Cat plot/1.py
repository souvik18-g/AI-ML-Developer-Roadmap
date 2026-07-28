import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


data=sns.load_dataset("tips")

sns.catplot(x="size",y="tip",data=data,hue="sex",palette="magma",kind="box")
plt.savefig("1.2.kind of graph.png")# kind=['strip', 'swarm', 'box', 'violin', 'boxen', 'point', 'bar', 'count']