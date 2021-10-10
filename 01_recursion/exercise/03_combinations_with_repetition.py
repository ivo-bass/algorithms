def combinations_with_repetition(n, k, arr, result, idx):
    if len(result) == k:
        print(' '.join(map(str, result)))
        return

    for current_idx in range(idx, n):
        result.append(arr[current_idx])
        combinations_with_repetition(n, k, arr, result, current_idx)
        # backtrack: remove the current element from the solution
        result.pop()



def main():
    n = int(input())
    k = int(input())
    arr = [i for i in range(1, n + 1)]
    combinations_with_repetition(n, k, arr, [], 0)


main()