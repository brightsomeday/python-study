# 실습 3. 접근 제어와 정보은닉 연습
# 문제1. UserAccount 클래스 : 비밀번호 보호

class Useraccount:
    
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def show(self):
        print(self.username)
        print(self.__password)

    def get_password(self):
        return self.__password

useraccount = Useraccount("신재욱", "qwer1234")
print(useraccount.username)
print(useraccount.get_password())



# # 문제 2. Student 클래스 : 성적 검증(@property 사용)
# class Studnet:
#     def __init__(self, score):
#         self.__score = score

#     def set_volume(self, score):
#         if 0 <= score <= 100:
#             self.__score = score
#         else:
#             print("점수는 0~100 사이만 가능합니다.")

#     def get_volume(self):
#         return self.__volume

# sp = Speaker()
# a = int(input("입력하세요:"))
# sp.set_volume(a)                                            # 잘 변경 됨

# print(sp.get_volume())