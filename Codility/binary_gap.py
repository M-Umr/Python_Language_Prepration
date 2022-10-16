#This solution gives 100% accuracy, in Codility

def solution(N):
    binary_str = format(N,'b')
    return len(max(binary_str.strip('0').split('1')))