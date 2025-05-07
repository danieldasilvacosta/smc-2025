def weighted_jaccard(A, B):
    mins, maxs = 0, 0
    height = A.shape[0]
    width = A.shape[1]

    for h in range(0, height):
        for w in range(0, width):
            a = A[h, w]
            b = B[h, w]
            mins += min(a, b)
            maxs += max(a, b)

    return mins / maxs