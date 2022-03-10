n,m,k = map(int,input().split())
data = list(map(int,input().split()))
data.sort()
data.reverse()
L1 = data[0]
L2 = data[1]
sum = 0
count = 0
while True :
         for i in range(k) :
             if(count >= m) :
                 break
             count += 1
             sum += L1
             print(sum,count)
         if(count >= m) :
             break
         sum += L2
         count += 1
         print(sum,count)
      


         

