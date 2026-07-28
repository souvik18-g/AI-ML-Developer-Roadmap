import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


data=sns.load_dataset("penguins").head(25)
print(data)

sns.scatterplot(x='bill_length_mm',y='bill_depth_mm',data=data,hue='sex',style='sex',size='sex',sizes=(50,100),palette="Accent",alpha=1,markers={'Male':'o',
                                                                                                                                               'Female':'d'})
#here style decide diffrent style of markers
#size=decided to size of sex(male,female) & sizes=(values of them )
#palette= choose the color combination
#alpha= choose the visibality
#markers= markers of male female mind it here use this format 

plt.savefig("4.2nd.png")