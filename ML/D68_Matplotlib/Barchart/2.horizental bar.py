import matplotlib.pyplot as plt

week = ["D1","D2","D3","D4","D5"]

attendence = [91,80,75,89,95]
plt.barh(week,attendence,color="green",label="attendence") #for make horizental bar chart
plt.legend() # label show in box
plt.ylabel("Attendence(%)") # x axis is Day
plt.xlabel("Day") # y axis is Attendence(%)
# plt.ylim() # limit in y 0 to 100
plt.title("Attendence data") # heading in this chart is Attendence data
plt.yticks(["D1","D2","D3","D4","D5"],["mon","tue","wed","thu","fri"]) # change D1,...,D5 to mon,...fri
                                                                       
plt.savefig("2.attendence repot in horizental.png") # save this