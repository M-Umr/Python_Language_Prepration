#This solution gives 100% accuracy

def flippingMatrix(matrix):

    len_mat = len(matrix)
    s = 0
    for i in range(len_mat//2):
        for j in range(len_mat//2):
            s += max(matrix[i][j], matrix[i][len_mat-j-1], matrix[len_mat-i-1][j], matrix[len_mat-i-1][len_mat-j-1])

    return s
