import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

data=sns.load_dataset("tips")

fg=sns.FacetGrid(data,col="day",hue="sex") # column day

fg.map(plt.scatter,"total_bill","tip").add_legend()

plt.savefig("2.day wise graph.png")