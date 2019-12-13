
import random

print("                  ***Welcome to The Dice Rolling Simulator***                    \n")

welcome=input('Would you like to roll the dice now? (Yes/No): \n')
welcome=welcome.lower() # to make the input become lowercase, no matter the input is uppercase or lowercase, the system can identify

if welcome == 'no':
    print('See you next time!') 

elif welcome == 'yes':

    while True:
        result=random.randint(1,6) # the dice has 6 sides with numbers 1 to 6, for every roll, the result is randomly generated from 1 to 6
        print(f'Your number is {result}.')
        ask=input('Do you want to roll again? (Yes/No): \n')
        ask=ask.lower()

        if ask == 'yes':
            pass # if user enter 'yes', the simulator starts agian

        elif ask == 'no':
            print('Have a good one!')
            break # if user enter 'no', simulator ends

        else: 
            ask_again=input('Please enter a valid answer(Yes/No): \n')
            ask_again=ask_again.lower() # if user enter an unknown input, ask them to input again

            if ask_again == 'yes': # if user enter 'yes', the simulator starts agian
                pass

            elif ask_again == 'no': # if user enter 'no', simulator ends
                print('Have a good one!')
                break

            else: 
                print('Unknown answer.\nSee you next time!') # if there is an unknown input again, simulator ends
                break        

else:
    print('Unknown answer.\nSee you next time!')


    
    

