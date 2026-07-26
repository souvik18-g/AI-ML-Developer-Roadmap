import matplotlib.pyplot as plt

hours=[4,5,6,7,8]
marks=[65,75,80,85,93]

plt.scatter(hours,marks,color="blue",marker="+",label="progression") #about graph
plt.title("Progress") #heaading of graph
plt.xlabel("Hours") #x axis name
plt.ylabel("Marks(%)") # yaxis name
plt.legend() # make box where label inside it
plt.grid(color="gray",linestyle=":") #background line like lines in graph paper
plt.ylim(60,95)#here we set limit start & end 
plt.xlim(3,9)  #we can write same in yaxis
  
plt.savefig("1.progreesion report.png") #save

