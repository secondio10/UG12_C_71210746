x = input("input: ")
y = len (x)
print ("Output: ")

for a in range (y):
    for b in range (a+1):
        print(x [b], end="")
    print()
for a in range(y):
    for b in range(y - a - 1):
        print(x [b], end = "")
    print()