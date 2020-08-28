x = int(input("Enter no :"))
f = 1


def fact(n):
    if n > 0:
        return n * fact(n - 1)
    elif n == 0:
        return f
    else:
        return "Sorry! negative number "


print(fact(x))
