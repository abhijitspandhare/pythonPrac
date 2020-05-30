from math import sqrt, floor, ceil 
  
# Function to string into grid form  
def gridStr(string) : 
  
    l = len(string) 
    k = 0
    #import pdb;pdb.set_trace(); 
    row = floor(sqrt(l))  
    column = ceil(sqrt(l))  
  
    if (row * column < l) : 
        row = column 
    s = [[0 for j in range(column) ]  
            for i in range(row)] 
    
    # convert the string into grid  
    for i in range(row) : 
        for j in range(column) :  
              
            if k >= l : 
                s[i][j] = " "
                k += 1
                  
            else : 
                s[i][j] = string[k]  
                k += 1
  
    # Printing the grid  
    for i in range(row) : 
        for j in range(column) : 
            if s[i][j] == " " : 
                break
                  
            print(s[i][j], end = "") 
          
        print()


def search(searchword):
    for w in searchword:
        pass
        
      
# Driver code  
if __name__ == "__main__" :
    
    string = input("Enter Sequence of characters : ");#"GEEKSFORGEEKS"

    gridStr(string)
    searchword = input(" Enter word to search : ").split(' ')
    search(searchword)

      
