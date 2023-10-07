def shell_sort(myList, n):
 
    h = n // 2
    while h > 0:
        for i in range(h, n):
            t = myList[i]
            j = i
            while j >= h and myList[j - h] > t:
                myList[j] = myList[j - h]
                j -= h 
                myList[j] = t
                h = h // 2
 
 
myList = [34, 12, 20, 7, 13, 15, 2, 23]
n = len(myList)
print('Array before Sorting:')
print(myList)
shell_sort(myList, n)
print('Array after Sorting:')
print(myList)