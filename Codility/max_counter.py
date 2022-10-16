#This solution will give 88% accuracy

def solution(N, A):
    # write your code in Python 3.6
    counter_arr = [0] * N
    max_arr = 0
    length_arr = len(A)
    val_index = 0
    for i in range(length_arr):
        if A[i] >= 1 and A[i] <= N:
            val_index = A[i]
            counter_arr[val_index-1] += 1
            if max_arr < counter_arr[val_index-1]:
                max_arr = counter_arr[val_index-1]
        else:
            counter_arr = [max_arr]*N
    return counter_arr