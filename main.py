import random


player_name = input("please enter your name: ")
round_score = 0
total_score = 0
while True:
     diceValue = random.randint(1, 6)
     if diceValue != 1 and round_score < 100:
         round_score += diceValue
         print (f"dice {diceValue}")               
         print (f"Your current score is {round_score}")
         if round_score >= 100:
             print("🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉")
             print(f"🎉🎉🎉 congratulations you won 🎉🎉🎉")
             print("🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉")
             break
         roll_again = input("Roll again or Hold? 'r' or 'h': ").rstrip()
         if roll_again == "r":
             continue
         elif roll_again == "h":
             total_score += round_score
             round_score = 0
             print (f"Your total score is {total_score}")
             print("**********************************************************************")
             continue
         else:
             print("invalid choice")
             valid_choice = input("Roll again or Hold? 'r' or 'h': ")
     
     elif diceValue == 1:
         round_score = 0
         print("You have lost your round score!!!")
         print("**********************************************************************")