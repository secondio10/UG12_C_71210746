x = int(input("Masukkan awal deret: "))
y = int(input("Masukkan akhir deret: "))

if(x+1)%2==0:
    for a in range(x+1,y,2):
        if a % 9 == 0 or a % 11 == 0: continue
        print (a,end=" ")

else:
    for a in range(x,y,2):
        if a % 9 == 0 or a % 11 == 0 : continue
        print(a, end =" ")