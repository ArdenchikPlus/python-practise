def maxnum():
    x = int(input())
    y = int(input())
    z = int(input())
    n = x
    if y > n:
        n=y
    if z > n:
        n=z
    return n
result = maxnum()
print(result)