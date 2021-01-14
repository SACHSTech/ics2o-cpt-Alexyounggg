
import random
total = 0
item_one = True
item_two = True
item_three = True
item_four = True
item_five = True

print("*** Welcome to the Computer Buyer Game ***")

money_claim = input("Type money claim: ")

while money_claim != "money claim":
  money_claim = input("Please type money claim. Watch for capitals: ")

if money_claim == "money claim":
  total += 500
  print("You just claimed 500 dollars")

while True:
  action = input("What would you like to do next?( Instruction,risk,shop): ")

  if action == "instruction":
    print("You can also risk your money. There is a 50-50 odd to either gain or lose money.")
    print("You can buy computer parts in the shop! If you buy all the items you win the game!")
    print("If you have 0 dollars, you lost the game. Reset the program to restart")
    

  elif action == "risk":
      risk_money = int(input("How much do you want to risk?: "))
      if risk_money > total:
        risk_money = int(input("That is too much money. How much do you want to gamble?: "))
      elif risk_money <= total:
        fifty_chance = random.randint(0,1)
        if fifty_chance == 0:
            total += risk_money
            print("Your total is", total)
        elif fifty_chance == 1:
            total -= risk_money
            print("Your total is", total)

  elif action == "shop":
    shop_items = int(input("Welcome to the shop! Please pick a an item.\n 1. Gaming Mouse: $50 \n 2. Gaming Keyboard: $150 \n 3. I7 CPU: $300 \n 4. 3080 GPU: $700 \n 5. 144hrz monitor: $300 \n 6. Put the number here: "))
    while shop_items >= 6:
      shop_items = int(input("Please pick a number between 1-5: "))
    
    if shop_items == 1 and total >= 50 and item_one == True:
      item_one = False 
      print("You have bought item one!")
    
    elif shop_items == 2 and total >= 150 and item_two == True:
      item_two = False
      print("You have bought item two!")

    elif shop_items == 3 and total >= 300 and item_three == True:
      item_three = False
      print("You have bought item item three")

    elif shop_items == 4 and total >= 700 and item_four == True:
      item_three = False
      print("You have bought item four")

    elif shop_items == 5 and total >= 300 and item_five == True:
      item_three = False
      print("You have bought item five")

    elif shop_items == 1 and total < 50 or shop_items == 2 and total < 150 or shop_items == 3 and total < 300 or shop_items == 4 and total < 700 or shop_items == 5 and total < 300 

    elif item_one or item_two or item_three or item_four or item_five == False:
      print("You have bought this item already")

    









