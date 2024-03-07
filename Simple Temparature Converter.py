'''Overview
In this assignment, you will create a Python program that converts temperatures between Fahrenheit and Celsius. The program will prompt the user to enter a temperature in Fahrenheit and convert it to Celsius, or vice versa, depending on the user's choice. This assignment will help you practice using loops, if statements, and user input/output in Python.
Objectives
Use if statements to handle conditional logic.
Implement loops to allow multiple conversions without restarting the program.
Apply input and output operations to interact with the user.
Requirements
User Choice: The program should first ask the user whether they want to convert a temperature from Fahrenheit to Celsius or from Celsius to Fahrenheit. Use input to get the user's choice and use an if statement to determine which formula to use.  Allow for upper and lowercase characters.
Temperature Input: Prompt the user to input the temperature.
Conversion:
If converting from Fahrenheit to Celsius, use the formula: C = (F - 32) * 5/9.
If converting from Celsius to Fahrenheit, use the formula: F = C * 9/5 + 32.
Perform the conversion and display the result to the user.
Loop for Multiple Conversions: After displaying the conversion result, ask the user if they want to perform another conversion. The program should continue running until the user chooses to exit.  This will require a while loop.
Example Output
Would you like to convert temperature from:
F:  Fahrenheit to Celsius
C: Celsius to Fahrenheit
Enter your choice (F or C): C
Enter temperature in Celsius: 25
25 C is 77.0 F.
Do you want to perform another conversion? (Y/N): Y
Would you like to convert temperature from:
F:  Fahrenheit to Celsius
C: Celsius to Fahrenheit
Enter your choice (F or C): F
Enter temperature in Fahrenheit: 77
77 F is 25.0 C.
Do you want to perform another conversion? (Y/N): N
Goodbye!'''

while True: #using while to perform the loop

    #Asking user for their choice of conversion
    print("Would you like to convert temparature from:")
    print("F: Fahrenheit to Celsius")
    print("C: Celsius to Fahrenheit")

    # Prompting user to enter their choice using input and using choice variable to save the response
    choice=input("Enter your choice (F or C): ")

    # Using if elif else statement to check for the condition
    if (choice == 'C' or choice=='c') : #if user inputs 'C' or'c' then convert temparature from celcius to fahrenheit
        temparature= int(input("Enter temparature in celcius: "))
        convertedTemparature = (temparature*(9/5)+32)      #use this formula for conversion to fahrenheit
        print(temparature,"C is", convertedTemparature, "F")  #Print the result to the user
    elif(choice == 'F' or choice=='f'):  #if user inputs 'F' or'f' then convert temparature from fahrenheit to celcius
        temparature=  int(input("Enter temparature in Fahrenheit: "))
        convertedTemparature = (temparature-32)*5/9          #use this formula for conversion to celcius
        print(temparature,"F is", convertedTemparature, "C")     #Print the result to the user
    else: # if user inputs anything other than c and f characters print the response is invalid
        print("INVALID RESPONSE")
    repeat= input("Do you want to perform another conversion? (Y/N): ") #Ask user if they want to perform another conversion
    if (repeat=='N' or repeat=='n'):    #if user inputs 'N' or 'n' then break out of the loop else continue the loop
        print("Goodbye!")
        break
    


