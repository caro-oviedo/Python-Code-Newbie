def binary_search(list_name, key):
    first = 0
    last = len(list_name)-1 

    while first <= last: 
        mid = first + last // 2
        
        if list_name[mid] == key: 
            return mid
        elif list_name[mid] > key: 
            last = mid -1 
        else: 
            first = mid  
    return None

list1 = [1,3,5,7,9]
result = binary_search(list1, 9)
print(result)

