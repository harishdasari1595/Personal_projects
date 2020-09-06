################################
# Timecomplexity:  O(logN)
# Spacecomplexity: O(1)
################################
def isPerfectSquare(num):
    
    # If number is smaller than 2 return the value
    if num < 2:
        return True
    # Pointers for traversing the input range
    low,high = 2, num//2
    # Binary search logic for finding the perfect square
    while low <= high:
        mid = (low + high)//2
        if mid ** 2 == num:
            return True
        elif mid**2 > num:
            high = mid -1
        else:
                low = mid +1
        else:
            return False

if __name__ == "__main__":

    nums = int(input())
    if isPerfectSquare(nums):
        print ("The given number {} is a perfect square".format(nums))
    else:
        print ("The given number {} is not a perfect square".format(nums))