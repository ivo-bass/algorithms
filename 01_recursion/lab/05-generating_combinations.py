IS_TEST = True
DATA = "1 2 3 4"
K = 2


def gen_combinations(arr, vector, index, border):
    if index >= len(vector):
        print(" ".join(map(str, vector)))
    else:
        for i in range(border, len(arr)):
            vector[index] = arr[i]
            gen_combinations(arr, vector, index+1, i+1)


def solution(test=IS_TEST):
    data = input() if not test else DATA
    k = int(input()) if not test else K
    arr = [int(s) for s in data.split(" ")]
    vector = [0]*k
    gen_combinations(arr, vector, 0, 0)


solution()
