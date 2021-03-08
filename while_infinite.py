while True:
    print('반복을 계속 할까요??')

    answer = input()

    if answer == '예':
        print('반복을 계속합니다..')
    elif answer == '아니오':
        print('반복을 종료하니다..')
        break

    else:
        print('잘못된 입력입니다..')
