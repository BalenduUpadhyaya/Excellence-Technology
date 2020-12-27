           # Returns count of maximum consecutive 1's in array 
     ##Task-Assume we have list like this
             ##[0,0,0,1,1,1,0,0,0,1,1,0,1,1,1,1,0,0,1,1] Basically a list of zero’s and one’s.
            ##Write a python function to the number of maximum consecutive  one’s present in the array. 
            ##E.g output for the above array would be 4
   
arr=[]    #Blank Array
n=int(input("How many total number of 0's and 1's you want to enter: "))
for i in range(1,n+1):
    arr.append(int(input("Enter " + str(i)+ " number: ")))
  
  
  #Python function to the number of maximum consecutive  one’s present in the array
def getMaxLength(arr, n): 
  
    count = 0 
      
    # initialize max 
    result = 0 
  
    for i in range(0, n): 
      
        # Reset count when 0 is found 
        if (arr[i] == 0): 
            count = 0
  
        # If 1 is found, increment count  and update result if count becomes more. 
        else: 
              
            # increase count 
            count+= 1 
            result = max(result, count)  
          
    return result  
print("The number of maximum consecutive  one’s present in the array is ",getMaxLength(arr, n))
