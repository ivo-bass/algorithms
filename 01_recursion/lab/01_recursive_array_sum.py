def arr_sum(arr, idx=0):
    if idx == len(arr)-1:
        return arr[idx]
    return arr[idx] + arr_sum(arr, idx+1)


tests = (
    ([1, 2, 3, 4], 10),
    ([-1, 0, 1], 0),
)

for arr, expected in tests:
    actual = arr_sum(arr)
    print()
    print(actual == expected)
    print(f"Actual: {actual}")
    print(f"Expected: {expected}")
