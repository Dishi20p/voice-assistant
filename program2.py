#if conditional statements
age=int(input("Enter your age: "))
if age>18:
    print("You can Vote!!!")
elif age==18:
    print("Yeah! You are 18 now, You can Vote!!!")    
else:
    print("Sorry,You have to wait...")    

# #For loop
for i in range(1,20):
    if i % 3==0:
        print("Divisible by 3")
        break
else:
    print("Not divisible by 3")    
    

#while Loop
while age>18:
    print("You can have a license")
    break
else :
    print("You can not have a license")   