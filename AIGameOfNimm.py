#https://codeinplace.stanford.edu/cip3/share/QSbYhcdWSu1fF3hnTkgN

import random

def main():
    """
    The AI Game of Nimm, play with Karel.
    
    Strategy: Karel choose the random number of 1, 2 or 3, the code 
    structure and while condition are clear, take care of the last
    1, 2 or 3 stones is the key to solve the challenge. Be careful,
    beat Karel is not easy.
    Learning Note: always watch the random number where the variable 
    is live.
    """
    a = 0
    b = 2
    d = 1
    c = 20
    message1 = str("Karel would you like to remove 1, 2 or 3 stones? ")
    message2 = str("Player would you like to remove 1, 2 or 3 stones? ")
    message3 = str("Please enter 1, 2 or 3: ")
    
    print("There are " + str(c) + " stones left.")
    
    while c >= 4:
        # Karel removes stones.
        a = random.randint(1, 3)
        print(message1, a)
        c -= a
        print(" ")
        print("There are " + str(c) + " stones left.")
        
        # Player removes stones. 
        # Check the c value if there is only 1, 2 or none stone left.
        b = int(input(message2)) 
        if 0 < b < 4:
            c -= b
            if c <= 0:
                announce_the_winner1()
            elif c == 1:
                print(" ")
                print("There are " + str(c) + " stones left.")
                a = random.randint(1, 3)
                print(message1, a)
                c -= a
                announce_the_winner2()
            else:
                print(" ")
                print("There are " + str(c) + " stones left.")
        else:
            d = int(input(message3))
            if 0 < d < 4:
                c -= d
                if c <= 0: 
                    announce_the_winner1()
                elif c == 1:
                    print(" ")
                    print("There are " + str(c) + " stones left.")
                    a = random.randint(1, 3)
                    print(message1, a)
                    c -= a
                    announce_the_winner2()
                else:
                    print(" ")
                    print("There are " + str(c) + " stones left.")
            else:
                while not 0 < d < 4:
                    d = int(input(message3))
                c-= d
                if c <= 0:
                    announce_the_winner1()
                elif c == 1:
                    print(" ")
                    print("There are " + str(c) + " stones left.")
                    a = random.randint(1, 3)
                    print(message1, a)
                    c -= a
                    announce_the_winner2()
                else:
                    print(" ")
                    print("There are " + str(c) + " stones left.")
                    
     # Take care of the last 1, 2 or 3 stones if some left after loop.
    if 0 < c <= 3:
        a = random.randint(1, 3)
        print(message1, a)
        c -= a
        if c <= 0:
            announce_the_winner2()
        elif c == 1:
            print(" ")
            print("There are " + str(c) + " stones left.")
            b = int(input(message2)) 
            c -= b
            announce_the_winner1()
        else:
            print(" ")
            print("There are " + str(c) + " stones left.")
            b = int(input(message2)) 
            if 0 < b < 4:
                c -= b
                if c <= 0:
                    announce_the_winner1()
                else:
                    print(" ")
                    print("There are " + str(c) + " stones left.")
                    a = random.randint(1, 3)
                    print(message1, a)
                    announce_the_winner2()


def announce_the_winner1():
    print(" ")
    print("Game over\n")
    print("Karel wins")
    
def announce_the_winner2():
    print(" ")
    print("Game over\n")
    print("Player wins")

if __name__ == '__main__':
    main()