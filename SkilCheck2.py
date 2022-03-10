
arr1 = [9,20,28,18,11]
arr2 = [30,1,21,17,28]
arr1t = [0] * len(arr1)
arr2t = [0] * len(arr2)
answer = []
for i in range(len(arr1)) :
        a = list(bin(arr1[i])[2:])
        b = list(bin(arr2[i])[2:])
        if len(a) < 5 :
            while len(a) < 5 :
                a.insert(0,0)
        if len(b) < 5 :
            while len(b) < 5 :
                b.insert(0,0)
        arr1t[i] = a
        arr2t[i] = b

for i in range(5) :
    for j in range(5) :
        if arr1t[i][j] == 1 or arr2t[i][j] == 1 :
            answer.append('#')
        else :
            answer.append(" ")

print(answer)
