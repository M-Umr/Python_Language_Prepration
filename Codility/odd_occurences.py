#This solution gives 100% accuracy

def solution(A):
    # write your code in Python 3.6
    val = 0
    for i in range(len(A)):
        val = val ^ A[i]
    return val