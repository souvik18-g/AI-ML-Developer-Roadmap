import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


data=sns.load_dataset("penguins")
print(data)
# sns.lineplot(x='bill_length_mm',y='body_mass_g',data=data)
sns.lineplot(x='bill_length_mm',y='body_mass_g',data=data,hue='sex',style='sex',palette={'Male':'blue',
                                                                                         'Female':'red'},markers=["o","^"]) #diffrenciate use hue,style cahnge the line 
                                                                            # palette control the color we can easily write only palettte ='Accent'
plt.savefig('3c.import dataset & compare sex.png')