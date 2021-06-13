# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    
    total = sum(range(X+1))

    #print(total)

    chked = [None for i in range(X)]
    chk_sum = 0
    for i in range(len(A)) :
        if( chked[A[i]-1]  == None) :
            chked[A[i]-1] = A[i]
            chk_sum +=  A[i]
            if total == chk_sum : 
                return i
        
    if total != chk_sum :
        return -1


    #print(chk_sum)

    pass


solution(2, [1,1,1])

solution(5, [1,3,1,4,2,3,5,4])
