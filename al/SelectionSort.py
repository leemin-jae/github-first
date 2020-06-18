array = [1, 10, 5, 8, 7 ,6, 4, 3, 2, 9]

for i in range(10):
    min = 9999
    for j in range(i,10):
        if(min > array[j]):
            min = array[j]
            index = j
    temp = array[i]
    array[i] = array[index]
    array[index] = temp
    for k in range(10):
        print(array[k], end = " ")
    print()
for i in range(10):
    print(array[i], end = " ")
