import matplotlib.pyplot as plt


plt.scatter([4,5,6,7,8],[65,75,80,85,93],color="blue",marker="+",label="section A")
plt.scatter([4,5,6,7,8],[60,73,77,82,90],color="green",marker="^",label="section B") 
plt.title("Progress") #heaading of graph
plt.xlabel("Hours") #x axis name
plt.ylabel("Marks(%)") # yaxis name
plt.legend() # make box where label inside it
plt.grid(color="gray",linestyle=":") #background line like lines in graph paper
plt.ylim(60,95)#here we set limit start & end 
plt.xlim(3,9)  #we can write same in yaxis
  
plt.savefig("2.progreesion report two section.png") #save

