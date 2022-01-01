T= int(input())
for i in range(T):
    N, K = map(int, input().split())

    popl = input().split()


    j = 0
    while (K >= 0 and j < len(popl) - 1):
        if (int(popl[j]) < int(popl[j + 1])):
            popl.pop(j)
            K -= 1
        else:
            j += 1
    






