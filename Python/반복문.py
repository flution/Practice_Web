##for num in range(0, 5, 1):
##    print('programming')



##sum = 0
##
##for i in range(1, 11, 1):
##    sum += i
##print(sum)


###입력한 값의 범위 알아맞히기
##
##favorite = int(input('내가 가장 좋아하는 숫자는?'))
##
##start = int(input('범위 시작값'))
##end = int(input('범위 끝값'))
##
##for i in range(start, end, 1):
##    if favorite == i:
##        print('내가 좋아하는 숫자가 있습니다')
##    else:
##        print('범위 밖입니다. 다시 입력해주세요')

##dan = int(input("몇 단을 적어드릴까요? : "))
##val = 0
##for val in range(1, 10, 1):
##    print('%d * %d = %d' % (dan, val, dan*val))

##for dan in range(2, 10, 1):
##	for val in range(1, 10, 1):
##		print('%d * %d = %d' % (dan, val, dan*val))
##	print()

##print('*')
##print('**')
##print('***')
##print('****')
##print('*****')
##
##star = '*'
##
##for col in range(1, 6, 1):
##    for row in range(0, col, 1):
##        print(star, end = '') #왜 공백을 썼냐? 안주면 위아래로 찍혀요!
##

##sum  = 0
##val = 1
##
##while val < 101:
##    if val % 2 != 0:
##        sum = sum + val
##    val = val + 1
##    
##    
##print('1부터 100까지의 홀수의 합 : ', sum)


#사용자로부터 단수를 입력받아 구구단 출력

##val = 1
##dan = 2
##
##while val < 10:
##    print(dan, '*', val, '=', dan * val)
##    print(str(dan) + '*' + str(val) + ' = ' + str(dan * val))
##    print('%d * %d = %d' % (dan, val, dan*val))
##    val += 1
##무한 루프는 수행 조건에 의해서 언젠가는 조건이 무너질 수 있게 설계해야 한다.

##hap = 0
##inum = 0
##
##while True:
##    inum = int(input("정수를 입력하세요 : "))
##    hap += inum
##    if inum == -1:
##        break
##    print('누적된 합 : ' + str(hap))

## 1부터 100까지, 브레이크 예제. - 배터리 예제와 비슷하다.
##a = 0
##while True:
##    if a > 100:
##        break
##    print('a :', a)
##    a = a + 1
##print('a는 100보다 크다')


#continue문

a = 0
while a < 100:
    a = a + 1
    if a > 80 and a < 90:
        continue
    print('a는 : ', a)















