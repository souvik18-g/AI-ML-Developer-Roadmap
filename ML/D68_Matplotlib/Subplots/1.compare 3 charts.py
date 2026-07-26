import matplotlib.pyplot as plt
hours=[4,5,6,7,8]
marks=[65,75,80,85,93]

plt.subplot(2,2,1)
plt.plot(hours,marks,color="blue",marker="o")
plt.title("1.Graph")

plt.subplot(2,2,2)
plt.bar(hours,marks,color="green")
plt.title("2.Bar")

plt.subplot(2,2,3)
plt.pie(hours,labels=marks,autopct='%1.1f%%',colors=["brown","green","red","blue","yellow"])
plt.title("3.Pie")

plt.savefig("1.Compare3.png")

