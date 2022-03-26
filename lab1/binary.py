def binary_search(A, start, end, target):
    if start > end:
        return -1
    else:
        mid = (start + end) // 2
        if A[mid] == target:
            return mid
        elif A[mid] < target:
            return binary_search(A, mid+1, end, target)
        elif A[mid] > target:
            return binary_search(A, start, mid-1, target)