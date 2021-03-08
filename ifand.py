print('수를 입력하세요')

a = int(input())

if a > 10 and a % 2 == 0:
    print('10보다 큰 짝수입니다.')
    
elif a > 10 and a % 2 != 0:
    print('10보다 큰 홀수입니다.')
    
elif a % 2 == 0:
    print('10보다 작은 짝수입니다.')
    
else:
    print('10보다 작은 홀수입니다.')
