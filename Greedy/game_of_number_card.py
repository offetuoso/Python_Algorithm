n, m = map(int, input().split())

result = 0


for i in range(n):
    data =  list(map(int, input().split()))
    
    minumum = min(data)
    result = max(result, minumum)


print(result) 

