# # try exept     가장 기본 예제

# try: # 예외가 발생할 수 있는 코드
#     num = int(input("숫자를 입력하세요."))
#     print("입력한 숫자: ", num)     # 에러시 출력 안됨
# except ValueError:  # 예외가 발생했을 때 실행할 코드
#     print("숫자가 아닌 값을 입력했습니다.")

# # int() 변환 실패 -> ValueError
# # 프로그램이 바로 죽지 않고 메시지 출력




# try:
#     a = int(input("첫번쨰 숫자: "))
#     b = int(input("두번쨰 숫자: "))
#     result = a/b
#     print("결과: ", result)

# except ValueError:
#     print("숫자만 입력해야 합니다.")
# except ZeroDivisionError:
#     print("0으로 나눌 수 없습니다.")
# else:       # try가 성공했을 때만 실행 -> 에러가 나면 실행되지 않고 에러가 나지 않았을 경우만 실행됨
#     print("입력에 성공 하였습니다.")
# finally:        # 에러가 나던 안 나던 항상 실행됨
#     print("언제든")



# while True:     # try가 성공 할 떄 까지 실행 됨 (계속 반복 성공시 까지)
#     try:
#         age = int(input("나이를 입력하세요: "))
#         print("나이: ", age)
#         break   # 정상적인 숫자 입력시 종료
#     except ValueError:
#         print("숫자를 다시 입력하세요.")      # 다시 while문 실행




# r_age = 0

# while True:     # try가 성공 할 떄 까지 실행 됨 (계속 반복 성공시 까지)
#     try:
#         age = int(input("나이를 입력하세요: "))
#         print(r_age)
#         break   # 정상적인 숫자 입력시 종료
#     except ValueError:
#         print("숫자를 다시 입력하세요.")      # 다시 while문 실행

# print(r_age)





# # 디버깅이 어려워 질 수 있어서 마지막 수단!!
# try:
#     x = int("abc")
# except Exception as e:
#     print("알 수 없는 에러", e)




try:
    age = int(input("나이 입력: "))
    # 강제 에러 처리 예) 나이가 음수인 사람은 있을 수 없다
    # 예) 1200년에 태어난 사람이 지금까지 살아 있을 수 없음
    # 하지만 코드상 모두 숫자이기에 따로 에러가 나지 않는다.
    if age < 0:
        raise ValueError("나이는 음수가 될 수 없습니다.")
    if age > 100:
        raise ValueError("나이는 100세가 될 수 없습니다.")
    
    print("나이 ", age)
except ValueError as e:
    print("에러 발생", e)