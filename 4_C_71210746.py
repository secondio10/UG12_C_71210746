x = int(input("Input: "))
print("Output: ")

for a in range (1,x+1):
    for b in range(1,x+1):
        if(b == 1) or (a == x) or (b == a ):
            print("*", end =" ")
        else:
            print(" ", end = " ")
    print()