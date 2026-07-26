import matplotlib.pyplot as plt

x=['sun','mon','tue','wed','thu','fri','sat']
y=[50,34,52,45,40,30,25]
plt.plot(x,y)
plt.title("bakery week sales graph!")
plt.xlabel("Days of week")
plt.ylabel("sales in doller($)")
plt.savefig("2.bakery report.png")