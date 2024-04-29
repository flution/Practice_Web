##bus = 10
##taxi = 20
##truck = 30
##
###변수를 10개, 100개로 늘려주면 힘드니까. 배열을 등장시킨다.
##
##sum = bus + taxi + truck
##print(sum)

##리스트이름 = [값1, 값2, 값3] #이렇게 쓰면 된다고?


##total_sum = 0;
##ktx = [1,2,3,4,5,6,7,8,9,10]
##
##for i in range (0, 10, 1):
##    total_sum += ktx[i]
##
##for i in range (0, 100,):
##    ktx.append(i)
##
##print(ktx)
##
##print(total_sum)


##ktx = []
##
##for i in range(0, 100):
##    ktx.append(i)
##
##for i in range(0, 100):
##    print(ktx[i]

#리스트에 들어갈 수 있는 것들.
##ktx = []
##ktx = [1,2,3,4,5]
##ktx = [3.14, 1.59, 2.65]
##ktx = ["대한민국은", "민주공화국이다"]
##ktx = [1,2,'박수',4,5,'박수']

#리스트의 인덱스 범위 지정하는 법
#리스트이름[시작인덱스 : 끝인덱스미만]
##ktx = [10,20,30,40,50,60,70]
##print(ktx[0 : 2])
##print(ktx[0 : 3])
##
##
###리스트이름[:끝인덱스 +1]
###리스트이름[시작인덱스 :]
##
##print(ktx[ :3])
##print(ktx[3:])


#리스트 + 리스트

##ktx = [10,20,30,40]
##srt = [40,50,60]
##
##ktx[1:3] = [] #이렇게 하면 20,30이 소실되고 [10,40] 

##print(ktx + srt) #리스트끼리 더하는거? 가능
##print(ktx * 3) #리스트를 곱해서 3번 순회하는것? 가능.
##
###index[i] = x 이렇게도 수정 가능함
##ktx[0] = 100
##ktx[2] = 300

##ktx[2:3] = [300,301,302] # index[2]에 이중 리스트를 삽입하겠다.
##ktx[2] = [300,301,302] = 이렇게 하면 [10,20,[300,301,302],40]
##Q. 그럼 이차원 배열을 빼는 방법은 없을까? 배열을 통째로 or 이차원 배열의 요소만.
##print(ktx) # [10,20,300,301,302,40]
##del(ktx[2]) # 300을 삭제하였다
##print(ktx)# [ 10,20,301,302,40 ]




#리스트의 메소드들 사용하기
ktx = [10,20,30,40]

print('현재 리스트: ', ktx) # [10,20,30,40]

ktx.append(50) # [ 10,20,30,40,50 ]
print('append 함수 사용 : ', ktx)

ktx.pop()
print('pop 함수 사용 : ', ktx) # [ 10,20,30,40]

ktx.reverse()
print('reverse 함수 사용 : ', ktx) # [ 40,30,20,10 ]

ktx.sort()
print('remove 함수 사용 : ', ktx) # [10,20,30,40 ]

ktx.insert(1, 'data')
print('insert 함수 사용 : ', ktx) # [10,"data",20,30,40 ]

tgv = [100,200,300]
ktx.extend(tgv) # [10, "data", 20, 30, 40, 100, 200, 300 ]
#ktx = ktx + tgv
print('extend 함수 사용 : ', ktx) #
print('+ 사용 : ', ktx + tgv) # [10, "data", 20, 30, 40, 100, 200, 300, 100, 200, 300 ]
#왜냐하면 이미 ktx = ktx + tgv 상태에서 + tgv를 다시 해준거임.

cntlist = len(ktx)
print("len 함수 : ", cntlist) # len함수는 7.
       
