#by Javi Mack
#created isa a basic backroooms adventure game that 
# allows you to pick a name 
# throw trait points for stats
# start at first floor
#have randomly generated chances of finding items, enemies, or escaping
import os
import random

run = True
menu = True
rules =False
play = False
key = False
fight = False
standing = True
canrun = True
story = True
jellytime = True 
boss1 = False

hp = 100
hpmax = 100
mus = 10
sma =0
dex = 0
luc = 10
x = 0
y = 0
points = 20
dialo = 0
whatwhat = "string"
HP = 0
HPMAX = 0
def statspawn():
    points = random.randint(1, 10)
    return points
    
def out():
    alert = random.randint(0, 1)
    return alert
def endlessmaze():

    dialo= random.randint(1, 5)
    whatwhat = "string"
    if dialo == 1:
        whatwhat = "Space\nEmpty Space"
    elif dialo == 2:
        whatwhat = "Space\nI feel lonely"
    elif dialo == 3:
        whatwhat = "Space\nThere is nothing here"
    elif dialo == 4:
        whatwhat = "Space\nI think I heard something"
    elif dialo == 5:
        whatwhat = "Space\nI miss tv"
    return whatwhat
def spawn():
    mapdeci = random.randint(1, 20)
    if mapdeci == 1:
            free = random.randint(1, 3)
            if free != 1:
                spawn()
            else:
                return spawn()
    elif mapdeci == 2:
        print("A monster has spawned")
        hp =- 2
    elif mapdeci == 3:
        pass
    elif mapdeci == 4:
        pass
    elif mapdeci == 5:
        pass
    elif mapdeci == 6:
        pass
    elif mapdeci == 7:
        pass
    elif mapdeci == 8:
        pass
    elif mapdeci == 9:
        pass
    elif mapdeci == 10:
        pass
    else:
        print("it is empty")
        input("> ")
def edgedia():
    dialo= random.randint(1, 5)
    whatwhat = "string"
    if dialo == 1:
        whatwhat = "Edge\nHit an edge"
    elif dialo == 2:
        whatwhat = "Edge\nIm at one of the corners"
    elif dialo == 3:
        whatwhat = "Edge\nEdgy"
    elif dialo == 4:
        whatwhat = "Edge\nI thought there would be a exit"
    elif dialo == 5:
        whatwhat = "Edge\nIm all alone!"
    return whatwhat
def walldia():
    dialo= random.randint(1, 3)
    whatwhat = "string"
    if dialo == 1:
        whatwhat = "Wall\nHit an wall"
    elif dialo == 2:
        whatwhat = "Wall\nMaybe if I just follow this wall"
    elif dialo == 3:
        whatwhat = "Wall\nCan't go further this way"
    return whatwhat
       #x = 0     x = 1    x = 2     x = 3    x = 4   x = 5
map = [["edge",  "wall",  "wall",  "wall",  "wall", "edge"],  # y = 0
       ["wall", "space", "space", "space", "space", "wall"],  # y = 1
       ["wall", "space", "space", "space",  "exit", "wall"],  # y = 2
       ["wall", "space", "space", "space", "space", "wall"],  # y = 3
       ["wall", "space", "space", "space", "space", "wall"],  # y = 4
       ["edge",  "wall",  "wall",  "wall",  "wall", "edge"]]  # y = 5

y_len = len(map)-1
x_len = len(map[0])-1
current_tile=map[y][x]
#print(current_tile)
biom = {
    "space": {
        "t": endlessmaze(),
        "e": True,
        "f": False},
    "wall": {
        "t": walldia(),
        "e": True,
        "f": False},
    "edge": {
        "t": edgedia(),
        "e": True,
        "f": False},
    "exit": {
        "t": "SPACE",
        "e": False,
        "f": True} #if biom[map[y][x]]["e"]:
}

e_list = ["Skull", "Orc", "Slime"]
boss1list = ["unknown"]
p_list = ["Almond Water", "Book", "Coffee", "Gun", "Knife"]

mobs = {
    "Skull": {
        "HP": 10,
        "Atk": 10,
        "Escape": 7,
        "Reward": 3},
    "Orc": {
        "HP": 8,
        "Atk": 5,
        "Escape": 4,
        "Reward": 2},
    "Slime": {
        "HP": 5,
        "Atk": 1,
        "Escape": 2,
        "Reward": 1},
    "unknown": {
        "HP": 100,
        "Atk": 50,
        "Escape": 10,
        "Reward": 20},
}
mobboss1 = {
    "unknown": {
        "HP": 100,
        "Atk": 50,
        "Escape": 10,
        "Reward": 20},
    },

current_tile=map[y][x]
#print(current_tile)
name_of_tile = biom[current_tile]["t"]
#print(name_of_tile)

def clear():
    os.system("cls")
    pass
def draw():
    print("xX--------------------------------Xx")

def save():
    list = [
        name,
        str(hp),
        str(mus),
        str(sma),
        str(dex),
        str(luc),
        str(x),
        str(y),
        str(key)
    ]

    f = open("loadbackrooms.txt", "w")

    for item in list:
        f.write(item+"\n")
    f.close()
def events(): #WAI TILL END OF TUT
    global fight, play, run, hp, mus, sma, dex, luc, hpmax
    jellytime = True
    while jellytime:
        if luc == 2:
            storytime = random.randint(1, 6)  
            if storytime == 1:
                print ("You found some Almond Water")
                hp += 2
                hpmax += 2
                jellytime = False
            elif storytime == 2:
                print ("You found a knife")
                mus += 1
                jellytime = False
            elif storytime == 3:
                print ("You found a comic")
                sma += 1
                jellytime = False
            elif storytime == 4:
                print ("You found abandoned shoes")
                dex += 1
                jellytime = False
            elif storytime == 5:
                jellytime = False
                battle()
            elif storytime == 6:
                print ("You found dice")
                luc += 2
        elif luc == 3:
          storytime = random.randint(1, 6) 
          if storytime == 1:
                print ("You found some Almond Water")
                hp += 2
                hpmax += 2
                jellytime = False
          elif storytime == 2:
                print ("You found a knife")
                mus += 1
                jellytime = False
          elif storytime == 3:
                print ("You found a comic")
                sma += 1
                jellytime = False
          elif storytime == 4:
                print ("You found abandoned shoes")
                dex += 1
                jellytime = False
          elif storytime == 5:
                jellytime = False
                battle()
          elif storytime == 6:
                print ("You found dice")
                luc += 2
        elif luc == 4:
            storytime = random.randint(1, 6)  
            if storytime == 1:
                print ("You found some Almond Water")
                hp += 3
                hpmax += 3
                jellytime = False
            elif storytime == 2:
                print ("You found a scythe")
                mus += 1
                jellytime = False
            elif storytime == 3:
                print ("You found a comic")
                sma += 1
                jellytime = False
            elif storytime == 4:
                print ("You found abandoned shoes")
                dex += 1
                jellytime = False
            elif storytime == 5:
                jellytime = False
                battle()
            elif storytime == 6:
                print ("You found dice")
                luc += 2
        elif luc == 5:
            storytime = random.randint(1, 6)  
            if storytime == 1:
                print ("You found some Almond Water")
                hp += 4
                hpmax += 4
                jellytime = False
            elif storytime == 2:
                print ("You found a axe")
                mus += 2
                jellytime = False
            elif storytime == 3:
                print ("You found a comic")
                sma += 1
                jellytime = False
            elif storytime == 4:
                print ("You found abandoned shoes")
                dex += 2
                jellytime = False
            elif storytime == 5:
                jellytime = False
                battle()
            elif storytime == 6:
                print ("You found dice")
                luc += 2
        elif luc == 6: 
            storytime = random.randint(1, 5)
            if storytime == 1:
                print ("You found some Almond Water")
                hp += 4
                hpmax += 4
                jellytime = False
            elif storytime == 2:
                print ("You found a axe")
                mus += 3
                jellytime = False
            elif storytime == 3:
                print ("You found a manga")
                sma += 2
                jellytime = False
            elif storytime == 4:
                print ("You found shoes")
                dex += 3
                jellytime = False
        elif luc == 7:
            storytime = random.randint(1, 5)  
            if storytime == 1:
                print ("You found some Almond Water")
                hp += 4
                hpmax += 6
                jellytime = False
            elif storytime == 2:
                print ("You found a axe")
                mus += 4
                jellytime = False
            elif storytime == 3:
                print ("You found a manga")
                sma += 2
                jellytime = False
            elif storytime == 4:
                print ("You found shoes")
                dex += 4
                jellytime = False
        elif luc == 8:
            storytime = random.randint(1, 5)  
            if storytime == 1:
                print ("You found some Almond Water")
                hp += 6
                hpmax += 6
                jellytime = False
            elif storytime == 2:
                print ("You found a spear")
                mus += 6
                jellytime = False
            elif storytime == 3:
                print ("You found a light novel")
                sma += 3
                jellytime = False
            elif storytime == 4:
                print ("You found new shoes")
                dex += 6
                jellytime = False
        elif luc == 9:
            storytime = random.randint(1, 5)  
            if storytime == 1:
                print ("You found some Almond Water")
                hp += 8
                hpmax += 8
                jellytime = False
            elif storytime == 2:
                print ("You found a sword")
                mus += 8
                jellytime = False
            elif storytime == 3:
                print ("You found a sci fi book")
                sma += 4
                jellytime = False
            elif storytime == 4:
                print ("You found brand new shoes")
                dex += 8
                jellytime = False
        elif luc == 10:
            storytime = random.randint(1, 5)  
            if storytime == 1:
                print ("You found some Almond Water")
                hp += 10
                hpmax += 10
                jellytime = False
            elif storytime == 2:
                print ("You found a Gun")
                mus += 10
                jellytime = False
            elif storytime == 3:
                print ("You found a dictionary")
                sma += 5
                jellytime = False
            elif storytime == 4:
                print ("You found brand new sneakers")
                dex += 10
                jellytime = False
        else:
            jellytime = False
            
def heal():
    global hp, hpmax
    
    if hpmax <= hp:
        hp = hpmax
    else:
        hp += 1
def enemychoice():
    war = random.randint(1, 100)  
    if war is (1, 30):
        war = "Slime"
        return war
    elif war is (31, 70):
        war = "Orc"
        return war
    elif war is (71, 94):
        war = "Skull"
        return war
    elif war is (95, 100):
        war is "unknown"
        return war
def bossbattle1():
    global fight, play, run, hp, mus
    enemy = random.choice(boss1list)
    HP = mobboss1[enemy]["HP"]
    escape = mobboss1[enemy]["Escape"]
    HPMAX = HP
    Atk = mobboss1[enemy]["Atk"]
    prize = mobboss1[enemy]["Reward"]
    alert = out()

    while fight:
        canrun = True
        clear()
        draw()
        print("Run or fight the " + enemy + "!" )
        draw()
        print(enemy + "' HP: " +str(HP) + "/" + str(HPMAX))
        print(name + "'s HP: " +str(hp) + "/" +str(hpmax))
        draw()
        print("1 - ATTACK")
        if dex >= escape and canrun == True:
            print("2 - ATTEMPT TO RUN")
            
            
        draw()

        choice = input("> ")
        if choice =="1":
            HP -= mus
            print(name + " dealt " + str(mus) + " damage to the " + enemy + ".")
            if hp>0:
                hp -= Atk
                print(enemy + " dealt " + str(Atk) + " damage to you.")
            input("> ")
        elif choice == "2":
            alert = out()
            if alert == 1:
                clear()
                print("you escaped")
                fight = False
                
            else:
                print("Failed to escape")
                hp -= Atk
                print(enemy + " dealt " + str(Atk) + " damage to you.")
                canrun = False
        if hp <= 0:
            print(enemy + " has killed " + name + "\n" + name + " could not survive the backrooms...")
            draw()
            fight = False
            play = False
            run = False
            print("GAME OVER")
            input("> ")
            quit()
        if HP <= 0:
            clear()
            print("You have beat the " + enemy)
            print("You feel stronger")
            draw()
            fight = False
            mus += prize

def battle():
    global fight, play, run, hp, mus
    enemy = random.choice(e_list)
    HP = mobs[enemy]["HP"]
    escape = mobs[enemy]["Escape"]
    HPMAX = HP
    Atk = mobs[enemy]["Atk"]
    prize = mobs[enemy]["Reward"]
    alert = out()

    while fight:
        canrun = True
        clear()
        draw()
        print("Run or fight the " + enemy + "!" )
        draw()
        print(enemy + "' HP: " +str(HP) + "/" + str(HPMAX))
        print(name + "'s HP: " +str(hp) + "/" +str(hpmax))
        draw()
        print("1 - ATTACK")
        if dex >= escape and canrun == True:
            print("2 - ATTEMPT TO RUN")
            
            
        draw()

        choice = input("> ")
        if choice =="1":
            HP -= mus
            print(name + " dealt " + str(mus) + " damage to the " + enemy + ".")
            if hp>0:
                hp -= Atk
                print(enemy + " dealt " + str(Atk) + " damage to you.")
            input("> ")
        elif choice == "2":
            alert = out()
            if alert == 1:
                clear()
                print("you escaped")
                fight = False
                
            else:
                print("Failed to escape")
                hp -= Atk
                print(enemy + " dealt " + str(Atk) + " damage to you.")
                canrun = False
        if hp <= 0:
            print(enemy + " has killed " + name + "\n" + name + " could not survive the backrooms...")
            draw()
            fight = False
            play = False
            run = False
            print("GAME OVER")
            input("> ")
            quit()
        if HP <= 0:
            clear()
            print("You have beat the " + enemy)
            print("You feel stronger")
            draw()
            fight = False
            mus += prize




while run:
    while menu:
        clear()
        
        draw()
        print("1. NEWGAME")
        print("2. LOAD GAME")
        print("3. RULES")
        print("4. QUIT GAME")
        draw()
        if rules:
            print("In order to havea chance at survival here are some rules\n1. At any point you decide to come back to the menu enter 0")
            rules = False
            choice = ""
            
        else: 
           choice = input("# ")

        

        if choice == "1":
            clear()
            mus = statspawn()
            sma = statspawn()
            dex = statspawn()
            luc = 10
            x = random.randint(0, 5)
            y = random.randint(0, 5)
            clear()
            name = input("What would you like to be called? : ")
            clear()
            menu = False
            play = True
            pass
        elif choice == "2":
            try:

                f = open("loadbackrooms.txt", "r")
                load_list = f.readlines()
                if len(load_list) == 9:
                    name = load_list[0]
                    hp = int(load_list[1][:-1])
                    mus = int(load_list[2][:-1])
                    sma = int(load_list[3][:-1])
                    dex = int(load_list[4][:-1])
                    luc = int(load_list[5][:-1])
                    x = int(load_list[6][:-1])
                    y = int(load_list[7][:-1])
                    key = bool(load_list[8][:-1])
                    clear()
                    print (f"Welcome back {name}")
                    print(hp, mus, sma, dex, luc)
                    print(current_tile)
                    input("> ")
                    menu = False
                    play = True
                else:
                    print("Corrupt save file")
                    input("> ")
            except OSError:
                print("No save file found")
                input("> ")

        elif choice == "3":
                rules = True
        elif choice == "4":
                quit()
    while play:
        canrun = True
        save()
        clear()
        if not standing:
            if biom[map[y][x]]["e"]:
                event = random.randint(1,5) #1,5
                if event > 4:
                    event = random.randint(1,2)
                    if event > 1:
                        fight = True
                        battle()
                    else:
                        #story = True
                        events()
                        
                else: 
                    endlessmaze()
                    edgedia()
                    walldia()
            elif biom[map[y][x]]["f"]:
                level2 = random.randint(2,2)
                if level2 == 1:
                    save()
                    play = False
                    run = False
                    print("You escaped to level 2")
                    input("> ")
                    quit()
                if level2 ==2:
                    boss1 = True
                    bossbattle1()

        draw()
        print("LOCATION: " +biom[map[y][x]]["t"])
        draw()
        print("NAME: " +name)
        print("HP: "+ str(hp)+ "/" + str(hpmax))
        print("Str: "+ str(mus))
        print("IQ: "+ str(sma))
        print("Speed: "+ str(dex))
        print("Luck: "+ str(luc))
        print("COORD:", x,y)
        current_tile=map[y][x]
        name_of_tile = biom[current_tile]["t"]
        print(current_tile)
        draw()
        print("0 - SAVE AND QUIT")
        if y > 0:
            print("1 - Up")
        if x < x_len:
            print("2 - Right")
        if x > 0:
            print("3 - Left")
        if y < y_len:
            print("4 - Down")
        draw()
        dest = input("> ")
        if dest == "0":
            play = False
            menu = True
            save()
        elif dest ==  "1":
            if y > 0:
                y -= 1
                standing = False
                heal()
            else:
                y = 0
                print("Can't go that way")
                dest = input("> ")
        elif dest ==  "2":
            if x < 5:
                x += 1
                standing = False
                heal()
            else:
                x = 5
                print("Can't go that way")
                dest = input("> ")
        elif dest ==  "3":
            if x > 0:
                x -= 1  
                standing = False
                heal()
            else:
                x = 0
                print("Can't go that way")
                dest = input("> ")
                
        elif dest ==  "4":
            if y < 5:
                y += 1  
                standing = False
                heal()
            else:
                print("Can't go that way")
                y = 5
                dest = input("> ")