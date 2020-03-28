import math

def pageCount(n, p):
    #starting from page 1:
    start = math.ceil((p - 1) / 2)

    #starting from lst page:
    if n % 2 == 1:
        end = math.floor((n - p) / 2)
    else:
        end = math.ceil((n - p) / 2)

    return min(start,end)

#print(pageCount(5,4))

def pageCount2(n, p):
    return min(p//2, n//2 - p//2)


print(pageCount2(6,4))