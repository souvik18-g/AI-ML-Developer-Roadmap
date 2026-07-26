import matplotlib.pyplot as plt

region = ["east","west","south","north"]
revenue = [3000,2500,2000,2700]

plt.pie(revenue,labels=region,autopct='%1.1f%%',colors=["brown","green","red","blue"])
plt.title("revenue of each portion")
plt.savefig("1.piechart.png")