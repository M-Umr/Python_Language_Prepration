#This solution gives 100% accuracy

def findMedian(arr):
    sort_arr = sorted(arr)
    length_arr = int(len(arr)/2)
    return sort_arr[length_arr]
