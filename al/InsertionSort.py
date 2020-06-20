array = [1, 10, 5, 8, 7 ,6, 4, 3, 2, 9]

for i in range(9):
    print(i)
    j = i
    while array[j]>array[j+1]:
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp
        j -= 1
        for k in range(10):
            print(array[k], end = " ")
        print()
for i in range(10):
    print(array[i], end = " ")
