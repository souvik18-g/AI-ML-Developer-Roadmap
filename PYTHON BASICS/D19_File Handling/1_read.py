with open ('example.txt', 'r') as file: #open the file in read mode
    print(file.read()) #print the content of the file


with open ('example.txt', 'r') as file: #open the file in read mode
    print(file.readline()) #print the 1st line of the file
    print(file.readline()) #print the 2nd line of the file

with open ('example.txt', 'r') as file: #open the file in read mode
    print(file.readlines())  #print all lines of the file as a list