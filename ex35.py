from sys import exit
#Didn't follow prompt exactly felt like there were changes i made that made this code easier for someone if they didnt have the book infront of them

def gold_room():
    print("This room is full of hundreds of gold bars. How much do you take?")
    
    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
        #If input contains 0 or 1 continue with converting number into integer 
    else:
        dead("Man, learn to type a number.")
        
    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    # if how much is less than 50 
    else:
        dead("You greedy bastard! You")
        #if more than 50 you "die"

def bear_room():
    #display setup for the bears room
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move to the bear?")
    print("Do you take honey or taunt bear")
    bear_moved = False
    #tarcking bears movement 
    
    while True:
        choice = input("> ")
        #user input choice
        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
            # if the user takes honey this will happen
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can now open door.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            #opens door after bear moves. (go to gold room)
            gold_room()
        else:
            print("I got no idea what that means.")
            #if you type a command that isn't right let them know
    
def cthulu_room():
    print(" Here you see the great evil Cthulu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do yuou flee for your life or eat your head?")
    
    choice = input("> ")
    
    if "flee" in choice:
        start()
        #if you use the flee function start
    elif "head" in choice:
        dead("Well that was tasty!")
        #if you chose head you die
    else:
        cthulu_room()
    
def dead(why):
    print(why, "Good job!")
    exit(0)
    
def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("which one do you take?")
    
    choice = input("> ")
    
    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulu_room()
        
    else:
        dead("You stumble around the room until you starve.")
        
start()
    
            