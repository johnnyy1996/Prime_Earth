#DC: Battle for Prime Earth!

from graphics import *
import time

def countdown(window, Point, t):
    while t:
        count = Text(Point,str(t)).draw(window)
        time.sleep(1)
        t -= 1
        count.undraw()
    print('Perish Song!')

class button: 
    def __init__(self, win, center, width, height, label):
        w,h = width / 2.0, height / 2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.activate()

    def clicked(self, p):
        return(self.active and self.xmin <= p.getX() <= self.xmax and self.ymin <= p.getY() <= self.ymax)

    def getLabel(self):
        return self.label.getText()

    def activate(self):
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = False

    def remove(self):
        self.rect.undraw()
        self.label.undraw()

class heroes_and_villains:
    def __init__(self, Name, HP, Attack, Defense, SpAttack, SpDefense, Speed):
        self.Name = Name
        self.HP = HP
        self.Attack = Attack
        self.Defense = Defense
        self.SpAttack = SpAttack
        self.SpDefense = SpDefense
        self.Speed = Speed

    def printStats(self):
        print("Name:", self.Name)
        print("HP:", self.HP)
        print("Attack:", self.Attack)
        print("Defense:", self.Defense)
        print("SpAttack:", self.SpAttack)
        print("SpDefense:", self.SpDefense)
        print("Speed:", self.Speed)

class HeroAttacks:
    def __init__(self,Name, HP, Attack, Defense, SpAttack, SpDefense, Speed, Attacks):
        self.Name = Name
        self.HP = HP
        self.Attack = Attack
        self.Defense = Defense
        self.SpAttack = SpAttack
        self.SpDefense = SpDefense
        self.Speed = Speed
        self.Attack1 = Attacks.Attack1
        self.Attack2 = Attacks.Attack2
        self.Attack3 = Attacks.Attack3
        self.Attack4 = Attacks.Attack4
        self.Attack1Power = Attacks.Attack1Power
        self.Attack2Power = Attacks.Attack2Power
        self.Attack3Power = Attacks.Attack3Power
        self.Attack4Power = Attacks.Attack4Power
        self.Attack1Accuracy = Attacks.Attack1Accuracy
        self.Attack2Accuracy = Attacks.Attack2Accuracy
        self.Attack3Accuracy = Attacks.Attack3Accuracy
        self.Attack4Accuracy = Attacks.Attack4Accuracy

    def printStats(self):
        print("Name:", self.Name)
        print("HP:", self.HP)
        print("Attack:", self.Attack)
        print("Defense:", self.Defense)
        print("SpAttack:", self.SpAttack)
        print("SpDefense:", self.SpDefense)
        print("Speed:", self.Speed)
        print("\n")

    def printAttacks(self):
        print("Attack:", self.Attack1)
        print("Power:", self.Attack1Power)
        print("Accuracy:", self.Attack1Accuracy)
        print("\n")
        print("Attack:", self.Attack2)
        print("Power:", self.Attack2Power)
        print("Accuracy:", self.Attack2Accuracy)
        print("\n")
        print("Attack:", self.Attack3)
        print("Power:", self.Attack3Power)
        print("Accuracy:", self.Attack3Accuracy)
        print("\n")
        print("Attack:", self.Attack4)
        print("Power:", self.Attack4Power)
        print("Accuracy:", self.Attack4Accuracy)
        print("\n")

class Attacks:
    def __init__(self, Attack1, Attack1Power, Attack1Accuracy, Attack2, Attack2Power, Attack2Accuracy, Attack3, Attack3Power, Attack3Accuracy, Attack4, Attack4Power, Attack4Accuracy):
        self.Attack1 = Attack1
        self.Attack2 = Attack2
        self.Attack3 = Attack3
        self.Attack4 = Attack4
        self.Attack1Power = Attack1Power
        self.Attack2Power = Attack2Power
        self.Attack3Power = Attack3Power
        self.Attack4Power = Attack4Power
        self.Attack1Accuracy = Attack1Accuracy
        self.Attack2Accuracy = Attack2Accuracy
        self.Attack3Accuracy = Attack3Accuracy
        self.Attack4Accuracy = Attack4Accuracy


def welcome(window):
    title = Text(Point(25,45), "The Pokémon League")
    title.setSize(18)
    title.setTextColor("blue")  
    title.setStyle("italic")
    title.draw(window)
    startButton = button(window,Point(25,25), 12, 6, "START")
    pt = window.getMouse()
    #while loop is used to continue getting clicks until the button is pressed
    while not startButton.clicked(pt):
        pt = window.getMouse()
    if startButton.clicked(pt):
        title.undraw()
        startButton.remove()
        logIn_SignUp(window)

def logIn_SignUp(window):
    logIn_Buttton = button(window,Point(25, 29.5), 12, 6, "Log In")
    signUp_Button = button(window,Point(25, 21.5), 12, 6, "Sign Up")
    #modify this so that the user doesnt have to double click to get to sign up
    #use a pt and compare it to the click of log in and sign up buttons
    pt = window.getMouse()
    while not (logIn_Buttton.clicked(pt) or signUp_Button.clicked(pt)):
        pt = window.getMouse()
    if logIn_Buttton.clicked(pt):
        logIn_Buttton.remove()
        signUp_Button.remove()
        logIn(window)
    elif signUp_Button.clicked(pt):
        signUp_Button.remove()
        logIn_Buttton.remove()
        signUp(window)

def logIn(window):
    usernameText = Text(Point(10, 32.5), "Username:").draw(window)
    passwordText = Text(Point(10, 27.5), "Password:").draw(window)
    username = Entry(Point(33,32.5), 18)
    password = Entry(Point(33,27.5), 18)
    username.setText("Ex. Johnnyy96")
    password.setText("************")
    username.draw(window)
    password.draw(window)
    logInButton = button(window,Point(25, 17.5), 12, 6, "Log In")
    pt = window.getMouse()
    while not logInButton.clicked(pt):
        pt = window.getMouse()
    if logInButton.clicked(pt):
        #might be easier to make a function the performs this action
        #for both this and the signUp functions
        #print username text or password text depending on the violation
        #this scenario is when both the user does not exist and the password is wrong
        while not userexists(username.getText()) or not username_password_match(username.getText(), password.getText()):
            pt = Point(0,0)
            if not userexists(username.getText()):
                print("User does not exist!")
            elif not username_password_match(username.getText(), password.getText()):
                print("Incorrect Password!")
            while not logInButton.clicked(pt):
                pt = window.getMouse()
        usernameText.undraw()
        passwordText.undraw()
        username.undraw()
        password.undraw()
        logInButton.remove()
        mainMenu(window)
    
def signUp(window):
    #click an enter button and check if the user already exists. if it does
    #print an error. Otherwise, continue to create the new user
    usernameText = Text(Point(10, 32.5), "Username:").draw(window)
    passwordText = Text(Point(10, 27.5), "Password:").draw(window)
    username = Entry(Point(28,32.5), 12)
    password = Entry(Point(28,27.5), 12)
    username.draw(window)
    password.draw(window)
    enterButton = button(window,Point(28, 20), 12, 6, "Enter")
    #create a function to return true if the button is clicked
    #using a loop can check it each time it is clicked
    pt = window.getMouse()
    while not enterButton.clicked(pt):
        pt = window.getMouse()
    if enterButton.clicked(pt):
    #use the username entered by the user to see if it already exists
        while userexists(username.getText()):
            pt = Point(0,0)
            print("Try again")
            while not enterButton.clicked(pt):
                pt = window.getMouse()
        outfile = open("User_Information.txt", "a")
        print(username.getText(), password.getText(), "0", file = outfile)
        outfile.close()
        usernameText.undraw()
        passwordText.undraw()
        username.undraw()
        password.undraw()
        enterButton.remove()
        mainMenu(window)

def userexists(username):
        #create empty lists for the usernames and passwords of current users
        #make the username and the password in the same line and use split to split it
        #into two different strings and process them this way!!
        list_of_usernames = []
        #accompanying_passwords = []
        infile = open("User_Information.txt", "r")
        #check if file is empty
        for line in infile:
            if line == "\n":
                break
            #only need the username to avoid duplicates
            #duplicate passwords are allowed
            else:
                user, code, score = line.split()
                list_of_usernames.append(user)
            #might not need to keep track of password lists as passwords are irrelevant
            #accompanying_passwords.append(code)
        infile.close()
        #print(list_of_usernames)
        if not list_of_usernames:
            print("list is empty")
            return False
        for name in range(len(list_of_usernames)):
            if list_of_usernames[name] == username:
                return True
        return False

def username_password_match(username, password):
        list_of_usernames = []
        accompanying_passwords = []

        infile = open("User_Information.txt", "r")
        for line in infile:
            if line == "\n":
                break
            else:
                user, code, score = line.split()
                list_of_usernames.append(user)
                accompanying_passwords.append(code)
        infile.close()
        for name in range(len(list_of_usernames)):
            if list_of_usernames[name] == username and accompanying_passwords[name] == password:
                return True
        return False
    
def mainMenu(window):
    returnButtonPressed = True
    while returnButtonPressed:
        startButton = button(window,Point(25, 37.5), 20, 5, "Start")
        characterInfo = button(window,Point(25, 27.5), 20, 5, "Characters")
        leaderboardsButton = button(window,Point(25, 17.5), 20, 5, "Leaderboards")
        _quit_ = button(window,Point(25, 7.5), 20, 5, "Quit")
        pt = window.getMouse()
        while not (startButton.clicked(pt) or characterInfo.clicked(pt) or leaderboardsButton.clicked(pt) or _quit_.clicked(pt)):
            pt = window.getMouse()
        startButton.remove()
        characterInfo.remove()
        leaderboardsButton.remove()
        _quit_.remove()
        if startButton.clicked(pt):
            start(window)
            returnButtonPressed = False
        elif characterInfo.clicked(pt):
            character(window)       
        elif leaderboardsButton.clicked(pt):
            returnButtonPressed = leaderboards()
        elif _quit_.clicked(pt):
            quitWindow(window)
            returnButtonPressed = False
        
def start(window):
    text1 = Text(Point(25, 47), "Choose Your").draw(window)
    text2 = Text(Point(25, 44), "Character").draw(window)
    char1 = button(window,Point(25, 35), 22, 4, "Mewtwo")
    char2 = button(window,Point(25, 29), 22, 4, "Lugia")
    char3 = button(window,Point(25, 23), 22, 4, "Ho-oh")
    char4 = button(window,Point(25, 17), 22, 4, "Rayquaza")
    char5 = button(window,Point(25, 11), 22, 4, "Dialga")
    char6 = button(window,Point(25, 5), 22, 4, "Palkia")
    pt = window.getMouse()
    while not (char1.clicked(pt) or char2.clicked(pt) or char3.clicked(pt) or char4.clicked(pt) or char5.clicked(pt) or char6.clicked(pt)):
        pt = window.getMouse()
    text1.undraw()
    text2.undraw()
    char1.remove()
    char2.remove()
    char3.remove()
    char4.remove()
    char5.remove()
    char6.remove()
    if char1.clicked(pt):
        char1Attacks = Attacks("Psystrike", 100, 1.0, "Ice Beam", 90, 1.0, "Fire Blast", 110, .85, "Focus Blast", 120, .70)
        char1Name = HeroAttacks("Mewtwo", 106, 110, 90, 154, 90, 130, char1Attacks)
        char1Name.printStats()
        char1Name.printAttacks()
    elif char2.clicked(pt):
        char2Attacks = Attacks("Aeroblast", 100, .95, "Blizzard", 110, .70, "Hydro Pump", 110, .80, "Thunderbolt", 90, 1.0)
        char2Name = HeroAttacks("Lugia", 106, 110, 90, 154, 90, 130, char2Attacks)
        char2Name.printStats()
        char2Name.printAttacks()
    elif char3.clicked(pt):
        char3Attacks = Attacks("Sacred Fire", 100, .95, "Earthquake", 100, 1.0, "Thunder", 110, .70, "Fire Blast", 110, .85)
        char3Name = HeroAttacks("Ho-oh", 106, 110, 90, 154, 90, 130, char3Attacks)
        char3Name.printStats()
        char3Name.printAttacks()
    elif char4.clicked(pt):
        char4Attacks = Attacks("Dragon Ascent", 120, 1.0, "Extreme Speed", 80, 1.0, "Iron Tail", 100, .75, "V-create", 180, .95)
        char3Name = HeroAttacks("Rayquaza", 106, 110, 90, 154, 90, 130, char4Attacks)
        char3Name.printStats()
        char3Name.printAttacks()
    elif char5.clicked(pt):
        char5Attacks = Attacks("Draco Meteor", 130, .90, "Earth Power", 90, 1.0, "Roar of Time", 150, .90, "Flamethrower", 90, 1.0)
        char5 = HeroAttacks("Dialga", 106, 110, 90, 154, 90, 130, char5Attacks)
        char5.printStats()
        char5.printAttacks()
    elif char6.clicked(pt):
        char6Attacks = Attacks("Spacial Rend", 100, .95, "Focust Punch", 150, 1.0, "Aqua Tail", 90, .90, "Stone Edge", 100, .80)
        char6 = HeroAttacks("Palkia", 106, 110, 90, 154, 90, 130, char6Attacks)
        char6.printStats()
        char6.printAttacks()

#def game(window, character):
        

def character(window):
    charButtonPressed = True
    char1 = button(window,Point(25, 45), 22, 4, "Mewtwo")
    char2 = button(window,Point(25, 39), 22, 4, "Lugia")
    char3 = button(window,Point(25, 33), 22, 4, "Ho-oh")
    char4 = button(window,Point(25, 27), 22, 4, "Rayquaza")
    char5 = button(window,Point(25, 21), 22, 4, "Dialga")
    char6 = button(window,Point(25, 15), 22, 4, "Palkia")
    back = button(window,Point(25, 5), 22, 4, "Return")
    while charButtonPressed:
        pt = window.getMouse()
        while not (char1.clicked(pt) or char2.clicked(pt) or char3.clicked(pt) or char4.clicked(pt) or char5.clicked(pt) or char6.clicked(pt) or back.clicked(pt)):
            pt = window.getMouse()
        if char1.clicked(pt):
            characterButton("Mewtow's Stats", "Mewtwo", 106, 110, 90, 154, 90, 130)
        elif char2.clicked(pt):
            characterButton("Lugia's Stats", "Lugia", 106, 90, 130, 90, 154, 110)
        elif char3.clicked(pt):
            characterButton("Ho-oh's Stats", "Ho-oh", 106, 130, 90, 110, 154, 90)
        elif char4.clicked(pt):
            characterButton("Rayquaza's Stats", "Rayquaza", 105, 150, 90, 150, 90, 95)
        elif char5.clicked(pt):
            characterButton("Dialga's Stats", "Dialga", 100, 120, 120, 150, 100, 90)
        elif char6.clicked(pt):
            characterButton("Palia's Stats", "Palkia", 90, 120, 100, 150, 120, 100)
        elif back.clicked(pt):
            charButtonPressed = False
            char1.remove()
            char2.remove()
            char3.remove()
            char4.remove()
            char5.remove()
            char6.remove()
            back.remove()

def characterButton(window, Name, HP, Attack, Defense, SpAttack, SpDefense, Speed):
    win = GraphWin(window)
    win.setCoords(0,0,50,50)
    hero = heroes_and_villains(Name, HP, Attack, Defense, SpAttack, SpDefense, Speed)
    hero.printStats()
    closeButton = button(win, Point(25, 5), 33, 5, "Close")
    pt = win.getMouse()
    while not closeButton.clicked(pt):
        pt = win.getMouse()
    if closeButton.clicked(pt):
        win.close()

#modify this after everything is set to contain only the top 10 scores
def leaderboards():
    win = GraphWin("Leaderboards")
    win.setCoords(0,0,50,50)
    
    infile = open("User_Information.txt", "r")
    list_of_usernames = []
    accompanying_passwords = []
    scores =  []

    for line in infile:
        user, code, score = line.split()
        list_of_usernames.append(user)  #adds the users to a list for later use
        #accompanying_passwords.append(code)
        scores.append(score)    #adds the accompanying scores to a list for later use

    #print the users and their accompanying scores
    for user in range(len(list_of_usernames)):
        Text(Point(17, 47-(user*5)), list_of_usernames[user]).draw(win)
        Text(Point(33, 47-(user*5)), scores[user]).draw(win)
    closeButton = button(win, Point(25, 5), 33, 5, "Close")
    pt = win.getMouse()
    while not closeButton.clicked(pt):
        pt = win.getMouse()
    if closeButton.clicked(pt):
        win.close()
        return True

def quitWindow(window):
    #create a function to do this in one go for each element
    #instead of rewriting it three times
    thanks = Text(Point(25,32), "Thanks")
    _for_ = Text(Point(25,25), "For")
    playing = Text(Point(25,18), "Playing!")
    thanks.setSize(18)
    _for_.setSize(18)
    playing.setSize(18)
    thanks.draw(window)
    _for_.draw(window)
    playing.draw(window)
    
def main():
    win = GraphWin("Battle for Prime Earth")
    win.setCoords(0,0,50,50)
    #countdown(win, Point(25,25), 99)
    mainMenu(win)
    #welcome(win)
    if win.getMouse():
        win.close()
    
main()

#create a funtion to include the pt-while loop that I continue
#to use throughout the program

#use the technique that allows you to use any number of parameters (check textbook)
