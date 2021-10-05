array = input().split(' ')


def reverse_array(arr):
    if not arr:
        return []
    print(arr.pop(), end=' ')
    return reverse_array(arr)


reverse_array(array)