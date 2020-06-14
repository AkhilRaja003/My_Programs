import Triangle as tri
import Square as sq
import Circle as cr
a = 8

b = 5

c = mul(a,b)
print(c)

print("For Area of Triangle")

height = 8
base = 6

tria =  tri.area(height,base)
print(tria)

print("Perimeter of Triangle")

s1 = int(input("S1 value:"))
s2 = int(input("S2 value:"))
s3 = int(input("S3 value:"))
tri1 = tri.perimeter(s1,s2,s3)
print(tri1)

print("Area of Square")

side = int(input("Give Side of square value:"))
sq1 = sq.area(side)
print(sq1)

print("Perimeter of Square")

side = int(input("Give Side of square value:"))
sqp = sq.perimeter(side)
print(sqp)

print("Area of Circle")
radius = int(input("Give Radius of circle value:"))
cr1 = cr.area(radius)
print(cr1)

print("Circumference of Circle")

r = int(input("Give Radius of circle value:"))
cr2 = cr.circumference(r)
print(cr2)

###########################################################################