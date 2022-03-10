n, m = map(int,input().split())
a, b, d = map(int,input().split())
ta = a
tb = b
td = d
dis = [(-1,0),(0,1),(1,0),(0,-1)]
data = []
count = 1
for i in range(n) :
    data.append(list(map(int,input().split())))


while 1 :
    for i in range(4) :
        d = d - 1
        if(d < 0) :
            d = 3

        if(d == 0) :
            a = a + dis[d][0]
            b = b + dis[d][1]

            if(data[a][b] == 1) :
                a = a - dis[d][0]
                b = b - dis[d][1]

            else :
                data[a][b] = 1
                count += 1

        if(d == 1) :
            a = a + dis[d][0]
            b = b + dis[d][1]

            if(data[a][b] == 1) :
                a = a - dis[d][0]
                b = b - dis[d][1]

            else :
                data[a][b] = 1
                count += 1


        if(d == 2) :
            a = a + dis[d][0]
            b = b + dis[d][1]

            if(data[a][b] == 1) :
                a = a - dis[d][0]
                b = b - dis[d][1]

            else :
                data[a][b] = 1
                count += 1

        if(d == 3) :
            a = a + dis[d][0]
            b = b + dis[d][1]

            if(data[a][b] == 1) :
                a = a - dis[d][0]
                b = b - dis[d][1]

            else :
                data[a][b] = 1
                count += 1
            
    if(a == ta and b == tb) :
        d = td
        td = d
        if(d == 0) :
            a = a + 1
            if(data[a][b] == 1) :
                break
            else :
                ta = a
                count += 1
        
        if(d == 1) :
            b = b - 1
            if(data[a][b] == 1) :
                break
            else :
                tb = b
                count += 1
            
        if(d == 2) :
            a = a - 1
            if(data[a][b] == 1) :
                break
            else :
                ta = a
                count += 1
            
        if(d == 3) :
            b = b + 1
            if(data[a][b] == 1) :
                break
            else :
                tb = b
                count += 1
        
        
print(count)      
    

        

