x = int(input("Enter x value:"))
y = int(input("Enter y value:"))
for i in range(x,y+1):
    if i%2==0:
        print(i,"Is Even")
    else:
        print(i,"Is Odd")