#                                       ----------------------------------------------------------------------------------
#                                                                       Jungle Game
#                                       ----------------------------------------------------------------------------------
def Jungle_Game():
    print(''' Piyush, the adventure boy, who was traveling alone to reach his destination,
        the waterfall, in the Amazon jungle, got lost after traveling 150 kilometers.
        Now, you need to guide him and help him reach his destination.
        Piyush has two paths ahead of him: left and right. Now, you must guide him, as his life is in your hands.''')
    print("RULES","\n","for left=1","\n","right=2")
    print("lets gooooooooooooooo..............")
    n=int(input("(1) for LEFT OR (2) for RIGHT--->"))
    if n==1:
        print("After walking for a while, two paths appeared.")
        n1=int(input("left(1) or right(2)"))
        if n1==1:
            print("there is river with crocodile")
            print("GAME OVER")
        elif n1==2:
            print("Oh no, there's a tiger in front and it's coming towards you!")
            print("GAME OVER")
    elif n==2:
        print("After walking for a while, two paths appeared.")
        m=int(input("left (1) and right (2)"))
        if m==1: 
            print("Ooops, game over!")
        elif m==2:
            print("The Amazon jungle is so complicated, and then again, two paths appeared.")
            print("An unknown person is coming towards me.")
            print("He is asking me if I need help.")
            m2=int(input("1 for help or 2 for not help"))
            if m2==1:
                print("I can hear something, and oh my God, it's the sound of a waterfall!")
                print("Piyush has reached his destination.")
                print("won the game!")
            elif m2==2:
                print("Let's go ahead, let's go!")
    else:
        print("hello")
Jungle_Game()