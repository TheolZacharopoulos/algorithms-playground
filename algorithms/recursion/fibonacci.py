# Classic (binary) recursive fibonacci: O(2^n)
def bad_fibonacci(n):
    if n <= 1:
        return n
    return bad_fibonacci(n - 1) + bad_fibonacci(n - 2)


# Improved (linear) recursive fibonacci: O(n)
def good_fibonacci(n):
    if n <= 1:
        return n, 0
    a, b = good_fibonacci(n - 1)
    return a+b, a


print(good_fibonacci(30)[0])
print(bad_fibonacci(30))
