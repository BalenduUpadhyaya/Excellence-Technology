     # Task given is Setup a dict structure like this in python
           #Dict1: (this is a key, value pair of user id and username) { “1” : “name1”, “2” : “name2”,“3” : “name3”} etc.. 
            #Dict2: (this is a key value pair of user id and exam score) { “1” : 50, “2” : 60 “3” : 70}
        #These are just sample data assume there are hundreds of users 
                #Write a function in python in python, which will return maximum i.e function should return dictionary like{ “3” : 70}

      

                           ##     We can make this dictionay of n number of users.
     
Dictionary_1={}  #Blank Dictionary
Key=(int(input("Enter how many key-value pair you want: ")))            #Any number of key-value pair
print()
for i in range(1,Key+1):
    Dictionary_1[str(i)]=input("Enter the username for the  " +str(i)+" user id:")
print("This is a key, value pair of user id and username",(Dictionary_1))
print()
print("Now for userid and username  -   Enter the following details")
print()
Dictionary_2={}   #Blank Dictionary

#Key=(int(input("Enter how many key-value pair you want: "))) 
for i in range(1,Key+1):
    Dictionary_2[str(i)]=input("Enter the marks for the " +str(i)+" user id:")
print("This is a key, value pair of user id and exam score",(Dictionary_2))

      #we have to fetch the maximum score key and value  
max_key = max(Dictionary_2, key=Dictionary_2.get)    #This will fetch the maximum score key .
Dictionary_3={max_key:int(Dictionary_2[max_key])}
print(Dictionary_3)



