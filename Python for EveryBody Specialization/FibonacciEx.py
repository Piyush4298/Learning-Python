def fib(n):
    a = 0
    b = 1
    if n <= 0:
        print("Sorry! Try with greater values :)")
        pass
    elif n == 1:
        print(a)
    else:
        print(a, end=" ")
        print(b, end=" ")

    for i in range(2, n):

        c = a + b
        a, b = b, c
        print(c, end=" ")


fib(int(input("Enter how many numbers you want: ")))
