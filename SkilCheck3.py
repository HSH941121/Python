List = []
x = 13
sum = 0
while True :
    if x <=0 :
        break
    List.append(x % 10)
    x = x // 10

for i in range(len(List)) :
        sum = sum + List[i]
if x % sum == 0 :
    print("True")
else :
    print("else")

print(List)
print(sum)
