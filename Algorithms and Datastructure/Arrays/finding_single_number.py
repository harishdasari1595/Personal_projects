################################
# Timecomplexity:  O(N)
# Spacecomplexity: O(N)
################################
#Hashmap approach
from collections import defaultdict

def singleNumber(nums):
    hash_map = defaultdict(int)
    # Storing key as elements of array and value as count of the array 
    for i in nums:
        hash_map[i] += 1
    # Finding the element which occured exactly once or value == 1
    for i in hash_map:
        if hash_map[i] == 1:
            return i
         
if __name__ == "__main__":
    arr = [1,2,1,2,1,2,3]
    result = singleNumber(arr)
    print (result)