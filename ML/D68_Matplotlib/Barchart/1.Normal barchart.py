import matplotlib.pyplot as plt

week = ["D1","D2","D3","D4","D5"]

attendence = [85,80,75,89,95]
plt.bar(week,attendence,color="green",label="attendence")
plt.legend() # label show in box
plt.xlabel("Day") # x axis is Day
plt.ylabel("Attendence(%)") # y axis is Attendence(%)
plt.ylim(0,100) # limit in y 0 to 100
plt.title("Attendence data") # heading in this chart is Attendence data
plt.xticks(["D1","D2","D3","D4","D5"],["mon","tue","wed","thu","fri"]) # change D1,...,D5 to mon,...fri
                                                                       # same we do y axis
plt.savefig("1.attendence repot.png") # save this