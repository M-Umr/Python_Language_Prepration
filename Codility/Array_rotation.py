#This solution gives 100% accuracy

def solution(A, K):
    if len(A) != 0:
        for i in range(K):
            last_val = A[-1]
            A.pop()
            A.insert(0,last_val)
        return A
    else:
        return A