







import time


def start_game():

    print("""
    ▒███████▒ ▒█████   ███▄ ▄███▓ ▄▄▄▄    ██▓▓█████    ▓█████▄  ▒█████  ▓█████▄   ▄████ ▓█████  ██▀███  
    ▒ ▒ ▒ ▄▀░▒██▒  ██▒▓██▒▀█▀ ██▒▓█████▄ ▓██▒▓█   ▀    ▒██▀ ██▌▒██▒  ██▒▒██▀ ██▌ ██▒ ▀█▒▓█   ▀ ▓██ ▒ ██▒
    ░ ▒ ▄▀▒░ ▒██░  ██▒▓██    ▓██░▒██▒ ▄██▒██▒▒███      ░██   █▌▒██░  ██▒░██   █▌▒██░▄▄▄░▒███   ▓██ ░▄█ ▒
    ▄▀▒   ░▒██   ██░▒██    ▒██ ▒██░█▀  ░██░▒▓█  ▄    ░▓█▄   ▌▒██   ██░░▓█▄   ▌░▓█  ██▓▒▓█  ▄ ▒██▀▀█▄  
    ▒███████▒░ ████▓▒░▒██▒   ░██▒░▓█  ▀█▓░██░░▒████▒   ░▒████▓ ░ ████▓▒░░▒████▓ ░▒▓███▀▒░▒████▒░██▓ ▒██▒
    ░▒▒ ▓░▒░▒░ ▒░▒░▒░ ░ ▒░   ░  ░░▒▓███▀▒░▓  ░░ ▒░ ░    ▒▒▓  ▒ ░ ▒░▒░▒░  ▒▒▓  ▒  ░▒   ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
    ░░▒ ▒ ░ ▒  ░ ▒ ▒░ ░  ░      ░▒░▒   ░  ▒ ░ ░ ░  ░    ░ ▒  ▒   ░ ▒ ▒░  ░ ▒  ▒   ░   ░  ░ ░  ░  ░▒ ░ ▒░
    ░ ░ ░ ░ ░░ ░ ░ ▒  ░      ░    ░    ░  ▒ ░   ░       ░ ░  ░ ░ ░ ░ ▒   ░ ░  ░ ░ ░   ░    ░     ░░   ░ 
    ░ ░        ░ ░         ░    ░       ░     ░  ░      ░        ░ ░     ░          ░    ░  ░   ░     
    ░                                  ░                ░                ░                              
    """)

    time.sleep(2)
    print("Hello and welcome to Zombie Dodger. You must guide yourself to safety as quickly as possible!")    
    print("\n")
    time.sleep(2)
    name = input("Please Enter your name or make one up if you're shy :   ")
    print("\n")
    time.sleep(2)
    print("Welcome {}".format(name))
    print("\n")
    time.sleep(2)
    print("Lets get started! The scenario :")
    print("\n")
    time.sleep(2)
    print("You were in a car accident a week ago, since then you've been in a coma.")
    print("\n")
    time.sleep(3)
    print("while you've been asleep a chemical spill has infected people with an unknown virus which is turning people into the undead.")
    print("\n")
    time.sleep(4)
    print("Youve just woken up, you are lay in a hospital bed in a room on your own.")
    print("\n")
    time.sleep(2)
    print("As your senses start to return, you realise something is wrong.")
    print("\n")
    time.sleep(2)
    print("The room is dark, nothing is turned on, no lights outside the door and your clothes are on top of you.")
    print("\n")
    time.sleep(3)
    print("You quickly get up and get dressed. The door is locked but you use a key that has been slid back under the door, realising that youve been locked in!")
    print("\n")
    time.sleep(4)
    print("As you open the door you hear a radio playing:")
    print("\n")
    time.sleep(3)
    print("'Attention, Attention! This is a recording.\
    All survivors and uninfected please head to the safe zone located at your local TA barracks'\
    \n'Stay out of sight and where possible, let off a flare for rescue'")
    time.sleep(6)
    print("\n")
    print("To your left is a lift at the bottom of the corridor, to the right are the doors to the stairwell.")
start_game()


def bk_down():
    print("\n")
    time.sleep(2)
    Bk = input("Would you like to go back?   :")
    if Bk.upper() == "Y" or Bk.upper() == "YES":
        start_stairs()
    elif Bk.upper() == "N" or Bk.upper() == "NO":
        print("""
        ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███  
        ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
        ▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
        ░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  
        ░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
        ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
        ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
        ░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░ 
            ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░     
                                                            ░                   
        """)
        exit() 
    else:
        bk_down.upper() != "Y" or bk_down.upper() != "Yes"or bk_down.upper() != "N" or bk_down.upper() != "No"
        print("I did not understand that answer, please try again")
        bk_down()


def climb_flare():
    print ("You continue walking, hoping this is the rightway")
    print("\n")
    time.sleep(2)       
    print ("""Unfortunatley You Have Reached a Dead End. You only have one option
            that is to return tothe stairwell""")
    print("\n")
    time.sleep(2)
    print("\n")
    print("You return to the stairwell and climb to the top.")
    time.sleep(2)
    print("\n")
    print ("""You are now on the Roof. You look around,
            there is no one else to be seen""" )
    time.sleep(2)
    print("\n")
    print ("You breathe a sigh of relief")
    time.sleep(2)
    print("\n")
     #go back towhere?.
    print ("You release the Flare")
    time.sleep(2)
    print ("""

    ▓██   ██▓ ▒█████   █    ██     █     █░ ▒█████   ███▄    █  ▐██▌ 
    ▒██  ██▒▒██▒  ██▒ ██  ▓██▒   ▓█░ █ ░█░▒██▒  ██▒ ██ ▀█   █  ▐██▌ 
    ▒██ ██░▒██░  ██▒▓██  ▒██░   ▒█░ █ ░█ ▒██░  ██▒▓██  ▀█ ██▒ ▐██▌ 
    ░ ▐██▓░▒██   ██░▓▓█  ░██░   ░█░ █ ░█ ▒██   ██░▓██▒  ▐▌██▒ ▓██▒ 
    ░ ██▒▓░░ ████▓▒░▒▒█████▓    ░░██▒██▓ ░ ████▓▒░▒██░   ▓██░ ▒▄▄  
    ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒    ░ ▓░▒ ▒  ░ ▒░▒░▒░ ░ ▒░   ▒ ▒  ░▀▀▒ 
    ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░      ▒ ░ ░    ░ ▒ ▒░ ░ ░░   ░ ▒░ ░  ░ 
    ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░      ░   ░  ░ ░ ░ ▒     ░   ░ ░     ░ 
    ░ ░         ░ ░     ░            ░        ░ ░           ░  ░    
    ░ ░                                                             

    """)
    time.sleep(2)
    print("\n")
    print ("You made it\
                OUT ALIVE""")
    time.sleep(2)
    print ("""
        ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███  
        ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
        ▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
        ░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  
        ░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
        ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
        ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
        ░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░ 
            ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░     
                                                            ░                   
        """)
    time.sleep(2) 
    exit()
         
                
def ent_floor (): 
    print("\n")
    floor_s = input("Do you want to enter the floor or keep climbing? : ")
    if floor_s.upper() == ("Y") or floor_s.upper == ("YES"):
        weapon_choice1()
    elif floor_s.upper() == ("N") or floor_s == ("NO"):
        print("\n")
        climb_stairs()
    else:
        print("\n")
        print("Please enter a valid input!")
        ent_floor()


def yes_path():    

    time.sleep(2)
    print("You decide to enter the room, It's dark and there is a nasty smell!")
    print("\n")
    time.sleep(2)
    print("You feel around on the wall and find the light switch.......")
    print("\n")
    time.sleep(3)
    print("You gasp putting your hands to your face and say, 'Oh my God'.")
    print("\n")
    time.sleep(3)
    print("not only is the room full of mutilated corpses but......")
    print("\n")
    time.sleep(3)
    print("The switch and your hand are covered in bits of blood and entrails.")
    print("\n")
    time.sleep(3)
    print("you decide to leave the room as quickly as possible!")
    print("\n")
    time.sleep(3)
    no_path()
              
             
def room_unlocked():
    print("\n")
    yes_or_no = input("Would you like to enter room?\
    \n YES = Enter  \
    \n NO = Go up  : ")
    print("\n")
    if yes_or_no.upper() == "Y" or yes_or_no.upper() == "YES":
        yes_path()
    elif yes_or_no.upper() == "N" or yes_or_no.upper() == "NO":
        no_path()
    else:
        print("Invalid input, try again.")
        room_unlocked()
            
def return_search():
    print("\n")
    ret_end = input("Do you wish to return and search the room?\
            \nYes = Y\
            \n No = N ")# return to where
    if ret_end.upper() == ("Y") or ret_end.upper == ("YES"):
        time.sleep(2)
        weapon_choice2()
            
    elif ret_end.upper == ("N") or ret_end.upper == ("NO"):
        print("GAME OVER")
        exit()
    else:
        print("Please enter a valid input")
        return_search()

        


def climb_stairs():
    print("\n")
    print("You start to climb the stairs and make your way straight to the top.")
    print("\n")
    time.sleep(2)
    print ("You Have Reached The Roof")
    print("\n")
    time.sleep(2)
    print ("You Have Not Got a Flare")
    print("\n")
    time.sleep(2)
    return_search()


def weapon_choice2 (): 
    print ("At the end of the floor you find a room./")
    time.sleep(2)
    print("\n")
    print("However, the room is chained shut with a piece of rope")
    time.sleep(2)
    print("\n")
    print ("You have a variety of weapons at your disposal that will help you to gain entry")
    time.sleep(2)
    ent_floor = input("Do you use your weapon to open the door? : ")
    if ent_floor.upper() == ("Y") or ent_floor.upper == ("YES"):
        print("\n")
        print ("You choose to enter")
        time.sleep(2)
        print("\n")
        print ("You cut the rope and enter the room,you find a Flare. This should come in handy")
        time.sleep(2)
        climb_flare()
    elif ent_floor.upper() == ("N") or ent_floor == ("NO"):
        climb_stairs()
    else:
        weapon_choice2.upper() != "Y" or weapon_choice2.upper() != "Yws"or weapon_choice2.upper() != "N" or weapon_choice2.upper() != "No"
        print("I did not understand that answer, please try again")
        weapon_choice2()

def start_hosp():
    print("You wonder down the corridor while passing lots of locked doors.")
    print("\n")
    time.sleep(3)
    print("You try the handles of all the doors trying to see if any are open.")
    print("\n")
    time.sleep(2)
    print("Finaly you find a door that eerily creaks open.")
    print("\n")
    time.sleep(4)
    print("Do you enter the room or not?")
    print("\n")
    (time.sleep(2))
    room_unlocked()


def continue_path():
        print("You decide not to enter the second floor and keep climbing the stairs.")
        time.sleep(3)       
        print("\n")
        print("Panting and out of breath you reach the fourth floor.")       
        time.sleep(3)
        print("\n")
        print("The door is unlocked! 'Will this ever end?'")
        print("\n")
        weapon_choice2()
        

def door_unlocked():
    yes_or_continue = input("Which do you choose? [Y/C] ")
    if yes_or_continue.upper() == "Y" or yes_or_continue.upper() == "YES":
        start_hosp()
    elif yes_or_continue.upper() == "C" or yes_or_continue.upper() == "CONTINUE":
        continue_path()
    else:
        print("Invalid input, try again.")
        print("\n")
        door_unlocked()  
def no_path():
    print("\n")
    print("You continue hastily down the corridor.")
    time.sleep(3)
    print("\n")
    print("You wonder down the corridor for what seems like a long time,")
    time.sleep(1)
    print("\n")
    time.sleep(3)
    print("At last you come to a set of stairs, You make your way up the stairs.")
    print("\n")
    time.sleep(3)
    print("As you climb the stairs you bump head first into a Zombie!")
    print("\n")
    time.sleep(3)
    print("You are attacked by the Zombie, It goes to bite your face.......")
    print("\n")
    time.sleep(3)
    
    print("\n")
    print("You use your weapon to defend your self,")
    time.sleep(3)
    print("\n")
    print("Blood is splattering all over the place!")
    print("\n")
    time.sleep(3)
    print("You kill the Zombie, His head falls down the stairs.")
    print("\n")
    time.sleep(3)
    print("It makes a bumping sound as it hits every step on its way down.")
    print("\n")
    time.sleep(3)
    print("You continue up the stairs until you reach the next floor.")
    print("\n")
    time.sleep(3)
    print("There is a door unlocked, Do you want to enter the second floor or continue up the stairs.")
    print("\n")
    door_unlocked()

def weapon_choice1():

    time.sleep(2)
    print("As you walk down the corridor you spot an open box with a variety of weapons :\
    \n 1 : Knife,\
    \n 2 : Axe,\
    \n 3 : Saw\
        \n 4 : Machete.")
    print("\n")
    time.sleep(3)
    print("Which one do you choose?")
    print("\n")
    time.sleep(1)
    w_list1 = (input("please enter your choice:"))
    time.sleep(1)
    if w_list1 == "1":
        print("\n")
        time.sleep(1)
        print("You chose the Knife")
        time.sleep(1)
        continue_path()

    elif w_list1 == "2":
        print("\n")
        print("You chose the axe")
        no_path()

    elif w_list1 == "3":
        print("\n")
        print("You chose the saw")
        no_path()

    elif w_list1 == "4":
        print("\n")
        print("You chose the machete")
        print("\n")
        no_path()
    else:
        weapon_choice1.upper() != "1" or weapon_choice1.upper() != "2"or weapon_choice1.upper() != "3" or weapon_choice1.upper() != "4"
        print("I did not understand that answer, please try again")
        weapon_choice1()
        
        
def car_park():
    print("As you reach the edge of the carpark you take a look around.")
    print("\n")
    time.sleep(2)
    print("Most roads are blocked, you can see two possible routes.")
    print("\n")
    time.sleep(2)
    print("One leads to the City, the other leads to the park.")
    print("\n")
    time.sleep(1)
    print("Which way will you walk?")
    print("\n")
    time.sleep(1)
    print("\n")
    print("To the city : 1\
    \n To the park : 2")    
    print("\n")
    walk_choice()
    
    
def back5():
    print("\n")
    bk_stairs = input("Would you like to go back?")
    if   bk_stairs.upper() == "Y" or bk_stairs.upper() == "YES":
        print("\n")
        stairs_lift()
    elif bk_stairs.upper() == "N" or bk_stairs.upper() == "N" or bk_stairs.upper() == "NO":
        print("""
        ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███  
        ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
        ▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
        ░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  
        ░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
        ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
        ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
        ░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░ 
            ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░     
                                                            ░                   
        """)
        exit()
    else:
        print("Did not understand input, please try again")
        back5()
        

def back4():
    print("\n")
    bk_stairs = input("Would you like to go back?  :  ")
    print("\n")
    if   bk_stairs.upper() == "Y" or bk_stairs.upper() == "YES":
      start_stairs()
    elif bk_stairs.upper() == "N" or bk_stairs.upper() == "N" or bk_stairs.upper() == "NO":
        print("""
        ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███  
        ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
        ▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
        ░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  
        ░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
        ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
        ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
        ░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░ 
            ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░     
                                                            ░                   
        """) 
        exit()
    else:
        print("Did not understand input, please try again")
        back4()

def succes():
    print("Success!!!")
    print("\n")
    print("""

    ▓██   ██▓ ▒█████   █    ██     █     █░ ▒█████   ███▄    █  ▐██▌ 
    ▒██  ██▒▒██▒  ██▒ ██  ▓██▒   ▓█░ █ ░█░▒██▒  ██▒ ██ ▀█   █  ▐██▌ 
    ▒██ ██░▒██░  ██▒▓██  ▒██░   ▒█░ █ ░█ ▒██░  ██▒▓██  ▀█ ██▒ ▐██▌ 
    ░ ▐██▓░▒██   ██░▓▓█  ░██░   ░█░ █ ░█ ▒██   ██░▓██▒  ▐▌██▒ ▓██▒ 
    ░ ██▒▓░░ ████▓▒░▒▒█████▓    ░░██▒██▓ ░ ████▓▒░▒██░   ▓██░ ▒▄▄  
    ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒    ░ ▓░▒ ▒  ░ ▒░▒░▒░ ░ ▒░   ▒ ▒  ░▀▀▒ 
    ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░      ▒ ░ ░    ░ ▒ ▒░ ░ ░░   ░ ▒░ ░  ░ 
    ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░      ░   ░  ░ ░ ░ ▒     ░   ░ ░     ░ 
    ░ ░         ░ ░     ░            ░        ░ ░           ░  ░    
    ░ ░                                                             

    """)
    lines = ["You greet the soldiers manning the gates as they let you enter, and you look around in amazement. You see people at a burger stand,",
      "eating hot food and drinking cold drinks, and you are relieved to see some semblence of normal life continuing",
      "You are filled with relief and a sense of security, your ordeal is over, CONGRATULATIONS !"]


    from time import sleep
    import sys

    for line in lines:          
        for c in line:          
            print(c, end='')    
            sys.stdout.flush()  
            sleep(0.1)          
        print('')
    exit()


def c2():
    print("\n")
    choice2 = input("Do you want to go Left or Right?")
    if choice2.upper() == "L" or choice2.upper() == "Left":
        print("\n")
        print("You walk down street, find shortcut bypassing the roadblock coming to a fence")
        print("\n")
        time.sleep(1)
        print("You climb the fence, and come to a road which you follow")
        print("\n")
        time.sleep(1)
        print("Congratulations! You have reached the safe zone! You have won!")
        print("\n")
        time.sleep(1)
        succes()
    if choice2.upper() == "R" or choice2.upper() == "RIGHT":
        print("\n")
        time.sleep(1)
        print("You reach the end of the alleyway, and ariive at a street where people are looting and killing each other. You are able to quickly ride past on the bike")
        print("\n")
        time.sleep(1)
        print("Congratulations! You have reached the safe zone!")
        print("\n")
        succes()
    else:
        choice2.upper() != "L" or choice2.upper() != "Left"or choice2.upper() != "R" or choice2.upper() != "Right"
        print("\n")
        print("I did not understand that answer, please try again")
        c2()

def back():
        print("\n")
        gcc1 = input("Yes or No?")
        if gcc1.upper() == "Y" or gcc1.upper() == "YES":
            start()
        elif gcc1.upper() == "N" or gcc1.upper() == "No":
            ("""
            ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███  
            ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
            ▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
            ░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  
            ░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
            ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
            ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
            ░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░ 
                ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░     
                                                                ░                   
            """) 
            quit()
        else:
            gcc1.upper() != "Y" or gcc1.upper() != "Yes"or gcc1.upper() != "N" or gcc1.upper() != "No"
            print("\n")
            print("I did not understand that answer, please try again")
            print("\n")
            back()

def bike():
        rblock = input("L or R ?")
        if rblock.upper() == "L" or rblock.upper() == "LEFT":
            print("You Walk down the street, finding a shortcut bypassing the roadblock")
            time.sleep(1)
            print("\n")
            print("Congratulations! You have reached the safe zone! You have won!")
            time.sleep(1)
            print("\n")
            succes()    
        elif rblock.upper() == "R" or rblock.upper() == "RIGHT":
            print("You reach the end of the alleyway, ariiving at a street where people are looting and killing each other.")
            time.sleep(1)
            print("\n")
            print("They fear you are a zombie and collectively beat you to death (Better luck next time)")
            time.sleep(1)
            print("\n")
            print("Would you like to go back?")        
            print("\n")
            back()
        else:
            if rblock.upper() != "L" or rblock.upper() != "Left"or rblock.upper() != "R" or rblock.upper() != "Right":
                print("\n")
                print("I did not understand that answer, please try again")
                print("\n")
                bike()


def start():
    print("\n")
    print("You see a bike behind a locked gate, do you want to use your weapon to try and force gate open?")  
    time.sleep(1)
    print("\n") 
    choice1 = input ("Yes(y) or No(n)")   
    if choice1.upper() == "N" or choice1.upper() == "NO":
        print("\n")
        print("You continue down the road and see a large message painted on the wall SAFE ZONE with an arrow pointing straight ahead")
        time.sleep(2)
        print("\n")
        print("The road ahead is blocked by abandoned vehicles")
        time.sleep(1)
        print("\n")
        print("You face a decision, to go Left or Right?")
        time.sleep(1)
        print("\n")
        bike()
    elif choice1.upper() == "Y" or choice1.upper() == "YES":
        print("\n")
        print("You force open the gate, taking the bike and continuing up road")
        time.sleep(1)
        print("\n")
        print("You see a sign inidcating direction of safe zone (straight ahead)")
        time.sleep(1)
        print("\n")
        print("The road ahead is blocked by vehcle fires, will you take the street on the left, or the alley on right?")
        time.sleep(1)
        print("\n")
    else:
        if choice1.upper() != "Y" or choice1.upper() != "Yes"or choice1.upper() != "N" or choice1.upper() != "No":
            print("I did not understand that answer, please try again")
        start()
    c2()


def start_city():
    print("You take the route towards the city")
    print("\n")
    time.sleep(2)
    print("As you are walking past an alleyway you hear a noise.")
    print("\n")
    time.sleep(2)
    print("You turn to look, and realise a huge swarm of undead are heading towards you!")
    print("\n")
    time.sleep(2)
    print("You sprint as fast as possible, but they are quick!")
    print("\n")
    time.sleep(2)
    print("You are forced to run down the closest alleyway to escape.")
    print("\n")
    time.sleep(2)
    print("As you reach the end of the alleyway you can go 2 ways:\
        \n LEFT or RIGHT.")
    time.sleep(2)
    print("\n")
    choice1 = input("Which way will you go?")
    if choice1.upper() == "L" or choice1.upper() == "LEFT":
        print("\n")
        print("You ran into a dead end! You were caught and disembowled!")
        time.sleep(2)
        print("\n")
        ret = input("do you want to go back?")
        if ret.upper() == "Y" or ret.upper() == "YES":
            (start_city())
        elif ret.upper() == "N" or ret.upper() == "NO":
            print ("GAME OVER!")
    elif choice1.upper() == "R" or choice1.upper() == "RIGHT":
        print("You turn right and run to the end of the alleyway")
        road_choice()
    else:
        print("Did not understand input, please try again")
        start_city()

def road_choice():
    print("\n")
    time.sleep(2)
    print("You stop at the road. There are 3 ways you can go:")
    print("\n")
    print("Follow the road on the left : 1 ")
    print("\n")
    print("Follow the road on the right : 2")
    print("\n")
    print("Take the subway : 3 ")
    print("\n")
    choice2 = int(input("Which way would you like to go?"))
    if choice2 == (1):
        print("\n")
        print("You take the road on the left. As you round the corner, you see the road is blocked by a fire and the undead are approaching!\
        \n You have no choice but to go back.")
        time.sleep(1)
        print("\n")
        road_choice()
    elif choice2 == (3):
        time.sleep(2)
        print("\n")
        print("You take the subway, its pitch black but you can see daylight at the other end.\
            \n As you near the middle you hear a sound and see a shadow enter towards you followed by another........\
            \n You realise the undead have entered the subway! you have no choice but to turn back.")
        road_choice()
    elif choice2 == (2):
        time.sleep(1)
        print("\n")
        print("You take the road on the right")
        start()
    else:
        time.sleep(1)
        print("Please enter a valid input!") 
        road_choice()


def start_park():
    print("\n")
    print("You cautiously enter a park, making sure there are no signs of any undead.")
    print("\n")
    time.sleep(2)
    print("All looks clear so you decide to cut through to avoid the city")
    print("\n")
    time.sleep(2)
    print("As you are making your way through, you meet a group of people doing the same")
    print("\n")
    time.sleep(2)
    print("Up ahead is a moody looking forest you must pass through.")
    print("\n")
    time.sleep(2)
    print("Do you wish to follow them or turn round and make your way to the city?")
    print("\n")
    time.sleep(1)
    choice2 = input("Follow : 1\
        \n Turn back and enter city : 2\
        \n  :  ")
    if choice2 == "1":
        print("You enter the forest with the group. you are quickly ovverrun and caught.\
            \n Zombies suck your eyeballs from your head!")
        back3()
    elif choice2 == "2":
        start_city()
    else:
        print("Did not undersand input,please try again")
        start_park()        
        
        
def start_stairs():
    print("\n")
    time.sleep(2)
    ans2 = input("You are on floor 1. Would you like to go upstairs to investigate?\
    \n YES = Go up  \
    \n NO = Go down  :  ")
    print("\n")
    if ans2.upper() == "N" or ans2.upper() == "NO":
        time.sleep(1)
        print("\n")
        print("You choose downstairs, good choice.")
        door_choice()
    elif ans2.upper() == "Y" or ans2.upper() == "YES":
        time.sleep(1)
        print("\n")
        print("As you walk up the stairs to the next level, suddenly the door bursts off its hinges!\
        \n You try to run but you fall and are quickly dismembered by zombies!")
        back4()
    else:
        print("Did not undersand input,please try again")
        start_stairs()        

        
def back3():
    bk_stairs = input("Would you like to go back?")
    if   bk_stairs.upper() == "Y" or bk_stairs.upper() == "YES":
      start_park()
    elif bk_stairs.upper() == "N" or bk_stairs.upper() == "N" or bk_stairs.upper() == "NO":
        print("""  ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███  
                ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
                ▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
                ░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  
                ░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
                ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
                ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
                ░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░ 
                    ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░     
                                                                    ░                   """)
        exit()
    else:
        print("Did not undersand input,please try again")
        back3()        

def stairs_lift():
    print("\n")
    ans1 = input("Which way do you want to go, left or right?  : ")
    print("\n") 

    if ans1.upper() == "L" or ans1.upper() == "LEFT":
        print("You walk down the corridor towards the lift and press the call button")
        time.sleep(1)
        print("\n")
        print("The lift dings and the doors open.")
        print("\n")
        time.sleep(1)   
        print("The lift is full of Zombies!")
        print("\n")
        time.sleep(1)
        print("The zombies surge forward attacking you, They chew on your head and you are dead.")
        print("\n")
        back5()
    elif ans1.upper() == "R" or ans1.upper() == "RIGHT":
        time.sleep(2)
        print("You reach the stairwell and open the door:") 
        time.sleep(2)
        print("As you step into the stairwell you hear a noise upstairs.")
        print("\n")
        print("\n")
        start_stairs()
    else:
        print("Did not undersand input,please try again")
        stairs_lift()        


def bk_st_door():
    time.sleep(1)
    print("\n")
    bk1 = input("You chose door 1. You enter and find NOTHING just a radio playing. Go back? (Y/N) :  ?")
    if bk1.upper() == "Y" or bk1.upper() == "YES":
        door_choice()      
    elif bk1.upper() == "N" or bk1.upper() == "NO":
        time.sleep(1)
        print("\n")
        print("Well you cant just stay here all day!")
        stairs_lift()
    else:
         print("Did not undersand input,please try again")
         bk_st_door()


def weapon_choice():
    time.sleep(2)
    print("\n")
    print("The street is destroyed! Rubbish, abandoned cars and body parts litter the street")
    print("\n")
    time.sleep(2)
    print("As you walk across the car park you spot an open box with a variety of weapons :\
    \n 1 : Knife,\
    \n 2 : Axe,\
    \n 3 : Saw\
    \n 4 : Machete.")
    time.sleep(2)
    print("\n")
    print("Which one do you choose?")
    w_list = (input("please enter your choice:"))
    if w_list == "1":
        print("\n")
        print("You chose the Knife")
        print("\n")
        car_park()
    elif w_list == "2":
        print("\n")
        print("You chose the axe")
        print("\n")
        car_park()
    elif w_list == "3":
        print("\n")
        print("You chose the saw")
        print("\n")
        car_park()
    elif w_list == "4":
        print("\n")
        print("You chose the machete")
        print("\n")
        car_park()
    else:
        print("\n")
        print("Please input a valid choice")
        weapon_choice()
        print("\n")


def walk_choice():
    choice = int(input("Please enter your choice:"))
    if choice == (1):
            start_city()
    elif choice == (2):
            start_park()
    else:
        print("Did not understand input,please try again")
        walk_choice()


def door_choice():
    print("\n")
    print("You go down the stairs and reach the bottom, there are 3 doors:")
    print("\n")
    time.sleep(2)
    print("Door 1 has no sign, but there is a muffled voice coming from inside")
    print("\n")
    time.sleep(2)
    print("Door 2 is labelled: 'To Wards A-G'")
    print("\n")
    time.sleep(2)
    print("Door 3 is labelled EXIT")
    print("\n")
    time.sleep(2)
    ans3 = input("Which door are you going to take? Door  : ")
    print("\n")
    if ans3 == "1":
        bk_st_door()
    elif ans3 == "2": 
        time.sleep(1)
        print("\n")
        print("You make your way through the door into a silent corridor. You stare in disbelief as the door slams shut behind you")
        weapon_choice1()
    elif ans3 == "3":
        time.sleep(1)
        print("\n")
        print("You make your way through the exit and stare in disbelief as the door slams shut behind you")
        weapon_choice()
    else:
        print("Did not undersand input,please try again")
        door_choice()


stairs_lift()
start_stairs()



    

