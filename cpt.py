
import random
total = 0
count = 0
quiz = True
game = True
item_one = True
item_two = True
item_three = True
item_four = True
item_five = True

print("*** Welcome to the Computer Buyer Game ***")

# Input word to start the game
money_claim = input("Enter 'money claim': ").lower()

#Loop the code until user enters money claim
while money_claim != "money claim":
  money_claim = input("Please type money claim: ").lower()

if money_claim == "money claim":
  total += 500
  print("You just claimed 500 dollars\n")

# Main program loop
while game:
  action = input("What would you like to do next?( Instruction, risk, shop, \nmoney check, money earn): ")

  # Prints text if user enters instruction
  if action == "instruction":
    print("\n*** Instructions ***")
    print("-You can risk your money.\n There is a 50-50 odd to either gain or lose money.")
    print("-You can use money check to see your balance!")
    print("-Money earn will give you 10 questions where you can answer\n to earn money")
    print("-You can buy computer parts in the shop! \n If you buy all the items you win the game!")
    print("-If you have 0 dollars, you lose the game. \nYou will need to reset the program to play again\n")
    
  # If user enters risk, allow them to enter money
  elif action == "risk":
    while True:
      try:
        risk_money = int(input("\nHow much do you want to risk? Your current balance is " +str(total) + "(Enterinteger): "))
        while risk_money > total or risk_money <= 0:
          risk_money = int(input("That is too much/too little money.\nYour balance is " +str(total)+ "\nHow much do you want to risk?(Enter integer): "))
      except ValueError:
        print("Please enter a number")
        continue
      else:
        break

    # If the risk is equal/lower than their total, there is a 50-50 chance for them to win or lose the amount  
    if risk_money <= total:
      fifty_chance = random.randint(0,1)
      if fifty_chance == 0:
          total += risk_money
          print("You have won. Your balance is", total, "\n")
      elif fifty_chance == 1:
          total -= risk_money
          print("You have lost.Your balance is", total , "\n")
  
  # If user enters shop, set a list of items they can buy
  elif action == "shop":
    while True:
      try: 
        shop_items = int(input("\nWelcome to the shop! Please pick an item.\n 1. Gaming Mouse: $50 \n 2. Gaming Keyboard: $150 \n 3. I7 CPU: $300 \n 4. 3080 GPU: $700 \n 5. 144hrz monitor: $350 \n Put the number here: "))
        while shop_items >= 6:
          shop_items = int(input("Please pick a number between 1-5: "))
      except ValueError:
        print("Please type a number")
        continue
      else:
        break
    
    if shop_items == 1 and total >= 50 and item_one == True:
      item_one = False 
      total -= 50
      print("Your new balance is " +str(total)+ ". You have bought item one!\n")
    
    elif shop_items == 2 and total >= 150 and item_two == True:
      item_two = False
      total -= 150
      print("Your new balance is " +str(total)+ ". You have bought item two!\n")

    elif shop_items == 3 and total >= 300 and item_three == True:
      item_three = False
      total -= 300
      print("Your new balance is " +str(total)+ ". You have bought item three!\n")

    elif shop_items == 4 and total >= 700 and item_four == True:
      item_four = False
      total -= 700
      print("Your new balance is " +str(total)+ ". You have bought item four!\n")

    elif shop_items == 5 and total >= 350 and item_five == True:
      item_five = False
      total -= 350
      print("Your new balance is " +str(total)+ ". You have bought item five!\n")

    #If an item is bought, output that the item is bought
    elif item_one == False and shop_items == 1 or item_two == False and shop_items == 2 or item_three== False and shop_items == 3 or item_four == False and shop_items == 4 or item_five == False and shop_items == 5:
      print("You have bought this item already\n")

    # Output statement if user does not have the required money to buy an item
    elif shop_items == 1 and total < 50 or shop_items == 2 and total < 150 or shop_items == 3 and total < 300 or shop_items == 4 and total < 700 or shop_items == 5 and total < 350 or item_one and item_two and item_three and item_four and item_five == True:
      print("You do not have enough money to buy the item.\n")

  #If user enters money check, outputs their current balance
  elif action == "money check":
    print("\nYour current amount of money is " +str(total)+ "\n")

  #If the quiz is done and user enters money earn, output they already done the test
  elif action == "money earn" and quiz == False:
    print("\nYou have already done this test!\n")
  #If the quiz is not done and user enters money earn, allow the quiz to be done
  elif action == "money earn" and quiz == True:
    quiz = False 
    print("\nYou can only do these questions once per game. There will be ten questions and every correct answer will give you 50 dollars")
    question_one = input("\n1. What is not a part of a computer?\nA. Monitor B. Keyboard C. CPU D. Phone : ").lower()
    question_two = input("\n2. What is the correct computer malware?\nA. Adware B. Busy C. Scary D. Fizy : ").lower()
    question_three = input("\n3. Which one is an operating system?\nA. Windows B. Sky C. Pear. D Skying : ").lower()
    question_four = input("\n4. How many bytes are in a kilobyte?\nA. 800 B. 1024 C. 1000. D 500 : ").lower()
    question_five = input("\n5. What is part of the networking program?\nA. Fan B. Lights C. Modem D. Book : ").lower()
    question_six = input("\n6. What computer device is the brain of the computer?\nA. CPU B. GPU C. Motherboard D. RAM : ").lower()
    question_seven = input("\n7. How many bits are in a byte?\nA. 5 B. 6 C. 7 D. 8 : ").lower()
    question_eight = input("\n8. Which of the following is generally used to measure data transfer speed?\nA. Mbps B. Mhz C. Ghz D. MB/s : ").lower()
    question_nine = input("\n9. What does RAM stand for? Type your answer: ").lower()
    question_ten = input("\n10. What does GPU stand for? Type your answer: ").lower()
    
    #The start where it checks for the correct answers
    if question_one == "d":
      count += 1 
      print("\n1. Correct")
    else:
      print("\n1. Incorrect")

    if question_two == "a":
      count += 1
      print("2. Correct")
    else:
      print("2. Incorrect")

    if question_three == "a":
      count += 1
      print("3. Correct")
    else:
      print("3. Incorrect")

    if question_four == "b":
      count += 1
      print("4. Correct")
    else:
      print("4. Incorrect")

    if question_five == "c":
      count += 1
      print("5. Correct")
    else:
      print("5. Incorrect")
    
    if question_six == "a":
      count += 1
      print("6. Correct")
    else:
      print("6. Incorrect")
    
    if question_seven == "d":
      count += 1
      print("7. Correct")
    else:
      print("7. Incorrect")

    if question_eight == "a":
      count+= 1
      print("8. Correct")
    else:
      print("8. Incorrect")

    if question_nine == "random access memory":
      count += 1
      print("9. Correct")
    else:
      print("9. Incorrect")
    
    #Ending of where it checks for correct answers
    if question_ten == "graphics processing unit":
      count += 1
      print("10. Correct")
    else:
      print("10. Incorrect")
    
    #Multiply to find the amount of money earned 
    money_earn = count * 50
    total += money_earn
    
    print("You got " +str(count)+ " out of 10. You have earned " +str(money_earn)+ ". \nYour new total is " +str(total)+ ".\n")

  #User is outputted this message if they do not enter the required words 
  else: 
    print("\nPlease enter instruction, risk, shop, money check or money earn\n")

  # Break the program if all items are bought 
  if total > 0 and item_one == False and item_two == False and item_three == False and item_four == False and item_five == False:
      game = False
      print("Congratulations. You have won the game!")
  
  # Break the program when your total reaches zero
  if total == 0:
      game = False 
      print("You have lost the game. Restart the program to play again.")



    









