from __future__ import print_function
import random
import time
# Red is back slash
# Blue is forward slash
# Yellow is straight line down
# Black is a colon.
# For Mr. Landfrieds 3rd Period Comp. Sci.

def setvar():
  global wire1
  global wire2
  global wire3
  global wire4
  global wire5
  wire1 = rand = random.randint(1,4)
  wire2 = rand = random.randint(1,4)
  wire3 = rand = random.choice([0, 0, 0, 1, 2, 3, 4])
  wire4 = rand = random.randint(1,4)
  wire5 = rand = random.choice([0, 0, 0, 1, 2, 3, 4])
def wires():
    global wire1c
    global wire2c
    global wire3c
    global wire4c
    global wire5c
    setvar()
    if wire1 == 1:
      wire1c = "\\"
    elif wire1 == 2:
      wire1c = "/"
    elif wire1 == 3:
      wire1c = "|"
    elif wire1 == 4:
      wire1c = ":"
    else:
      wire1c = " "
    if wire2 == 1:
      wire2c = "\\"
    elif wire2 == 2:
      wire2c = "/"
    elif wire2 == 3:
      wire2c = "|"
    elif wire2 == 4:
      wire2c = ":"
    else:
      wire2c = " "
    if wire3 == 1:
      wire3c = "\\"
    elif wire3 == 2:
      wire3c = "/"
    elif wire3 == 3:
      wire3c = "|"
    elif wire3 == 4:
      wire3c = ":"
    else:
      wire3c = " "
    if wire4 == 1:
      wire4c = "\\"
    elif wire4 == 2:
      wire4c = "/"
    elif wire4 == 3:
      wire4c = "|"
    elif wire4 == 4:
      wire4c = ":"
    else:
      wire4c = " "
    if wire5 == 1:
      wire5c = "\\"
    elif wire5 == 2:
      wire5c = "/"
    elif wire5 == 3:
      wire5c = "|"
    elif wire5 == 4:
      wire5c = ":"
    else:
        wire5c = " "
    global liste
    liste = [wire1c, wire2c, wire3c, wire4c, wire5c]
    nowires = 5
    mor = 0
    rules = print("""
    
    # Red is back slash
    # Blue is forward slash
    # Yellow is straight line down
    # Black is a colon.
    
    A wire module can have 3-5 wires on it.
    Only one correct wire needs to be cut to defuse.
    Wire ordering begins with the first on top.
    Rules from bottom to top can overwrite eachother.
    
    3 Wires:
      If there are no red wires, cut the second wire.
      Otherwise, if the last wire is black, cut the last wire.
      Otherwise, if there is more than one blue wire, cut the last wire.
      Otherwise, cut the first wire.
    
    4 Wires:
      If there are more than one red wires, cut the second wire.
      Otherwise, If the last wire is yellow, and there are no red wires, cut the last wire.
      Otherwise, If there is exactly one blue wire, cut the second wire.
      Otherwise, if there is more than one yellow wire, cut the fourth wire.
      Otherwise, cut the first wire.
      
    5 wires:
      if the last wire is black, cut the fourth wire.
      Otherwise, if there is exactly one red wire, and more than one yellow wire, cut the first wire.
      Otherwise, if there are no black wires, cut the second wire.
      Otherwise, cut the first wire.
      
    """)
    for morethan2 in liste:
      if morethan2 == " ":
        mor += 1
        if mor <= 2:
          setvar()
    for x in liste:
        if x == " ":
            nowires -= 1
    print ("""
    Plaids' Wires
    -------------
    1  2  3  4  5
    """, wire1c, "  ", wire2c, "  ", wire3c, "  ", wire4c, "  ", wire5c,
    

    sep = "")
    
    # Red is back slash
    # Blue is forward slash
    # Yellow is straight line down
    # Black is a colon.
    if nowires == 3:
      threewires()
    if nowires == 4:
      fourwires()
    if nowires == 5:
      fivewires()
    

def threewires():
  global rope
  rope = raw_input("Which wire to cut?: ")
  global winner
  global wire1c
  global wire2c
  global wire3c
  global wire4c
  global wire5c
  global wire1
  global wire2
  global wire3
  global wire4
  global wire5
  liste = [wire1c, wire2c, wire3c, wire4c, wire5c]
  winner = 0
  redcount = 0
  for wireee in liste:
    if wireee == "\\":
      redcount +1
      if redcount >= 1:
        winner = 2
  lastwhite = 0
  bluewires = 0
  for blu in liste:
    if blu == "/":
      bluewires += 1
  iswire5there = False
  if wire5 > 0:
    iswire5there = True
  if iswire5there == True:
    if wire5 == 4:
      winner = 5
  elif iswire5there == False:
    if wire4 == 4:
      winner = 4
  if winner == 0:
    winner = 1
  ending()
def fourwires():
  global winner
  winner = 0
  redcount = 0
  for wireee in liste:
    if wireee == "\\":
      redcount +1
      if redcount >= 1:
        winner = 2
  iswire5there = False
  if wire5 > 0:
    iswire5there = True
  if iswire5there == True and wire5 == "|" and redcount == 0:
    winner = 1
  bluewires = 0
  for blu in liste:
    if blu == "/":
      bluewires += 1
  if bluewires == 1:
    winner = 2
  yellowwires = 0
  for yello in liste:
    if yello == "|":
      yellowwires += 1
  if iswire5there == True:
    if yellowwires >= 2:
      winner = 5
  if iswire5there == False:
    if yellowwires >= 2:
      winner = 4
  if winner == 0:
    winner = 1
  global rope
  rope = raw_input("Which wire to cut?: ")
  ending()
  
def fivewires():
  global winner
  winner = 0
  if wire5 == ":":
    winner = 4
  yellowwires = 0
  for yello in liste:
    if yello == "|":
      yellowwires += 1
  redcount = 0
  for wireee in liste:
    if wireee == "\\":
      redcount +1
      if redcount == 1 and yellowwires >= 2:
        winner = 4
  iswire5there = False
  if wire5 > 0:
    iswire5there = True
  blackwires = 0
  for blac in liste:
    if blac == ":":
      blackwires += 1
  if blackwires == 0:
    winner = 2
  if iswire5there == True:
    if wire5c == ":":
      winner = 4
  elif iswire5there == False:
    if wire4c == ":":
      winner = 4
  if winner == 0:
    winner = 1
  global rope
  rope = raw_input("Which wire to cut?: ")
  ending()
def ending():
  global winner
  global rope
  if int(rope) == winner:
    print("Bomb defused.")
    print(" ")
    print(" ")
    playagain = raw_input("Play Again?:")
    if playagain.lower() == "yes" or playagain.lower() == "y":
      print("Booting sequence up again.")
      time.sleep(1)
      wires()
    elif playagain.lower() == "no" or playagain.lower() == "n":
      print("Logging off..")
      time.sleep(1)
      print("Goodbye.")
  else:
    winstreak = 0
    print("Bomb has not been defused.")
    playagain = raw_input("Play Again?:")
    if playagain.lower() == "yes" or playagain.lower() == "y":
      print("Booting sequence up again.")
      time.sleep(1)
      wires()
    elif playagain.lower() == "no" or playagain.lower() == "n":
      print("Logging off..")
      time.sleep(1)
      print("Goodbye.")
      
start = raw_input("Type anything when you're ready to play. ")
if start != "4020200":
  wires()