# name, age, grade = "Alice", 14, 2
# print('이름:', name)
# print('나이:', age)
# print('학년:', grade)



# a, b, c, d = 10 + 5, (3*4) - 2, 7 // 2 + 1, 2 ** 3 % 5
# print(a, b, c, d)



# x = 1
# y = 2
# x, y = y, x
# print(x, y)



# a = 1
# b = 3.14
# c = '안녕'
# d = True
# print(type(a))  
# print(type(b))  
# print(type(c))  
# print(type(d))        # type을 쓰는 이유 = 숫자, 문자인지 확인하여 비교를 하기 위해 사용



# # 가능한 경우

# print(int(3.7))         # 3(소수점 이하 절삭) -> 프로그램 중 소수점나올 경우 날리고 싶을때 int로 날리면 됨
# print(int("10"))        # 10
# print(int(True))        # 1     True는 파이썬에서 1이다
# print(int(False))       # 0     False는 파이썬에서 0이다

# #불가능한 경우 (에러발생)

# print(int("3.14"))      # valueError : invalid literal
# print(int("abc"))       # valueError



# cat = '고양이'
# age = 15
# gender = '수컷'
# name = '꽁꽁이'
# skill = '냥냥 펀치'

# print(f'우리집 {cat}은 나이가 {age}살이고 성별은 {gender}입니다.\n이름은 {name}이고 주특기는 {skill}입니다.')
# # f를 붙이면 변수의 내용이 들어가고 f를 붙이면 {cat}값이 나온다. 왜...? 파이썬은 +를 지원하지 않아 사용
# # 장점 : 자료형의 번환 없이 문자열과 정수를 함께 넣을 수 있다는 점



# Title = '아바타: 불과 재'
# condition = '상영중'
# day = "2025.12.17."
# story = '판도라를 위협하는 재의 부족, 더 이상 인간만이 적이 아니다! 모두의 운명을 뒤흔들 거대한 전투가 시작된다! 인간들과의 전쟁으로 첫째 아들 ‘네테이얌’을 잃은 후, ‘제이크’와 ‘네이티리’는 깊은 슬픔에 빠진다. 상실에 빠진 이들 앞에 바랑이 이끄는 재의 부족이 등장하면서, 판도라는 더욱 큰 위험에 빠지게 되고, ‘설리’ 가족은 선택의 기로에 서게 되는데…'
# nation = '미국'
# b = 8.15
# a = 8.95
# ranking = '1위/417만명'

# print(f'영화 제목은 {Title}이고 상영 상태는 {condition}입니다.\n개봉 날짜는 {day}이고 줄거리는 {story}입니다.\n장르 국가는 {nation}이고 실 관람객 평점은 {str(real_rating)}이지만 네티즌 평점은 {str(rating)}입니다.\n순위와 누적 관객수는 {ranking}입니다.')



# name = '신재욱'
# age = '27'
# MBTI = 'ENFP'
# hobby = "클라이밍"
# specialty = '경청하기'
# Ffood = '고기'
# Hfood = '참외'
# blood_type = 'O형'
# Fgame = '롤'
# Fsport = '야구'
# region = '포항'
# Fcolor = '하얀색'
# brithday = '4/29'
# Fteam = '두산'
# Fsing = 'Duet'
# Fmovie = '님아 그 강을 건너지 마시오'
# Fdrink = '물'
# Fnation = '스위스'
# respect_person = '아인슈타인'
# Fcoffee = '아아'

# print(f'저의 이름은 {name}이고 나이는 {age}입니다.\n취미는 {hobby}이고 MBTI는 {MBTI}입니다.\n특기는 {specialty}이고 좋아하는 음식은 {Ffood}와 싫어하는 음식은 {Hfood}입니다.\n혈액형은 {blood_type}이고 좋아하는 게임은 {Fgame}입니다.\n좋아하는 스포츠는 {Fsport}이고 고향은 {region}입니다. 좋아하는 색은 {Fcolor}이고 생일은 {brithday}입니다. 좋아하는 야구팀과 음악은 {Fteam}이랑 {Fsing}이고 좋아하는 영화는 {Fmovie}입니다. 좋아하는 음료는 {Fdrink}이지만 좋아하는 커피는 {Fcoffee}입니다. 좋아하는 국가는 {Fnation}이고 존경하는 인물은 {respect_person}입니다.')



# pay = 300000
# book = 80000
# luanch = 9000
# day = 5
# work = 120000
# money=(pay-book-luanch*day+120000)*1.2*(2/3)
# print(int(money))

# # 시작 용돈
# money = 300000

# # 책 구매
# money -= 80000

# # 평일 점심값(9천원씩 5일간)
# money -= 9000*5

# # 과외 알바 수입
# money += 120000

# # 부모님 추가 용돈 (현재 금액의 20%)
# money += money*0.2

# # 전기요금 등으로 1/3 지출
# money -= money / 3

# # 최종
# print(f"최종 남은 금액 : {int(money)}원")


























