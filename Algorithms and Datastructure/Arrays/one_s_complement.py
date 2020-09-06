################################
# Timecomplexity:  O(N)
# Spacecomplexity: O(1)
################################


def findComplement(num):
    
    temp_array  = num
    # Bit for performing xor with each bit
    one_bit = 1
    # Loop for performing one's compliment
    while temp_array :
        # Performing XOR operation over each bit
        num = num ^ one_bit
        # Performing left bit by 1
        one_bit = one_bit << 1 
        # Performing right bit on temp_array by 1
        temp_array = temp_array >> 1
    return num

if __name__ == "__main__":

    print(findComplement(5))
    