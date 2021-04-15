import timeit

# Initial inefficient
def exp1(a, b):
    res = 1
    while b:
        res *= a
        b -= 1
    return res

# Exponentiation by factor squaring
def exp2(a, b):
    if b == 1:
        return a
    if b == 2:
        return a * a
    if b % 2 == 1:
        return a * exp2(a, b - 1)
    
    res = exp2(a, b // 2)
    return res * res

# Even more optimized
def exp3(a, b):
    res = 1

    while b:
        if b % 2 == 1:
            res *= a
        b = b // 2
        a *= a
    
    return res

# Bitwise
def exp4(a, b):
    res = 1

    while b:
        if b & 1:
            res *= a
        b >>= 1
        a *= a

    return res

print(timeit.timeit("exp1(2, 30)", globals=globals()))
print(timeit.timeit("exp2(2, 30)", globals=globals()))
print(timeit.timeit("exp3(2, 30)", globals=globals()))
print(timeit.timeit("exp4(2, 30)", globals=globals()))