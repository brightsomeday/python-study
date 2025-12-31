# sample_list = ['1','2',4,'heloo']

# print(sample_list[0])



# sample_list = '1234'

# print(sample_list[0])



# sample_list = '1234'

# print(len(sample_list))



# sample_list = [1,2,3,4]

# print(len(sample_list))



# list1 = list()

# # 문자열을 리스트로
# strlist = list("codingOn")

# print(list1, '첫번쨰 확인')
# print(strlist, '데이터 값 들어온거 확인용')



# #인덱스 설명
# sample = [1,123,4,21,34,2,3,4,123,4,21,3,412,3,42134,4000]

# print(sample[int(len(sample)/2)])



# fruits = ["aplle", "banana", "cherry"]

# fruits[0] = "orange"

# print(fruits)



# #슬라이싱
# nums= [10,20,30,40,50,60,70,80,90]

# print(nums[0:4])


# #슬라이싱은 끝나는 자리부터 세지 않는다
# nums= [10,20,30,40,50,60,70,80,90]

# print(nums[-1:-4])

# #하지만 이건 가능하다
# nums= [10,20,30,40,50,60,70,80,90]

# print(nums[-4:-1])


# # 역순으로 만들기
# nums= [10,20,30,40,50,60,70,80,90]

# print(nums[::-1])

# nums= 'ABCDEFG'

# print(nums[::-1])



# # 실습 1.
# nums = [10, 20, 30, 40, 50]
# print(nums[0], nums[4])

# nums = [100, 200, 300, 400, 500, 600, 700]
# print(nums[2:5])

# nums = [1,2,3,4,5]
# nums[0] = nums[0]*2
# nums[1] = nums[1]*2
# nums[2] = nums[2]*2
# nums[3] = nums[3]*2
# nums[4] = nums[4]*2
# print(nums)

# items = ["a","b","c","d","e"]
# print(items[::-1])

# data=["zero","one","two","three","four","five"]
# print(data[0:10:2])

# movies = ["인셉션","인터스텔라","어벤져스","라라랜드","기생충"]
# movies[2] = "매트릭스"
# movies[3] = "타이타닉"
# print(movies)

# subjects=["국어","수학","영어","물리","화학","생물","역사","지구과학","윤리"]
# list1=subjects[3:6]
# print(list1)

# data=["A","B","C","D","E","F","G","H","I"]
# list1=data[0:3]
# list2=data[3:6]
# list3=data[6:9]
# print(list1[::-1],list2[::-1],list3[::-1])



# #리스트 요소 삭제 -del
# #리스트 연산 - 포함 여부 검사(in, not in)
# # 실습2
# fruits = ["apple", "banana", "cherry", "grape", "watermelon", "strawberry"]
# del fruits[1:4]
# print(fruits)

# letters = ["A", "B"]
# letter=letters*3
# del letter[2]
# print(letter)



# # append(x): 리스트 끝에 요소 추가 -> 리스트 마지막에 하나의 요소를 추가함
# # extend(iterable): 리스트 끝에 여러 요소 추가 -> 다른 리스트나 이터러블의 모든 요소를 추가함
# # insert(index,x): 원하는 위치에 요소 삽입 -> 지정된 인덱스에 요소를 삽입함
# # remove(x): 특정 값을 찾아 삭제 -> 가장 처음 발견된 해당 값(x)을 삭제함
# # pop(index): 인덱스 요소를 꺼내고 삭제 -> 인덱스를 지정하면 해당하는 인덱스의 요소를 삭제하고 반환함
# #                                   -> 인덱스를 지정하지 않으면 마지막 요소를 삭제하고 반환함
# # 리스트 정렬 : sort(), sorted() -> sort:오름차순,sorted:내림차순
# # reverse(): 리스트 요소 뒤집기 -> 원본 변경
# # count(x):값의 개수 세기
# # max(),min(): 최대/최소값 찾기
# # sum(): 요소들의 합 구하기



#실습
day1 = int(input("1일차 소비 금액 : "))
day2 = int(input("2일차 소비 금액 : "))
day3 = int(input("3일차 소비 금액 : "))
day4 = int(input("4일차 소비 금액 : "))
day5 = int(input("5일차 소비 금액 : "))
day6 = int(input("6일차 소비 금액 : "))
day7 = int(input("7일차 소비 금액 : "))
day8 = int(input("8일차 소비 금액 : "))
day9 = int(input("9일차 소비 금액 : "))
day10 = int(input("10일차 소비 금액 : "))

#data list 작성
data = [day1, day2, day3, day4, day5, day6, day7, day8, day9, day10]

#data 마지막에 5000원 추가
data.append(5000)

#data 앞에 3000원 추가
data.insert(0,3000)

#data에 0을 삭제
data.remove(0)

#부분분석하기
#처음 5일 분석
data1=data[0:5]
#마지막 5일 분석
data2=data[6:11]

#계산
#전체 소비 금액
datasum=sum(data)
#전체 소비 금액 평균
data_average=datasum/len(data)
#처음 5일 소비 금액 평균
data1_average=sum(data1)/len(data1)
#마지막 5일 소비 금액 평균
data2_average=sum(data2)/len(data2)

# data copy값 만들기
data_copy=data
#data_copy 수정
data_copy=data_copy[1:10]

print(f"""처음 5일 : {data1}
마지막 5일 : {data2}
총 소비 : {datasum}
전체 평균 : {data_average}
처음 5일 평균 : {data1_average}
마지막 5일 평균 : {data2_average}
수정된 리스트 : {data_copy}
원본 리스트 : {data}""")