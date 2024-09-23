def power(x, p):
    result = 1
    for _ in range(p):
        result *= x
    return result

def evaluate(A, x):
    result = 0
    for k in range(len(A)):
        result += A[k] * power(x, k)
    return result

# Polynomial coefficients
A = [12.3, 40.7, -9.1, 7.7, 6.4, 0, 8.9]
# Value at which to evaluate the polynomial
x = 5.4

# Evaluate the polynomial
result = evaluate(A, x)
print(f"The value of the polynomial at x = {x} is {result}")
