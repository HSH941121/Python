arr = [3,2,6]
divisor = 10
answer = []
sw = False
for i in range(len(arr)) :
    if arr[i] % divisor == 0 :
        answer.append(arr[i])
        sw = True
if sw == False :
    answer.append(-1)
answer.sort()

print(answer)
