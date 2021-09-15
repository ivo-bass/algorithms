def factorial(num):
    if num == 1:
        return num
    return num*factorial(num-1)


tests = (
    (5, 120),
    (10, 3628800),
)

for num, expected in tests:
    actual = factorial(num)
    print()
    print(actual == expected)
    print(f"Actual: {actual}")
    print(f"Expected: {expected}")
