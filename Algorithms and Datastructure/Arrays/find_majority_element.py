################################
# Timecomplexity:  O(N)
# Spacecomplexity: O(1)
################################

def find_majority_element(arr):

    count    = 1
    majority = arr[0]
    majority_value = len(arr)/2
    value_count = 0
    for i in range (1, len(arr)):
        if arr[i] == majority:
            if count == 0:
                count += 1
            majority = arr[i]
            print (majority)
            count += 1 
        else:
            count -= 1
        if count == 0:
            count += 1
            majority = arr[i]
  
    for i in range(len(arr)):
        if arr[i] == majority:
            value_count += 1

    if value_count >= majority_value:
        return majority
    else:
        return None 

if __name__ == "__main__":

    arr = [2,2,1,1,1,2,2]
    result = find_majority_element(arr)
    if result != None:
        print ("The majority element in the array is as follows: ", result)
    else:
        print ("There are no majority elements in this array ")

