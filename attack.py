import random

playerhp = 360
enemyatkl = 60
enemyatkh = 90

while playerhp > 0:
    dmg = random.randrange(enemyatkl, enemyatkh)
    playerhp -= dmg
    
    
    if playerhp <= 30:
      playerhp = 30
      
    print("Enemy strikes for", dmg, "points of damage. Current HP is", playerhp)
    
    if playerhp == 30:
      print("You have died. Yo cannot respawn, as you are dead.")
      break