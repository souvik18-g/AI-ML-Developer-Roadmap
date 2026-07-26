import matplotlib.pyplot as plt

marks = [45,89,55,60,65,76,98,85,49,68,35,37,72,31,52,91,40,82,71,69,57]
plt.hist(marks,bins=7,color="skyblue",edgecolor="black")
plt.title("students marks")
plt.xlabel("marks")
plt.ylabel("students number")
plt.savefig("1.student mark.png")