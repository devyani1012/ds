n=int(input("input no of rows:"))
num=0
for i in range(n):
    for j in range(i+1):
        print(chr(65+j),end="")
        num+=1
    print()    