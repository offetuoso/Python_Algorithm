n = input()
k = list(map(int, input().split()))
k.sort();

result = 0
count = 0

for i in k :
    count += 1
    if i == count :
       result += 1
       count = 0

print(result)   