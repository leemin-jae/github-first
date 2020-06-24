num = int(input())
h = 0

for i in range(1,num+1):
    if i <=99:
        h += 1
    else:
        k = list(map(int,str(i)))
        if (k[0] - k[1] == k[1] - k[2]) :
            h += 1

print(h)