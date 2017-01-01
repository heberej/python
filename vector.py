class Point():
    x = 0.0
    y = 0.0
    z = 0.0
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ',' + str(self.z) + ')'

    def mid(self, endPoint):
        midPoint = Point(0.0, 0.0, 0.0)
        
        midPoint.x = (endPoint.x + self.x) / 2.0    
        midPoint.y = (endPoint.y + self.y) / 2.0
        midPoint.z = (endPoint.z + self.z) / 2.0
        
        return midPoint


class Vector():
    a1 = 0.0
    a2 = 0.0
    a3 = 0.0
    
    def __init__(self, who):
        self.name = who
        
    def __str__(self):
        return '<' + str(self.a1) + ',' + str(self.a2) + ',' + str(self.a3) + '>'
        
        
        
v1 = Vector('first')

print(v1) 
    
    
    
    
     