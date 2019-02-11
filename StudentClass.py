class Student:

    school = 'BVB' #outside __init__ => class var

    def __init__(self, m1,m2,m3):
        self.m1 = m1   #inside __init__ => instance var
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    @classmethod     #decorator
    def getSchool(cls):
        return cls.school

    @staticmethod    #decorator
    def info():
        print("This is student class, in abc module")

s1 = Student(112,111,80)
s2 = Student(212,130,19)

print("Student S1 Avg: ", s1.avg())
print("Student S2 Avg: ", s2.avg())

print("Both Students studies at: ", Student.getSchool())
