#####################################################################################################
 # The first function fails if the characters in the magazine are not in the same order of ransomNote
 # The second function works well in any condition
#####################################################################################################
def canConstruct(ransomNote, magazine):
    i = 0
    j = 0
    count = 0
    # Checking the boundary cases
    if (len(ransomNote) > len(magazine)):
        return "false" 
    # looping over the ransomNote and finding the respective characters in the magazine
    while i < len(ransomNote):
        # Condition for valid character match
        if ransomNote[i] == magazine[j]:
            print(ransomNote[i], magazine[j])
            i += 1
            j +=1
            count +=1
        # Incrementing the j pointer if match not found
        else:
            j += 1
            if j == len(magazine):
                return "false"
    # If the frequency of characters matches than return "true" or return "False" 
    if count == len(ransomNote):
        return "true"
    return "false"

def hash_map_canConnect(ransomNote, magazine):
    
    # Checking the boundary cases 
    if (len(ransomNote) > len(magazine)):
        return "false"
    # Initializing dictionary 
    count = {}
    # Storing the characters as key in the magazine and its respective frequency as value
    for i in magazine:
        if i in count:
             count[i] += 1
        else:
            count[i] = 1
    # Loop for finding the character in the present in the ransomnote
    for j in ransomNote:
        if j not in count:
            return "false"
        if count[j] == 0:
            return "false"
        count[j] -= 1
    return "true"


if __name__ == "__main__":
#######################################################################
    # order in magazine is not preserved
    # a =  "acdffth"
    # b =  "ggdgacrfffyyth"
    a = "a"
    b = "b"
    # # Order in the magazine is preserved
    # c =  "aaghf"
    # d =  "rrtauaghoof"

    # a = "sfgfsag"
    # b ="sdf"
    print ("The first function will fail",canConstruct(a,b))
    print (hash_map_canConnect(a, b))
########################################################################
    # print (canConstruct(c,d))
    # print (hash_map_canConnect(c, d))
        