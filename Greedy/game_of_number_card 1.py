n, m = map(int, input().split())

arr = []
for i in range(0, n):
    k =  list(map(int, input().split()))
    arr.append(k)

minumum = 10001
maximum = 0

for i in range(0, n-1):
    for j in range(0, m):
       
       if( minumum > min(arr[i]) or min(arr[i]) == arr[i][j] ) :
           minumum = arr[i][j]
           maximum = arr[i+1][j]

print(maximum) 

