###################     CLASS RECTANGLE      ####################
class Rectangle :
    def __init__(self,length, bredth):
        self.length = length
        self.bredth = bredth

    def Area(self):
        A = self.length * self.bredth
        return A

    def Perimater(self):
        P = (self.length + self.bredth) * 2
        return P
####################################################################
################         CLASS  TRIANGLE         ###################
class Triangle :
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def Perimeter(self):
        P = self.a + self.b + self.c
        return P

    def Area(self):
        s = self.Perimeter() / 2
        A = (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
        return A
#####################################################################
################          CLASS RHOMBUS              ################
class Rhombus :
    def __init__(self,p_diagonal,q_diagonal,a_side):
        self.p_diagonal = p_diagonal
        self.q_diagonal = q_diagonal
        self.a_side     = a_side

    def Area(self):
        A = (self.p_diagonal * self.q_diagonal) / 2
        return A

    def Perimeter(self):

        P = 4 * self.a_side
        return P
#####################################################################
#################         CLASS CIRCLE                #################

class Circle :
    def __init__(self,radius):
        self.radius = radius

    def Area(self):
        A = 3.14 * (self.radius ** 2)
        return A

    def Diameter(self):
        D = 2 * self.radius
        return D

    def Circumference(self):
        C = 2 * 3.14 * self.radius
        return C

#####################################################################
##################         CLASS TRAPEZIUM        ######################
class Trapezium:
    def __init__(self,a_base,b_base,c_side,d_side,height):
        self.a_base = a_base
        self.b_base = b_base
        self.c_side = c_side
        self.d_side = d_side
        self.height = height

    def Area(self):
        A = ((self.a_base + self.b_base) / 2 ) * self.height
        return A

    def Perimeter(self):
        P = self.a_base + self.b_base + self.c_side + self.d_side
        return P
######################################################################
####################       CLASS PARALLELOGRAM    ####################
class Parallelogram :
    def __init__(self,para_base,para_height,para_side):
        self.para_base = para_base
        self.para_height = para_height
        self.para_side = para_side

    def Area(self):
        A = self.para_base * self.para_height
        return A

    def Perimeter(self):
        P = 2 * ( self.para_base + self.para_side)
        return P

#######################################################################
####################           CLASS SQUARE      ######################
class Square :
    def __init__(self,sq_side):
        self.sq_side = sq_side

    def Area(self):
        A = (self.sq_side) ** 2
        return A

    def Perimeter(self):
        P = 4 * self.sq_side
        return P

#######################################################################