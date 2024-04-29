###딕셔너리변수 = {키1 : 값1, 키2: 값2...} #object형
## 
##product = {'컵라면' : 1000, '삼각김밥' : 2000, '음료수' : 1500 }
##
##print(product) # {'컵라면' : 1000, '삼각김밥' : 2000, '음료수' : 1500 }
##
##product['오뎅'] = 2000
##product['아이스크림'] = 3000
##
##print(product)
### {'컵라면': 1000, '삼각김밥': 2000, '음료수': 1500,
###'오뎅': 2000, '아이스크림': 3000}
##
##del(product['오뎅']) #'오뎅'의 key-value를 지운다.
##
##print(product)
### {'컵라면': 1000, '삼각김밥': 2000, '음료수': 1500, '아이스크림': 3000}
##
##
###딕셔너리이름.get(키)
##print(product.get('컵라면')) #1000(value값)
##
###딕셔너리이름.keys()
##print(product.keys())
###dict_keys(['컵라면', '삼각김밥', '음료수', '아이스크림'])
##
##
###딕셔너리이름.values()
##print(product.values()) # dict_values([1000, 2000, 1500, 3000])
##
##
### dict_어쩌구 나오는거 불편하다. 가려달라.
##print(list(product.values())) #list로 가리면 해결! keys()도 똑같음.
##
##
### index에서 값을 찾고 싶은데요.
##
##item = input('상품을 입력하세요 : ')
##
##if item in product: #for in 문과 비슷하게 사용되는 형태.
##    
##    print('상품이 있습니다.')
##else:
##    print('상품이 없습니다.')
##    
##word = {'boy' : '소년', 'girl' : '소녀', 'family' : '가족' }
##print(word)


#나라 : 수도
capital = {
    '네팔': '카트만두',
    '대한민국': '서울',
    '일본': '도쿄',
    '중국': '베이징',
    '이탈리아': '로마',
    '러시아': '모스크바',
    '독일': '베를린',
    '미국': '워싱턴',
    '이라크': '바그다드',
    '인도': '뉴델리',
    '브라질': '브라질리아',
    '캐나다': '오타와',
    '룩셈부르크': '룩셈부르크',
    '헝가리': '부다페스트'
}

while(True):
    country = input(str(list(capital.keys())) + ' 해당 나라의 수도는 어디일까요? ')

if country in capital:
    print(country, '의 수도는 ', capital.get(country), ' 입니다.')
elif country == 'q':
    break;
else:
    print('그런 나라는 없습니다'.)

# 세미콜론을 사용할 수 있지만, 권장하지는 않는다.

    
