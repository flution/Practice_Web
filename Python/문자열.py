#문자열의 기본
##print('I' + ' love ' + 'you')
##
##str1 = 'i '
##str2 = 'love '
##str3 = 'you '
##
##result = str1 + str2 + str3
##
##print(result)
##
##
###곱하기
##print('-' * 30)
##print('I '+ 'love ' *3 + 'you')
##print('-' * 30)

#문자열 변수
##char str[10] = "abcde";
##str[1] = 'l'

##str = '답은 정해져 있어 너는 대답만 해'
##print(str[0], end='') #답
##print(str[3], end='') #정
##print(str[10], end='') #너


##str1 = '다시 합창 합시다'
##str2 = ''
##
##count = len(str1)
##for i in range(0, count):
##    str2 += str1[count - (i+!)]
##
##print('str1 : ', str1)
##print('str2 : ', str2)


#문자열 잘라서 출력하기
##str = 'To be or not to be'
##
##print(str[0] + str[1] + str[2] + str[3] + str[4])
##print(str[0:5]) # index[0]부터 index[4]까지 출력하라. #To be
##print(str[6:8]) # or
##print(str[9:16]) # not to
##
##print(str[0:]) # 전체 문자 다 나오게
##print(str[:8]) # To be or
##print(str[: ]) 


#문자열 서식
#현재 시간은 5시입니다. % 5 (정수는 그냥 넣어도 괜찮아)~
#체온은 36.5도입니다. %f (실수는 %f 처리할 것.)
#'나는 %s에 살고 있습니다.% '서울'

#%d, %f, %s, %c %o %x 이런것들.


##value = int(input('정수값을 입력하세요 : '))
##print('현재 시간은 %d시 입니다.' % value)
##
##value = float(input('실수값을 입력하세요 : '))
##print('현재 체온은 %.1f도 입니다.' % value)
##
##value = input('문자열을 입력하세요 : ')
##print("나는 %s에 살고 있습니다." % value)

#let a = { const name, const age }


##a = (1,2,3)
##a = (4,5,6)
##print(id(a))
##
##
##print(id(a),a)

#강수 확률은 60%입니다.

##print('강수 확률은 %d%%입니다.' % 60)

#'현재 시간은 {0}시 {1}분 입니다.' .format(12 30) => 문자열 안에 {} 에 서을 넣어준다.

##print('현재 시간은 {0}시 {1}분 입니다.'.format(12,30))

#시와 분 입력받게 하기

##value1 = int(input('지금은 몇 시입니까?'))
##value2 = int(input('지금은 몇 분입니까?'))
##print('현재 시간은 {0}시 {1}분 입니다.'.format(value1,value2))
##
##value1 = input('문자열을 대입하세요')
##print('나는 {0}에 살고 있습니다.'.format(value1))



# 24-04-29 날짜에 시작한 부분들.


### 문자열의 개수 알아내기 count
##개수 = 문자열.count('검색할 문자 또는 문자열')
##
##string1 = '간장 공장 공장장은 강 공장장이고 된장 공장 공장장은 공 공장장이다.'
##
##chr1 = string1.count('공')
##chr2 = string1.count('장')
##
##print('공의 개수 : %d' % chr1)
##print('장의 개수 : %d' % chr2)
##
##string2 = '내가 그린 기린 그림은 잘 그린 기린 그림이고 네가 그린 기린 그림은 잘 못 그린 기린 그림이다.'
##
##str1 = string2.count('그린')
##str2 = string2.count('기린')
##str3 = string2.count('그림')
##
##print('그린의 개수 : %d' % str1)
##print('기린의 개수 : %d' % str2)
##print('그림의 개수 : %d' % str3)


#새로운 문자열 = 구분자.join(문자열) / 구분자.join(리스트)

##train_str = '칙칙폭폭'
##
##div_str = '-'.join(train_str)
##
##print(div_str)

##ani_list = ['강아지', '고양이', '원숭이', '코끼리']
##div_list = '+'.join(ani_list)
##print(div_list)

##time_list = ['09', '48', '50']
##
##div_list = ':'.join(time_list)
##print(div_list)

#리스트 = 문자열.split(구분자)

##planet_str = '수성-금성-지구-화성-목성'
##
##planet_list = planet_str.split("-")
##
##print(planet_list)


##time_str = '09시:54분:10초'
##time_list = time_str.split(':')
##print(time_list)

#대소문자 변환
#변경된 문자열 = 문자열.upper()
#변경된 문자열 = 문자열.lower()

##eng_str = input('영문자를 입력하세요')
##
##upper_str = eng_str.upper()
##lower_str = eng_str.lower()
##
##print('대문자로 변환 : %s' % upper_str)
##print('소문자로 변환 : %s' % lower_str)

#문자열 공백 제거 trim(0 , strip()

##string1 = '  죽는 날까지 하늘을 우러러'
##print(string1)
##lstrip_str = string1.lstrip()
##print(lstrip_str)
##
##string2 = '  잎새에 이는 바람에도 '
##print(string2)

##isXXXX

#문자열.isalpha()
#문자열.isupper()
#문자열.islower()
#문자열.isspace()

##string1 = input('문자열을 입력하세요 : ')
##
##if string1.isalpha():
##    print('문자열은 글자로 구성되어 있습니다.')
##    if string1.isupper():
##        print('문자열은 대문자로 구성되어있습니다.')
##    elif string1.islower():
##        print('문자열은 소문자로 구서오디어 있습니다.')
##elif string1.isdigit():
##    print('문자열은 숫자로 구성되어 있습니다.')
##elif string1.isspacce():
##    print('문자열은 공백으로 구성되어 있습니다.')
##else:
##    print('출력할 수 없는 입력값입니다.')


##fp = open('C:/Users/fluti/Documents/Kosta/Python/test.txt', 'r', encoding='utf-8')
##ansi 파일을 읽는데 왜죠?
##str =fp.read()
##print(str)
##fp.close()
##
##한 라인씩 읽기
##strline = fp.readline()
##print(strline)
##
##while 문 이용해서 끝까지 읽게 하기
##while True:
##    strline = fp.readline()
##    if strline == '':
##        break
##    print(strline)
##
##한 라인이 아니라 통째로 읽기
##readlines() => list 타입으로 리턴한다. / text기반만 가능
##
##strline = fp.readlines()
##print(strline)
##
##그렇다면, 반복문을 이용해서 편하게 잘라보자
##for strlist in strline:
##    print(strlist)
##
##fp.close()
##
##반환값 = os.path.exists(파일명), 파일 시스템
##파일에 접근하려면 os가 필요하다.
##
##import os
##
##fName = r'C:\Users\fluti\Documents\Kosta\Python\test.txt'
##
##if os.path.exists(fName):
##    fp = open(fName, 'r', encoding= 'utf-8')
##    with open(fName, 'r', encoding = 'utf-8') as fp:
##        #with써서 open() close()를 없앰.
##        strline = fp.readlines()
##
##    for strlist in strline:
##        print(strlist)
##
##    fp.close()
##else:
##    print("%s 파일은 존재하지 않습니다.")
##
##
##파일객체.write(입력 문자열)
##    
##fName = r'C:\Users\fluti\Documents\Kosta\Python\test2.txt'
##
##파일을 쓰기 모드로 열겠다. 'w'는 / 'r'은 파일을 읽기모드로 열겠다(수정X)
##이걸 사용하면, txt 파일이 만들어 지는 개념임.
##이걸 가지고 복사기능을 만들 수 있을 것이다. r/w만 알게되면.
##with open(fName, 'w') as fp:
##    while True:
##        instr = input('데이터 입력 : ')
##
##        if instr == '\q':
##            break
##        fp.writelines(instr + '\n')



# 4교시 시작
## 파일 복사
##
##import os
##
##srcfile = 'C:/Users/fluti/Documents/Kosta/Python/test.txt' # 소스 파일 경로
##destfile = 'C:/Users/fluti/Documents/Kosta/Python/dest.txt' # 대상 파일 경로
##
##if os.path.exists(srcfile): #소스파일이 있나요 혹시?
##    sfp = open(srcfile, 'r', encoding = 'utf-8') #소스파일을 읽기전용으로 열어주십쇼
##    dfp = open(destfile, 'w', encoding = 'utf-8') #복제할 파일을 쓰기전용으로 읽어주십쇼.
##
##    slist = sfp.readlines() #리스트 형태로 한줄 한줄 읽어오는 readlines()
##    for instr in slist: #slist에서 instr을 하나하나 대조하며 반복하라
##        dfp.writelines(instr) #dfp에 instr 파일을 한줄한줄 써라.
##
##    sfp.close() # 얘도.
##    dfp.close() #계속 열려있어서 입구 뚫리기 싫으면 닫아두도록 해라.
##else:
##    print('복사할 수 없습니다.')


#이미지 복사(바이너리 파일 복사)

##import os
##
##srcfile = 'C:/Users/fluti/Documents/Kosta/Python/wheat_fox.jpg' # 소스 파일 경로
##destfile = 'C:/Users/fluti/Documents/Kosta/Python/wheat_fox_copy,jpg' # 대상 파일 경로
##if os.path.exists(srcfile): #소스파일이 있나요 혹시?
##    sfp = open(srcfile, 'rb') #소스파일을 읽기전용으로 열어주십쇼
##    dfp = open(destfile, 'wb') #복제할 파일을 쓰기전용으로 읽어주십쇼.
##
##    while True:
##        sbyte = sfp.read()
##        if not sbyte:
##            break
##        dfp.write(sbyte)
##        
##      
##    sfp.close() # 얘도.
##    dfp.close() #계속 열려있어서 입구 뚫리기 싫으면 닫아두도록 해라.
##    print('wheat_fox.jpg 파일을 복사하였습니다.')    
##else:
##    print('wheat_fox.jpg 파일을 복사하지 못했습니다.')





