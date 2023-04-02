import math

class Figur:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return self.name

    def Umfang(self):
        return 0
    
    def Flaeche(self):
        return 0
    
    
class Punkt(Figur):
    def __init__(self, x, y):
        super().__init__("Punkt")
        self.x = x
        self.y = y

    def __str__(self):
        return f"Punkt ({self.x}, {self.y})"


class Kreis(Figur):
    def __init__(self, mittelpunkt, radius):
        super().__init__("Kreis")
        self.mittelpunkt = mittelpunkt
        self.radius = radius

    def __str__(self):
        return f"Kreis m= {self.mittelpunkt} r= {self.radius}"
    
    def Umfang(self):
        return self.radius*2 * math.pi
    
    def Flaeche(self):
        return self.radius**2 *math.pi
    

class Rechteck(Figur):
    def __init__(self, A, B, C):
        super().__init__("Rechteck")
        self.A = A
        self.B = B
        self.C = C

    def Umfang(self):
        laenge = ((self.B.x - self.A.x)**2 + (self.B.y - self.A.y)**2)**0.5
        breite = ((self.C.x - self.A.x)**2 + (self.C.y - self.A.y)**2)**0.5
        return 2*(laenge + breite)
    
    def Flaeche(self):
        laenge = ((self.B.x - self.A.x)**2 + (self.B.y - self.A.y)**2)**0.5
        breite = ((self.C.x - self.A.x)**2 + (self.C.y - self.A.y)**2)**0.5
        return (laenge * breite)
    
    def __str__(self):
        return f"Reckteck a={self.A} b={self.B}"
    
class Dreieck(Figur):
    def __init__(self, A, B, C):
        super().__init__("Dreieck")
        self.A = A
        self.B = B
        self.C = C
    
    def Umfang(self):
        AB = ((self.B.x - self.A.x)**2 + (self.B.y - self.A.y)**2)**0.5
        AC = ((self.C.x - self.A.x)**2 + (self.C.y - self.A.y)**2)**0.5
        BC = ((self.C.x - self.B.x)**2 + (self.C.y - self.B.y)**2)**0.5
        return AB + AC + BC
    
    def Flaeche(self):
        AB = Punkt(self.A.x-self.B.x, self.A.y-self.B.y)
        AC = Punkt(self.A.x-self.C.x, self.A.y-self.C.y)
        return 0.5*((AB.x*AC.y)-(AC.x*AB.y))
    
    def __str__(self):
        return f"Dreieck a={self.A} b={self.B} c={self.C}"
    
        

p1 = Punkt(0,0)
p2 = Punkt(5,0)
p3 = Punkt(0,5)

print(p1)
k1 = Kreis(p1,10)
print(k1)
u1 = round(k1.Umfang(),3)
a1 = round(k1.Flaeche(),3)
print(f"Kreis Umfang: {u1}, Fläche: {a1}")

r1 = Rechteck(p1,p2,p3)
print(r1)
u2 = round(r1.Umfang(),3)
a2 = round(r1.Flaeche(),3)
print(f"Rechteck Umfang:{u2}, Fläche {a2}")

d1 = Dreieck(p1,p2,p3)
print(d1)
u3 = round(d1.Umfang(),3)
a3 = d1.Flaeche()
print(f"Dreieck Umfang: {u3}, Fläche: {a3}")














    
    