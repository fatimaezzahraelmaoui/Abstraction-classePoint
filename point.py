import math

class Point:
    nb = 0
    def __init__(self,x,y):
        self.__abs = x
        self.__ord = y
        Point.nb += 1
    
    @property
    def abs(self):
        return self.__ord
    @abs.setter
    def abs(self,x):
        self.__abs = x
    
    @property
    def ord(self):
        return self.__ord
    
    @ord.setter
    def ord(self,y):
        self.__ord = y
        
    def __str__(self):
        print("abs =",self.__abs)
        print("ord =",self.__ord)
    
    def __eq__(self,other):
        if self.__abs == other.abs and self.__ord == other.ord:
            return True
        else :
            return False
    
    def CalculerDistance(self,z):
         return math.sqrt(math.pow(z -self.__abs,2)+math.pow(z-self.__ord,2))
    
    def CalculerMilieu(self,u):
        M_x = (self.__abs + u)/2 
        M_y = (self.__ord + u)/2
        return (M_x , M_y)
        
    
class TroisPoint:
    def __init__(self,point1,point2,point3):
        self.__point1 = point1
        self.__point2 = point2
        self.__point3 = point3
    
    @property
    def point1(self):
        return self.__point1
    
    @point1.setter
    def point1(self,point1):
        self.__point1 = point1
    
    @property
    def point2(self):
        return self.__point2
    
    @point2.setter
    def point2(self,point2):
        self.__point2 = point2
    
    @property
    def point3(self):
        return self.__point3
    
    @point3.setter
    def point3(self,point3):
        self.__point3 = point3
    
    def Sontalignes(self):
        dis_AB = self.__point1 * (self.__point2)
        dis_AC = self.__point1 *(self.__point3)
        dis_BC = self.__point2 *(self.__point3)
        
        return  dis_AB == dis_AC + dis_BC or dis_AC == dis_BC + dis_AB or dis_BC == dis_AC + dis_AB
    
    def Estisocèle(self):
        dis_AB = self._point1*(self._point2)
        dis_AC = self._point1*(self._point3)
        dis_BC = self._point2*(self.__point3)
                            
        return   dis_AB == dis_AC or dis_AC == dis_BC + dis_AB or dis_BC == dis_AB
    
    @staticmethod
    def Sontalignes(self):
       dis_AB = self.__point1 * (self.__point2)
       dis_AC = self.__point1 * (self.__point3)
       dis_BC = self.__point2 * (self.__point3)
        
       return  dis_AB == dis_AC + dis_BC or dis_AC == dis_BC + dis_AB or dis_BC == dis_AC + dis_AB
    
    @staticmethod
    def Estisocèle(self):
        dis_AB = self.__point1 * (self._point2)
        dis_AC = self.__point1 * (self.__point3)
        dis_BC = self.__point2 * (self.__point3)
                            
        return   dis_AB == dis_AC or dis_AC == dis_BC + dis_AB or dis_BC == dis_AB

    
po1 = Point(4,6)
print(po1.CalculerDistance(2))
print(po1.CalculerMilieu(2))