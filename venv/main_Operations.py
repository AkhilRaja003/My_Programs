from classes_func import Rectangle
from classes_func import Triangle
from classes_func import Rhombus
from classes_func import Circle
from classes_func import Trapezium
from classes_func import Parallelogram
from classes_func import Square


def main():
    print('##############    RECTANGLE OPERATIONS    ################')
    length = float(input('Enter Length of Rectangle: '))
    bredth = float(input('Enter Breadth of Rectangle : '))
    Rect = Rectangle(length,bredth)
    print('length rectangle = ',Rect.length)
    print('bredth rectangle =', Rect.bredth)
    rect_area = Rect.Area()
    print('Area of the Rectangle is {:.2f}'.format(rect_area))
    rect_perm = Rect.Perimater()
    print('Perimeter of Rectangle is {:.2f}'.format(rect_perm))
    print('##############    TRIANGLE OPERATIONS    ################')
    a = float(input('Enter Side a : '))
    b = float(input('Enter Side b : '))
    c = float(input('Enter Side c : '))
    tri = Triangle(a,b,c)
    print('Side a is {:.2f}\n Side b is {:.2f}\n Side c is {:.2f}'.format(tri.a, tri.b, tri.c))
    tr_area = tri.Area()
    print('Area of the given Triangle is {:.2f}'.format(tr_area))
    tr_per = tri.Perimeter()
    print('Perimeter of the given Triangle is {:.2f}'.format(tr_per))


    print("##############     RHOMBUS OPERATIONS      ##############")

    p_diagonal = float(input("Give p_diagonal value:"))
    q_diagonal = float(input("Give q_diagonal value:"))
    a_side = float(input("Give (side-a) value:"))

    Rh = Rhombus(p_diagonal,q_diagonal,a_side)

    print("Diagonal(p) value :",Rh.p_diagonal)
    print("Diagonal(q) value :",Rh.q_diagonal)
    print("Diagonal a(side) value :", Rh.a_side)

    rh_area = Rh.Area()
    print('Area of the Rhombus is {:.2f}'.format(rh_area))

    rh_per = Rh.Perimeter()
    print('Perimeter of the Rhombus is {:.2f}'.format(rh_per))

    print("##############      CIRCLE OPERATIONS     ###############")

    radius = float(input("Give any value of radius:"))

    Cr = Circle(radius)

    print("Radius value:",Cr.radius)

    cr_area = Cr.Area()
    print('Area of the Circle is {:.2f}'.format(cr_area))

    cr_dia = Cr.Diameter()
    print('Diameter of the Circle is {:.2f}'.format(cr_dia))

    cr_circum = Cr.Circumference()
    print('Circumference of the Circle is {:.2f}'.format(cr_circum))

    print("##############    TRAPEZIUM OPERATIONS   ################")

    a_base = float(input("Enter any value for a_base:"))
    b_base = float(input("Enter any value for b_base:"))
    c_side = float(input("Enter any value for c_side:"))
    d_side = float(input("Enter any value for d_side:"))
    height = float(input("Enter any value for Height:"))

    Tra = Trapezium(a_base,b_base,c_side,d_side,height)

    print("a_base value is:",Tra.a_base)
    print("b_base value is:",Tra.b_base)
    print("c_side value is:",Tra.c_side)
    print("d_side value is:",Tra.d_side)
    print("Height value is:",Tra.height)

    tra_area = Tra.Area()
    print("Area of Trapezium is {:.2f}".format(tra_area))

    tra_per = Tra.Perimeter()
    print("Perimeter of Trapezium is {:.2f}".format(tra_per))

    print("##############   PARALLELOGRAM OPERATIONS  ##############")

    para_base = float(input("Enter any value for para_base:"))
    para_side = float(input("Enter any value for para_side:"))
    para_height = float(input("Enter any value for para_height:"))

    Para = Parallelogram(para_side,para_base,para_height)

    print("para_base value is:",Para.para_base)
    print("para_side value is:",Para.para_side)
    print("para_height value is:",Para.para_height)

    para_area = Para.Area()
    print("Area of Parallelogram is {:.2f}".format(para_area))

    para_per = Para.Perimeter()
    print("Perimeter of Parallelogram is {:.2f}".format(para_per))

    print("#############       SQUARE OPERATIONS      ##############")

    sq_side = float(input("Enter value of side(square)"))

    Sq = Square(sq_side)

    print("Sq_side is :",Sq.sq_side)

    sq_area = Sq.Area()
    print("Area of Square is {:.2f}".format(sq_area))

    sq_per = Sq.Perimeter()
    print("Perimeter of Square is {:.2f}".format(sq_per))




#main()
if __name__ == '__main__':
    main()