#파일명: s0620_1.py

try:
    print(b)
    a=[1,2,3,4]
    print(a[3])
    print(4/2)
except IndexError as message:
    print("인덱싱 할 수 없습니다.")
    print(f"메시지: {message}")
except ZeroDivisionError as message:
    print("0으로 나눌 수 없습니다.")
    print(f"메시지: {message}")
except Exception as message:
    print("예상외의 에러가 발생했습니다.")
else:
    print("에러가 발생하지 않습니다.")
finally:
    print("프로그램을 종료합니다.")
    
