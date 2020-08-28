class Student:
    def __init__(self, name, rollno):
        self.rollno = rollno
        self.name = "Piyush"
        #self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollno)
        #self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand = "Dell"
            self.cpu = 'i3'
            self.ram = '4GB'

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student('Piyush', 39)
s1.show()
#lap1=s1.Laptop
lap1=Student.Laptop()
lap1.show()