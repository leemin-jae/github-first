number = 8
sorted = [0 for i in range(8)]

def merge(a, m, mid, n):
    i = m
    j = mid +1
    k = m

    while i <= mid and j <= n:
        if a[i] <= a[j]:
            sorted[k] = a[i]
            i += 1
        else:
            sorted[k] = a[j]
            j += 1
        k += 1
    if i > mid :
        for t in range(j,n+1):
            sorted[k] = a[t]
            k += 1
    else:
        for t in range(i,mid+1):
            sorted[k] = a[t]
            k += 1

    for t in range(m,n+1):
        a[t] = sorted[t]

def mergeSort(a , m , n):
    if(m<n):
        mid = (m+n)//2
        mergeSort(a,m,mid)
        mergeSort(a,mid+1, n)
        merge(a, m, mid,n)

array = [100,24,367,2,3,5,9,1]

mergeSort(array, 0 , 7)

for i in range(8):
    print(sorted[i])