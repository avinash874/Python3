a=int(input("Enter your age: "))

if(a>=18):
    print("You are above the age of consent")
    print("Good for you")

elif(a<0):
    print("You have entered an invalid age")  #This condition is never true because age cannot be negative. It should be "elif(a<18 and a>=0):" to check for ages between 0 and 17. 

elif(a==0):
    print("You are not age of consent")

else:
    print("You are below the age of consent")    

print("End of program")    