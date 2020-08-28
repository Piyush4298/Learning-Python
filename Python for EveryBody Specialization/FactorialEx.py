def fact(n):
    f = 1

    if n < 0:
        pass
    elif n == 0:
        print("0! = ",end=" ")
    else:
        for i in range(1, n + 1):
            f = f * i
    return f


x = int(input("Enter the number: "))
if x >= 0:
    print(fact(x))
else:
    print("Sorry! no factorial for -ve number")
