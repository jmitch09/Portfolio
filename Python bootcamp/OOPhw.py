import math

class Line:

        def __init__(self,coor1,coor2):
                self.coor1 = coor1
                self.coor2 = coor2

        def distance(self):
                return math.sqrt((self.coor1[0] - self.coor2[0])**2 + (self.coor1[1] - self.coor2[1])**2)

        def slope(self):
                return (self.coor1[1] - self.coor2[1]) / (self.coor1[0] - self.coor2[0])

class Cylinder:

        def __init__(self,height=1,radius=1):
                self.height = height
                self.radius = radius

        def volume(self):
                return math.pi * (self.radius**2) * self.height

        def surface_area(self):
                return (2 * math.pi * self.radius * self.height) + (2 * math.pi * (self.radius**2))
        
def main():
        my_line = Line((3,2),(8,10))
        print(my_line.distance()) #expected 9.4
        print(my_line.slope()) #expected 1.6

        my_cylinder = Cylinder(2,3)
        print(my_cylinder.volume()) #expected 56.5
        print(my_cylinder.surface_area()) #expected 94.2

if __name__ == "__main__":
        main()