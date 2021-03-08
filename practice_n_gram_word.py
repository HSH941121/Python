n = int(input('단위를 입력해주세요'))
text = input('단어를 입력해주세요')
word = text.split()

if len(word) < n:
    print('Wrong')
else:
    for i in range(len(word) - (n-1)):
        for j in range(n):
            print(word[i+j],end=' ')

        print()
        
