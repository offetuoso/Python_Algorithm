n, k = map(int, input().split()) 	#n=13, k=5

result = 0

while True :
    # n을 K로 나눈 몫에 k를 곱하여,
    # 나눌수 있는 값을 계산             # roof 1 step                         # roof 2 step
    target = (n // k) * k 		#target = 10 						#target = 0
    result += (n - target)       #result += 3  <<한번에 카운트 3을 추가하고     #result(4) += 2
    n = target                   #n = target   <<13을 10으로 만듬          #n=0

    if n < k :                   #false                                #true
        break
    result += 1				#나눗셈에 대한 result(3) +1	
    n //= k					#n = 2

result += (n - 1)                                                      #result(6) += -1   <n을 0까지 만들면서, 횟수 -1
print(result)                                                          #5      