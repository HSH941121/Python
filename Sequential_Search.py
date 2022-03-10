def sequential_search(n,target,array) :

    for i in range(n) :

        if array[i] == target :
            return i + 1


print("생성할 원소 개수를 입력하시고 한칸띄운다음 입력하시오")
input_data = input().split()

n = int(input_data[0])
target = input_data[1]


print("원소 개수 만큼 입력하시오")
array = input().split()

print(sequential_search(n,target,array))
