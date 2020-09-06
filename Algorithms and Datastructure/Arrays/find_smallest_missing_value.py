 
def find_SmallestMissingValue(nums):

    n = len(nums)
    one_exists = False
    # Loop for checking 1 exist or not
    for value in range(n):
        if nums[value] == 1:
            one_exists = True
    # Returning smallest positive integer if condition satisfy
    if one_exists is False:
        return 1
    # Preprocessing the input array
    for value in range(n):
        if nums[value] <= 0 or nums[value] > n:
            nums[value] = 1
    # Loop for finding the smallest integer value
    for value in range(n):
        index = abs(nums[value])
       
        if index < n:
            nums[index] = -1 * abs(nums[index])     
        else:
            nums[0] = -1 * abs(nums[0])
           
    # Various conditions for returning the smallest positive integer value
    for i in range(1,n):
        if (nums[i] > 0):
            return i 
    if nums[0] > 0:
        return n
    return n+1 

if __name__ == "__main__":

    arr =  [2,1,4,8,5,6,9,7,5,41,489,45,8,12]
    result = find_SmallestMissingValue(arr)
    print ("The smallest positive missing value is: ",result)            
     