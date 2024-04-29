# 함수의 정의? void

## c언어에서는 int plus(int a , int b { retunr a + b; } 방식으로 지원함.
## JS에서는 function plus(a,b) { return a + b }
## 파이썬에서의 예제는?

##def plus(a,b):
##    return a + b
##
##def minus(a,b):
##    return a - b
##
##def multiple(a,b):
##    return a * b
##
##
##def divide(a,b):
##    return a / b
##
##num1 = int(input('첫번째 수 : '))
##num2 = int(input('두번째 수 : '))
##
##print(plus(num1,num2))
##print(minus(num1,num2))
##print(multiple(num1,num2))
##print(divide(num1,num2))


#구구단 함수로 만들기

##dan = int(input('단수를 입력하세요 : '))
##
##for val in range(1, 10, 1):
##    print('%d * %d = %d' % (dan, val, dan * val))
##
###실제로 묶어보기
##
##/
##dan = int(input('단수를 입력하세요 : '))
##
##def gugudan(dan):
##    for val in range(1, 10, 1):
##        print('%d * %d = %d' % (dan, val, dan * val))
##

###내부 서버에 존재하는 내용
##id = 'jamsuham'
##pw = '1234'
##
### 로그인 구현 로직. 맞는지 아닌지 확인한다.
##def account(Pid, Ppw): 
##    if id == Pid:  # 전역 변수 id 대신에 함수의 매개변수 Pid를 사용
##        if pw == Ppw:  # 전역 변수 pw 대신에 함수의 매개변수 Ppw를 사용
##            print('로그인 되었습니다.')
##        else:
##            print('비밀번호가 틀렸습니다.')
##    else:
##        print('아이디가 틀렸습니다.')
##
### 내가 form에 입력하는 값
##userid = input('사용자 아이디 : ')
##userpw = input('사용자 비밀번호 : ')
##
##account(userid, userpw)



##def coffee_Machine(sel_coffee):
##	print("1. 물을 준비한다.")
##	print("2. 컵을 준비한다.")
##
##	if coffee == "1" or coffee == "아메리카노":
##	    print("3-1. 아메리카노를 탄다.")
##	elif coffee == "2" or coffee == "카페라떼":
##	    print("3-2. 카페라떼를 탄다.")
##	elif coffee == "3" or coffee == "카페모카":
##	    print("3-3. 카페모카를 탄다.")
##	else:
##	    print("3-4. 해당 사항이 없습니다.")
##	print('4. 물을 붓는다.')
##	print()
##
##
###주문
##for val in range(0, 3, 1):
##    coffee = input("메뉴판을 보고 커피를 선택해주세요. \n 1. 아메리카노 \n 2. 카페라떼 \n 3. 카페모카 " + " \n select : ")
##    print()
##
##    coffee_machine(coffee)
##    print('서비스 완료')

hap = 100

def sum(value):
    global hap
    hap = hap + value
    print(hap)

sum(10)
print(hap)




