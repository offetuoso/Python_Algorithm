# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    
    print ((Y-X) )
    print ((Y-X) % D )

    print  ((Y-X) // D )
    
    
    if (Y == X)   :
        return 0
    
    return  (Y-X) % D == 0 and (Y-X) // D or ((Y-X) // D) + 1  

    


    pass

solution(2, 2, 1)


#solution(1, 101, 10)



