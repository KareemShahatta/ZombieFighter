import random
#KareemShahatta 06/11/2023

#main function to generate the number of zombies, greet the user, and start the game
def main():
  zombies = random.randint(5,11)
  createEquation(greetUser() , zombies , 3)

#Obtains the username and greeting the user
def greetUser():                    
  print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
  username = input("Hello survivor! What is your name?  ")
  print(f"\nNice to meet you, {username}!")
  print("Our city is under attack by zombies, and we need your help.")
  print("A random wave of 5 - 10 zombies will attack and have three shots to defeat them.")
  print("In order to defeat the zombies, you must solve addition/subtraction equations.")
  print("Solve the equation right, to defeat a zombie, but solve it wrong, you lose an attempt.")
  print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
  return username

#Display the number of zobmies and attempts remianing
def displayInfo(zombies , hearts):
  print("Z "* zombies)
  print(f"Number of attempts H:{hearts}\n")

#Get the user's answer for solving the equation and checks it
def getUserInput():
  while(True):
    try:
      return int(input("Your answer: "))
    except:
      print("Not a valid answer, try again")

#Displays a random message out of four if the user got the answer right 
def rightAnswer():
  replies = ["That is correct" , "Perfect!", "Correct!" , "We have a math wizard!"]
  print(">>" + random.choice(replies))
  print("═════════════════════════════") #A line to sperate the current equaton form the next one

#Displays a random message out of four if the user got the answer wrong 
def wrongAnswer():
  replies = ["That is incorrect!" , "Maybe retake math 101?", "Incorrect!" , "Wrong!"]
  print(">>" + random.choice(replies))
  print("═════════════════════════════") #A line to sperate the current equaton form the next one

#Asks the user if they want to play again
def playAgain():
  answer = input("Press Y if you want to play again: ")
  if answer.lower() == 'y':
    main()
  else:
    print("Thank you for playing!")

#Displays a message with the user name if they lost the game and asks if they want to play again
def playerLost(username):
  print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
  print(f"Unfortunately {username}, you failed to defeat the evil zombies. :(")
  playAgain()

#Displays a message with the user name if they won the game and asks if they want to play again
def playerWon(username):
  print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
  print(f"Congratulation {username}, you defeated all the evil zombies! :D")
  playAgain()

#Check if the user won, lost , or is still playing the game before making a new equation
def checkStatus(username , zombies, hearts):
  if hearts == 0:
    playerLost(username)
  elif zombies == 0:
    playerWon(username)
  else:
    createEquation(username, zombies, hearts)

#Creates a random math equation for the user to solve
def createEquation(username , zombies , hearts):
  
  #Display the user's current status
  displayInfo(zombies , hearts) 

  #Create the random numbers for the equation
  num1 = random.randint(1,10)
  num2 = random.randint(1,10)
  result = 0

  #Determine if the question is (+ , - , x)
  operator = random.randint(1,4)
  if operator == 1:
    result = num1 + num2
    print(f"Equation {num1} + {num2}:")
  elif operator == 2:
    result = num1 * num2
    print(f"Equation {num1} x {num2}:")
  else:
    result = num1 - num2
    print(f"Equation {num1} - {num2}:")

  #Gets the user's answer and processes it
  if getUserInput() == result:
    rightAnswer()
    checkStatus(username , zombies - 1, hearts)
  else:
    wrongAnswer()
    checkStatus(username , zombies, hearts - 1)

#Check that we are in the main module 
if __name__ == "__main__":
  main()