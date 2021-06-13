# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    N = len(A)

    for value in A :
        if not (-1000 <= value <= 1000) :
            print("out of range value")

    if not (0 <= N <= 100) :
        print("out of range N")
    elif not (0 <= K <= 100) :
        print("out of range K")  
    else :
        
        B = []
        for i in range(0,N) :
            B.append(0)        

        for i in range(0,N) :
            print("i ",i)
            print("Ai ",A[i])
            rotate = (i+K) % N
            print("rotate ",rotate)
            B[rotate] = (A[i])

        A = B
       
    return A

    pass



# 0 1 2

# 2 1 0

# 


A = solution([3, 8, 9, 7, 6], 3)

print(A)

