n,k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i in range(k) :
    A = sorted(A)
    B = sorted(B,reverse=True)

    A[0] , B[0] = B[0], A[0]


print(sum(A))
