import time
import random

#This is the constructor class. This determines a template of the individual attributes of the particular objects that the child classes will inherit.
class master():
  def __init__(self, name = "unknown", weapon = "unknown", attackdamage = 0, hp = 0, hpregen = 0, hpregen2 = 0, coins = 0):

    self.name = name
    self.weapon = weapon
    self.attackdamage = attackdamage
    self.hp = hp
    self.hpregen = hpregen
    self.hpregen2 = hpregen2
    self.coins = coins

#This provides a random number for the regen for the individual characters.
ranregen = random.randint(1,5)
ranregen2 = random.randint(1,5)

#This is the elf child class which has inherited the individual attributes from the class named "master". The "super().__init__" allows for me to determine what stats I want for the elf.
#An example of instantiation as an object is created.
class elf(master):
  def __init__(self, name = "unknown", weapon = "unknown", attackdamage = 0, hp = 0, hpregen = 0, coins = 0):
    super().__init__(name = "Elf", weapon = "dagger", attackdamage = 10, hp = 50, hpregen = ranregen, coins = 200)
  def speak(self):
    print(self.name,"attacks with a",self.weapon,"and deals",self.attackdamage,"amount of damage.")
    print(self.name,"has an hp of",str(self.hp)+".")   
    print(self.name,"can regain",str(self.hpregen),"health.")   
    print()
    time.sleep(1)

#This is the ork child class which has inherited the individual attributes from the class named "master". The "super().__init__" allows for me to determine what stats I want for the ork.
class ork(master):
  def __init__(self, name = "unknown", weapon = "unknown", attackdamage = 0, hp = 0, hpregen2 = 0, coins = 0):
    super().__init__(name = "Ork", weapon = "club", attackdamage = 7, hp = 70, hpregen2 = ranregen2, coins = 200)
  def speak(self):
    print(self.name,"attacks with a",self.weapon,"and deals",self.attackdamage,"amount of damage.")
    print(self.name,"has an hp of",str(self.hp)+".")  
    print(self.name,"can regain",str(self.hpregen2),"health.")
    print()
    time.sleep(1)

#This is the shop specifically for the elf. This subroutine allows for the user to choose their individual powerups depending on the amount of coins they have.
def elf_shop(elf):

  price_DRH = 30
  price_TRH = 60
  price_DAD = 70
  price_TAD = 120

  if elf.coins < price_DRH and elf.coins < price_TRH and elf.coins < price_DAD and elf.coins < price_TAD:
    print("\nYou don't have enough coins for any powerups!\n")
    pass
  else:
    print()
    print("You have been attacked!")
    time.sleep(1)
    print("...but you can get a powerup!")
    time.sleep(1)
    print("...but it will cost you coins!")
    time.sleep(1)
    print("Do you want to:")
    time.sleep(1)
    print()
    print("Double regain health for 30 coins")
    time.sleep(1)
    print("...or")
    time.sleep(1)
    print("Triple regain health for 60 coins")
    time.sleep(1)
    print("...or")
    time.sleep(1)
    print("Double attack damage for 70 coins")
    time.sleep(1)
    print("...or")
    shopinput = input("Triple attack damage for 120 coins: ").lower()
    if shopinput == "double regain health":
      if elf.coins < price_DRH:
        print("You don't have enough coins for this powerup!")
        return
      else:
        elf.coins = elf.coins - price_DRH
        print("\nYou now have",elf.coins,"coins left")
        elf.hpregen = elf.hpregen * 2
        print("You now have DOUBLE regain health!")
    elif shopinput == "triple regain health":
      if elf.coins < price_TRH:
        print("You don't have enough coins for this powerup!")
        return
      else:
        elf.coins = elf.coins - price_TRH
        print("\nYou now have",elf.coins,"coins left")
        elf.hpregen = elf.hpregen * 3
        print("You now have TRIPLE regain health!")
    elif shopinput == "double attack damage":
      if elf.coins < price_DAD:
        print("You don't have enough coins for this powerup!")
        return
      else:
        elf.coins = elf.coins - price_DAD
        print("\nYou now have",elf.coins,"coins left")
        elf.attackdamage = elf.attackdamage * 2
        print("You now have DOUBLE attack damage!")
    elif shopinput == "triple attack damage":
      if elf.coins < price_TAD:
        print("You don't have enough coins for this powerup!")
        return
      else:  
        elf.coins = elf.coins - price_TAD
        print("\nYou now have",elf.coins,"coins left")
        elf.attackdamage = elf.attackdamage * 3
        print("You now have TRIPLE attack damage!")
    else:
      print("\nThat is not a valid input! No powerup for you!")
      pass
    if elf.coins <= 0:
      print("\nYou have no coins left!")
      return

#This is the shop specifically for the ork. This subroutine allows for the user to choose their individual powerups depending on the amount of coins they have.
def ork_shop(ork):

  price_DRH = 30
  price_TRH = 60
  price_DAD = 70
  price_TAD = 120

  if ork.coins < price_DRH and ork.coins < price_TRH and ork.coins < price_DAD and ork.coins < price_TAD:
    print("\nYou don't have enough coins for any powerups!\n")
    pass
  else:
    print()
    print("You have been attacked!")
    time.sleep(1)
    print("...but you can get a powerup!")
    time.sleep(1)
    print("...but it will cost you coins!")
    time.sleep(1)
    print("Do you want to:")
    time.sleep(1)
    print()
    print("Double regain health for 30 coins")
    time.sleep(1)
    print("...or")
    time.sleep(1)
    print("Triple regain health for 60 coins")
    time.sleep(1)
    print("...or")
    time.sleep(1)
    print("Double attack damage for 70 coins")
    time.sleep(1)
    print("...or")
    shopinput = input("Triple attack damage for 120 coins: ").lower()
    if shopinput == "double regain health":
      if ork.coins < price_DRH:
        print("You don't have enough coins for this powerup!")
        return
      else:  
        ork.coins = ork.coins - price_DRH
        print("\nYou now have",elf.coins,"coins left")
        ork.hpregen = ork.hpregen * 2
        print("You now have DOUBLE regain health!")
    elif shopinput == "triple regain health":
      if ork.coins < price_TRH:
        print("You don't have enough coins for this powerup!")
        return
      else:
        ork.coins = ork.coins - price_TRH
        print("\nYou now have",elf.coins,"coins left")
        ork.hpregen = ork.hpregen * 3
        print("You now have TRIPLE regain health!")
    elif shopinput == "double attack damage":
      if ork.coins < price_DAD:
        print("You don't have enough coins for this powerup!")
        return
      else:  
        ork.coins = ork.coins - price_DAD
        print("\nYou now have",ork.coins,"coins left")
        ork.attackdamage = ork.attackdamage * 2
        print("You now have DOUBLE attack damage!")
    elif shopinput == "triple attack damage":
      if ork.coins < price_TAD:
        print("You don't have enough coins for this powerup!")
        return
      else:  
        ork.coins = ork.coins - price_TAD
        print("\nYou now have",ork.coins,"coins left")
        ork.attackdamage = ork.attackdamage * 3
        print("You now have TRIPLE attack damage!")
    else:
      print("\nThat is not a valid input! No powerup for you!")
      pass
    if ork.coins <= 0:
      print("\nYou have no coins left!")
      return

#These small subroutines revert the stats effected by the powerups to their original attributes. 
#Otherwise it would create a logic error where the stat would continously be powered up which would create an unfair battle.
def elf_hp_revert(elf):
  elf.hpregen = ranregen

def ork_hp_revert(ork):
  ork.hpregen = ranregen2

def elf_AD_revert(elf):
  elf.attackdamage = 10

def ork_AD_revert(ork):
  ork.attackdamage = 7

#This subroutine determines whether the computer (if it is the ork) can purchase powerups from the shop like the player which can allow the computer to purchase powerups.
#"diceroll = random.randint(1,2)" allows for the computer's input to be randomised and thus makes the game unpredictable.
def ork_diceroll(ork):
  price_DAD = 70
  price_TAD = 120
  diceroll = random.randint(1,2)
  if ork.coins < price_DAD and ork.coins < price_TAD:
    print(ork.name,"don't have enough coins for any powerups!\n")
    pass
  else:
    if diceroll == 1:
      if ork.coins < price_DAD:
        return
      else:
        ork.coins = ork.coins - price_DAD
        print(ork.name,"now has DOUBLE attack damage!")
        print(ork.name,"now has",ork.coins,"coins left")
        ork.attackdamage = ork.attackdamage * 2
    elif diceroll == 2:
      if ork.coins < price_TAD:
        print("You don't have enough coins for this powerup!")
        return
      else:
        ork.coins = ork.coins - price_TAD
        print(ork.name,"now has TRIPLE attack damage!")
        print(ork.name,"now has",ork.coins,"coins left")
        ork.attackdamage = ork.attackdamage * 3
    else:
      pass
    if ork.coins <= 0:
      print(ork.name,"has no coins left!")
      return

#This subroutine determines whether the computer (if it is the elf) can purchase powerups from the shop like the player which can allow the computer to purchase powerups.
#"diceroll = random.randint(1,2)" allows for the computer's input to be randomised and thus makes the game unpredictable.
def elf_diceroll(elf):
  price_DAD = 70
  price_TAD = 120
  diceroll = random.randint(1,2)
  if elf.coins < price_DAD and elf.coins < price_TAD:
    print(elf.name,"don't have enough coins for any powerups!\n")
    pass
  else:
    if diceroll == 1:
      if elf.coins < price_DAD:
        return
      else:
        elf.coins = elf.coins - price_DAD
        print(elf.name,"now has DOUBLE attack damage!")
        print(elf.name,"now has",elf.coins,"coins left")
        elf.attackdamage = elf.attackdamage * 2
    elif diceroll == 2:
      if elf.coins < price_TAD:
        print("You don't have enough coins for this powerup!")
        return
      else:
        elf.coins = elf.coins - price_TAD
        print(elf.name,"now has TRIPLE attack damage!")
        print(elf.name,"now has",elf.coins,"coins left")
        elf.attackdamage = elf.attackdamage * 3
    else:
      pass
    if elf.coins <= 0:
      print(elf.name,"has no coins left!")
      return

#This is the subroutine which is where the method of of the code takes place which is when player fights the CPU if they selected the elf as their playable character.
#The user can then battle the CPU by either attacking or regaining health. The user can take advantage of the shop subroutine already determined previously but the CPU can also get powerups as well.
#The elf and the ork classes are passed into the subroutine "elf_choice" which allows for the subroutine to take in the individual attributes of these two classes and allows them to fight each other.
def elf_choice(elf, ork):
  while ork.hp > 0 and elf.hp > 0:
    print("You have",elf.coins,"coins.")
    print(ork.name, "goes into battle with", elf.name)
    print()
    ork_diceroll(ork)
    print(ork.name,"deals",ork.attackdamage,"attack damage onto",elf.name,"using",str(ork.weapon)+".")
    elf.hp -= ork.attackdamage
    print(elf.name, "has", elf.hp, "hp remaining")
    ork_AD_revert(ork)
    if elf.hp <= 0:
      print("\n**********************************\n")
      print(elf.name,"has been defeated!")
      break
    elif ork.hp <= 0:
      print("\n**********************************\n")
      print(ork.name,"has been defeated!")
      break
    elf_shop(elf)
    userinput = input("What are you going to do?\nAttack?\nRegain health? ")
    if userinput == "attack":
      print()
      print(elf.name,"deals",elf.attackdamage,"attack damage onto",ork.name,"using",str(elf.weapon)+".")
      ork.hp -= elf.attackdamage
      print(ork.name, "has", ork.hp, "hp remaining")
      elf_AD_revert(elf)
      if elf.hp <= 0:
        print("\n**********************************\n")
        print(elf.name,"has been defeated!")
        break
      elif ork.hp <= 0:
        print("\n**********************************\n")
        print(ork.name,"has been defeated!")
        break
    else:
      print()
      elf.hp += elf.hpregen
      print(elf.name, "has regenerated",elf.hpregen, "health.")
      print(elf.name, "has", elf.hp, "hp remaining")
      elf_hp_revert(elf)

  #This is the subroutine which is where the method of of the code takes place which is when player fights the CPU if they selected the ork as their playable character.
  #The user can then battle the CPU by either attacking or regaining health. The user can take advantage of the shop subroutine already determined previously but the CPU can also get powerups as well.
  #The elf and the ork classes are passed into the subroutine "elf_choice" which allows for the subroutine to take in the individual attributes of these two classes and allows them to fight each other.
def ork_choice(elf, ork):
  while ork.hp > 0 and elf.hp > 0:
    print("You have",ork.coins,"coins.")
    print(elf.name, "goes into battle with", ork.name)
    print()
    elf_diceroll(elf)
    print(elf.name,"deals",elf.attackdamage,"attack damage onto",ork.name,"using",str(elf.weapon)+".")
    ork.hp -= elf.attackdamage
    print(ork.name, "has", ork.hp, "hp remaining")
    elf_AD_revert(elf)
    if elf.hp <= 0:
      print()
      print("**********************************")
      print()
      print(elf.name,"has been defeated!")
      break
    elif ork.hp <= 0:
      print()
      print("**********************************")
      print()
      print(ork.name,"has been defeated!")
      break
    ork_shop(ork)
    userinput = input("What are you going to do?\nAttack?\nRegain health? ")
    if userinput == "attack":
      print()
      print(ork.name,"deals",ork.attackdamage,"attack damage onto",elf.name,"using",str(elf.weapon)+".")
      elf.hp -= ork.attackdamage
      print(elf.name, "has", elf.hp, "hp remaining")
      ork_AD_revert(ork)
      if elf.hp <= 0:
        print()
        print("**********************************")
        print()
        print(elf.name,"has been defeated!")
        break
      elif ork.hp <= 0:
        print()
        print("**********************************")
        print()
        print(ork.name,"has been defeated!")
        break
    else:
      print()
      ork.hp += ork.hpregen2
      print(ork.name, "has regenerated",ork.hpregen2, "health.")
      print(ork.name, "has", ork.hp, "hp remaining")
      ork_hp_revert(ork)
      
#These subroutines are run at the beginning of the code which displays the individual stats for the two characters using the ".speak" subroutine.
elf_object = elf()
elf_object.speak()
ork_object = ork()
ork_object.speak()

#This allows for the user to pick their character. Depending on what they pick, a certain subroutine is executed and the battle begins.
player_choice = input("What character do you want to pick? Ork or Elf? ").lower()
if player_choice == "elf":
  player_choice = elf()
  elf_choice(elf_object, ork_object)
else:
  player_choice = ork()
  ork_choice(elf_object, ork_object)


    

    
    
  
  
