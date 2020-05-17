def max_of_2(a, b):
    if a > b:
        return a
    else:
        return b

def maximum_of(a, b, c):
    result = max_of_2(a ,b)
    max_num =  max_of_2(c, result)
    return max_num

n1, n2, n3 = 3, 5, 1
print(maximum_of(n1, n2, n3))
