import matplotlib.pyplot as plt

fig,ax=plt.subplots(1,2,figsize=(10,5)) # (row,column,figsize=(width,hight))
                                      #not compulsury to  write figsize

x= [1,2,3,4,5]
y= [10,20,15,25,30]

ax[0].plot(x,y,color="skyblue",marker="o")
ax[0].set_title("Plot")

ax[1].bar(x,y,color="green")
ax[1].set_title("Bar")
plt.tight_layout() #not compulsury #fit in canvas
plt.suptitle("COMPARE LINE & BAR")
plt.savefig("3.Update.png")