a = 10
b = 2

print(int.__mul__(a,b))

class student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

#Operator (>=) overloadingd
    def __ge__(self, other):
        if self.m1 >= other.m1 and self.m2 >= other.m2:
            return True
        else:
            return False

    def __str__(self):
        return self.m1, self.m2



s1 = student(34, 32)
s2 = student(34, 34)

if s1 >= s2:
    print("S1 >= S2")
else:
    print("S1 <= S2")