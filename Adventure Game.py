'''Programming Assignment: Adventure Game in "To Le Do"
Objective:
Develop a text-based adventure game in Python set in the fantastical land of "To Le Do." Your game will feature a choice between two paths: becoming a Wizard or a Knight. Each path leads to three further choices, with only one path leading to success. The assignment will test your ability to use basic programming concepts like variables, user input, if statements, and loops, including adding error checking to handle invalid inputs.
Assignment Details:
Game Introduction:
Begin your game by welcoming the player to "To Le Do," and provide your description of this wonderous land.
Prompt the player to choose their path: Wizard or Knight. 

Path Selection:
Wizard Path: The player seeks the ancient tome that holds the secrets of the universe.
Knight Path: The player vows to defeat the dragon terrorizing "To Le Do" for centuries.

Wizard Choices:
Search the Ancient Library: "You spend years among the tomes, but the book is nowhere to be found. Your quest ends in wisdom, but not victory."
Explore the Forbidden Cave: "The cave is treacherous and full of traps. Unfortunately, you do not make it out alive."
Venture into the Enchanted Forest: "Within the heart of the Enchanted Forest, you find the ancient tome. Your quest is a success! The secrets of the universe are yours."

Knight Choices:
Attack in the Dragon's Lair: "You fight valiantly in the dragon's lair, but it's too strong in its home territory. You fall in battle, remembered as a hero."
Challenge to a Duel: "The dragon accepts your challenge but proves too powerful in combat. The kingdom mourns its brave knight."
Seek the help of a Sorcerer: "With the help of a sorcerer, you weaken the dragon and defeat it in battle. The kingdom is saved, and you are hailed as its greatest hero."

Error Checking:
Implement loops around the input sections to ensure that players can only proceed with valid choices. If an invalid option is entered, the game should inform the player and prompt them to choose again.  The program should ignore case.
Implementation Guidelines:
Describe the land of To Le Do in your own words at the beginning of the program.
Prompt the user for inputs, describing the choices exactly.  Be sure to allow the user to enter answers in upper and lower case.
Use if statements to direct the flow of the game based on the player's choices.
Include nested if statements within each main path to handle the subsequent choices.
Apply while loops to validate user inputs, ensuring the game continues to prompt for a decision until a valid choice is made.
Store player inputs in variables and use these to determine the game's outcome.
Provide clear and concise feedback for each choice, mirroring the exact text provided above for each outcome.
Use only programming techniques already covered in class.
The code must be completely your own work, not Chegg's nor ChatGPT nor your friend. If you need help, ask during the lab.
'''

playing = True

while playing:
    #describing the land of 'To Le Do'
    print("Welcome to the enchanting land of To Le Do, where mystical adventures await! As you step into this magical realm, you are faced with a crucial decision – will you become a Wizard, delving into the secrets of the universe, or a Knight, bravely standing against the ancient dragon that has haunted To Le Do for centuries?")

    choice=input("Choose your path (Wizard/Knight): ").upper()  #asking user their choice of path

    #if the input is invalid, again ask the user for input
    while choice!="WIZARD" and choice!="KNIGHT":
        choice=input("Your choice was not reconized. Please Enter your choice of path again (Wizard/Knight): ").upper()

    #Wizard's path
    if choice=="WIZARD":
        print("That was a great choice. Your quest will be to uncover the ancient tome holding the universe's secrets. Navigate through magical challenges and make choices that will shape your destiny.")
        print("1. Search the 'Ancient Library'")
        print("2. Explore the 'Forbidden Cave'")
        print("3. Venture into the 'Enchanted Forest'")
        wizardChoice=input("Where would you like to go?(Ancient Library/Fobidden Cave/ Enchanted Forest) ").upper() #asking user their choice of path

        #if the choice is invalid ask again 
        while wizardChoice!="ANCIENT LIBRARY" and wizardChoice!="FORBIDDEN CAVE" and wizardChoice!="ENCHANTED FOREST":
            wizardChoice=input("I did not recognize that location. Only write the name of the path(Ancient Library/Fobidden Cave/ Enchanted Forest) ").upper()
        
        #final conclusions for each path of choice
        if wizardChoice=="ANCIENT LIBRARY":
            print("You spend years among the tomes, but the book is nowhere to be found. Your quest ends in wisdom, but not victory.")
        elif wizardChoice=="FORBIDDEN CAVE":
            print("The cave is treacherous and full of traps. Unfortunately, you do not make it out alive.")
        elif wizardChoice=="ENCHANTED FOREST":
            print("Within the heart of the Enchanted Forest, you find the ancient tome. Your quest is a success! The secrets of the universe are yours.")

    #Knight's path
    elif choice=="KNIGHT":
        print("Excellent! Your mission will be to defeat the menacing dragon that looms over To Le Do. Steel yourself for challenges that will test your valor.")
        print("1. Attack in the 'Dragon's Lair'")
        print("2. Challenge to a 'Duel'")
        print("3. Seek the help of a 'Sorcerer")
        knightChoice=input("Which way would you like to go?(Dragon's Lair/Duel/Sorcerer) ").upper()

        #if the choice is invalid ask again 
        while knightChoice!="DRAGON'S LAIR" and knightChoice!="DUEL" and knightChoice!="SORCERER":
            knightChoice=input("I did not recognize that location. Only write the name of the path(Dragon's Lair/Duel/Sorcerer) ").upper() #asking user their choice of path
        
        #final conclusions for each path of choice
        if knightChoice=="DRAGON'S LAIR":
            print("You fight valiantly in the dragon's lair, but it's too strong in its home territory. You fall in battle, remembered as a hero.")
        elif knightChoice=="DUEL":
            print("The dragon accepts your challenge but proves too powerful in combat. The kingdom mourns its brave knight.")
        elif knightChoice=="SORCERER":
            print("With the help of a sorcerer, you weaken the dragon and defeat it in battle. The kingdom is saved, and you are hailed as its greatest hero.")
    
    #Asking user if they want to play again and running this game again if they want to play
    play=input("Do you want to play again?(Y/N) ").upper()
    while play!= 'N' and play!='Y':
        play=input("Invalid choice. Do you want to play again?(Y/N) ").upper()
    if play=='Y':
        playing=True
    elif play=='N':
        playing=False

