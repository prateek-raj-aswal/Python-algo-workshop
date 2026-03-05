# Remove duplicates from sorted array
# Two-pointer algorithm
def remove_duplicate(arr):
    slow = 0
    
    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]
            
    return slow + 1
    
arr = [1,1,2,2,3,4]
print(remove_duplicate(arr))
