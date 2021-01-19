
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

# Enter money claim to start the game
money_claim = input("Enter 'money claim': ").lower()

#Loop the code until user enters money claim
while money_claim != "money claim":
  money_claim = input("Please type money claim: ").lower()

if money_claim == "money claim":
  total += 500
  print("You just claimed 500 dollars")

# Main program loop
while game:
  action = input("What would you like to do next?( Instruction, risk, shop, \nmoney check, money earn): ")

  if action == "instruction":
    print("-You can also risk your money.\n There is a 50-50 odd to either gain or lose money.")
    print("-You can buy computer parts in the shop! \n If you buy all the items you win the game!")
    print("-If you have 0 dollars, you lose the game. \nReset the program to restart")
    

  elif action == "risk":
    while True:
      try:
        risk_money = int(input("How much do you want to risk? Your current balance is " +str(total) + "(Enterinteger): "))
        while risk_money > total or risk_money <= 0:
          risk_money = int(input("That is too much/too little money.\nYour balance is " +str(total)+ "\nHow much do you want to risk?(Enter integer): "))
      except ValueError:
        print("Please enter a number")
        continue
      else:
        break
      
    if risk_money <= total:
      fifty_chance = random.randint(0,1)
      if fifty_chance == 0:
          total += risk_money
          print("You have won. Your balance is", total)
      elif fifty_chance == 1:
          total -= risk_money
          print("You have lost.Your balance is", total)

  elif action == "shop":
    while True:
      try: 
        shop_items = int(input("Welcome to the shop! Please pick a an item.\n 1. Gaming Mouse: $50 \n 2. Gaming Keyboard: $150 \n 3. I7 CPU: $300 \n 4. 3080 GPU: $700 \n 5. 144hrz monitor: $350 \n 6. Put the number here: "))
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
      print("Your new balance is " +str(total)+ ". You have bought item one!")
    
    elif shop_items == 2 and total >= 150 and item_two == True:
      item_two = False
      total -= 150
      print("Your new balance is " +str(total)+ ". You have bought item two!")

    elif shop_items == 3 and total >= 300 and item_three == True:
      item_three = False
      total -= 300
      print("Your new balance is " +str(total)+ ". You have bought item three!")

    elif shop_items == 4 and total >= 700 and item_four == True:
      item_four = False
      total -= 700
      print("Your new balance is " +str(total)+ ". You have bought item four!")

    elif shop_items == 5 and total >= 350 and item_five == True:
      item_five = False
      total -= 350
      print("Your new balance is " +str(total)+ ". You have bought item five!")

    elif item_one == False and shop_items == 1 or item_two == False and shop_items == 2 or item_three== False and shop_items == 3 or item_four == False and shop_items == 4 or item_five == False and shop_items == 5:
      print("You have bought this item already")

    elif shop_items == 1 and total < 50 or shop_items == 2 and total < 150 or shop_items == 3 and total < 300 or shop_items == 4 and total < 700 or shop_items == 5 and total < 350 or item_one and item_two and item_three and item_four and item_five == True:
      print("You do not have enough money to buy the item.")

  elif action == "money check":
    print("Your current amount of money is " +str(total))

  elif action == "money earn" and quiz == False:
    print("You have already done this test!")
  elif action == "money earn" and quiz == True:
    quiz = False 
    print("You can only do these questions once per game. There will be five questions and every answer right will give you 100 dollars")
    question_one = input("1. What is not a part of a computer?\nA. Monitor B. Keyboard C. CPU D. Phone :")
    question_two = input("2. What is the correct computer malware?\nA. Adware B. Busy C. Scary D. Fizy : ")
    question_three = input("3. Which one is an operating system?\nA. Windows B. Sky C. Pear. D Skying : ")
    question_four = input("4. How many bytes are in a kilobyte?\nA. 800 B. 1024 C. 1000. D. 500 : ")
    question_five = input("What is part of the networking program?\nA. Fan B. Lights C. Modem D. Book : ")
    

    if question_one == "D".lower():
      count += 1 

    if question_two == "A".lower():
      count += 1

    if question_three == "A".lower():
      count += 1

    if question_four == "B".lower():
      count += 1

    if question_five == "C".lower():
      count += 1
    
    #Multiply to find the amount of money earned 
    money_earn = count * 100
    total += money_earn
    
    print("You got " +str(count)+ " out of 5. You have earned " +str(money_earn)+ ". Your new total is " +str(total)+ ".")

  
  else: 
    print("Please enter instruction, risk, shop, or money check")

  # Break the program if all items are bought 
  if total > 0 and item_one == False and item_two == False and item_three == False and item_four == False and item_five == False:
      game = False
      print("Congratulations. You have won the game!")
  
  # Break the program when your total reaches zero
  if total == 0:
      game = False 
      print("You have lost the game. Restart program to play again.")



    









