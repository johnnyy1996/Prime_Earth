#DC: Battle for Prime Earth!

from graphics import *

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
    def __init__(self, name, power, defense, speed, health, attack1, attack2, attack3, attack4):
        self.name = name
        self.power = power
        self.defense = defense
        self.health = health
        self.attack1 = attack1
        self.attack2 = attack2
        self.attack3 = attack3
        self.attack4 = attack4
        #special should be removed for now until it can be efficiently added to the game
        #self.special = special

    #def attack1():

        #have a function to print out the character info in the info screen



def welcome(window):
    title = Text(Point(25,45), "Battle for Prime Earth!")
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
    logIn_Buttton = button(window,Point(25, 37.5), 12, 6, "Log In")
    signUp_Button = button(window,Point(25, 12.5), 12, 6, "Sign Up")
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
    username = Entry(Point(25,37.5), 24)
    username.draw(window)
    username.setText("Ex. Johnnyy96")
    password = Entry(Point(25,12.5), 24)
    password.setText("************")
    password.draw(window)
    
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
        print(username.getText(), password.getText(), file = outfile)
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
                user, code = line.split()
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
    
def mainMenu(window):
    start = button(window,Point(25, 37.5), 20, 5, "Start")
    characterInfo = button(window,Point(25, 27.5), 20, 5, "Characters")
    leaderboards = button(window,Point(25, 17.5), 20, 5, "Leaderboards")
    _quit_ = button(window,Point(25, 7.5), 20, 5, "Quit")
    if start.clicked(window.getMouse()):
        start.remove()
        characterInfo.remove()
        leaderboards.remove()
        _quit_.remove()
        character(window)

#def start():

def character(window):
    Superman = button(window,Point(25, 45), 22, 5, "Superman")
    Batman = button(window,Point(25, 37), 22, 5, "Batman")
    WonderWoman = button(window,Point(25, 29), 22, 5, "WonderWoman")
    TheFlash = button(window,Point(25, 21), 22, 5, "The Flash")
    GreenLantern = button(window,Point(25, 13), 22, 5, "Green Lantern")
    Cyborg = button(window,Point(25, 5), 22, 5, "Cyborg")

#def leaderboards():

#def _quit_():
    
def main():
    win = GraphWin("Battle for Prime Earth")
    win.setCoords(0,0,50,50)
    welcome(win)
    
main()
