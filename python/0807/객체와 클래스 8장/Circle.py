import math

# Circle 클래스를 정의한다.   원의 면적 구하기 
class Circle:
    def __init__(self, radius = 0):
        self.radius = radius

    def setRadius(self, radius):
        self.radius = radius

    def getArea(self):
        return math.pi*self.radius*self.radius
    
    def getPerimeter(self):
        return 2*math.pi*self.radius
    
#Cirecle 객체를 생성한다.

circle1 = Circle(10)
print("원의 면적", circle1.getArea())
print("원의 면적", circle1.getPerimeter())
circle2 = Circle()
circle2.setRadius(5)
print("원의 면적", circle2.getArea())
print("원의 면적", circle2.getPerimeter())