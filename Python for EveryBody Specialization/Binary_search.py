pos = -1


def search(lst, n):
    l = 0
    u = len(lst) - 1
    for i in lst:
        mid = int((l + u) / 2)
        if lst[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if lst[mid] < n:
                l = mid + 1
            else:
                u = mid - 1
    return False


lst = [7, 8, 9, 12, 58, 78, 99]

n = int(input('Enter number to be searched: '))

if search(lst, n):
    print('Found at:', pos + 1)
else:
    print('Not found in the given list!')
