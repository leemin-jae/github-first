data = [1, 10, 5, 8, 7 ,6, 4, 3, 2, 9]
number = 10

def quickSort(datas, start, end):
    if start >= end:
        return

    key = start
    i = start + 1
    j = end

    while i <= j :
        while datas[i] <= datas[key]:
            i += 1
        while (datas[j] >= datas[key] and j > start):
            j -= 1
        if(i>j):
            temp = data[j] 
            datas[j] = datas[key]
            datas[key] = temp
        else:
            temp = datas[j] 
            datas[j] = datas[i]
            datas[i] = temp

    quickSort(datas, start, j-1)
    quickSort(datas, j+1, end)


quickSort(data, 0 , number -1)


for k in range(10):
    print(data[k], end = " ")
