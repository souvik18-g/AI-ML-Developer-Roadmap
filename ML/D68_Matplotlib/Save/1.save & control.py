import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[10,20,15,25]
plt.plot(x,y,marker='o')
plt.savefig("1.save & control.png",dpi=350,bbox_inches='tight')#file name,dpi(control resolution),bbox_inches='tight'(file will no extra space in canvas)