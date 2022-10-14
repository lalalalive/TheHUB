#파일명 :s0607_3.py

import csv


def average(scores):
    sum=0
    for score in scores:
        sum+=int(score)
    avg=sum/len(scores)
    return avg

def grade(avg):
    if 90<=avg<=100:gpa="A"
    elif 80<=avg<90:gpa="B"
    elif 70<=avg<80:gpa="C"
    elif 60<=avg<70:gpa="D"
    elif 50<=avg<60:gpa="E"
    else:           gpa="F"
    return gpa


wfile=open('csv\\class_total_avg.csv','w',newline='')
csvfile=csv.writer(wfile)
csvfile.writerow(['이름','반','주소','국어','영어','수학','과학','역사','평균','등급'])
for n in range(1,4):    
    rfile=open(f'csv\\class_{n}.csv','r')
    rows=list(csv.reader(rfile))    
    for row in rows:        
        scores=row[3:]
        avg=average(scores)
        gpa=grade(avg)
        row.insert(1,n)
        csvfile.writerow(row+[avg, gpa])
    
    rfile.close()
wfile.close()    