# Two Sum in Sorted Array
# Find two numbers whose sum = target. 
# Time → O(n)
# Space → O(1)


def two_sum(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        s = arr[left] + arr[right]
        
        if s == target:
            return (left, right)
        elif s < target:
            left += 1
        else:
            right -=1
            
    return None
    
arr = [1,2,3,4,6,8]
print(two_sum(arr, 10))
