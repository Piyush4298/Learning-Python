pos = -1


def search(lst1, n1):
    for i in lst1:
        if n1 in lst1:
            globals()['pos'] = lst1.index(i)
            return True
    return False


lst = [5, 9, 10, 3, 6, 88]
n = int(input("Enter no to be searched: "))

if search(lst, n):
    print("Found at position:", pos + 1)
else:
    print("Not Found in the given List!")
