import matplotlib.pyplot as plt

Day=["mon","tue","wed","thu","fri"]
attendendece=[90,85,88,82,75]

plt.plot(Day,attendendece,color="blue",linestyle='--',marker="o",label="attendence in this week") #about graph
plt.title("attendence") #heaading of graph
plt.xlabel("Day") #x axis name
plt.ylabel("attendence percentage(%)") # yaxis name
plt.legend() # make box where label inside it
plt.grid(color="gray",linestyle=":") #background line like lines in graph paper
plt.ylim(75,95)#here we set limit start & end 
               #we can write same in yaxis
plt.xticks(["mon","tue","wed","thu","fri"],["D1","D2","D3","D4","D5"])    # use this we can update x & y
                                                                         #same we do it for y            
plt.savefig("3.using lineshape,colour.png") #save
