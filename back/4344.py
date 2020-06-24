te = int(input())

for j in range(te):
    student = list(map(int,input().split()))
    ave = float(sum(student[1:])/student[0])
    re = 0
    for i in range(1,len(student)):
        if(float(student[i]) > ave):
            re += 1
    f = re/student[0]*100
    print(str("%.3f"%round(f,3)) + "%")