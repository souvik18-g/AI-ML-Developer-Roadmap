import matplotlib.pyplot as plt
import seaborn as sns


x=[1,2,3,4,5,6,7]
y=[2,4,6,8,10,12,14]

sns.lineplot(x=x,y=y)
plt.savefig("1.linechart using seaborn.png")