################################
# Timecomplexity:  O(N + K)
# Spacecomplexity: O(N)
################################
def remove_k_elem(num, k):
    # Boundary cases for this problem
    if len(num) == k:
        return 0
    if k == 0:
        return num 
    # Declaring stack for storing the element in the stack
    stack = []
    remove_element = k 
    # Loop for removing the k most significant digits
    for current_elem in num:
        # Condition for becoming the most significant digit
        while remove_element and stack and stack[-1] > current_elem:
            # Poping the top of the stack
            poped_num = stack.pop()
            print("The poped element is: ",poped_num)
            # Decreasing the k value
            remove_element -= 1
        stack.append(current_elem)
    # Formatiing the output string by removing the leading 0's
    # Removing the k digits from right if the number is in ascending order
    result = "".join(stack[0: len(num)-k]).lstrip("0")
    
    if len(result):
        return result
    else:
        return 0

if __name__ == "__main__":

    print(remove_k_elem(input(), int(input())))