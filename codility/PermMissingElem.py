def solution(A):
    N = len(A)+1

    return  sum (range(N+1)) - sum(A)


A = [2, 3, 1, 5]

solution(A)