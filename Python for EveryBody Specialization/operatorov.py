class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        a1 = self.m1 + other.m1
        a2 = self.m2 + other.m2
        a3 = Student(a1, a2)
        return a3

    def __sub__(self, other):
        b1 = self.m1 - other.m1
        b2 = self.m2 - other.m2
        b3 = Student(b1, b2)
        return b3


s1 = Student(68, 69)
s2 = Student(80, 70)

s3 = s1 + s2
s4 = s1 - s2
print(s3.m1,s3.m2)
print(s4.m1,s4.m2)
