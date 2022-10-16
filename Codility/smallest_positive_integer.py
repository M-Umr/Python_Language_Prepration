
def solution(A):
    max_a = max(A)
    possible_numbers = set(range(1, max_a + 2))
    min_list = possible_numbers - set(A)
    if len(min_list) > 0:
        return min(min_list)
    elif max_a < 0:
        return 1