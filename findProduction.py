n = int(input())
array1 = list(map(int,input().split()))
m = int(input())
array2 = list(map(int,input().split()))

array1 = sorted(array1)


def binary_search(array,target,start,end) :

    
    while start <= end :
        mid = (start + end) // 2
        if target == array[mid] :
            return 'yes'

        elif target > array[mid] :
            start = mid + 1

        else :
            end = mid - 1
    return 'no'

for i in array2 :
    result = binary_search(array1,i,0,n-1)
    print(result,end = ' ')

