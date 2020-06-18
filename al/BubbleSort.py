array = [1, 10, 5, 8, 7 ,6, 4, 3, 2, 9]

for i in range(10):
    for j in range(9-i):
        if array[j] > array[j+1]:
            temp = array[j]
            array[j] = array[j+1]
            array[j+1] = temp
            for k in range(10):
                print(array[k], end = " ")
            print()
for i in range(10):
    print(array[i], end = " ")
