l = [0 for i in range(10001)]

# for i in range(1,len(l)+1):
#     if(i != 0):
#         a = str(i)
#         sum = 0
#         for j in range(len(a)):
#             sum += int(a[j])
#         if(i+sum <= 10000):
#             l[i + sum] += 1

# for i in range(1,10001):
#     if(l[i] == 0):
#         print(i)

def d(n):
    if(n > 10000 and l[n] != 0):
        return
    a = str(n)
    sum = 0
    for j in range(len(a)):
        sum += int(a[j])
    if(n+sum <= 10000):
        l[n + sum] += 1
        d(n + sum)


for i in range(1,10001):
    if(l[i] == 0):
        d(i)

for i in range(1,10001):
    if(l[i] == 0):
        print(i)