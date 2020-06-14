num = int(input("Enter multiple value:"))
x = int(input("Enter x value:"))
y = int(input("Enter y value:"))

for i in range ( x , y+1):
    print(num,"*",i,"=",num * i)
    i=i+1