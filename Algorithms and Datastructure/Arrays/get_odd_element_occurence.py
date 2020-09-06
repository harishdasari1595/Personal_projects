################################
# Timecomplexity:  O(N)
# Spacecomplexity: O(1)
################################

# Function for finding the single odd element occurence
def getOddOccurence(arr):
    res=0
    for i in arr:
        res=res^i
        #print (res)
    return res

if __name__=='__main__':
    arr=[2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2]
    arr2=[1,2,5,4,5,5,2,1,4]
    print(getOddOccurence(arr))
