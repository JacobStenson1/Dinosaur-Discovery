import time, sys, random, os
import msvcrt as m
clear = lambda:os.system("cls")


#Opened: 35

#Options file is text_file_e .
#Data/D_Name file is text_file_n .
#name = NAME OF DINOSAUR.


#CREATE FUNCTIONS FOR DIFFERENT GAMES, FOR DIFFERENT DINOS.

GameName = "Dinosaur Discovery"

newpath = r'Data' 
if not os.path.exists(newpath):
    os.makedirs(newpath)

newpath = r'Data/Saves' 
if not os.path.exists(newpath):
    os.makedirs(newpath)

if not os.path.exists('Data/Saves/ChosenDino.txt'):
    text_file_Dino = open("Data/Saves/ChosenDino.txt", "w")

if not os.path.exists('Data/What is to come.txt'):
    text_file_tc = open("Data/What is to come.txt", "a")

#---------------------------------------

yes         = ["Yes","yes","YES","Yes!","yes!","YES!","y","Y"]
no          = ["no","No","NO","no!","No!","NO!"]

flee        = ["flee","Flee","FLEE","f","F","Flee!","FLEE!","flee!","run","Run","RUN", "RUN THE FUCK AWAY"]
fight       = ["fight","FIGHT","Fight","fight!","FIGHT!","Fight!"]

menuStart   = ["Start","start","1","START","s","S"]
menuOptions = ["Options","option","Option","options","Three","2"]
menuCredits = ["Credits","credits","CREDITS","c","C","3"]
menuInfo    = ["Options Data","Options data","options Data","options data","OPTIONS DATA","data options","4","Data for options"]
menuToCome  = ["To come in future patches","5","TO COME", "to come", "To come"]
menuAdmin   = ["Admin", "Admin Commands","ADMIN COMMANDS","admin commands","6","aDMIN cOMMANDS","ADMIN", "admin"]
menuhelp    = ["Help","help","HELP","7","Help!","help!","HELP!","help me"]
menuQuit    = ["Quit","quit","QUIT","8","q","Q","Quit!","quit!","QUIT!"]

counter = 0

CrtPassword         = ["Admin","123", "fuck admins"]

startload           = ["Load","1","load","LOAD","l","L"]
startnew            = ["New","2","new","NEW","New game","NEW GAME", "new game", "n", "N"]

dietc               = ["c","C","CARNIVORE","Carnivore","carnivore"]
dieth               = ["h","H","HERBIVORE","Herbivore","herbivore"]

classRaptor         = ["Raptor","r","R","RAPTOR","raptor","1"]
classTyrannosaur    = ["Carnosaur","carnosaur","c","C","CARNOSAUR","2"]
classCroc           = ["Crocodile","crocodile",   "CROCODILE", "Croc", "croc"]

Brachio             = ["Brachio","Brachiosaurus","BRACHIOSAURUS","brachiosaurus","b","B"]

whichraptorV        = ["1","V","v","VELOCIRAPTOR","velociraptor","Velociraptor"]
whichraptorU        = ["2","U","u","UTAHRAPTOR","utahraptor","Utahraptor"]
whichcarnoC         = ["Carnotaur","carnotaur","c","C","CARNOTAUR","1"]
whichcarnoA         = ["Allosaurus","A","a","ALLOSAURUS", "allosaurus","2"]
whichcarnoTR        = ["Tyrannosaurus Rex","TR","tr","tyrannosarus rex", "TYRANNOSAURUS REX","3"]

WhichHerbivoreTypeS = ["Sauropod","Sauropods","S","s","SAUROPOD","SAURPODS","sauropds","sauropod","Sauro"]
WhichHerbivoreTypeD = [] #Duckbilled
WhichHerbivoreTypeC = [] #Ceratopsian
WhichHerbivoreTypeSt= ["Stegosaurus", "S", "stegosaurus", "STEGOSAURUS", "s", "Stego", "STEGO", "stego","st","ST","St"]

BattleEnd = False
placeholder = "nothing"
Total_Block = 0

SetPrevious = "Tree"
newnameyorn = "wow"

NormMove = True
EnemyD = True

Player_Level = 1

goes = 1
BlkGo = 0
SvGo = 0
AtckGo = 0

continuesaving1 = "y"

# Items on the map and what they correspond to...

Player      = "!"
Dirt        = "."
Rock        = "*"
Enemy       = "x"
Tree        = "+"
FallenTree  = "¬"
EdgeTree    = "="
DeadEnemy   = "~"
##

ArrayGame = [[Dirt]*15 for i in range(15)]

PlayerColumn = 0
PlayerRow = 0

rangeforlen = (len(ArrayGame))
x=0
y=1

isright = "no"

RowMax = len(ArrayGame)
RowMax = RowMax - 1

ColumnMax = len(ArrayGame[0])
ColumnMax = ColumnMax - 1

#print(ColumnMax)

ColumnMin = 0
RowMin = 0

MoveEYorN = 0

Total_Block_User = 0
Total_Attack_User = 0
Total_Attack_AI = 0
Total_Block_AI = 0

Score=0

EnemyR = 5
EnemyC = 5
ArrayGame[EnemyR][EnemyC] = Enemy

"""DINOSAUR VALUES"""
#   0         1           2          3      
#[Attack],[Health],[FoodConsuming],[Diet/Class],[],[]

##Dino =[
##    [1500,190,25,"C"],       #0- Velociraptor 
##    [65,200,35,"C"],        #1- Utahraptor 
##    [80,300,30,"C"],        #2- Carnosaurus
##    [85,450,30,"C"],        #3- Allosaurus
##    [100,350,35,"C"],       #4- T-Rex
##    [100,750,175,"H"],      #5- Brachiosaurus
##    [75,700,100,"H"],       #6- Stegosaurus
##    [70,550,115,"H"],       #7- Pachycephalosaurus
##    [90,375,40,"C"],        #8- Spinosaurus
##    [125,600,45,"C"],       #9- Indominous Rex [Do I really want this? Could be OP?]
##    [60,600,100,"H"],       #10- Triceratops
##    [80,650,100,"H"],       #11- Parasorolophus
##]


#   0         1           2            3      
#Attack     Health  FoodConsuming   Diet/Class

Dino_Stats = {
    "Velociraptor":         [800,190,25,"C"],
    "Utahraptor":           [65,200,35,"C"],
    "Carnosaurus":          [80,300,30,"C"],
    "Allosaurus":           [90,450,30,"C"],
    "T-Rex":                [100,350,35,"C"],
    "Brachiosaurus":        [90,750,175,"H"],
    "Stegosaurus":          [75,700,100,"H"],
    "Pachycephalosaurus":   [70,550,115,"H"],
    "Spinosaurus":          [100,375,40,"C"],
    "Indominous Rex":       [125,700,45,"C"], #OP? Do I want this? Could be OP?
    "Triceratops":          [60,600,100,"H"],
    "Parasorolophus":       [75,550,100,"H"],
}


"""Below is in a text file""" """Move it to a text file"""

BreedingRateC = 1
BreedingRateH = 5
MaxHerd = 10
FoodAtSlowingStart = 250
DamageH = 25
DamageC = 75
FoodConsumingRateH = 25
FoodConsumingRateC = 20
HealthC = 300
HealthH = 500
AlphaStatBoost = 1.25
BuffedAttack = 1.5
DeBuffedAttack = 0.75

"""Options in the text file are sorted into lines so more easily accessible with line code."""


text_file_e = open("Data/Options.txt", "a")
text_file_n = open("Data/Saves/D_Name.txt", "a")
text_file_Dino = open("Data/Saves/ChosenDino.txt", "a")
#text_file_n.write(".")

def EndGame(): #Ends the game if this is put somewhere in the game looping while loop.
    global x
    x=53

def linespace():
    print("")
def Linespace():
    print("")
def lineespace():
    print("...")
def ToCome():
    print("This feature has yet to be implimented. Please check the 'To Come section' to see if it is a feature that will appear in future patches.")
def InvalidInput():
    print("Invalid input. Please run the program again and enter a valid input.")

EnemyR = 5
EnemyC = 5

def Load():
    global dino, Health, FoodConsumingRate, DinoType, newnameyorn, Score
    Loaded = True
    if not os.path.exists('Data/Saves/Save1.txt'):
        print("You do not have a Save1. Therefore I cannot load a save from this.")
        pass
    else:
        loadsave1 = input("I see you have a save1 file. Would you like to me load from here? ")
        if loadsave1 in yes:
            save1 = open('Data/Saves/Save1.txt', "r")
##            dino = save1.readline(1)
##            Health = save1.readline(2)
##            FoodConsumingRate = save1.readline(3)
##            DinoType = save1.readline(4)

            fp = open("Data/Saves/Save1.txt")
            for i, line in enumerate(fp):
                if i == 0:
                    dino = save1.readline().rstrip("\n")
                elif i == 1:
                    Health = save1.readline().rstrip("\n")
                elif i == 2:
                    FoodConsumingRate = save1.readline().rstrip("\n")
                elif i == 3:
                    DinoType = save1.readline().rstrip("\n")
                elif i == 4:
                    Score = save1.readline().rstrip("\n")
                elif i > 29:
                    break
            fp.close()

            newnameyorn = "no"
            Score = int(Score)
            
            print("Save1 loaded. Press any key to continue.")
            p=ord(m.getch())
        if loadsave1 == "n":
            print("Alright. Games gonna break here. Press any key to continue.")
            print("game breaks because you are goign to try and continue without having any values for dino etc")
            b=ord(m.getch())        
        
        
def Save():
    global continuesaving1, Score
    continuesaving1 = "y"
    while continuesaving1 != "n":
        if not os.path.exists('Data/Saves/Save1.txt'):
            print("I see you do not have a Save1.")
            time.sleep(0.25)
            text_file_save1 = open("Data/Saves/Save1.txt", "w")
            print("Save1 Created.")
            text_file_save1.write(dino+"\n")
            text_file_save1.write(str(Health)+"\n")
            text_file_save1.write(str(FoodConsumingRate)+"\n")
            text_file_save1.write(DinoType+"\n")
            text_file_save1.write(str(Score)+"\n")
            print("Progress saved. Press any key to continue.")
            continuesaving1 = "n"
            b=ord(m.getch())
        else:
            print("I have detected that you already have a 'Save1' in your Saves folder. Do you want to overwrite this?")
            continuelol = input("(y or n)? ")
            if continuelol == "y":
                os.remove("Data/Saves/Save1.txt")
            else:
                continuesaving1 == "n"

def LoadTrees():
    global ArrayGame, Tree, EdgeTree
    ArrayGame[10][10]                   = Tree
    ArrayGame[10][11]                   = Tree
    ArrayGame[10][12]                   = Tree
    ArrayGame[10][13]                   = Tree
    ArrayGame[10][14]                   = EdgeTree
    ArrayGame[11][10]                   = Tree
    ArrayGame[11][11]                   = Tree
    ArrayGame[11][12]                   = Tree
    ArrayGame[11][13]                   = Tree
    ArrayGame[11][14]                   = EdgeTree

def CoOrdsForItems(): #Setting out the board. Placing each block of things (rocks).
    global Rock, Dirt, Player, EnemyC, EnemyR, EnemyD
    ArrayGame[2][0]                     = Rock
    ArrayGame[2][1]                     = Rock
    ArrayGame[PlayerRow][PlayerColumn]  = Player
    if EnemyD == False:
        if BattleEnd == True:
            ArrayGame[EnemyR][EnemyC]   = DeadEnemy
            
        ArrayGame[EnemyR][EnemyC]       = Enemy
        ArrayGame[4][4]                 = Enemy
    LoadTrees()

def TempCoordsItemsinMap():
    global Rock, Dirt, Player, EnemyC, EnemyR
    if OppHlth != 0:
        ArrayGame[EnemyR][EnemyC]       = Enemy
    else:
        pass
    LoadTrees()
    

def MovingEnemies(): #Moving the enemies on the board. (enemies)
    global EnemyC, EnemyR, ArrayGame, Enemy, Dirt, Player, PlayerRow, PlayerColumn, MoveEYorN
    MoveEYorN = 0
    if BattleEnd != True:
        if PlayerRow > EnemyR:
            ArrayGame[EnemyR][EnemyC] = Dirt
            EnemyR = EnemyR + 1
            ArrayGame[EnemyR][EnemyC] = Enemy
        elif PlayerRow < EnemyR:
            ArrayGame[EnemyR][EnemyC] = Dirt
            EnemyR = EnemyR - 1
            ArrayGame[EnemyR][EnemyC] = Enemy
        elif PlayerColumn > EnemyC:
            ArrayGame[EnemyR][EnemyC] = Dirt
            EnemyC = EnemyC + 1
            ArrayGame[EnemyR][EnemyC] = Enemy
        elif PlayerColumn < EnemyC:
            ArrayGame[EnemyR][EnemyC] = Dirt
            EnemyC = EnemyC - 1
            ArrayGame[EnemyR][EnemyC] = Enemy
        else:
            pass
    else:
        pass
    
def RemoveEnemyFromMap():
    global EnemyR, EnemyC, ArrayGame, Dirt
    ArrayGame[EnemyR][EnemyC] = Dirt

def CheckIfPlayerOnEnemy():
    global ArrayGame, PlayerRow, PlayerColumn, Enemy
    if ArrayGame[PlayerRow][PlayerColumn] == Enemy:
        Battle()

def CheckBelow0HP():
    global OppHlth, Health
    if OppHlth < 0:
        OppHlth = 0
    else:
        pass
    
    if Health < 0:
        Health = 0
    else:
        pass

def MeetingWithEnemy():
    EnemyGreet = random.randint(0,3)
    
    EnemyGreeting = {
    0:["You appear to have crossed paths with an enemy!"],
    1:["Wait! An enemy is nearby!"],
    2:["Stop! You may be in danger, there is an enemy nearby!"],
    3:["Uh oh. You've crossed paths with an enemy!"],

    }
    print(EnemyGreeting[EnemyGreet][0])
    
    
def MenuStart():                                    #user chooses their dinosaur for the game.
    global menuStart, mainmenuchoice, dino, FoodConsumingRate, Health
    lorn = input("Load game or new game? ")
    linespace()
    if lorn in startload:
        Load()                                      #load game here
    elif lorn in startnew:
        print("Welcome!")
        print("Please choose your main diet Dinosaur...")
        linespace()
        diet = input("Carnivore or Herbivore? ")
        if diet in dietc:
            print("You have chosen CARNIVORE!")
            linespace()
            print("Please choose your class...")
            print("Raptor, Carnosaur, Crocodiles.")
            linespace()
            classc = input("Please choose your dinosaur class... ")
            if classc in classRaptor:
                linespace()
                print("You have chosen the Raptor class.")
                print("You now have a choice of raptors.")
                print("Choose your Raptor:")
                lineespace()
                print("""- Utahraptor
- Velociraptor""")
                whichraptor = input("- ")
                if whichraptor in whichraptorV: #####Velociraptor ----
                    dino = "VRaptor"
                    Health = 150
                    FoodConsumingRate = 25 #per input
                    DinoType= "C"
                    
                if whichraptor in whichraptorU: #####Utahraptor ----
                    dino = "URaptor"
                    Health = 200
                    FoodConsumingRate = 20 #per input
                    DinoType= "C"                   
                else:
                    linespace()
            elif classc in classTyrannosaur:
                print("You have chosen the Carnosaur class.")
                print("You now have a choice of Carnosaurs")
                print("Please choose your Carnosaur:")
                lineespace()
                print("""- Carnotaurus
- Allosaurus
- Tyrannosaurus Rex
""")
                whichcarno = input("- ")
                if whichcarno in whichcarnoC:#####Carnotaurus ----
                    dino = "Carno"
                    DinoType = "C"
                elif whichcarno in whichcarnoA: #####Allosaurus ----
                    dino = "Allo"
                    DinoType = "C"
                elif whichcarno in whichcarnoTR: #####T-Rex ----
                    dino = "TRex"
                    DinoType = "C"
                else:
                    InvalidInput()
            elif classc in classCroc:
                print("You have chosen the Croc class.") ### Make sure when you add these to add them to opponent type so player can vs them in a battle.
                ToCome()
            else:
                linespace()
        elif diet in dieth:
            print("You have chosen HERBIVORE")
            linespace()
            print("Choose your class of Herbivore.")
            print("""- Sauropods
- Duckbilled
- Ceratopsians
- Stegosaurs
---(S, D, C, St)---""")
            WhichHerbivoreType = input("- ")
            if WhichHerbivoreType in WhichHerbivoreTypeS:
                print("Please choose your dinosaur.")
                print("""
Brachiosaurus
""")
                whichsauro = input("Which Sauropod would you like to use? ")
                if whichsauro in Brachio:       #####Brachio --------
                    dino = "Brachio"
                    DinoType = "H"
                    linespace()
            elif WhichHerbivoreType in WhichHerbivoreTypeD:
                #Duckbilled
                DinoType = "H"
                linespace()
            elif WhichHerbivoreType in WhichHerbivoreTypeC:
                #Ceratopsians
                DinoType = "H"
                linespace()
            elif WhichHerbivoreType in WhichHerbivoreTypeSt: #####Stegosaurus ----
                dino = "Stego"
                DinoType = "H"
                linespace()
            else:
                InvalidInput()

def MenuHelp():
    print("Help section of the menu...")
    print("Being created...")
    input("Press enter to go back to the main menu...")
    #read the text file for this. and print it to the screen. HELP needs to be made.

def DinoSave():
    text_file_Dino.write("%s" %dino)

def MenuOptions():
    global mainmenuchoice, menuOptions, text_file_e, linespace, editoptions
    text_file_e = open("Data/Options.txt", "r")
    print("Changing options now currently (as of patch 1.0) does not affect gameplay.")
    print("Opening Options file, and relaying to the screen...")
    time.sleep(1)
    linespace()
    print(text_file_e.read())                         #print the options here from a text file.
    linespace()
    linespace()
    editoptions = input("Would you like to edit the options('y' or 'n'? ")
    if editoptions == "y":
        editoptionsline = int(input("The value which you wish to edit, what line is it on? "))
        text_file_e = open("Data/Options.txt","r")
        text_file_e = open("Data/Options.txt","a")
        editoptions = input("What would you like to change this value to? ")
        text_file_e.write("%s" %editoptions)
        text_file_e.close()
    else:
        Linespace()

def MenuCredits():
    global mainmenuchoice, menuCredits
    time.sleep(1)
    linespace()
    print("© JacobStenson, JS. JAVER Soluions LTD.")
    print("All rights go to Jacob Stenson, the owner and creator of this game.")
    print("DINOSAURS V1.1 2017.")
    print("GAME INCOMPLETE.")

def MenuInfo():
    global mainmenuchoice, menuInfo, linespace
    #all this does is it reads the options file and prints the content to the screen.
    print("Information...")
    print("You can find out all of the information about the game here...")
    linespace()

    text_file_e = open("Data/Options.txt", "r")
    print(text_file_e.read())

    #
    """print("     Carnivores:")
    print("CARNOSAURS:")
    print("- Damage: 75 ")
    print("- Food Consumption Rate: 30")
    print("- Health: 300")
    print("- Breeding rate: 001")"""
    #
    
def MenuToCome():
    global mainmenuchoice, menToCome
    #reads the to come file and prints the content to the screen.
    print("EVERYTHING TO COME IN FUTURE PATCHES:...")
    time.sleep(1)
    lineespace()
    linespace()
    text_file_tc = open("Data/What is to come.txt", "r")
    print(text_file_tc.read())

def MenuAdminCommands():
    global password, CrtPassword
    print("Admin commands terminal")
    password = input("Please enter the password... ")
    if password in CrtPassword:
        print("Working...")
        time.sleep(0.5)
        clear()
        print("Correct password entered.")
        time.sleep(0.5)
        print("Use any of the following commands to do shit.")
        linespace()
        print("Use 1, 2, 3... respectively.")
        print("""1. Change the "to come section of the program".
""")
        AdmnCmdChc = input("- ")
        if AdmnCmdChc == "1":
            clear()
            text_file_tocome=open("What is to come....txt", "r")
            print(text_file_tocome.read()) 
            print("Changing 'to come'")
            print("What do you want to add? ")
            linespace()
            AddToCome = input("")
            text_file_tocome=open("What is to come....txt", "a")
            text_file_tocome.write('\n'+AddToCome+'\n')
            text_file_tocome=open("What is to come....txt", "r")
            print(text_file_tocome.read())            
    else:
        print("Wrong password, gtfo bitch.")

def MenuQuit():
    global mainmenuchoice, menuQuit, InvalidInput
    print("Quitting",GameName,".")
    time.sleep(1)
    sys.exit()

##def TestingForF5():
##    print("Press any key to start the game.")
##    b=ord(m.getch())
##    clear()
##    if b == 255:
##        print("Error. Wrong button press, do not use the F5")
##        x=input("Press enter to exit. Just double click the game file and dont use F5- ")
##        sys.exit()

def MovePlayerRight():                      #Moves user's icon to the right
    global PlayerColumn, PlayerRow, Player, Dirt, ColumnMin, ColumnMax, RowMin, RowMax, ArrayGame, Rock, Score, x, Enemy, Size, SetPrevious, Tree, FallenTree, NormMove
    if ArrayGame[PlayerRow][PlayerColumn] == ArrayGame[10][14] or ArrayGame[PlayerRow][PlayerColumn] == ArrayGame[10][14]: #EdgeTree: #if the player is on the edge then they cant move off. run the code below and skip the movement.
        pass
    elif ArrayGame[PlayerRow][PlayerColumn] == Tree: # ArrayGame[10][10] or ArrayGame[PlayerRow][PlayerColumn] == ArrayGame[10][11] or ArrayGame[PlayerRow][PlayerColumn] == ArrayGame[10][12] or ArrayGame[PlayerRow][PlayerColumn] == ArrayGame[10][13] or ArrayGame[PlayerRow][PlayerColumn] == ArrayGame[11][10] or ArrayGame[PlayerRow][PlayerColumn] == ArrayGame[11][11] or ArrayGame[PlayerRow][PlayerColumn] == ArrayGame[11][12] or ArrayGame[PlayerRow][PlayerColumn] == ArrayGame[11][13]:
        ArrayGame[PlayerRow][PlayerColumn] = Dirt           #Sets the current "Position" of the player to a blank Dirt.
        PlayerColumn = PlayerColumn + 1                     #Moves the player's Column value to one to the right.
        ArrayGame[PlayerRow][PlayerColumn] = Player         #Sets the player's pointer to the new values on the array
        Score=Score+1
        NormMove = False
    elif ArrayGame[PlayerRow][PlayerColumn] == Tree: #ArrayGame[10][10] or ArrayGame[PlayerRow][PlayerColumn] == ArrayGame[10][11] or ArrayGame[PlayerRow][PlayerColumn] == ArrayGame[10][12] or ArrayGame[PlayerRow][PlayerColumn] == ArrayGame[10][13] or ArrayGame[PlayerRow][PlayerColumn] == ArrayGame[11][10] or ArrayGame[PlayerRow][PlayerColumn] == ArrayGame[11][11] or ArrayGame[PlayerRow][PlayerColumn] == ArrayGame[11][12] or ArrayGame[PlayerRow][PlayerColumn] == ArrayGame[11][13]:
        ArrayGame[PlayerRow][PlayerColumn] = Dirt           #Sets the current "Position" of the player to a blank Dirt.
        PlayerColumn = PlayerColumn + 1                     #Moves the player's Column value to one to the right.
        ArrayGame[PlayerRow][PlayerColumn] = Player         #Sets the player's pointer to the new values on the array
        Score=Score+1
        NormMove = False
    elif PlayerColumn == ColumnMax:
        pass                                                #If edge of board then cant go right. Above this stops you.
    elif ArrayGame[PlayerRow][PlayerColumn+1] == Rock:      #Checks if youre moving into a rock. If so dont move.
        pass
    elif ArrayGame[PlayerRow][PlayerColumn+1] == Enemy:     #Checks if youre moving into an enemy. If so, still move and initiate a battle.
        ArrayGame[PlayerRow][PlayerColumn] = Dirt                               
        PlayerColumn = PlayerColumn + 1                                         
        ArrayGame[PlayerRow][PlayerColumn] = Player
        clear()
        MeetingWithEnemy()
        FightYorN = input("Fight or Flee? ")
        while FightYorN not in fight or FightYorN not in flee:
            Linespace()
            if FightYorN in fight:                             #Battle function called here and is run from here. making this long so it stands out.
                Battle()
                break
            elif FightYorN in flee:
                #no                                          #if user does not want to fight. puts them a block above the enemy.
                break
            else:
                print("Fight yes or no error.")
                FightYorN = input("Fight or Flee? ")
    else:
        if NormMove == True:
            ArrayGame[PlayerRow][PlayerColumn] = Dirt           #Sets the current "Position" of the player to a blank Dirt.
            PlayerColumn = PlayerColumn + 1                     #Moves the player's Column value to one to the right.
            ArrayGame[PlayerRow][PlayerColumn] = Player         #Sets the player's pointer to the new values on the array
            Score=Score+1

def MovePlayerLeft():                       #Moves user's icon to the left
    global PlayerColumn, PlayerRow, Dirt, Player, ColumnMin, ColumnMax, RowMin, RowMax, ArrayGame, Score, x, Enemy
    if ArrayGame[PlayerRow][PlayerColumn] == ArrayGame[RowMin][ColumnMin] or ArrayGame[PlayerRow][PlayerColumn] == ArrayGame[1][ColumnMin] or ArrayGame[PlayerRow][PlayerColumn] == ArrayGame[2][ColumnMin] or ArrayGame[PlayerRow][PlayerColumn] == ArrayGame[3][ColumnMin] or ArrayGame[PlayerRow][PlayerColumn] == ArrayGame[4][ColumnMin] or ArrayGame[PlayerRow][PlayerColumn] == ArrayGame[5][ColumnMin] or ArrayGame[PlayerRow][PlayerColumn] == ArrayGame[6][ColumnMin] or ArrayGame[PlayerRow][PlayerColumn] == ArrayGame[7][ColumnMin] or ArrayGame[PlayerRow][PlayerColumn] == ArrayGame[8][ColumnMin] or ArrayGame[PlayerRow][PlayerColumn] == ArrayGame[9][ColumnMin] or ArrayGame[PlayerRow][PlayerColumn] == ArrayGame[10][ColumnMin] or ArrayGame[PlayerRow][PlayerColumn] == ArrayGame[11][ColumnMin] or ArrayGame[PlayerRow][PlayerColumn] == ArrayGame[12][ColumnMin] or ArrayGame[PlayerRow][PlayerColumn] == ArrayGame[13][ColumnMin] or ArrayGame[PlayerRow][PlayerColumn] == ArrayGame[14][ColumnMin]:
        pass                                                 #Checks if youre on the edge of the map. if so dont allow movement.
    else:
        if ArrayGame[PlayerRow][PlayerColumn-1] == Rock:     #Checks if youre moving into a rock. If so dont move.
            pass
        elif ArrayGame[PlayerRow][PlayerColumn-1] == Enemy:      #Checks if youre moving into an enemy. If you are you still move and initiate a battle.
            ArrayGame[PlayerRow][PlayerColumn] = Dirt                               
            PlayerColumn = PlayerColumn - 1                                         
            ArrayGame[PlayerRow][PlayerColumn] = Player
            clear()
            MeetingWithEnemy()
            FightYorN = input("Fight or Flee? ")
            while FightYorN not in fight or FightYorN not in flee:
                Linespace()
                if FightYorN in fight:                             #Battle function called here and is run from here. making this long so it stands out.
                    Battle()
                    break
                elif FightYorN in flee:
                    #no                                          #if user does not want to fight. puts them a block above the enemy.
                    break
                else:
                    print("Fight yes or no error.")
                    FightYorN = input("Fight or Flee? ")
        else:
            ArrayGame[PlayerRow][PlayerColumn] = Dirt        #Sets the current "Position" of the player to a blank Dirt.
            PlayerColumn = PlayerColumn- 1                   #Moves the player's Column value to one to the left.
            ArrayGame[PlayerRow][PlayerColumn] = Player     #Sets the player's pointer to the new values on the array
            Score+=1

def MovePlayerDown():                       #Moves user's icon down
    global PlayerRow, Dirt, Player, ColumnMin, ColumnMax, RowMin, RowMax, ArrayGame, Score, x, PlayerColumn, Enemy
    if ArrayGame[PlayerRow][PlayerColumn] == ArrayGame[RowMax][ColumnMin] or ArrayGame[PlayerRow][PlayerColumn] == ArrayGame[RowMax][1] or ArrayGame[PlayerRow][PlayerColumn] == ArrayGame[RowMax][2] or ArrayGame[PlayerRow][PlayerColumn] == ArrayGame[RowMax][3] or ArrayGame[PlayerRow][PlayerColumn] == ArrayGame[RowMax][4] or ArrayGame[PlayerRow][PlayerColumn] == ArrayGame[RowMax][5] or ArrayGame[PlayerRow][PlayerColumn] == ArrayGame[RowMax][6] or ArrayGame[PlayerRow][PlayerColumn] == ArrayGame[RowMax][7] or ArrayGame[PlayerRow][PlayerColumn] == ArrayGame[RowMax][8] or ArrayGame[PlayerRow][PlayerColumn] == ArrayGame[RowMax][9] or ArrayGame[PlayerRow][PlayerColumn] == ArrayGame[RowMax][10] or ArrayGame[PlayerRow][PlayerColumn] == ArrayGame[RowMax][11] or ArrayGame[PlayerRow][PlayerColumn] == ArrayGame[RowMax][12] or ArrayGame[PlayerRow][PlayerColumn] == ArrayGame[RowMax][13] or ArrayGame[PlayerRow][PlayerColumn] == ArrayGame[RowMax][14]:
        pass
    else:
        if ArrayGame[PlayerRow+1][PlayerColumn] == Rock: #Checks if youre moving into a rock. If so dont move.
            pass
        elif ArrayGame[PlayerRow+1][PlayerColumn] == Enemy:      #Checks if youre moving into an enemy. If you are you still move and initiate a battle.                            
            ArrayGame[PlayerRow][PlayerColumn] = Dirt                               
            PlayerRow = PlayerRow + 1                                         
            ArrayGame[PlayerRow][PlayerColumn] = Player
            clear()
            MeetingWithEnemy()
            FightYorN = input("Fight or Flee? ")
            Linespace()
            if FightYorN in fight:                             #Battle function called here and is run from here. making this long so it stands out.
                Battle()
            elif FightYorN in flee:
                #no                                          #if user does not want to fight. puts them a block above the enemy.
                pass
            else:
                print("Fight yes or no error.")
        else:                                           #Moves if all other arguments arent true
            ArrayGame[PlayerRow][PlayerColumn] = Dirt
            PlayerRow = PlayerRow + 1
            ArrayGame[PlayerRow][PlayerColumn] = Player
            Score+=1

def MovePlayerUp():                         #Moves user's icon up
    global PlayerRow, Dirt, Player, ColumnMin, ColumnMax, RowMin, RowMax, ArrayGame, Score, x, PlayerColumn, Enemy
    if ArrayGame[PlayerRow][PlayerColumn] == ArrayGame[RowMin][ColumnMin] or ArrayGame[PlayerRow][PlayerColumn] == ArrayGame[RowMin][1] or ArrayGame[PlayerRow][PlayerColumn] == ArrayGame[RowMin][2] or ArrayGame[PlayerRow][PlayerColumn] == ArrayGame[RowMin][3] or ArrayGame[PlayerRow][PlayerColumn] == ArrayGame[RowMin][4] or ArrayGame[PlayerRow][PlayerColumn] == ArrayGame[RowMin][5] or ArrayGame[PlayerRow][PlayerColumn] == ArrayGame[RowMin][6] or ArrayGame[PlayerRow][PlayerColumn] == ArrayGame[RowMin][7] or ArrayGame[PlayerRow][PlayerColumn] == ArrayGame[RowMin][8] or ArrayGame[PlayerRow][PlayerColumn] == ArrayGame[RowMin][9]or ArrayGame[PlayerRow][PlayerColumn] == ArrayGame[RowMin][10]or ArrayGame[PlayerRow][PlayerColumn] == ArrayGame[RowMin][11]or ArrayGame[PlayerRow][PlayerColumn] == ArrayGame[RowMin][12]or ArrayGame[PlayerRow][PlayerColumn] == ArrayGame[RowMin][13]or ArrayGame[PlayerRow][PlayerColumn] == ArrayGame[RowMin][14]:
        pass
    else:
        if ArrayGame[PlayerRow-1][PlayerColumn] == Rock: #Checks if youre moving into a rock. If so dont move.
            pass
        elif ArrayGame[PlayerRow-1][PlayerColumn] == Enemy:      #Checks if youre moving into an enemy. If you are you still move and initiate a battle.
            ArrayGame[PlayerRow][PlayerColumn] = Dirt                               
            PlayerRow = PlayerRow - 1                                         
            ArrayGame[PlayerRow][PlayerColumn] = Player
            clear()
            MeetingWithEnemy()
            FightYorN = input("Fight or Flee? ")
            Linespace()
            if FightYorN in fight:                             #Battle function called here and is run from here. making this long so it stands out.
                Battle()
            elif FightYorN in flee:
                #no                                          #if user does not want to fight. puts them a block above the enemy.
                pass
            else:
                print("Fight yes or no error.")
        else:
            ArrayGame[PlayerRow][PlayerColumn] = Dirt
            PlayerRow = PlayerRow - 1
            ArrayGame[PlayerRow][PlayerColumn] = Player
            Score+=1

def OnlyRaptor():
    global dino
    #the only dinosaur in the game at the moment is the vraptor therefore if the player chooses another one the game will not work and the following code will be run.
    if dino != "VRaptor":
        print("""You cannot use this Dinosaur currently.
It is in production! Sorry for any inconvenience caused.
Please re-run the program and select the 'Velociraptor' class.
Thank you.""")
        print("wow",dino,"wow")
        print("Press any key to continue...")
        b = ord(m.getch())
        sys.exit()
    elif dino == "VRaptor":
        pass
    else:
        InvalidInput()

def ValuesForDinos():
    global dino, Dino, DinoType, OpponentType, Health, Attack, Size
    if dino == "VRaptor":
        Attack = Dino_Stats["Velociraptor"][0]
        Health = Dino_Stats["Velociraptor"][1]
        Size = "S"
        DinoType = "C"
    elif dino == "URaptor":
        Attack = Dino_Stats["Utahraptor"][0]
        Health = Dino_Stats["Utahraptor"][1]
        Size = "S"
        DinoType = "C"
    elif dino == "Carno":
        Attack = Dino_Stats["Carnosaur"][0]
        Health = Dino_Stats["Carnosaur"][1]
        Size = "M"
        DinoType = "C"
    elif dino == "Allo":
        Attack = Dino_Stats["Allosaurus"][0]
        Health = Dino_Stats["Allosaurus"][1]
        Size = "M"
        DinoType = "C"
    elif dino == "TRex":
        Attack = Dino_Stats["T-Rex"][0]
        Health = Dino_Stats["T-Rex"][1]
        Size = "H"
        DinoType = "C"
    elif dino == "Brachio":
        Attack = Dino_Stats["Brachiosaurus"][0]
        Health = Dino_Stats["Brachiosaurus"][1]
        Size = "L"
        DinoType = "H"
    elif dino == "Stego":
        Attack = Dino_Stats["Stegosaurus"][0]
        Health = Dino_Stats["Stegosaurus"][1]
        Size = "H"
        DinoType = "H"
    else:
        print("Dino Type defining error.")

def First_Battle_Opponent():
    global OpponentType, Opponent, First_Battle_Opponent, OppAtck, OppHlth
    First_Battle_Opponent = random.randint(0,6)
    if First_Battle_Opponent == 0:
        #Triceratops
        OpponentType = "H"
        Opponent = "a herd of Triceratops"
        OppAtck = Dino_Stats["Triceratops"][0]
        OppHlth = Dino_Stats["Triceratops"][1]
    elif First_Battle_Opponent == 1:
        #Stegosaurus
        OpponentType = "H"
        Opponent = "a herd of Stegosaurus"
        OppAtck = Dino_Stats["Stegosaurus"][0]
        OppHlth = Dino_Stats["Stegosaurus"][1]
    elif First_Battle_Opponent == 2:
        #Brachiosaurus
        OpponentType = "H"
        Opponent = "a herd of Brachiosaurus"
        OppAtck = Dino_Stats["Brachiosaurus"][0]
        OppHlth = Dino_Stats["Brachiosaurus"][1]
    elif First_Battle_Opponent == 3:
        #Parasorolophus
        OpponentType = "H"
        Opponent = "a herd of Parasorolophus"
        OppAtck = Dino_Stats["Stegosaurus"][0]
        OppHlth = Dino_Stats["Stegosaurus"][1]
    elif First_Battle_Opponent == 4:
        #T-Rex
        OpponentType = "C"
        Opponent = "a T-Rex"
        OppAtck = Dino_Stats["T-Rex"][0]
        OppHlth = Dino_Stats["T-Rex"][1]
    elif First_Battle_Opponent == 5:
        #Allo
        OpponentType = "C"
        Opponent = "an Allosaurus"
        OppAtck = Dino_Stats["Allosaurus"][0]
        OppHlth = Dino_Stats["Allosaurus"][1]
    elif First_Battle_Opponent == 6:
        #Carno
        OpponentType = "C"
        Opponent = "a Carnosaurus"
        OppAtck = Dino_Stats["Carnosaurus"][0]
        OppHlth = Dino_Stats["Carnosaurus"][1]
    elif First_Battle_Opponent == 7:
        #Utahraptor
        OpponentType = "C"
        OppAtck = Dino_Stats["Utahraptor"][0]
        OppHlth = Dino_Stats["Utahraptor"][0]
    elif First_Battle_Opponent == 8:
        #Pachy
        OpponentType = "H"
        OppAtck = Dino_Stats["Pachycephalosarus"][0]
        OppHlth = Dino_Stats["Pachycephalosarus"][1]
    elif First_Battle_Opponent == 9:
        #Spino
        OpponentType = "C"
        OppAtck = Dino_Stats["Spinosaurus"][0]
        OppHlth = Dino_Stats["Spinosaurus"][1]
    elif First_Battle_Opponent == 10:
        #Velociraptor
        OpponentType = "C"
        OppAtck = Dino_Stats["Velociraptor"][0]
        OppHlth = Dino_Stats["Velociraptor"][1]
    else:
        print("Error getting dino for first plain.")

"""
def TempWhileCreating():
    global Opponent
    Opponent = "Stego"

"""
def Battle():
    global dino, Opponent, Attack, OppAtck, OppHlth, BattleEnd, q, goes, SvGo, BlkGo, AtckGo, counter, Health, Total_Block_User, Total_Attack_User, BattleEnd, Rock, ArrayGame, Player, PlayerRow, PlayerColumn, EnemyD
    print(dino,"VS",Opponent,". FIGHT!")
    AtckGo = 0
    BlkGo = 0
    for x in range(3):
        time.sleep(0.5)
        print("Ding!")
    time.sleep(0.5)
    Linespace()
    if DinoType == "C" and OpponentType == "H":                 #reduces user's attack damage if against a stronger opponent type
        Attack = Attack * BuffedAttack                          #or
        OppAtck = OppAtck * DeBuffedAttack                      #reduce opponent's attack damage if against users' stronger type.
    elif DinoType == "H" and OpponentType == "C":
        Attack = Attack * DeBuffedAttack
        OppAtck = OppAtck * BuffedAttack
    elif DinoType == "A" and OpponentType == "C":
        Attack = Attack * BuffedAttack
        OppAtck = OppAtck * DeBuffedAttack
    elif DinoType == "C" and OpponentType == "A":
        Attack = Attack * DeBuffedAttack
        OppAtck = OppAtck * BuffedAttack
    elif DinoType == "P" and OpponentType == "H":
        Attack = Attack * DeBuffedAttack
        OppAtck = OppAtck * BuffedAttack
    elif DinoType == "H" and OpponentType == "P":
        Attack = Attack * BuffedAttack
        OppAtck = OppAtck * DeBuffedAttack
    elif DinoType == "P" and OpponentType == "A":
        Attack = Attack * BuffedAttack
        OppAtck = OppAtck * DeBuffedAttack
    elif DinoType == "A" and OpponentType == "P":
        Attack = Attack * DeBuffedAttack
        OppAtck = OppAtck * BuffedAttack
        
    print("Battle buffs working fine.")
    Attack = int(round(Attack, 0))
    print("Attack of user:",Attack)
    print("Health of user:",Health)
    print("Attack of opponent:",OppAtck)
    print("Health of opponent:",OppHlth)
    
    #q = random.randint(0,1)
    q=0 #this is so that ai doesnt start and you dont have to re-run program to get to player again.
    
    if q == 0:                                  #User goes first.
        AtckGo=0
        AI_Atck_Go=0
        BlkGo=0
        Go_No=1
        #Player goes first.
        clear() 
        print(name,"'s Stats... as",dino)
        print("Health:",Health)
        print("Attack",Attack)
        linespace()
        print(Opponent,"'s Stats...")
        print("Health:",OppHlth)
        print("Attack:",OppAtck)
        print("------------------------------------")
        print("""What would you like to do?
1. Attack...
2. Block...

Go number:""",Go_No)

        print(BlkGo)
        print(AtckGo)
        
        BattleChoice = int(input("Use (1 or 2) do not typo!- "))
        if BattleChoice == 1:
            AtckGo = AtckGo + 1
        elif BattleChoice == 2:
            BlkGo = BlkGo + 1
        else:
            print("You did something wrong. Restart the game or keep going but remember you will lose a go if you dont restart...")
        Go_No = Go_No + 1
        
        clear()
        print("Attacked:",AtckGo,"times.")
        print("Blocked:",BlkGo,"times.")   
        
        OppOldHlth = OppHlth
        OldHlth = Health
        DmgToEmy = Attack * AtckGo
        OppHlth = OppHlth - DmgToEmy        #Calculating how much dmg is done to characters.
        #DmgToPlayer = OppAtck * AI_Atck_Go #Users go so no damage can be done to them.
        #Health = Health - DmgToPlayer
        Total_Block_User = Total_Block_User + BlkGo
        linespace()
        linespace()
        
        CheckBelow0HP()
        
        print("You dealt",DmgToEmy,"damage to the enemy.")
        print("Their health has depleted from",OppOldHlth,"Health. To",OppHlth,"Health.")
        linespace()
        #print(Opponent,"has dealt",DmgToPlayer,"damage to you!")
        #print("Your health has depleted from",OldHlth,"health to",Health,"health.")
        #linespace()
        print("Press any key to continue.")
        u = ord(m.getch())
        time.sleep(0.01)
        
        if OppHlth <=0:                                 #If enemy health is 0 or below. end battle.
            clear() 
            print("Holy moly you ONE HIT",Opponent,". Nice work! Heading back to the map now...")
            Linespace()
            print("""BATTLE CONCLUSION:
You earned""",placeholder,"""experience for that kill""")
            PlayerRow = PlayerRow-1
            ArrayGame[PlayerRow][PlayerColumn] = Player
            ArrayGame[EnemyR][EnemyC]   = DeadEnemy
            BattleEnd = True
            linespace()
            print("Press any key to continue...")
            do = ord(m.getch())
            #RemoveEnemyFromMap()
            pass
        elif Health <=0:
            clear()
            print("""You have been beaten down to 0 health. The game will now exit.
If you would like to play again...
Please re-open the game.

Thank you for playing""",GameName,"!")
            print("Your ending stats were:",placeholder,".")    #put something here in the future. At the moment no value can go here so there is just a "placeholder" variable.
            sys.exit()            
    elif q == 1:
        pass #this is like this. if it is not like this, the sequence of events will not be correct. LEAVE THIS.
    else:
        print("Random battle, choosing who to go first has encountered error.")

                    #AI_Battle_go AI's go.
        
## After here the first go code has ended.-- ##
##                                           ##
##                                           ##
    if BattleEnd == True:
        #Game Ends
        do = ord(m.getch())
    else:
        AI_Battle_Go()
        while BattleEnd != True: #While loop that runs until a win or loss.
            User_Battle_Go()
            if BattleEnd != True:
                AI_Battle_Go()
            else:
                ArrayGame[EnemyC][EnemyR] = Dirt                   
                break
        ArrayGame[EnemyC][EnemyR] = Dirt
        EnemyD = True
        
def AI_Battle_Go():
    global dino, Opponent, Attack, OppAtck, OppHlth, BattleEnd, q, goes, SvGo, BlkGo, AtckGo, counter, Health, Total_Block_AI, Total_Attack_AI
    Total_Block = 0
    Total_Attack_AI = 0
    Total_Block_AI = 0
    for i in range(0,2):
        AI_Atck_Go=0
        AI_Blk_Go=0
        clear()
        print(Opponent,"'s go!")
        linespace()
        lineespace()
        print(name,"'s Stats... as",dino)
        print("Health:",Health)
        print("Attack",Attack)
        linespace()
        print(Opponent,"'s Stats...")
        print("Health:",OppHlth)
        print("Attack:",OppAtck)
        print("------------------------------------")
        Opponent_Go = random.randint(0,1)       #this next bit could be made smaller but idk how to make a for loop print text that changed (like I am trying to achience below)

        clear()
        print("Opponent is having their go.")
        time.sleep(0.8)
        clear()
        print("Opponent is having their go..")
        time.sleep(0.7)
        clear()
        print("Opponent is having their go...")
        time.sleep(0.4)

        if Opponent_Go == 0:
            AI_Atck_Go += 1
        elif Opponent_Go == 1:
            AI_Blk_Go += 1
        else:
            print("Something went wrong - bot choosing AI go")

        clear()
        #print("The",Opponent,"attacked",AI_Atck_Go,"times.")
        #print("The",Opponent,"blocked",AI_Blk_Go,"times.")

        Total_Block_AI = Total_Block_AI + AI_Blk_Go
        Total_Attack_AI = Total_Attack_AI + AI_Atck_Go

        AI_Atck_Go = AI_Atck_Go - Total_Block_User
        
        if AI_Atck_Go <0:                       #Makes sure the amount of goes is not a minus number (idk if this fcks shit up but dont want to try)
            AI_Atck_Go = 0
        else:
            pass

        OppOldHlth = OppHlth
        OldHlth = Health
        #DmgToEmy = Attack * AtckGo          #Dont damage the enemy as its their turn and they cannot take damage. "Attack" still has values
        #OppHlth = OppHlth - DmgToEmy        #Calculating how much dmg is done to characters.
        DmgToPlayer = OppAtck * AI_Atck_Go
        Health = Health - DmgToPlayer

        CheckBelow0HP()
        
        #print("You dealt",DmgToEmy,"damage to the enemy.")
        #print("Their health has depleted from",OppOldHlth,"Health. To",OppHlth,"Health.")
        #linespace()
        print(Opponent,"has dealt",DmgToPlayer,"damage to you!")
        print("Your health has depleted from",OldHlth,"health to",Health,"health.")
        linespace()
        print("Press any key to continue.")
        u = ord(m.getch())
        if OppHlth <=0:
            clear()
            print("You have killed",Opponent,". Nice job! Heading back to the map now...")
            BattleEnd == True
            break
        elif Health <=0:
            clear()
            print("""You have been beaten down to 0 health. The game will now exit.
Thank you for playing...""")
            time.sleep(1)
            print("""

 _____  _                                    _____  _                                   
|  __ \(_)                                  |  __ \(_)                                  
| |  | |_ _ __   ___  ___  __ _ _   _ _ __  | |  | |_ ___  ___ _____   _____ _ __ _   _ 
| |  | | | '_ \ / _ \/ __|/ _` | | | | '__| | |  | | / __|/ __/ _ \ \ / / _ \ '__| | | |
| |__| | | | | | (_) \__ \ (_| | |_| | |    | |__| | \__ \ (_| (_) \ V /  __/ |  | |_| |
|_____/|_|_| |_|\___/|___/\__,_|\__,_|_|    |_____/|_|___/\___\___/ \_/ \___|_|   \__, |
                                                                                  __/ |
                                                                                  |___/ 
-=-=-    
If you would like to play again...
Please re-open the game.""")
            u = ord(m.getch())
            sys.exit()
    clear()
    #print(Opponent,"blocked for a total of",Total_Block_AI,"times.")
    print(Opponent,"attacked for a total of",Total_Attack_AI,"times.")
    linespace()
    print("Press any key to continue.")
    u = ord(m.getch())



def User_Battle_Go():
    global dino, Opponent, Attack, OppAtck, OppHlth, BattleEnd, q, goes, SvGo, BlkGo, AtckGo, counter, Health, Go_No, Total_Block_AI, Total_Block_User
    AtckGo=0
    AI_Atck_Go=0
    BlkGo=0
    Go_No=1
    for i in range(0,2):
        #Player goes first.
        clear()
        print(name,"'s Stats... as",dino)
        print("Health:",Health)
        print("Attack",Attack)
        linespace()
        print(Opponent,"'s Stats...")
        print("Health:",OppHlth)
        print("Attack:",OppAtck)
        print("------------------------------------")
        print("""What would you like to do?
1. Attack...
2. Block...

Go number:""",Go_No)
        BattleChoice = int(input("Use (1 or 2) do not typo!- "))
        if BattleChoice == 1:
            AtckGo += 1
        elif BattleChoice == 2:
            BlkGo += 1
        else:
            print("You did something wrong. Restart the game or keep going but remember you will lose a go if you dont restart...")
        Go_No = Go_No + 1
        
    clear()
    print("Attacked:",AtckGo,"times.")
    print("Blocked:",BlkGo,"times.")   

    AtckGo = AtckGo - Total_Block_AI
    if AtckGo <0:                       #Makes sure the amount of goes is not a minus number (idk if this fcks shit up but dont want to try)
        AtckGo = 0
    else:
        pass
    OppOldHlth = OppHlth
    OldHlth = Health
    DmgToEmy = Attack * AtckGo
    OppHlth = OppHlth - DmgToEmy        #Calculating how much dmg is done to characters.
    DmgToPlayer = OppAtck * AI_Atck_Go
    Health = Health - DmgToPlayer
    linespace()
    linespace()

    if Total_Block_AI >= 1:
        print("Opponent blocked for:",Total_Block_AI,". Therefore your amount of attacks were countered by",Total_Block_AI,"blocks.")
        print("Your new amount of attacks is:",AtckGo,".")
    else:
        pass
    linespace()
    print("You dealt",DmgToEmy,"damage to the enemy.")
    print("Their health has depleted from",OppOldHlth,"Health. To",OppHlth,"Health.")
    linespace()
    #print(Opponent,"has dealt",DmgToPlayer,"damage to you!")
    #print("Your health has depleted from",OldHlth,"health to",Health,"health.")
    #linespace()
    print("Press any key to continue.")
    u = ord(m.getch())
    
    if OppHlth <=0:
        clear()
        print("You have killed",Opponent,". Nice job! Heading back to the map now...")
        BattleEnd = True
    elif Health <=0:
        clear()
        print("""You have been beaten down to 0 health. The game will now exit.
Thank you for playing...""")
        time.sleep(1)
        print("""

_____  _                                    _____  _                                   
|  __ \(_)                                  |  __ \(_)                                  
| |  | |_ _ __   ___  ___  __ _ _   _ _ __  | |  | |_ ___  ___ _____   _____ _ __ _   _ 
| |  | | | '_ \ / _ \/ __|/ _` | | | | '__| | |  | | / __|/ __/ _ \ \ / / _ \ '__| | | |
| |__| | | | | | (_) \__ \ (_| | |_| | |    | |__| | \__ \ (_| (_) \ V /  __/ |  | |_| |
|_____/|_|_| |_|\___/|___/\__,_|\__,_|_|    |_____/|_|___/\___\___/ \_/ \___|_|   \__, |
                                                                                   __/ |
                                                                                  |___/ 
-=-=-    
If you would like to play again...
Please re-open the game.""")
        u = ord(m.getch())
        sys.exit()
        
    
    print("Press any key to continue.")
    u = ord(m.getch())

def Starting():
    global whichstart, dino, name, Name, isright, newnameyorn
    text_file_n = open("Data/Saves/D_Name.txt", "r")
    name = text_file_n.read()
    if name == "":
        print("I see you do not have a name. Welcome...")
        while isright in no:
            name = input("Please name your Dinosaur: ")
            text_file_n = open("Data/Saves/D_Name.txt","r")
            text_file_n = open("Data/Saves/D_Name.txt","w")
            text_file_n.write("%s" %name)
            text_file_n.close()
            isright = input("Is "+name+" the right name? ")
    else:
        if newnameyorn == "no":
            pass
        else:
            print("Your Dinosaur's name is: ", name)
            newnameyorn = input("Do you want your Dinosaur to have a new name? ")
        
        if newnameyorn in yes:
            while isright in no:
                name = input("Please name your Dinosaur: ")
                text_file_n = open("Data/Saves/D_Name.txt","r")
                text_file_n = open("Data/Saves/D_Name.txt","w")
                text_file_n.write("%s" %name)
                text_file_n.close()
                isright = input("Is "+name+" the right name? ")
        else:               #####---- Gets a name from the text file.
            print("Your dinosaur will keep its original name.")

    linespace()

    #Welcoming to the game
    print("You are",name,"and you are playing as a",dino)
    linespace()

#ESSENTIAL TO PRINTING THE 2D ARRAY WITHOUT THE STUPID """""""""""""""" THINGS.

def PrintArray():   
    for y in ArrayGame:                 #Prints the 2D array.
        String = ""
        for x in y:
            String += x
        print(String)

CoOrdsForItems()

#
#TestingForF5()
#---------------------------------#
#---------------------------------#


#Main Menu -

while y != 10:
    print("WELCOME TO")
    print("""
 _____  _                                    _____  _                                   
|  __ \(_)                                  |  __ \(_)                                  
| |  | |_ _ __   ___  ___  __ _ _   _ _ __  | |  | |_ ___  ___ _____   _____ _ __ _   _ 
| |  | | | '_ \ / _ \/ __|/ _` | | | | '__| | |  | | / __|/ __/ _ \ \ / / _ \ '__| | | |
| |__| | | | | | (_) \__ \ (_| | |_| | |    | |__| | \__ \ (_| (_) \ V /  __/ |  | |_| |
|_____/|_|_| |_|\___/|___/\__,_|\__,_|_|    |_____/|_|___/\___\___/ \_/ \___|_|   \__, |
                                                                                   __/ |
                                                                                  |___/ 
    """)#Game name.
    print("^ Written in Ascii word generator in 'big' text. ^")
    print("This game is still in development. Please do not take this as the final build.")
    lineespace()
    lineespace()
    
    print("- Start...")
    print("- Options...")
    print("- Credits...")
    print("- Options Data...")
    print("- To Come In Future Patches...")
    #print("- Admin commands...")
    print("- Help Section...")
    print("- Quit (Dont use 'quit')...")
    lineespace()
    mainmenuchoice = input("What would you like to do? ")
    clear()
    
    if mainmenuchoice in menuOptions: #to be completed. dont know how to edit number for one option.
        MenuOptions()
        print("Press any key to continue.")
        b = ord(m.getch())
    elif mainmenuchoice in menuStart: #THE START OF DINO SELECTION
        y=10
        MenuStart()
        clear()
        print("You have chosen the",dino,".")
        DinoSave()
        Starting()
        OnlyRaptor()
        ValuesForDinos()
    elif mainmenuchoice in menuCredits:
        MenuCredits()
        print("Press any key to continue.")
        b = ord(m.getch())
    elif mainmenuchoice in menuInfo:
        MenuInfo()
        print("Press any key to continue.")
        b = ord(m.getch())
    elif mainmenuchoice in menuToCome:
        MenuToCome()
        print("Press any key to continue.")
        b = ord(m.getch())
##    elif mainmenuchoice in menuAdmin:
##        MenuAdminCommands()
##        print("Press any key to continue.")
##        b = ord(m.getch())
    elif mainmenuchoice in menuhelp:
        MenuHelp()
    elif mainmenuchoice in menuQuit:
        MenuQuit()
    else:
        InvalidInput()
        print("Press any key to continue.")
        b = ord(m.getch())
    clear()
First_Battle_Opponent()

#Battle()        #Skips the movement map thing as it bugs out and flashes. Use if you want to debug.
#Save()

#End of main menu -

#--#


#Map -

while x != 53:
    clear()    
    print("         Name:       ",name)
    print("         Score:      ",Score)
    print("         Your Level: ",Player_Level)
    Linespace()
    #CoOrdsForItems()
    if MoveEYorN == 2:
        if ArrayGame[PlayerRow][PlayerColumn] == Tree or ArrayGame[PlayerRow][PlayerColumn] == EdgeTree:
            pass
        else:
            MovingEnemies()
    TempCoordsItemsinMap()
    #CheckIfPlayerOnEnemy()
    PrintArray()
    NormMove = True
    Linespace()
    print("What would you like to do? ")
    print("""'D' Move Right.
'A' Move Left.
'W' Move Up.
'S' Move Down.

'P' Save the game
'5' Force End. Make sure you have saved before doing this.
    """)
    print("Column",PlayerColumn)
    print("Row",PlayerRow)
    Linespace()
    
    x = ord(m.getch())
    
    if x == 100 or x == 77 or x == 68:
        MovePlayerRight()
        Linespace()
    elif x == 97 or x == 75 or x == 65:
        MovePlayerLeft()
        Linespace()
    elif x == 119 or x == 72 or x == 87:
        MovePlayerUp()
    elif x == 115 or x == 80 or x == 83:
        MovePlayerDown()
    elif x == 112:
        Save()
    else:
        pass
    MoveEYorN = MoveEYorN + 1


    
clear() # Clears the screen and prints end.

if x == 53:
    print("""Game was force Closed. Press any key to continue...
Thanks for playing!""")
else:
    print("""The game has ended for an unknown reason. Please note down what you did before this occured and contact the Devs.
Press any key to quit. We apologise for any inconvenience.
Thank you for playing.""")
y = ord(m.getch())


#end
