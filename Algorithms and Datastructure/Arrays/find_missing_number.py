
def add_missingNumber(nums):
    length         = len(nums)
    sum_of_first_n = int(length*(length+1)/2) 
    array_sum      = 0
    for i, value in enumerate(nums):
        array_sum  =  array_sum + value    
    missing_number = abs(sum_of_first_n - array_sum) 
    return int(missing_number)
            
def xor_missingNumber(nums):
    n = len(nums)
    x1 = nums[0] 
    x2 = 0
    for i in range(1, n): 
        x1 = x1 ^ nums[i]          
    for i in range(1 , n + 1): 
            x2 = x2 ^ i         
    
    return x1 ^ x2     

if  __name__ == "__main__":
    arr     = [9,6,4,2,3,5,7,0,1]
    result  = add_missingNumber(arr)
    result2 = xor_missingNumber(arr)
    print ("The missing number using addition based approach is: {}".format(result))
    print ("The missing number using xor based approach is: {}".format(result2))   