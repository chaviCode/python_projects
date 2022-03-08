def insertion_sort(arr):

    for i in range(1, len(arr)):
  
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
        
        arr[j+1] = key


list = [4, 7, 1, 9, 4, 5]
insertion_sort(list)
print(list)
