class A:
    def __init__(self):
        print('Constructor of A')

    def feature1(self):
        print('feature 1 of A')


class B:
    def __init__(self):
        print('Constructor of B')

    def feature2(self):
        print('feature 2 of B')


class C(A, B):
    def __init__(self):
        super().__init__()
        print('Constructor of C')


c = C()

print()
