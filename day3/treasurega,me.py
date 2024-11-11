print("Welcome to the Treasure Island Game Lets Play")
choice1 = input('Where you wanna Go "left" or "right"')
if choice1 == "left":
   choice2 = input('Coungrates you chosse right way to go now you reach the leak'
                   ' there is Island enter "wait" wait for the boat or enter'
                   ' "swim" swim to the Island')
   if choice2 == "wait":
       choice3 = input('coungrates you have reach the Island there are 3 door '
                       '"red" "yellow" "blue" which door you want open')
       if choice3 == "red":
           print("Sorry you choose the wrong door Game Over.")
       elif choice3 == "yellow":
           print("Congrates you got the trasure You Win.")
       elif choice3 == "blue":
           print("sorry you got the wrong door. Game Over")
       else:
           print("Sorry your choice donest exist Game Over")
else:
    print("Sorry you choose the wrong way Game Over")

