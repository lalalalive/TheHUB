#파일명: s0620_2.py

import csv

def average(scores):
    sum=0
    for score in scores:
        sum+=int(score)
    avg=sum/len(scores)
    return avg

for n in range(1,6):
    try:
        filename=f"csv\\class_{n}.csv"
        print(f"{n}반 학급 학생들 평균점수: ")
        file=open(filename,"r")
        
    except FileNotFoundError as message:
        print("해당 파일은 존재하지 않습니다.")
        print(message)
        print("\n")
    else:
        rows=list(csv.reader(file))
        for row in rows:
            name,address,*scores=row
            avg=average(scores)
            print(f"{name}의 평균: {avg:.1f}점")
        print("\n")
    finally:
        file.close()
        print()
        