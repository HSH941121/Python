n = int(input())
A = input().split()
x,y = 1,1
for i in A :
    if(i == 'L' and y > 1) :
        y -= 1

    if(i == 'R' and y < n) :
        y += 1

    if(i == 'U' and x > 1) :
        x -= 1

    if(i == 'D' and x < n ) :
        x += 1

print(x,y)
        
