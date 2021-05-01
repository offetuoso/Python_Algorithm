n, m, k = map(int, input().split()) 
l = list(map(int, input().split()));
l.sort();

first = l[n-1]
second = l[n-2]

count = (m // (k+1))*k 
count += m % (k+1)

count2 = m-count

print(count*first + count2*second)
 