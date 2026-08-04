import requests                         # Import the requests library

payload = {"age": 20, "roll": 57}       # Data to send to the server

# Send a POST request with form data
r = requests.post("https://httpbin.org/post", data=payload)

print(r.text)                           # Print the complete response as text

print()                                 # Print a blank line

print(r.json())                         # Convert JSON response to a Python dictionary and print it

r_json = r.json()                       # Store the dictionary in a variable

print(r_json["form"])                   # Print only the 'form' data returned by the server