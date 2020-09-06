# Function for checking the symmetric matrix property
def check_symmetric(arr, row, column):
    
    for i in range(row):
        for j in range(column):
            if arr[i][j] != arr[j][i]:
                return  "NO"
    return "YES"

if __name__ == "__main__":
    T     = int(input())
    count = 0
    
    while (count < T) and (1 <= T <= 10):
        try:
            N  = int(input())
            if (2 <= N <= 32):
                
                # Making the N*N matrix
                input_matrix = [[0 for col in range(N)] for row in range(N)]
                # Logic for building the matrix from user inputs
                for i in range(N):
                    input_array = (input())
                    for j, values in enumerate(input_array):
                        input_matrix[i][j] = int(values)
                
                # row    = len(input_matrix)
                # column = len(input_matrix[0])
                result = check_symmetric(input_matrix, N, N)
                print (result)
            else:
                print ("NO")
        except(EOFError):
            break
        count +=1
    