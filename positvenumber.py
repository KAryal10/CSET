# get input from user and print positive, zero, or negative

number = eval(input("Enter a number "))

if(number>0):
    print("It is positive")
elif(number<0):
    print("It is negative")
else:
    print("It is zero.")