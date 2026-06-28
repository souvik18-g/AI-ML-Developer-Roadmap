
try:
    with open("1.txt", "r") as f:
        print(f.read())
except Exception as a:
    print(a)

try:
    with open("2.txt", "r") as f:
        print(f.read())
except Exception as a:
        print(a)

try:
    with open("3.txt", "r") as f:
        print(f.read())
except Exception as a:
    print(a)

print("thanks")