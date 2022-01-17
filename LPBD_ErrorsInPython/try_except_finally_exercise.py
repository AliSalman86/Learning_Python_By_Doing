# This simple AI app that ask for a number and return if it odd/even and then ask for another number till user decides to stop playing

def interaction():
    while True: # keep looping until user reach break statement
        # User decided to play/play again, the code below ask for input or check if it even or odd
        # validating the user input and handle errors:
        try:
            user_input = int(input("Please input an integer number: ")) # ask the user to input integer number and then convert it from str to integer

        except ValueError:
            print("Please input integers only.")

        else:
            print("{} is {} number".format(user_input, 'even' if user_input % 2 == 0 else 'odd')) # print out the message '{user_input} is {even/odd}

        # previous game ended, asking user if the need to play more, break the loop if they don't.
        user_input = input("Do you want to play again? <y or n>") # quit if the user didn't input 'y'
        if user_input != 'y':
            print("Goodbye")
            break # break the while loop to quit

interaction()