# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    A.sort()
    odd = 0
    for i in range (0, len(A)) :

       if i % 2 == 0 :
            #print (A[i],' 홀')
            
            if i+1 != len(A) :
                odd = A[i]
            else :
                return A[i] 
       else :
            #print (A[i],' 짝')
            if odd != A[i] : 
                return odd 

    pass



#solution([9, 3, 9, 3, 9, 7, 9])

solution([9, 3, 9, 3, 9])