
def solution(A):
   
    minimum = 99999
    first = 0;
    summary = sum(A)
    for i in range(0,len(A)-1) :
        print(i)
        first += A[i]
        minimum = min(minimum, abs(first-(summary-first)))
    return minimum


solution([3,1,2,4,3])
      