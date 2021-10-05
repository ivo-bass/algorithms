n = int(input())


def print_nested_i(vector, index=0):
    if index == len(vector):
        print(' '.join(map(str, vector)))
        return
    for i in range(1, n+1):
        vector[index] = i
        print_nested_i(vector, index+1)


print_nested_i([0]*n, 0)
