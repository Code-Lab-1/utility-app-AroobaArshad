# Making a function that prints the menu for the vending machine 
# It displays all the products available alongwith their price, code and stock 
# Making categories of items to increase usability
# Using print function to display everything neatly

def PrintMenu():
  print('''--- Welcome to vending machine! ---
  \n  -~-~-~-~-~ Chocolates ~-~-~-~-~-
  Product   Price     Code   Stock
  \n  Twix      AED 3      10      5
  KitKat    AED 3      11      3
  Break     AED 2      12      6
  Flake     AED 2      13      5''')

  print('''\n\n  ~-~-~-~-~-~-~-~ Snacks ~-~-~-~-~-~-~-~
  Product     Price       Code     Stock
  \n  Pretzel     AED 4        20        5
  Cupcake     AED 2        21        7
  Popcorn     AED 2        22        5
  Cookie      AED 2        23        7''')

  print('''\n\n  ~-~-~-~-~-~-~- Cold Drinks -~-~-~-~-~-~-~
  Product      Price        Code      Stock
  \n  Coca Cola    AED 2         30         5 
  Fanta        AED 2         31         4
  Sprite       AED 2         32         4
  Lemonade     AED 2         33         2''') 

  print('''\n\n  ~-~-~-~-~-~-~-~-~-~ Hot Drinks ~-~-~-~-~-~-~-~-~-~
  Product         Price           Code         Stock
  \n  Hot Chocolate   AED 3            40            5
  Macha Latte     AED 5            41            4
  Coffee          AED 2            42            6
  Ginger tea      AED 2            43            3''')


# -Making a function that accepts any amount of money and returns the correct change- #
# -The arguments in the function are the name of the item chosen by user, item's price and amount of money entered by the user through input- #
# -The function also asks the user if they wish to pay with cash or credit/debit card- #
# -Using If Else statements to make sure correct amount of money is returned and correct remaining amount is demanded- #

def vend(name,price,userPrice):
  print("\nYou chose " + name + ". Do you want to pay with cash or credit/debit card?")
  answer = input("Please choose: a. Card   b. Cash  ")

  # If the user wishes to pay with card and chooses a:
  if answer == 'a':
    input("Insert your card and enter your pin code:")
    print("\nPlease wait... Authorizing...")
    print("*****************************")
    print("\nYour transaction was successful! Please remove your card. Here is your " + name + ".")

  # If the user wishes to pay with cash and chooses b:
  elif answer == 'b':
   print("Please enter " + str(price) + " Dhs.")
   userPrice = float(input())
   if userPrice == price:
     print ("Great! Here is your " + name + ".")

    # When less money is entered by the user, the machine asks for the rest of the money
   elif userPrice < price :
     Required_money = price - userPrice
     Response = float(input("You need to enter " + str(Required_money) + " Dhs more..."))
     if Response == Required_money:
       print("Great! Here is your " + name + " .")
     elif Response > Required_money:
       money = Response - Required_money
       print("Great! Here is your " + name + "." + "Your change is " + str(money) + " Dhs.")
     elif Response < Required_money:
       num = Required_money - Response
       Again = float(input("The money you entered is still not enough. Please enter " + str(num) + " Dhs more..."))
       if Again == num:
         print("Great! Here is your " + name + ".")
      
   else:
     change = userPrice - price
     print ("Great! Here is your " + name + "." + " Your change is " + str(change) + " Dhs.")


# -----Making an intelligence system that suggests other suitable items the user can buy----- #
# ----- The user can easily agree or disagree by typing  Y/y (for yes) and N/n (for no) -----#
# -----Using If Else statements that run the program depending on the user's answer-----#

def Something_Else(name,suggestion,price):
  print("\n" + suggestion + " goes great with " + name + "!" + " Would you like to buy it? Enter Y or N.")
  Answer = input()

  # When users agree, the code then runs the vend() function that deals with the payment
  if Answer == 'Y' or Answer == 'y':
    print("Great!")
    vend(suggestion,price,'userPrice')

  # When the user disagrees, the code prints "It's fine." and proceeds with the next step
  elif Answer == 'N' or Answer == 'n':
    print("It's fine!")
  else:
    print("Invalid Answer.")
    input("Enter only Y or N: ")
    if Answer == 'Y' or Answer == 'y':
      print("Great! You have bought " + suggestion + ".")
      vend(suggestion,price,'userPrice')
    elif Answer == 'N' or Answer == 'n':
      print("It's fine!") 



# === Making a function that asks the user if they want to buy something else === #
# === If they answer yes, the code runs the Vending_Machine function again. If they answer no, the code stops ===#

def asking_again():
  print("\nDo you want to buy something else?")
  userResponse = input("Enter Yes/No: ")
  if userResponse == "yes" or userResponse == "Yes":
    Vending_Machine()
  elif userResponse == "No" or userResponse == "no":
    print("\nThank you for your purchase. Have a great day!")



# === Main function that asks the user to enter the code of the item they want to buy === #
# === If wrong code is entered, the code prints "Invalid code" and asks for the code again === #

def Vending_Machine():
  userCode = int(input("\nPlease enter a code to purchase..."))

  if userCode == 10:
    vend('Twix',3,'userPrice')
    Something_Else('Twix','Coffee',2)
  elif userCode == 11:
    vend('Kitkat',3,'userPrice')
    Something_Else('KitKat','Coffee',2)
  elif userCode == 12:
    vend('Break',2,'userPrice')
    Something_Else('Break','Pretzel',3)
  elif userCode == 13:
    vend('Flake',2,'userPrice')
    Something_Else('Flake','Pretzel',3)
  elif userCode == 20:
    vend('Pretzel',4,'userPrice')
    Something_Else('Pretzel','Hot Chocolate',4)
  elif userCode == 21:
    vend('Cupcake',2,'userPrice')
    Something_Else('Cupcake','Ginger tea',4)
  elif userCode == 22:
    vend('Popcorn',2,'userPrice')
    Something_Else('Popcorn','Fanta',2)
  elif userCode == 23:
    vend('Cookie',2,'userPrice')
    Something_Else('Cookie','Coffee',2)
  elif userCode == 30:
    vend('Coca Cola',2,'userPrice')
    Something_Else('Coca Cola','Popcorn',3)
  elif userCode == 31:
    vend('Fanta',2,'userPrice')
    Something_Else('Fanta','Popcorn',3)
  elif userCode == 32:
    vend('Sprite',2,'userPrice')
    Something_Else('Sprite','Popcorn',3)
  elif userCode == 33:
    vend('Lemonade',2,'userPrice')
    Something_Else('Lemonade','Cupcake',2)
  elif userCode == 40:
    vend('Hot Chocolate',3,'userPrice')
    Something_Else('Hot Chocolate','Cupcake',2)
  elif userCode == 41:
    vend('Macha Latte',5,'userPrice')
    Something_Else('Macha Latte','Cookie',2)
  elif userCode == 42:
    vend('Coffee',2,'userPrice')
    Something_Else('Coffee','Cookie',2)
  elif userCode == 43:
    vend('Ginger tea',2,'userPrice')
    Something_Else('Ginger tea','Pretzel',3)
  else:
    print("Sorry, invalid code... Try again...")
    Vending_Machine()
  asking_again()


# === Calling the functions to operate the vending machine === #

PrintMenu()
Vending_Machine()

