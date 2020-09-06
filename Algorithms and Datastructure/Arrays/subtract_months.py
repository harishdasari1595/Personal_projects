
## USAGE:- python subtract_months.py

# This function will subtract the month from given tuple of year and months
# Input : List of tuples [(year, month, sub_month),   (year, month, sub_month ),  (year, month, sub_month ),.....]
# Output: List of tuples [(output_year, output_month),(output_year, output_month),(output_year, output_month),...]
# Time_complexity : O(N)
# Space_complexity: O(N)

def subtract_months(input_list):
    # List for storing the month information
    month_list  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    # List for storing the output values
    output_list = []
    # Loop for traversing through the input list
    for values  in input_list:
        # Variables for storing the year, month and subtraction month
        param = values
        year  = param[0]
        month = param[1]
        sub_month = param[2]
        # Boundary case for handling the invalid format input as specified in the problem statement
        if (year < 1000 or year > 9999) or (month < 1 or month > 12) or (sub_month < 0):
            output_list.append("None")
        else:
            # Subtracting the month and sub_month for finding the difference
            result = month - sub_month
            # Condition for finding the reslultant months and year if the month is greater than 12
            if sub_month > 12:
                # Calculating the resultant output year and month
                # By finding the quotient and remainder of sub_month/12
                output_year  = sub_month//12
                output_month = sub_month % 12
                # Finding the output month
                output_month = abs(month - output_month)
                # Handling the output_month == 0 boundary case  
                if output_month == 0:
                     output_list.append((year - 2, 12))
                else: 
                    output_list.append(((year - output_year), output_month))
            # If the result > 0 than it is in the same year  
            elif result > 0:
                output_month = month_list[result-1]
                output_list.append((year, output_month))
            # If the result == 0 which means month and sub_month are equal so decrease year by 1
            elif result == 0:
                output_month = month_list[-1]
                output_list.append((year-1, output_month))
            # If the result is negative than perform circular indexing of the month_array
            else:
                output_month = month_list[result-1]
                output_list.append((year-1, output_month))
    
    # Returning the output list
    return output_list

if __name__ == "__main__":
    # Input list of tuples
    input_list = [(2020,5,3), (2019,8,6), (2018, 18, 7),(2021, 12, 13)]
    # Calling the subtract_months function
    result = subtract_months(input_list)
    # Printing the output
    print(result)