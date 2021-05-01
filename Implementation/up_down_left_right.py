n = int(input())
m =  input().split()

x, y = 1, 1

move_type = ['U','D','L','R']

dx = [-1, +1, 0, 0]
dy = [0, 0, -1, +1]


for move in m:

    for i in range(0, len(move_type)) :
        if move == move_type[i] :
            if( 1 <= x+dx[i] <= n and 1 <= y+dy[i] <= n )  :
                x += dx[i]
                y += dy[i]

print(x,' ',y)
            