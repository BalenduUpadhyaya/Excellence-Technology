    # Task given is : Use python lists and make an list of numbers. Write a function which returns sum of the list of numbers




      #let u want to add n no of integer elements in the list so
n=(int(input("How many numbers you want to store in the list is :")))
        #First creating a blank list in which i am taking input from user
list=[]
for i in range(1,n+1):
    list.append(int(input("Enter " + str(i)+ " number: ")))
   #print("List is",list) It will print the created list


    #if we will not use sum function  of list,than we have to do this
sum=0
for index in range(0,len(list)):
    sum=sum+list[index]
print("The sum of the list of numbers is :",sum)



   #otherwise we can use in-built sum funtion of list which i have commented as the question is to write a function...(uncomment it if u want to check)
#sum=sum(list)
#print("The sum of the list of numbers is :",sum)


