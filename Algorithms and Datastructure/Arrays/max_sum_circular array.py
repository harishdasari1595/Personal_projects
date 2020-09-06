
################################
    # Timecomplexity:  O(N)
    # Spacecomplexity: O(1)
################################
# function for finding the maximum of the subarray by using kadane's algorithm
def kadane_algo(nums):
    # Variables for storing the cuurent and max sum of the array
    current_sum = nums[0]
    max_sum     = nums[0]
    # Loop for finding the maximum sum of the subarray
    for number in nums[1:]:
        current_sum = max(number, current_sum + number)
        max_sum     = max(current_sum, max_sum)
    return max_sum

# Function for finding the max sum of the circular subarray
def maxSubarraySumCircular(A):
    # Finding the maximum sum of a subarray using kadane's algorithm on input array
    max_kadane   = kadane_algo(A)
    # Variable for storing the circular sum
    circular_sum = 0
    # Loop for finding the max sum of the input array
    for index in range(len(A)):
        circular_sum += A[index]
        # making the input array as negative value
        A[index]      = -A[index]
    # Finding the circular sum by adding the total sum and kadane sum of negative array
    circular_sum = circular_sum + kadane_algo(A)
    
    # Condition for finding the max sum of the circular sub array
    if circular_sum > max_kadane and circular_sum != 0:
        return circular_sum
    else:
        return max_kadane
    
    

if __name__ == "__main__":

    input_Array = [1,5,7,-5,8,9,-5,5,9]
    # Finding the maximum subarray    
    max_subarray = kadane_algo(input_Array)
    # Finding the maximum sum of the circular subarray
    circular_max = maxSubarraySumCircular(input_Array)

    print ("The maximum sum of the subarray is as follows: ", max_subarray)
    print ("*" * 100)
    print ("The maximum sum of the circular subarray is as follows: ", circular_max)
        