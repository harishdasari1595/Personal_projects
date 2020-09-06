################################
# Timecomplexity:  O(N)
# Spacecomplexity: O(N)
################################

# Function for finding the judge
def find_judge(N, trust):
    # Edge case for a valid graph
    if len(trust) < N-1:
        return -1
    
    # List for creating storing the relationship status
    in_degree  = [0] * (N+1)
    out_degree = [0] * (N+1)
    for out_, in_ in trust:
        # Creating the trust status graph
        out_degree[out_] += 1
        in_degree [in_]  += 1
    for index in range(1, N+1):
        # Condition for finding the judge of the town
        if in_degree[index] ==  N-1 and out_degree[index] == 0:
            return index
    return -1

# Optimal function for finding the judge in the town 
def optimal_find_judge(N, trust):

    if len(trust) < N-1:
        return -1
    # Building the trust status list
    trust_status = [0] * (N+1)
    for out_, in_ in trust:
        trust_status[out_] -= 1
        trust_status[in_]  += 1
    for index in range(1, N+1):
        # Condition for finding the judge of the town
        if trust_status[index] == N-1:
            return index
    return -1

if __name__ == "__main__":

    trust  = [[1,3],[2,3],[3,1]]
    result = optimal_find_judge(int(input()), trust)
    if result > 0:
        print ("The judge in the town is {} ".format(result))
    else:
        print("There is no judge in the town")
      