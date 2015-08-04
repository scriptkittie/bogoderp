import random
import sys

bogoderp_list = list()
userinput = ""

def printList():
    for userinput in bogoderp_list:
        bogo_list_item = userinput + '\n'
        print bogo_list_item
    
def bogoderp():
    random.shuffle(bogoderp_list)
    
def checksort():
    length_of_list = len(bogoderp_list)
    length_of_list = length_of_list -1
    for position in range (length_of_list):
        current_item = bogoderp_list[position]
        item_after_current = bogoderp_list[position+1]
        if current_item  < item_after_current:
            continue
        else:
            print "The bogo gone derped.\n Let's try again."
            bogoderp()
            checksort()
    
    return "List is sorted"
    
def addList(userinput):
    bogoderp_list.append(userinput)
    while(True):
        userinput = raw_input("Enter your item you want added to the list: ")
        bogoderp_list.append(userinput)
        userinput = raw_input("Would you like to add another item to the list?")
        if userinput == "yes" or userinput == "Yes" or userinput == "Y" or userinput == "y":
            continue
        else:
            bogoderp()
            print checksort()
            printList()
            print "Thanks for playing. :^)"
            sys.exit
            break

    
def main():
    
    """
    Welcome to Bogoderp, where we implement bogosort because reasons.   
    
    Feel free to enter a list of items and bogosort will randomly sort them out, hoepfully
    it will sort it out to what we assign it to.  If it doesn't, bogosort it again, or 
    I don't know, get some coffee.
    
    """
    userinput = raw_input("Welcome to Bogoderp, plaese enter your first item to be stored for random sorting.\n >")
    addList(userinput)
    
    while(True):
        user_choice = "Would you like to make another list? \n >"
        if userinput == "yes" or userinput == "Yes" or userinput == "Y" or userinput == "y":
            main()
        else:
            sys.exit

main()