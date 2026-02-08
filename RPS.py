#RPS.py
#Name: Afrah Mohamoud 
#Date: 02/05/2026
#Assignment: Lab 03 
#Purpose: Play Rock, Paper, Scissors and track results.
import random

def main():
  wins = 0
  ties = 0
  losses = 0
  #Create a loop that continues as long as the user wants to play.
  #User can play as many games as they wish.
  play_again = "Y"

  while play_again == "Y":
    #Randomly choose the computer between 'R', 'P', or 'S'
    computer = random.choice(["R", "P", "S"])
    #Prompt the user for their RPS selection
    user = input("Choose R, P, or S: ").strip().upper()

    while user not in ["R", "P", "S"]:
      user = input("Invalid choice. Choose R, P, or S: ").strip().upper()

    #Determine winner and state what happened to the user
    if user == computer:
      ties += 1
      print("Tie!")
    elif (user == "R" and computer == "S") or (user == "P" and computer == "R") or (user == "S" and computer == "P"):
      wins += 1
      print("You win!")
    else:
      losses += 1
      print("You lose!")

    #Ask the user if they would like to play again.
    play_again = input("Play again? (Y/N): ").strip().upper()
    while play_again not in ["Y", "N"]:
      play_again = input("Please enter Y or N: ").strip().upper()

  #In the end, print the stats
  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()
