import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

data=np.linspace(1,10,20).reshape(4,5)

# print(data)

sns.heatmap(data)
plt.savefig("1.1st.png")


