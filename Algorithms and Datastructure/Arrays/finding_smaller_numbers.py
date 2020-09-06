
from collections import defaultdict

################################
# Timecomplexity:  O(NlogN)
# Spacecomplexity: O(N)
################################

def hash_map_smallest_number(arr):
    # Sorting the input array
    sorted_arr= sorted(arr)
    hash_map = defaultdict()
    for i, v in enumerate(sorted_arr):
        if v not in hash_map:
            hash_map[v] = i
    print (hash_map)
    return [hash_map[v] for v in arr]

################################
# Timecomplexity:  O(N)
# Spacecomplexity: O(N)
################################

def array_smallest_number(arr):
    # Creating a auxillary array of some size
    count = [0]* 101
    # Placing the value count in the auxillary array
    for val in arr:
        count[val] += 1
    # Counting the prefix sum of the auxillary array 
    for val in range(1, 101):
        count[val] = count[val - 1] + count[val]
    # Creating the resultant array
    output = [0] * len(arr)
    for index ,val in enumerate(arr):
        if val > 0:
            output[index] = count[val - 1]
    return output


if __name__ == "__main__":
    arr = [8,1,2,2,3]
    print("The smallest number value using the the hashmap approach is: ",hash_map_smallest_number(arr))
    print("The smallest number value using the array based approach is: ",array_smallest_number(arr))