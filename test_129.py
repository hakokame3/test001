
class Triangle:
    def __init__(self,b,h):
        self.bottom=b
        self.hight=h

    def area(self):
        s=self.bottom*self.hight/2
        return s

triangle=Triangle(10,5)
print(triangle.area())
