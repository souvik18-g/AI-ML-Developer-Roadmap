import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df=pd.DataFrame({
    'a':[2,4,6,8,10,12,14],
    'b':[3,5,7,9,11,13,15]
})



sns.lineplot(x='a',y='b',data=df)
plt.savefig("2.linechart using pandas dataframe.png")