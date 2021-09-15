def gen01(vector, index=0):
    if index == len(vector):
        print(''.join(map(str, vector)))
        return
    for i in range(2):
        vector[index] = i
        gen01(vector, index+1)


def generator(n):
    vector = [0]*n
    gen01(vector, 0)


generator(3)
