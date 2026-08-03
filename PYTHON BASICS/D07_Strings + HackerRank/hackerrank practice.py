# ===========================================
# Day 7 - Strings in Python
# ===========================================

# -------------------------------
# 1. Creating Strings
# -------------------------------
name = "Souvik"
print("Original String:", name)

# -------------------------------
# 2. String Indexing
# -------------------------------
print("\nString Indexing")
print(name[0])
print(name[1])
print(name[-1])
print(name[-2])

# -------------------------------
# 3. String Slicing
# -------------------------------
text = "Python Programming"

print("\nString Slicing")
print(text[0:6])      # Python
print(text[7:18])     # Programming
print(text[:6])
print(text[7:])
print(text[::2])
print(text[::-1])

# -------------------------------
# 4. upper()
# -------------------------------
print("\nupper()")
print("python".upper())

# -------------------------------
# 5. lower()
# -------------------------------
print("\nlower()")
print("PYTHON".lower())

# -------------------------------
# 6. strip()
# -------------------------------
print("\nstrip()")
print("   Hello World   ".strip())

# -------------------------------
# 7. split()
# -------------------------------
print("\nsplit()")
languages = "Python Java C++"
print(languages.split())

# -------------------------------
# 8. replace()
# -------------------------------
print("\nreplace()")
sentence = "I like Java"
print(sentence.replace("Java", "Python"))

# -------------------------------
# 9. find()
# -------------------------------
print("\nfind()")
text = "Hello Python"
print(text.find("Python"))
print(text.find("Java"))

# -------------------------------
# 10. count()
# -------------------------------
print("\ncount()")
text = "apple apple banana apple"
print(text.count("apple"))

# -------------------------------
# 11. f-Strings
# -------------------------------
print("\nf-Strings")

name = "Souvik"
age = 19

print(f"My name is {name}.")
print(f"I am {age} years old.")

# -------------------------------
# 12. Mini Practice Program
# -------------------------------
print("\nMini Practice Program")

user_name = input("Enter your name: ").strip()

print("Upper :", user_name.upper())
print("Lower :", user_name.lower())
print("Length:", len(user_name))
print("Reverse:", user_name[::-1])

print(f"Welcome, {user_name}!")

# -------------------------------
# 13. Extra String Examples
# -------------------------------
print("\nExtra Examples")

msg = "Python Programming"

print("Starts with Python:", msg.startswith("Python"))
print("Ends with ing:", msg.endswith("ing"))
print("Length:", len(msg))
print("Title:", msg.title())
print("Is Alphabet:", "Python".isalpha())
print("Is Digit:", "12345".isdigit())
print("Swap Case:", "PyThOn".swapcase())