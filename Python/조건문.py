##a = 11
##if a > 10 :
##    print('a는 10보다 큽니다.')
##else :
##    print('a는 10보다 작거나 같습니다.')

##id = 'elk'
##pw = '1234'
##
##userid = input('사용자 아이디 : ')
##userpw = input('사용자 비밀번호 : ')
##
##if id == userid:
##    if pw == userpw:
##        print('로그인 되었습니다.')
##    else:
##        print('비밀번호가 틀렸습니다.')
##else:
##    print('아이디가 틀렸습니다.')


##subject = input('좋아하는 과목은 ? : )
##
##if subject == 'python' :
##    print('내가 좋아하는 과목은 파이썬입니다.')
##elif subject == 'java' :
##    print('내가 좋아하는 과목은 자바입니다.')
##elif subject == 'C#' :
##    print('내가 좋아하는 과목은 C#입니다.')
##elif subject == 'node.js' :
##    print('내가 좋아하는 과목은 node.js입니다.')
##else:
##    print('그런거 없다.')


##shortcut = int(input('단축키를 입력하세요 : '))
##if shortcut == 1:
##    print("엄마 : 010-xxxx-xxxx")
##elif shortcut == 2:
##    print("아빠 : 010-xxxx-xxxx")
##elif shortcut == 3:
##    print("친구 : 010-xxxx-xxxx")
##else:
##    print("해당 단축키가 없습니다.")


##month = int(input("해당 달을 입력하세요 : "))
##if month <= 2 or month == 12:
##    print("해당 계절은 겨울입니다.")
##elif month > 2 and month < 6:
##    print("해당 게절은 봄입니다.")
##elif month > 5 and month < 9:
##    print("해당 계절은 여름입니다.")
##elif month > 8 and month < 12:
##    print("해당 계절은 가을입니다.")
##else:
##    print("잘못 입력하셨습니다.")


#0부터 100까지, 91~100은 A학점..
##score = int(input("당신의 점수를 입력하세요 : "))
##if score <= 100 and score > 90:
##    print("해당 학점은 A입니다.")
##elif score > 80 and score < 91:
##    print("해당 학점은 B입니다.")
##elif score > 70 and score < 81:
##    print("해당 학점은 C입니다.")
##elif score > 60 and score < 71:
##    print("해당 학점은 D입니다.")
##elif score < 61:
##    print("해당 학점은 F입니다.")
##else:
##    print("알맞은 값은 점수를 입력해주세요.")


#자판기
##print('=====자판기 메뉴=====')
##print('1.음료 1000원, 2.과자 2000원 3.껌 500원')
##print()
##
##cracker = 2000
##drink = 1000
##ggum = 500
##
##money = int(input('insert Coin : '))
##
##if money >=  cracker:
##    print("과자, 음료, 껌 모두 구매할 수 있습니다.")
##elif money < cracker and money >= drink:
##    print("음료, 껌을 구매할 수 있습니다.")
##elif money < drink and money >= ggum:
##    print("껌을 구매할 수 있습니다.")
##else:
##    print("아무것도 구매할 수 없습니다.")


if money >= cracker:
    pass
else:
    print("신분증을 제시하세요.")

