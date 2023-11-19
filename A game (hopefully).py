import time
import random

class master():
  def __init__(self, name = "unknown", weapon = "unknown", attackdamage = 0, hp = 0):
    
    self.name = name
    self.weapon = weapon
    self.attackdamage = attackdamage
    self.hp = hp

class elf(master):
  def __init__(self, name = "unknown", weapon = "unknown", attackdamage = 0, hp = 0):
    super().__init__(name = "Elf", weapon = "dagger", attackdamage = 2, hp = 20)
  def speak(self):
    print(self.name,"attacks with a",self.weapon,"and deals",self.attackdamage,"amount of damage.")
    print(self.name,"has an hp of",str(self.hp)+".")   
    print()
    time.sleep(1)

class ork(master):
  def __init__(self, name = "unknown", weapon = "unknown", attackdamage = 0, hp = 0):
    super().__init__(name = "Ork", weapon = "club", attackdamage = 4, hp = 40)
  def speak(self):
    print(self.name,"attacks with a",self.weapon,"and deals",self.attackdamage,"amount of damage.")
    print(self.name,"has an hp of",str(self.hp)+".")  
    print()
    time.sleep(1)

  def battle(ork, elf):
    while ork.hp > 0 and elf.hp > 0:
      print(ork.name, "goes into battle with", elf.name)
      print(ork.name,"deals",ork.attackdamage,"attack damage onto",elf.name,"using",str(ork.weapon)+".")
      elf.hp -= ork.attackdamage
      print(elf.name, "has", elf.hp, "hp remaining")
      print(elf.name, "goes into battle with", ork.name)
      if elf.hp == 0:
        print()
        print("**********************************")
        print()
        print(elf.name,"has been defeated!")
        break
        
      print(elf.name,"deals",elf.attackdamage,"attack damage onto",ork.name,"using",str(elf.weapon)+".")
      ork.hp -= elf.attackdamage
      print(ork.name, "has", ork.hp, "hp remaining")
      if ork.hp == 0:
        print()
        print("**********************************")
        print()
        print(ork.name,"has been defeated!")
        break
      print()
      time.sleep(1)
     
object = elf()
object.speak()
object2 = ork()
object2.speak()
object2.battle(object)
    

#object = elf()
#object.speak()

#object2 = ork()
#object2.speak()








    
       



