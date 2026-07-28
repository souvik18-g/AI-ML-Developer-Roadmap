import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

data=sns.load_dataset("tips")

fg=sns.FacetGrid(data,col="sex",hue="day") # column sex

fg.map(plt.scatter,"total_bill","tip").add_legend()

plt.savefig("1.sex wise two graph.png")