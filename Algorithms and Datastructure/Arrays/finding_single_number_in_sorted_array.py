################################
# Timecomplexity:  O(logN)
# Spacecomplexity: O(1)
################################

def singleNonDuplicate(nums):
    # Assigning the left and right pointer over the input list
    left = 0
    right = len(nums)-1
    
    # Logic for finding the single element in a sorted list
    while left < right:
        # Calculating the mid of the list
        mid = left + (right- left)//2
        # Checking the halves are even or not
        even_halves = (right-mid) % 2 == 0
        if nums[mid] == nums[mid+1]:
            # Case-1 (even halves and mid == mid+1)
            if even_halves:
                left = mid+2
            # Case-2 (odd halves and mid == mid+1)
            else:
                right = mid-1
        elif nums[mid] == nums[mid-1]:
            # Case-3 (even halves and mid == mid-1)
            if even_halves:
                right = mid -2
            # Case-4 (odd halves and mid==mid-1)
            else:
                left = mid+1
        # Case-5 (if the mid is the single element)
        else:
            return nums[mid]
    # Case-6 (the single element is the second last element)
    return nums[left]

if __name__ == "__main__":
    # Sorted array and having exactly one non repeating element
    nums = [1,1,5,5,48,48,50]
    print(singleNonDuplicate(nums))

            