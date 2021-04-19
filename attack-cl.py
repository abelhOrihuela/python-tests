'''
Examples of classes
'''
 
class Enemy:
  def __init__(self, atkl, atkh):
      self.atkl = atkl
      self.atkh = atkh
      
  def getAtk(self):
    print(self.atkl)
    
enemy = Enemy(20, 30)
enemy.getAtk()

enemy2 = Enemy(60, 90)
enemy2.getAtk()