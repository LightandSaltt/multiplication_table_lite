import time

def multiplication_table_Program():
    print("구구단 프로그램을 실행합니다.")
    time.sleep(2)
    print("원하시는 모드 번호를 입력해 주세요.")
    user_select = int(input("1. 전체 구구단 출력 / 2. 한 단의 구구단 출력 : "))
    if user_select == 1:
        all_multiplication_table()
    else:
        one_multiplication_table()

def all_multiplication_table():
    print("전체 구구단을 출력합니다.")
    for i in range(1, 10):
        time.sleep(1)
        print("----" , i, "단", "----")
        for j in range(1, 10):
            print(i, "*", j, "=", i * j)
            



def one_multiplication_table():
    number = int(input("단을 입력해 주세요. : "))
    time.sleep(2)
    print("----" , number, "단", "----")
    for i in range(1, 10):
        print(number, "*", i, "=", number * i)
        


multiplication_table_Program()