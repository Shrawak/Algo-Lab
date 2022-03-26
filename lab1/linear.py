def linear_search(A,target):
    for ele in A:
        if (ele == target):
            return A.index(ele)
    return -1