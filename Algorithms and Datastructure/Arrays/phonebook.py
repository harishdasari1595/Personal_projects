# Enter your code here. Read input from STDIN. Print output to STDOUT

def find_phonenumber(table, queries):

    for i in (queries):
        if i in table:
            print ("{}={}".format(i, table[i]))
        else:
            print("Not found")


if __name__ == "__main__":

    n = int(input())
    phonebook  = {}
    names_list = []
    for i in range(n):
        name, num = [value for value in input().split()]
        phonebook.update({name:int(num)})
    for names in range(n):
        names_list.append(input())
    find_phonenumber(phonebook, names_list)
   
