def binary(n):
    res = ''
    if n > 1:
        res += binary(n//2)
    res += str(n % 2)
    return res
