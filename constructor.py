class car:
    wheels=4 #class variable/static variable
    logo="yes"
    def __init__(self):
        self.com="audi"
        self.mil=30
c1 = car()
c2 = car()
c1.mil=20
c2.mil=21
c2.com="bmw"
c2.logo="no"

print(c1.com,c1.mil,c1.wheels,"rings:",c1.logo)
print(c2.com,c2.mil,c2.wheels,"rings:",c2.logo)
