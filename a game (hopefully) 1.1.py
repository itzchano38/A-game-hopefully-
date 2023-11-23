import time
import random

class master():
  def __init__(self, name = "unknown", weapon = "unknown", attackdamage = 0, hp = 0, hpregen = 0, hpregen2 = 0):

    self.name = name
    self.weapon = weapon
    self.attackdamage = attackdamage
    self.hp = hp
    self.hpregen = hpregen
    self.hpregen2 = hpregen2

ranregen = random.randint(1,5)
ranregen2 = random.randint(1,5)

class elf(master):
  def __init__(self, name = "unknown", weapon = "unknown", attackdamage = 0, hp = 0, hpregen = 0):
    super().__init__(name = "Elf", weapon = "dagger", attackdamage = 10, hp = 50, hpregen = ranregen)
  def speak(self):
    print(self.name,"attacks with a",self.weapon,"and deals",self.attackdamage,"amount of damage.")
    print(self.name,"has an hp of",str(self.hp)+".")   
    print(self.name,"can regain",str(self.hpregen),"health.")   
    print()
    time.sleep(1)

class ork(master):
  def __init__(self, name = "unknown", weapon = "unknown", attackdamage = 0, hp = 0, hpregen2 = 0):
    super().__init__(name = "Ork", weapon = "club", attackdamage = 7, hp = 70, hpregen2 = ranregen2)
  def speak(self):
    print(self.name,"attacks with a",self.weapon,"and deals",self.attackdamage,"amount of damage.")
    print(self.name,"has an hp of",str(self.hp)+".")  
    print(self.name,"can regain",str(self.hpregen2),"health.")
    print()
    time.sleep(1)

def elf_choice(elf, ork):
  while ork.hp > 0 and elf.hp > 0:
    print(ork.name, "goes into battle with", elf.name)
    print(ork.name,"deals",ork.attackdamage,"attack damage onto",elf.name,"using",str(ork.weapon)+".")
    elf.hp -= ork.attackdamage
    print(elf.name, "has", elf.hp, "hp remaining")
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
    print("What are you going to do?")
    print("Regain health?")
    userinput = input("Attack? ")
    if userinput == "attack":
      print()
      print(elf.name,"deals",elf.attackdamage,"attack damage onto",ork.name,"using",str(elf.weapon)+".")
      ork.hp -= elf.attackdamage
      print(ork.name, "has", ork.hp, "hp remaining")
    else:
      print()
      elf.hp += elf.hpregen
      print(elf.name, "has regenerated",elf.hpregen, "health.")
      print(elf.name, "has", elf.hp, "hp remaining")
  

def ork_choice(elf, ork):
  while ork.hp > 0 and elf.hp > 0:
    print(elf.name, "goes into battle with", ork.name)
    print(elf.name,"deals",elf.attackdamage,"attack damage onto",ork.name,"using",str(elf.weapon)+".")
    ork.hp -= elf.attackdamage
    print(ork.name, "has", ork.hp, "hp remaining")
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
    print("What are you going to do?")
    print("Regain health?")
    userinput = input("Attack? ")
    if userinput == "attack":
      print()
      print(elf.name,"deals",elf.attackdamage,"attack damage onto",ork.name,"using",str(elf.weapon)+".")
      elf.hp -= ork.attackdamage
      print(elf.name, "has", elf.hp, "hp remaining")
    else:
      print()
      ork.hp += ork.hpregen2
      print(ork.name, "has regenerated",ork.hpregen2, "health.")
      print(ork.name, "has", ork.hp, "hp remaining")
   



elf_object = elf()
elf_object.speak()
ork_object = ork()
ork_object.speak()

player_choice = input("What character do you want to pick? Ork or Elf? ").lower()
if player_choice == "elf":
  player_choice = elf()
  elf_choice(elf_object, ork_object)
else:
  player_choice = ork()
  ork_choice(elf_object, ork_object)





      
      
      
      
  





 
  