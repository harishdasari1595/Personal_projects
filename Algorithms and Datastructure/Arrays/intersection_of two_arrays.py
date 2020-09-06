################################
# Timecomplexity:  O(NlogN)
# Spacecomplexity: O(N)
################################
def intersection_of_arrays(arr1, arr2):

    arr1.sort()
    arr2.sort()
    i = 0
    j = 0
    result = []
    while i < len(arr1) and j < len(arr2):

        if arr1[i] == arr2[j]:
            result.append(arr1[i])
            i += 1
            j += 1 
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
    return result

if __name__ == "__main__":
    arr1 = [1,2,4,56,7]
    arr2 = [2,11,2,4]
    result = intersection_of_arrays(arr1, arr2)
    print (result)



        
