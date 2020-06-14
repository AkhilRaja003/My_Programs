a = float(input("enter 1st no:"))
b = float(input("enter 2nd number:"))
perimeter = 2* (a+b)
print("perimeter of rectangle is {:.2f}".format(perimeter))


print("*******************************************")


def area_of_rectangle(length,width):
    area = length * width
    print("Area of rectangle(using function) is {:.2f}".format(area))
area_of_rectangle(length = a , width = b )