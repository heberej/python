import math

class Plane():
    a = 0.0
    b = 0.0
    c = 0.0
    d = 0.0
    
    def __init__(self, a=None, b=None, c=None, d=None):
    
        if a is None:
            self.a = 0.0
        else:
            self.a = a
            self.b = b
            self.c = c
            self.d = d
             
            
    # add formatting for 7.3f
    
    def __str__(self):

        return '' + str(self.a) + 'x + ' + str(self.b) + 'y + ' + str(self.c) + 'z + ' + str(self.d) + ' = 0'  


    def intersect(self, vNormal, p1):
        
        t = (self.d + (self.a * p1.x) + (self.b * p1.y) + (self.c * p1.z)) / ((self.a*vNormal.a1) + (self.b*vNormal.a2) + (self.c*vNormal.a3));
         
        return Point(p1.x-(vNormal.a1 *t), p1.yx-(vNormal.a2 *t), p1.z-(vNormal.a3 *t))

        
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


    def dihedral(self, p2, p3, p4):
    
        midP = p2.mid(p3)
        normalV = p2.vector(p3)
        aPlane = midP.plane(p2, p3)
        
        # zeroV = 
        


    def distance(self, p2):
    
        return math.sqrt( math.sqr(p2.x - self.x) + math.sqr(p2.y - self.y) + math.sqr(p2.z - self.z))
    
    
    def mid(self, endPoint):
        midPoint = Point(0.0, 0.0, 0.0)
        
        midPoint.x = (endPoint.x + self.x) / 2.0    
        midPoint.y = (endPoint.y + self.y) / 2.0
        midPoint.z = (endPoint.z + self.z) / 2.0
        
        return midPoint

    def plane(self, endP1, endP2):
        """ Plane from Three Points
        
        """
        sEP1v = self.vector(endP1)
        sEP2v = self.vector(endP2)
        print('PQ: ' + str(sEP1v))
        print('PR: ' + str(sEP2v))
        
        
        cp = sEP1v.crossP(sEP2v)
        print("CP: " + str(cp))
        
        return Plane(cp.a1, cp.a2, cp.a3, cp.a1 * (-1 * self.x) + cp.a2 * (-1 * self.y) + cp.a3 * (-1.0 * self.z))        
    
    
         
    
    def vector(self, endPoint):
        v1 = Vector(0.0, 0.0, 0.0)
        
        v1.a1 = (endPoint.x - self.x)    
        v1.a2 = (endPoint.y - self.y)
        v1.a3 = (endPoint.z - self.z)
        
        return v1
             

class Vector():
    a1 = 0.0
    a2 = 0.0
    a3 = 0.0
    
    def __init__(self, a1=None, a2=None, a3=None):
        if a1 is None:
            self.a1 = 0.0
        else:
            self.a1 = a1
            self.a2 = a2
            self.a3 = a3
           
    def __str__(self):
        #    return '<' + str(self.a1) + ',' + str(self.a2) + ',' + str(self.a3) + '>'
    
        return '<%7.3f, %7.3f, %7.3f>' % (self.a1,self.a2,self.a3)


    def angle(self, v2):
    
        aDotb = self.dot(v2)
        absA  = self.mag()
        absB = v2.mag()
        
        cosine = aDotb / (absA * absB)
        
        if cosine == 0.0 :
            return math.pi / 2.0
        else:
            if cosine == 1.0:
                return 0.0
            else:
                if cosine < 0.0:
                    sine = math.sqrt(1.0 - (cosine * cosine))
                    return math.pi - math.fabs(math.atan(sine/cosine))
                else:
                    sine = math.sqrt(1.0 - (cosine * cosine))
                    return math.atan(sine/cosine)
                    
                        
    def crossP(self, v2):
        
        return Vector( self.a2*v2.a3 - self.a3*v2.a2, self.a3*v2.a1 - self.a1 * v2.a3, self.a1 *v2.a2- self.a2 * v2.a1)      
        
        
    def dot(self, v2):
    
        return self.a1 * v2.a1 + self.a2 * v2.a2 + self.a3 * v2.a3
    
    
    def mag(self):
        
        return math.sqrt((self.a1*self.a1) + (self.a2 * self.a2) + (self.a3 * self.a3))
        

    def plane(self, p1):
    
        d = (self.a1 * (-1 * p1.x)) + (self.a2 * (-1 * p1.y)) + (self.a3 * (-1 * p1.z)) 
        return Plane(self.a1, self.a2, self.a3, d)


    def sum(self, bVector):

        return Vector(self.a1 + bVector.a1, self.a2 + bVector.a2, self.a3 + bVector.a3)  
    
        
v1 = Vector(1.0, 2.0, 3.0)
v2 = Vector(3.0, 2.0, 1.0)

print(v1) 
print(v1.mag())    

print(v2) 
print(v2.mag())    
    
print(v1.sum(v2))
    
    
# CrossProduct Test
    
print("CrossProduct Test")

v3 = Vector(2, 1, -1)
v4 = Vector(-3, 4, 1)

print('V3 x V4 = ' + str(v3.crossP(v4)))
print('V4 x V3 = ' + str(v4.crossP(v3)))    

# Should generate
# V3 x V4 = <  5.000,   1.000,  11.000>
# V4 x V3 = < -5.000,  -1.000, -11.000>


# Plane from three Points Test

print("Plane from three Point Test")

p1 = Point(1, -2, 0)
p2 = Point(3, 1, 4)
p3 = Point(0, -1, 2)

print('Plane: ' + str(p1.plane(p2, p3)))
    
     
# Vector angle Tests

xAxis = Vector(1, 0, 0)
v5 = Vector(1,1,0)
print(xAxis.angle(v5))

v6 = Vector(0,1,0)
print(xAxis.angle(v6))

v7 = Vector(-1,1,0)
print(xAxis.angle(v7))

v8 = Vector(-1,0,0)
print(xAxis.angle(v8))
   
     
     