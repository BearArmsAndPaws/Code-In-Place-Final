# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 20:55:54 2024

@author: FatCat
"""
#I swear, there are so many things here that i could have just made into a function but it's too late and i don't feel like undoing all the work i did cause I'm lazy 😒


import random
#sets all the nessecary global functions
global name
global the_pronouns
global villian_pronouns
global villian_name
global protag_fight_health
global vil_fight_health
global fight_helper


def battle():
    global protect_amount
    global vil_fight_health
    player_attack_amount = 1
    global player_damage
    player_damage = play_dam
    global protag_fight_health
    def find_damage():
        global player_damage
        player_damage = play_dam
        #checks to see if the help buffs that the player received can come in check now
        helps = player_attack_amount % fight_helper[1]
        if helps == 0:
            player_damage
            add = player_damage*fight_helper[0]
            player_damage += add
    #keeps the battle going until either the player looses or wins
    while protag_fight_health != 0 or vil_fight_health != 0:
        if protag_fight_health <= 0:
            print("\nYou lost!")
            global win
            win = False
            break
        if vil_fight_health <= 0:
            win = True
            print("\nYou won!\n")
            
            break
        #Lists the player's health
        print("Your health:",protag_fight_health,"\n"+str(fight_name[1])+"'s health:",vil_fight_health,"\nProtects Left:",protect_amount)
        #gives player their options
        player_move = input("\nWould you like to attack or protect yourself? ").lower()
        #makes sure that players only pick the deisginated options
        while player_move != "attack" and  player_move != "protect":
            player_move = input("Please type either attack, protect.\n")
        #what happens when the player chooses attack
            #randomly chooses an integer to find how the villan will react
        if player_move == "attack":
            vil_move = random.randint(1,30)
            #if the integer to less than 8, the villian will not do anything
            if vil_move < fight_stats[0]:
                find_damage()
                #Informs the player of how the villian reacted
                print("\n" + str(fight_name[0]),fight_name[1],"did not protect "+str(fight_pronouns[2])+"self or fight back!")
                print("\nYou've done" ,player_damage,"damage!")
                #updates the healths 
                vil_fight_health -= player_damage
                player_attack_amount += 1 
                player_damage = play_dam
            elif vil_move < fight_stats[1]+1 and vil_move > fight_stats[0] - 1:
                find_damage()
                vil_dam = random.randint(fight_stats[3],fight_stats[2])
                print("\n" + str(fight_name[0]),fight_name[1],"fought back!")
                print("\nYou've done" ,player_damage,"damage, but",fight_name[0],fight_name[1],"did", vil_dam, "damage!")
                vil_fight_health -= player_damage
                protag_fight_health -= vil_dam
                player_attack_amount += 1 
            elif vil_move <= 30 and vil_move > fight_stats[1]:
                print("\n"+str(fight_name[0]),fight_name[1],"protected " + str(fight_pronouns[2])+"self!")
                print("\nYou've done no damage!")
        if player_move == "protect":
            
            vil_move = random.randint(1,30)
            if protect_amount == 0:
                while player_move == "protect":
                    player_move = input("You've run out of protects, you may only attack now. Type okay to continue.\n").lower()
            elif vil_move < fight_stats[1]:
                vil_dam = random.randint(fight_stats[3],fight_stats[2])
                print("\n"+str(fight_name[0]),fight_name[1],"attacked and", villian_pronouns[3], "attack rebounded!")
                print("\n"+str(fight_pronouns[0]).title()+" accidentally did", vil_dam,"damage to "+str(fight_pronouns[2]+"self!"))
                vil_fight_health -= vil_dam
            else:
                print("\n"+str(fight_name[0]),fight_name[1],"did not attack!")
                
            protect_amount -= 1
            if protect_amount == -1:
                protect_amount = 0
            


def Marx_battle ():
    
    global protag_fight_health
    protag_fight_health = 170
    global fight_name
    fight_name = villian_name
    global fight_pronouns
    fight_pronouns = villian_pronouns
    global play_dam
    play_dam = star_dam
    global fight_stats
    fight_stats = [6, 25, 40, 30]
    global protect_amount
    protect_amount = 6
    global vil_fight_health
    vil_fight_health = 400
    print("'Uh huh?' " , villian_pronouns[0], "says, sorta confused.")
    input()
    print("'And you're here to?'")
    input()
    print("'Take my revenge.' you say firmly.")
    input()
    print("'Oooh. Oh ho ho, alright, this will be fun,' " , villian_pronouns[0], "laughs.")
    input()
    print(villian_pronouns[3].title(), "group advances as backup, but", villian_pronouns[0], 'waves them away.')
    input()
    print("'Stand down guys, let's make this an even fight.'")
    input()
    if fight_helper[0] == 2:
        print("You draw your cool sword, glowering.")
        input()
        print("'Heh, nice swoord~,' Marx says, amused.")
        input()
        
    elif fight_helper[0] == 0.25:
        print("Your litte anteater buddy is worried, and hides behind your legs.")
        input()
        print("'Is that little loser supposed to help you fight?' Marx asks, mildly annoyed.")
        input()
        print("Anteater-buddy stops hiding after hearing this and yelps at Marx, as ready to fight as you are.")
    
        
        
    print(villian_pronouns[0].title(), "pulls out" , villian_pronouns[3], "giant steel sword studded with gems that shines with every swing.")
    input()  
    input()
    input()
    input()
    input()
    print("'Let's dance'.")
    input()
    battle()
    if win == True:
        print("Marx stubbles a bit before collapsing.")
        input()
        print("You made a deep cut, " + villian_pronouns[0] +"'s hurt bad.")
        input()
        input("You walk to Marx, victorious sword still in hand.\n")
        print("'hahA!'", villian_name[0], "laughs. 'Go on. DO IT. You know you want to.'")
        input()
        if fight_helper[0] == 0.25:
          print("Anteater-buddy crawls over to Marx's face and scratches" , villian_pronouns[3], "face, causing Marx to wince.") 
          input()
          print("'See, even the dumb anteater wants to do it. What's stopping you?'")
          input()
        print("'Do it.'")
        input()
        spare_rev = input("Do you want to spare Marx or finish the job? \nType spare or finish: ").lower()
        while spare_rev != "spare" and spare_rev != "finish":
            spare_rev = input("Please only type spare or finish: ")
        if spare_rev == "spare":
            print("'You're a monster, you know that?' you say, angrily.")
            input()
            input()
            input()
            print("'But I'm not...'")
            input()
            print("You toss your sword to the side and watch it tumble before returning your focus to Marx.")
            input()
            print("'I'm not you, " + str(villian_name[0]) +". But if I ever find out you burnt another village like you did mine, I'll be coming for you again.")
            input()
            if fight_helper[0] == 0.25:
                print("Anteater-buddy spits in Marx's face, before trotting next to you.")
            print("'Goodbye, Marx. Live, knowing you were beaten by one of your victims, live knowing the only reason you do so is because I chose to let you. Live in shame.'")
            input()
            print("You grab your sword and return it to its sheath, before walking away, oddly satisfied.")
            input()
            print("You hear Marx's pained breathing, and a few of" , villian_pronouns[3], "gang rushing towards you, but", villian_pronouns[0], "calls out to them and tells them to leave it.")
            input()
            print("'I respect the hell out of " + str(the_pronouns[2]) +", you hear Marx say, as you leave." )
            input()
            input()
            input()
            input()
            input()
            input()
            input()
            print("Merciful Ending")
        elif spare_rev == "finish":
            print("You slice Marx's wound one more time, causing", villian_pronouns[3], "to inhale sharply.")
            input()
            print("'You deserve this, " + villian_name[0] +"', you say, looking down at Marx.")
            input()
            print("Marx laughs. 'You're no better than me,'" , villian_pronouns[0],"says, as", villian_pronouns[0] ,"winces in pain.")
            input()
            print("'Leave " + str(the_pronouns[2]) + ", guys,' Marx says. 'I'm impressed.'")
            input()
            if fight_helper[0] == 0.25:
                print("Anteater-buddy makes an odd sound, a mix between laughter and distain before trotting up to you.")
                input()
            
            print("You leave, feeling satisfied, feeling happy, as you hear Marx stop breathing.")
            input()
            input()
            input()
            input()
            input()
            input()
            input()
            print("Vengeful Ending")
    elif win == False:
        print("You died lolz")
        input()
        try_again = input("Would you like to restart the battle?").lower()
        if try_again == "yes" or try_again == "y":
            battle()
        elif try_again == "no" or try_again == "n":
            try_again = input("Would you like to restart the story?").lower()
            if try_again == "yes" or try_again == "y":
                Starstruck()
            else:
                print("Thanks for playing! Bye.")
    
    
    
def clues_analysis():
    useless_clues = ["Drawing", "Coat", "List", "Torch", "Pouch", "Backpack", "Gold"]
    useless_clues_collected = []
    important_clues = ["Snackbag", "Bill", "Map", "Sword", "Letter", "Ring", "Wood", "Food", "Fabric", ]
    for i in range(len(useless_clues)):
        if useless_clues[i] in clues:
            useless_clues_collected.append(useless_clues[i])
            
            
            
            
    if important_clues[0] and important_clues[1] and important_clues[2] in clues:
        
        print("'Hometown?' you think, reading the snackbag. 'That must mean Marx is Woiseqinonen.' ")
        input()
        print("You sit around a bit trying to think about Woiseqinonen traditions.")
        input()
        print("You know that they have to make a pilgrimage once in their lifetime to find riches and glory.")
        input()
        print("But you're not sure what direction.")
        input()
        print("You pick up the bill, you know they might be going Renifor now.")
        input()
        print("You look at the map, you find your village with your finger, wander it to the village you're in right now, then to Renifor.")
        input()
        print("Your finger goes in an interesting pattern that looks like this: ")
        input()
        print("       x   <-- Your village was here                                                 ")
        print("        x                                                                            ")
        print("         x                                                                           ")
        print("          x                                                                          ")
        print("           x                                                                         ")
        print("            x                                                                        ")
        print("             x                                                                       ")
        print("              x                                                                      ")
        print("               x                                                                     ")
        print("                x                                                                    ")
        print("                 x                                                                   ")
        print("                  x                                                                  ")
        print("                   x                                                                 ")
        print("                    x                                                                ")
        print("                     x                                                               ")
        print("                      x                                                              ")
        print("                       x                                                             ")
        print("                        x                                                            ")
        print("                         x                                                           ")
        print("                          x                                                          ")
        print("                           x                                                         ")
        print("                            x                                                        ")
        print("                             x                                                       ")
        print("                              x                                                      ")
        print("                               x                                                     ")
        print("                                x                                                    ")
        print("                                 x                                                   ")
        print("                                  x                                                  ")
        print("                                   x                                                 ")
        print("                                    x                                                ")
        print("                                     x                                               ")
        print("                                      x                                              ")
        print("                                       x                                             ")
        print("                                        x                                            ")
        print("                                         x   <-- You are here                        ")
        print("                                        x                                            ")
        print("                                       x                                             ")
        print("                                      x                                              ")
        print("                                     x                                               ")
        print("                                    x                                                ")
        print("                                   x                                                 ")
        print("                                  x                                                  ")
        print("                                 x                                                   ")
        print("                                x                                                    ")
        print("                               x                                                     ")
        print("                              x                                                      ")
        print("                             x <-- Renifor is here                                   ")
        
        
        Marx_battle()
        
def clue_collections():
    buildings_explored = 0
    bookstore = False
    farm = False
    cottage = False
    bookshelf = False
    kitchen = 0
    dining_room = 0
    living_room = 0
    bathroom = 0
    crops = 0
    barn = 0
    shed = 0
    storage = 0
    inventory = 11
    global clues 
    clues = []  
    while buildings_explored < 3 or bookstore != True or farm != True or cottage != True:
        
        
        print("Inventory left: ", inventory)
        building = int(input("Do you want to go to \n1. A bookstore \n2. A small farm \n3. A small cottage \n"))
        while building != 1 and building != 2 and building != 3 :
            
            building = int(input("Chose a number from 1 to 3: "))
        if building == 1:
                print("The bookstore has been selected.")
                input()
            
                while bookshelf != 1 or bathroom != 1 or storage != 1:
                    
                    print("What do you want to search? \n1. The bookshelves \n2. The bathrooms\n3. The storage room")
                    search = int(input())
                    while search != 1 and search != 2 and search != 3:
                        search = int(input("Chose a number from 1 to 3: "))
                    if search == 1:
                        bookshelf = 1
                        print("You scour the bookshelves for any hint of where Marx could have gone.")
                        input()
                        print("All the books are either burnt behond recognition or have an obscene amount of smoke damage. ")
                        input()
                        print("But you do find something: on the floor right next to the bookshelves, you find a small snack bag labeled 'Marx's hometown frominge.'")
                        input()
                        print("Frominge is a snack from the North, particularly Woiseqino, a place obsessed with traditions. ")
                        input()
                        print("I wonder...")
                        input()
                        #I really should have made the following code a function -_-
                        dis_keep = input("Would you like to discard or keep the clue? ").lower()
                        while dis_keep != "keep" and dis_keep != "discard":
                            dis_keep = input("Please type keep or discard: ")
                        while dis_keep != "keep" and dis_keep != "discard":
                            dis_keep = input("Please type keep or discard: ")
                        if dis_keep == "keep":
                            
                            if inventory == 0:
                                if "Snackbag" in clues:
                                    pass
                                else:
                                    print("You have a full inventory, if you want to keep this, you must discard something from your inventory.")
                                    input("Press enter to see your inventory: ")
                                    print(clues)
                                    dis_keep = input("Do you want to keep or discard this object? ").lower()
                                    while dis_keep != "keep" and dis_keep != "discard":
                                        dis_keep = input("Please type keep or discard: ")
                                    if dis_keep == "keep":
                                        discard = input("Type the object you want to discard from your inventory: ").title()
                                        while discard not in clues:
                                            discard = input("This object is not in your inventory, check if you spelled it correctly.").title()
                                        if discard in clues:
                                            clues = list(map(lambda x: x.replace(discard, 'Snackbag'), clues))
                                        else:
                                            pass
                            else:
                                if "Snackbag" in clues:
                                    pass
                                else:
                                    clues.append("Snackbag")
                                    inventory -= 1
                        else:
                            pass
                    elif search == 2:
                        bathroom = 1
                        print("You walk into the bathrooms, there's ash and soot everywhere, a bit of rubble in front of a stall, and a half burnt mirror on the floor.")
                        input()
                        print("Oh dear.")
                        input()
                        print("You find an arm on the floor, is it human, is it fake? You don't know, because you kick it away.")
                        input()
                        print("Good thing you did, because underneath it was a small bill.")
                        input()
                        print("A bill for Renifor, a city down south.")
                        input()
                        print("You also find a burnt drawing, most likely done by a child...")
                        input()
                        dis_keep  = input("Do you want to keep or discard the bill? ").lower()
                        while dis_keep != "keep" and dis_keep != "discard":
                            dis_keep = input("Please type keep or discard: ")
                        if dis_keep == "keep":
                            
                            if inventory == 0:
                                if "Bill" in clues:
                                    pass
                                else:
                                    print("You have a full inventory, if you want to keep this, you must discard something from your inventory.")
                                    input("Press enter to see your inventory: ")
                                    print(clues)
                                    dis_keep = input("Do you want to keep or discard this object? ").lower()
                                    while dis_keep != "keep" and dis_keep != "discard":
                                        dis_keep = input("Please type keep or discard: ")
                                    if dis_keep == "keep":
                                        discard = input("Type the object you want to discard from your inventory: ").title()
                                        while discard not in clues:
                                            discard = input("This object is not in your inventory, check if you spelled it correctly.").title()
                                        if discard in clues:
                                            clues = list(map(lambda x: x.replace(discard, 'Bill'), clues))
                                    else:
                                            pass
                            else:
                                if "Bill" in clues:
                                    pass
                                else:
                                    clues.append("Bill")
                                    inventory -= 1
                        else:
                            pass
                        dis_keep  = input("Do you want to keep or discard the drawing? ").lower()
                        while dis_keep != "keep" and dis_keep != "discard":
                            dis_keep = input("Please type keep or discard: ")
                        if dis_keep == "keep":
                            
                            if inventory == 0:
                                if "Drawing" in clues:
                                    pass
                                else:
                                    print("You have a full inventory, if you want to keep this, you must discard something from your inventory.")
                                    input("Press enter to see your inventory: ")
                                    print(clues)
                                    dis_keep = input("Do you want to keep or discard this object? ").lower()
                                    while dis_keep != "keep" and dis_keep != "discard":
                                        dis_keep = input("Please type keep or discard: ")
                                    if dis_keep == "keep":
                                        discard = input("Type the object you want to discard from your inventory: ").title()
                                        while discard not in clues:
                                            discard = input("This object is not in your inventory, check if you spelled it correctly. ").title()
                                        if discard in clues:
                                            clues = list(map(lambda x: x.replace(discard, 'Drawing'), clues))
                                        else:
                                            pass
                            else:
                                if "Drawing" in clues:
                                    pass
                                else:
                                    clues.append("Drawing")
                                    inventory -= 1
                        else:
                            pass
                    elif search == 3:
                        storage = 1
                        print("The storage room is thick with smog.")
                        input()
                        print("You grab a stone on the floor and chuck it at a locker.")
                        input()
                        print("The stone doesn't dent it, but it does fall near something that catches your eye.")
                        input()
                        print("A small map labeled 'Bookstores across the country'.")
                        input()
                        print("It could be used for something besides bookshelves. ")
                        input()
                        dis_keep  = input("Do you want to keep or discard the map? ").lower()
                        while dis_keep != "keep" and dis_keep != "discard":
                            dis_keep = input("Please type keep or discard: ")
                        if dis_keep == "keep":
                            
                            if inventory == 0:
                                if "Map" in clues:
                                    pass
                                else:
                                    print("You have a full inventory, if you want to keep this, you must discard something from your inventory.")
                                    input("Press enter to see your inventory: ")
                                    print(clues)
                                    dis_keep = input("Do you want to keep or discard this object? ").lower()
                                    while dis_keep != "keep" and dis_keep != "discard":
                                        dis_keep = input("Please type keep or discard: ")
                                    if dis_keep == "keep":
                                        discard = input("Type the object you want to discard from your inventory: ").title()
                                        while discard not in clues:
                                            discard = input("This object is not in your inventory, check if you spelled it correctly. ").title()
                                        if discard in clues:
                                            clues = list(map(lambda x: x.replace(discard, 'Map'), clues))
                                        else:
                                            pass
                            else:
                                if "Map" in clues:
                                    pass
                                else:
                                    clues.append("Map")
                                    inventory -= 1
                    
                        bookstore = True
                        buildings_explored += 1
                    
        elif building == 2:
            print("The farm has been selected.")         
            input()

            while crops != 1 or barn != 1 or shed != 1:
                print("What do you want to search? \n1. The crops \n2. The barn\n3. The shed")
                search = int(input())
                while search != 1 and search != 2 and search != 3:
                    search = int(input("Chose a number from 1 to 3: "))
                if search == 1:
                    crops = 1
                    print("The crops are a thick black and disintegrate everytime you take a step.")
                    input()
                    print("*THUNK*, you step on something uncrunchy, un-plantlike.")
                    input()
                    print("You kick the dead ears of corn away and find a surprisingly big sword.")
                    input()
                    print("You can pick it up, but it's far too big for you to properly wield it.")
                    input()
                    print("It probably belonged to Marx's group.")
                    input()
                    print("You keep walking a find a crumpled letter, you can hardly make out the words, but you see something that looks like Marx.")
                    input()
                    dis_keep  = input("Do you want to keep or discard the sword? ").lower()
                    while dis_keep != "keep" and dis_keep != "discard":
                        dis_keep = input("Please type keep or discard: ")
                    if dis_keep == "keep":
                        
                        if inventory == 0:
                            if "Sword" in clues:
                                pass
                            else:
                                print("You have a full inventory, if you want to keep this, you must discard something from your inventory.")
                                input("Press enter to see your inventory: ")
                                print(clues)
                                dis_keep = input("Do you want to keep or discard this object? ").lower()
                                while dis_keep != "keep" and dis_keep != "discard":
                                    dis_keep = input("Please type keep or discard: ")
                                if dis_keep == "keep":
                                    discard = input("Type the object you want to discard from your inventory: ").title()
                                    while discard not in clues:
                                        discard = input("This object is not in your inventory, check if you spelled it correctly.").title()
                                    if discard in clues:
                                        clues = list(map(lambda x: x.replace(discard, 'Sword'), clues))
                                else:
                                        pass
                        else:
                            if "Sword" in clues:
                                pass
                            else:
                                clues.append("Sword")
                                inventory -= 1
                    else:
                        pass
                    dis_keep  = input("Do you want to keep or discard the letter? ").lower()
                    while dis_keep != "keep" and dis_keep != "discard":
                        dis_keep = input("Please type keep or discard: ")
                    if dis_keep == "keep":
                        
                        if inventory == 0:
                            if "Letter" in clues:
                                pass
                            else:
                                print("You have a full inventory, if you want to keep this, you must discard something from your inventory.")
                                input("Press enter to see your inventory: ")
                                print(clues)
                                dis_keep = input("Do you want to keep or discard this object? ").lower()
                                while dis_keep != "keep" and dis_keep != "discard":
                                    dis_keep = input("Please type keep or discard: ")
                                while dis_keep != "keep" and dis_keep != "discard":
                                    dis_keep = input("Please type keep or discard: ")
                                if dis_keep == "keep":
                                    discard = input("Type the object you want to discard from your inventory: ").title()
                                    while discard not in clues:
                                        discard = input("This object is not in your inventory, check if you spelled it correctly. ").title()
                                    if discard in clues:
                                        clues = list(map(lambda x: x.replace(discard, 'Letter'), clues))
                                    else:
                                        pass
                        else:
                            if "Letter" in clues:
                                pass
                            else:
                                clues.append("Letter")
                                inventory -= 1
                    else:
                        pass
                elif search == 2:
                    barn = 1
                    print("The barns reek of cow, bird, and another unknown animal.")
                    input()
                    print("But it also smells like barbeque. 'Would it be messed up to think yum?' you  wonder.")
                    input()
                    print("You kick dust and burnt milk around, all you find is a farmer's coat.")
                    input()
                    print("You look around a bit more, and find a paper.")
                    input()
                    print("The paper looks like a long list of items.")
                    input()
                    print("In your haste you make out the letter 'M'.")
                    input()
                    dis_keep  = input("Do you want to keep or discard the coat? ").lower()
                    while dis_keep != "keep" and dis_keep != "discard":
                        dis_keep = input("Please type keep or discard: ")
                    if dis_keep == "keep":
        
                        if inventory == 0:
                            if "Coat" in clues:
                                pass
                            else:
                                print("You have a full inventory, if you want to keep this, you must discard something from your inventory.")
                                input("Press enter to see your inventory: ")
                                print(clues)
                                dis_keep = input("Do you want to keep or discard this object? ").lower()
                                while dis_keep != "keep" and dis_keep != "discard":
                                    dis_keep = input("Please type keep or discard: ")
                                if dis_keep == "keep":
                                    discard = input("Type the object you want to discard from your inventory: ").title()
                                    while discard not in clues:
                                        discard = input("This object is not in your inventory, check if you spelled it correctly.").title()
                                    if discard in clues:
                                        clues = list(map(lambda x: x.replace(discard, 'Coat'), clues))
                                else:
                                        pass
                        else:
                            if "Coat" in clues:
                                pass
                            else:
                                clues.append("Coat")
                                inventory -= 1
                    else:
                        pass
                    dis_keep  = input("Do you want to keep or discard the list? ").lower()
                    while dis_keep != "keep" and dis_keep != "discard":
                        dis_keep = input("Please type keep or discard: ")
                    if dis_keep == "keep":
                        
                        if inventory == 0:
                            if "List" in clues:
                                pass
                            else:
                                print("You have a full inventory, if you want to keep this, you must discard something from your inventory.")
                                input("Press enter to see your inventory: ")
                                print(clues)
                                dis_keep = input("Do you want to keep or discard this object? ").lower()
                                while dis_keep != "keep" and dis_keep != "discard":
                                    dis_keep = input("Please type keep or discard: ")
                                if dis_keep == "keep":
                                    discard = input("Type the object you want to discard from your inventory: ").title()
                                    while discard not in clues:
                                        discard = input("This object is not in your inventory, check if you spelled it correctly. ").title()
                                    if discard in clues:
                                        clues = list(map(lambda x: x.replace(discard, 'List'), clues))
                                    else:
                                        pass
                        else:
                            if "List" in clues:
                                pass
                            else:
                                clues.append("List")
                                inventory -= 1
                    else:
                        pass
                    
                elif search == 3:
                    shed = 1
                    print("The shed's roof collapses right before you step in.")
                    input()
                    print("You throw some of the fallen boards outside so you have a place to step on.")
                    input()
                    print("Under one of the boards you threw out is a half-burnt torch.")
                    input()
                    print("It must be one of the torches that Marx's group used.")
                    input()
                    print("How it didn't burn down the shed, you'll never know.")
                    input()
                    print("You check the shelves and find a very expensive-looking ring made out of jade.")
                    input()
                    print("You inspect it a little bit more closly and find a custom engravement of a torch and sycle.")
                    input()
                    print("It might have belonged the Marx's group.")
                    input()
                    dis_keep  = input("Do you want to keep or discard the torch? ").lower()
                    while dis_keep != "keep" and dis_keep != "discard":
                        dis_keep = input("Please type keep or discard: ")
                    if dis_keep == "keep":
                        
                        if inventory == 0:
                            if "Torch" in clues:
                                pass
                            else:
                                print("You have a full inventory, if you want to keep this, you must discard something from your inventory.")
                                input("Press enter to see your inventory: ")
                                print(clues)
                                dis_keep = input("Do you want to keep or discard this object? ").lower()
                                while dis_keep != "keep" and dis_keep != "discard":
                                    dis_keep = input("Please type keep or discard: ")
                                if dis_keep == "keep":
                                    discard = input("Type the object you want to discard from your inventory: ").title()
                                    while discard not in clues:
                                        discard = input("This object is not in your inventory, check if you spelled it correctly.").title()
                                    if discard in clues:
                                        clues = list(map(lambda x: x.replace(discard, 'Torch'), clues))
                                else:
                                        pass
                        else:
                            if "Torch" in clues:
                                pass
                            else:
                                clues.append("Torch")
                                inventory -= 1
                    else:
                        pass
                    dis_keep  = input("Do you want to keep or discard the ring? ").lower()
                    while dis_keep != "keep" and dis_keep != "discard":
                        dis_keep = input("Please type keep or discard: ")
                    if dis_keep == "keep":
                        
                        if inventory == 0:
                            if "Ring" in clues:
                                pass
                            else:
                                print("You have a full inventory, if you want to keep this, you must discard something from your inventory.")
                                input("Press enter to see your inventory: ")
                                print(clues)
                                dis_keep = input("Do you want to keep or discard this object? ").lower()
                                while dis_keep != "keep" and dis_keep != "discard":
                                    dis_keep = input("Please type keep or discard: ")
                                if dis_keep == "keep":
                                    discard = input("Type the object you want to discard from your inventory: ").title()
                                    while discard not in clues:
                                        discard = input("This object is not in your inventory, check if you spelled it correctly. ").title()
                                    if discard in clues:
                                        clues = list(map(lambda x: x.replace(discard, 'Ring'), clues))
                                    else:
                                        pass
                        else:
                            if "Ring" in clues:
                                pass
                            else:
                                clues.append("Ring")
                                inventory -= 1
                    else:
                        pass
            farm = True
            buildings_explored += 1
       
        elif building == 3:
            print("The cottage has been selected.")
            input()
            while kitchen != 1 or dining_room != 1 or living_room != 1:
                print("What do you want to search? \n1. The kitchen \n2. The dining room\n3. The living room")
                search = int(input())
                while search != 1 and search != 2 and search != 3:
                    search = int(input("Chose a number from 1 to 3: "))
                if search == 1:
                        kitchen = 1
                        print("SUper duper totally awesome pouch of money")
                        input()
                        print("Super duper totally awesome burnt piece of wood. is a wood that does well trading")
                        input()
                        dis_keep  = input("Do you want to keep or discard the pouch of money? ").lower()
                        while dis_keep != "keep" and dis_keep != "discard":
                            dis_keep = input("Please type keep or discard: ")
                        if dis_keep == "keep":
                            
                            if inventory == 0:
                                if "Pouch" in clues:
                                    pass
                                else:
                                    print("You have a full inventory, if you want to keep this, you must discard something from your inventory.")
                                    input("Press enter to see your inventory: ")
                                    print(clues)
                                    dis_keep = input("Do you want to keep or discard this object? ").lower()
                                    while dis_keep != "keep" and dis_keep != "discard":
                                        dis_keep = input("Please type keep or discard: ")
                                    if dis_keep == "keep":
                                        discard = input("Type the object you want to discard from your inventory: ").title()
                                        while discard not in clues:
                                            discard = input("This object is not in your inventory, check if you spelled it correctly.").title()
                                        if discard in clues:
                                            clues = list(map(lambda x: x.replace(discard, 'Pouch'), clues))
                                    else:
                                            pass
                            else:
                                if "Pouch" in clues:
                                    pass
                                else:
                                    clues.append("Pouch")
                                    inventory -= 1
                        else:
                            pass
                        dis_keep  = input("Do you want to keep or discard the Trading Wood? ").lower()
                        while dis_keep != "keep" and dis_keep != "discard":
                            dis_keep = input("Please type keep or discard: ")
                        if dis_keep == "keep":
                            
                            if inventory == 0:
                                if "Wood" in clues:
                                    pass
                                else:
                                    print("You have a full inventory, if you want to keep this, you must discard something from your inventory.")
                                    input("Press enter to see your inventory: ")
                                    print(clues)
                                    dis_keep = input("Do you want to keep or discard this object? ").lower()
                                    while dis_keep != "keep" and dis_keep != "discard":
                                        dis_keep = input("Please type keep or discard: ")
                                    if dis_keep == "keep":
                                        discard = input("Type the object you want to discard from your inventory: ").title()
                                        while discard not in clues:
                                            discard = input("This object is not in your inventory, check if you spelled it correctly. ").title()
                                        if discard in clues:
                                            clues = list(map(lambda x: x.replace(discard, 'Wood'), clues))
                                        else:
                                            pass
                            else:
                                if "Wood" in clues:
                                    pass
                                else:
                                    clues.append("Wood")
                                    inventory -= 1
                        else:
                            pass
                    
                    
                elif search == 2:
                        dining_room = 1
                        print("A cool burnt up backpack")
                        input()
                        print("And crunch burnt food.")
                        input()
                        dis_keep  = input("Do you want to keep or discard the backpack? ").lower()
                        while dis_keep != "keep" and dis_keep != "discard":
                            dis_keep = input("Please type keep or discard: ")
                        if dis_keep == "keep":
                            
                            if inventory == 0:
                                if "Backpack" in clues:
                                    pass
                                else:
                                    print("You have a full inventory, if you want to keep this, you must discard something from your inventory.")
                                    input("Press enter to see your inventory: ")
                                    print(clues)
                                    dis_keep = input("Do you want to keep or discard this object? ").lower()
                                    if dis_keep == "keep":
                                        discard = input("Type the object you want to discard from your inventory: ").title()
                                        while dis_keep != "keep" and dis_keep != "discard":
                                            dis_keep = input("Please type keep or discard: ")
                                        while discard not in clues:
                                            discard = input("This object is not in your inventory, check if you spelled it correctly.").title()
                                        if discard in clues:
                                            clues = list(map(lambda x: x.replace(discard, 'Backpack'), clues))
                                    else:
                                            pass
                            else:
                                if "Backpack" in clues:
                                    pass
                                else:
                                    clues.append("Backpack")
                                    inventory -= 1
                        else:
                            pass
                        dis_keep  = input("Do you want to keep or discard the food? ").lower()
                        while dis_keep != "keep" and dis_keep != "discard":
                            dis_keep = input("Please type keep or discard: ")
                        if dis_keep == "keep":
                            
                            if inventory == 0:
                                if "Food" in clues:
                                    pass
                                else:
                                    print("You have a full inventory, if you want to keep this, you must discard something from your inventory.")
                                    input("Press enter to see your inventory: ")
                                    print(clues)
                                    dis_keep = input("Do you want to keep or discard this object? ").lower()
                                    while dis_keep != "keep" and dis_keep != "discard":
                                        dis_keep = input("Please type keep or discard: ")
                                    if dis_keep == "keep":
                                        discard = input("Type the object you want to discard from your inventory: ").title()
                                        while discard not in clues:
                                            discard = input("This object is not in your inventory, check if you spelled it correctly. ").title()
                                        if discard in clues:
                                            clues = list(map(lambda x: x.replace(discard, 'Food'), clues))
                                        else:
                                            pass
                            else:
                                if "Food" in clues:
                                    pass
                                else:
                                    clues.append("Food")
                                    inventory -= 1
                        else:
                            pass
                    
                elif search == 3:
                        living_room = 1
                        print("niche fabric")
                        input()
                        print("Weird piece of gold.")
                        input()
                        dis_keep  = input("Do you want to keep or discard the fabric? ").lower()
                        while dis_keep != "keep" and dis_keep != "discard":
                            dis_keep = input("Please type keep or discard: ")
                        while dis_keep != "keep" and dis_keep != "discard":
                            dis_keep = input("Please type keep or discard: ")
                        if dis_keep == "keep":
                            
                            if inventory == 0:
                                if "Fabric" in clues:
                                    pass
                                else:
                                    print("You have a full inventory, if you want to keep this, you must discard something from your inventory.")
                                    input("Press enter to see your inventory: ")
                                    print(clues)
                                    dis_keep = input("Do you want to keep or discard this object? ").lower()
                                    while dis_keep != "keep" and dis_keep != "discard":
                                        dis_keep = input("Please type keep or discard: ")
                                    if dis_keep == "keep":
                                        discard = input("Type the object you want to discard from your inventory: ").title()
                                        while discard not in clues:
                                            discard = input("This object is not in your inventory, check if you spelled it correctly. ").title()
                                        if discard in clues:
                                            clues = list(map(lambda x: x.replace(discard, 'Fabric'), clues))
                                        else:
                                            pass
                            else:
                                if "Fabric" in clues:
                                    pass
                                else:
                                    clues.append("Fabric")
                                    inventory -= 1
                        else:
                            pass
                        dis_keep  = input("Do you want to keep or discard the gold? ").lower()
                        while dis_keep != "keep" and dis_keep != "discard":
                            dis_keep = input("Please type keep or discard: ")
                        if dis_keep == "keep":
                            
                            if inventory == 0:
                                if "Gold" in clues:
                                    pass
                                else:
                                    print("You have a full inventory, if you want to keep this, you must discard something from your inventory.")
                                    input("Press enter to see your inventory: ")
                                    print(clues)
                                    dis_keep = input("Do you want to keep or discard this object? ").lower()
                                    while dis_keep != "keep" and dis_keep != "discard":
                                        dis_keep = input("Please type keep or discard: ")
                                    if dis_keep == "keep":
                                        discard = input("Type the object you want to discard from your inventory: ").title()
                                        while discard not in clues:
                                            discard = input("This object is not in your inventory, check if you spelled it correctly. ").title()
                                        if discard in clues:
                                            clues = list(map(lambda x: x.replace(discard, 'Gold'), clues))
                                        else:
                                            pass
                            else:
                                if "Gold" in clues:
                                    pass
                                else:
                                    clues.append("Gold")
                                    inventory -= 1
                        else:
                            pass
            cottage = True
            buildings_explored += 1
       
    print("You have visited all the buildings, press enter to analyze them.") 
    input()
    clues_analysis()

def Marx_vil():
    print("Well, after that ordeal, you continue walking.")
    input()
    if fight_helper[0] == 2:
        print("Now that you have your cool new sword, fighting Marx will probably be easier.")
    elif fight_helper[0] == 0.25:
        print("With your new anteater buddy by your side, Marx won't stand a chance.")
    else:
        print("You probably shouldn't have gone into the jungle, after all, you came out with nothing but new battle scars.")
    input()
    print("You make it to a local trade center, you sit down and trade a cheap piece of jewelry for some water.")
    input()
    input("'Oh my god, that's horrible!' a woman says.\n")
    input("You turn around and see the woman talking to someone with similar burn scars as yours.\n")
    print("'Yeah,", villian_pronouns[0],"said",villian_pronouns[3],"name was", villian_name[0] + " " + str(villian_name[1]) + ",' the person she's talking to says.\n ")
    input()
    input("At the mention of Marx's name, you sit up. \n")
    print("'"+str(villian_pronouns[0]).title()+ " did the same thing to me too,' you impulsively shout, as you pull up your sleeves to reveal your scars. ")
    input()
    print("'" + str(villian_pronouns[0]).title() + " also slaughtered your entire village?' the person asks. ")
    input()
    print("'Yeah, I'm actually looking for", villian_pronouns[2],"right now.'")
    input()
    print("'Well you can check out my village,' they say. 'Or at least, the remains of it...'")
    input()
    print("'Keep walking for a few miles and you'll see a rosted stump. Turn right there and keep walking. You'll find it.'")
    input()
    print("You say thank you, and start walking. It takes a while to get there, but you find the village.")
    input()
    print("It looks worse than how yours did.")
    input()
    print("Never mind that, first you have to find clues on where Marx might have went.")
    input()
    print("You search around, but you only find 3 buildings that are still (barely) standing.")
    input()
    clue_collections()
                

        
    
    
    
    
def vil_chat_star():
    print("'No, I'm just visting' you say. 'But I'd love to look around.'")
    input()
    print("'Oh wonderful!' the woman says. 'I'm Elizabeth and this is my husband Ralph. What's your name?")
    input()
    print("'It's",name[0],str(name[1])+"', you say, as you start walking with them.")
    input()
    print("They start pointing out shops and restaurants, it's useless, but it's helping you clear your mind. ")
    input()
    print("Suddenly, Ralph says something that peaks your interest. ")
    input()
    print("'That old cult at the end of that there jungle there,' he says, with a sort of tone on the word cult.")
    input()
    print("'Ralphie, no,' Elizabeth grumbles, but Ralph continues anyways.")
    input()
    print("'They sit by the end of the jungle, chanting curses, creating potions, worshipping...'")
    input()
    print("'How do you know?' you ask.")
    input()
    print("'How do I know?!' Ralph laughs. 'Why, the village went to war with them, 50 or so years ago. And guess who was the lucky boy who was first to sign up.'")
    input()
    print("'I've always regretted that decision. The things I've seen...' he trails off.")
    input()
    print(str(name[0])+", promise me you'll never go to that part of the jungle,' he begs.")
    input()
    print("'Uh-' you murmur, very confused. Luckily, Elizabeth comes to your rescue.")
    input()
    print("'Yes, yes,", the_pronouns[0], "promises, Ralphie,' she says, patting Ralph's back.")
    input()
    print("'Well it was great meeting you, "+ str(name[0]) + "', she exclaims. 'I hope you enjoy your time here!' she says, as she leads Ralph away. ")
    input()
    print("You wave goodbye and start walking to that nice seaside you saw earlier. ")
    sea_star()
    
        
def sea_star():
    global fight_helper
    fight_helper = [0,1]
    global fight_name
    fight_name = ["Water", "Snake"]
    global fight_pronouns
    fight_pronouns = ["it", "its", "it", "it", "it"]
    global play_dam
    play_dam = star_dam
    global fight_stats
    fight_stats = [15, 25, 20, 1]
    global protect_amount
    protect_amount = 8
    input()
    print("\nAs you reach the seaside, you take off your boots to feel the sand on your feet.")
    input()
    print("It's crispy and warm from the sun, it reminds you of your childhood.")
    input()
    print("'NOOOOOOOOOOO!' you hear a young girl's voice scream. ")
    input()
    print("Immediately after the scream, you hear a young boy's sobbing.")
    input()
    print("Out of instinct, you rush to where you heard the voices and find the boy and girl standing side by side in front of the sea, and a man behind them holding a knife.")
    input()
    print("'I know, I know,' he says through voice cracks, it's obvious he doesn't want to do it.")
    input()
    print("'Just close your eyes, and imagine the prettiest place you can,' the man whimpers, pulling up his knife.")
    input()
    print("'HEY!' you yell. 'Touch those kids and I'll use that knife to cut you apart, bit by bit,' you threaten, as you pull the children away.")
    input()
    print("'Woah, hey " + str(the_pronouns[4]) + ", don't threaten me like that!' he says.")
    input()
    print("'Well then you better have a good explanation for this,' you retort.")
    input()
    print("'I do! I do,' he quickly blurts out. 'Every year, a water snake comes out of the sea to terrorize the entire village, poisoning and eating our people, destroying buildings, and the only way to placate it is an annual sacrifice of one boy and girl.")
    input()
    print("'Really?' you say. 'Is it big, or?'")
    input()
    print("'A little smaller than a human, but very poisonous,' the man answers. 'Actually, there it is right now.'")
    input()
    print("You turn around and see a snake, almost as tall as you, staring straight at you, its eyes filled with hunger.")
    input()
    print("'Aww sh-'")
    print("\n\nYou are entering a battle. Would you like a quick tutorial?\n")
    tut = input("Type yes or no: ").lower()
    while tut != "yes" and tut != "no":
        tut = input("Please type either yes or no: ")
    if tut == "yes":
        print("\nYou will be able to either attack your enemy or protect yourself.")
        input()
        print("If you attack, your enemy will either fight back and damage you too, protect themselves, fully negating your attack, or nothing. ")
        input()
        print("If you protect yourself, there's a chance your enemy will attack. If your enemy attacks while you're protecting yourself, you will reflect their attack back at them, thus it would be wise for you to protect every so often.")
        input()
        print("However, you have a limited amount of protects. You can see how many protects you have left at the beginning of each move.")
        input()
        print("When you run out of protects, you cannot protect yourself anymore.")
        input()
        print("Good luck!")
        input()
        battle()
    elif tut == "no":
        battle()
        
    if win == True:
        print("You did it.")
        input()
        print("You beat it.")
        input()
        print("It lays at your feet, its fangs still fresh with poison.")
        input()
        print("You look at your arm. Uh oh.")
        input()
        print("Two puncture wounds right next to each other, green poison dripping from them, sizzling your skin, but you can't feel it. Your entire arm is numb.")
        input()
        print("'Welp.' you think, as you pass out.")
        input()
        input()
        input()
        print("You wake up with a gasp, you're still alive?")
        input()
        print("'" + str(the_pronouns[0]).title() + "'s awake!' you hear a voice say.")
        input()
        print("Turns out, after you passed out, the antidote to the snake's poison and other fun goodies washed onto the shore.")
        input()
        print("The village folk had fed you the antidote, and kept the rest treasure for themselves (these guys might not be good people).")
        input()
        print("But they also gave you a super cool sword that also popped up, so I guess that's good compensation. Still would have been cool to get that fur coat.")
        input("Press enter to see the sword's stats: ")
        print("Gained: One cool sword\n")
        input()
        print("Sword: From now on, everytime you attack, you will do 2 times more damage.")
        input()
        fight_helper[0] = 2
        Marx_vil()
    elif win == False:
        print("It's over, you lost.")
        input()
        print("The snake's poison overwhelmed you and you collapsed to the ground.")
        input()
        print("The last thing you saw, before you closed your eyes, was the snake going inching the children and biting them both.")
        input()
        print("You couldn't find Marx, you couldn't save the children. Your life has gone to waste.")
        input()
        print("YOU LOST.")
        try_again = input("Would you like to restart the battle?").lower()
        if try_again == "yes" or try_again == "y":
            sea_star()
        elif try_again == "no" or try_again == "n":
            try_again = input("Would you like to restart the story?").lower()
            if try_again == "yes" or try_again == "y":
                Starstruck()
            else:
                print("Thanks for playing! Bye.")
                
    
                
    
def vil_star():
    print("You walk into the village, it's very pretty. ")
    input()
    print("You notice a nice seaside where you can go to clear your mind. ")
    input()
    print("Just as you start walking, you feel a hand on your shoulder. ")
    input()
    print("It's a old couple with grey hair and matching jackets.")
    input()
    print("'Oh! Are you new here?' the woman asks. 'We'd love to show you around!'")
    input()
    print("Do you want to chat with them first, or go to the seaside immediately?")
    sea_chat = int(input("Type 1 to chat first, 2 to go to the seaside. "))
    if sea_chat == 1:
        vil_chat_star()
    elif sea_chat == 2:
        print("'No, I'm so sorry. I'd love to, but I'm in a bit of a hurry,' you say.")
        input()
        print("Oh it's totally fine,' the woman says. 'Maybe we can talk later?'")
        input()
        print("'Hopefully,' you say, as you walk away to the seaside.")
        sea_star()
def left_star():
    print("You choose to go left, thinking you'll have better chances of finding",villian_pronouns[2],"there, and start walking for a bit. ")
    input()
    print("You come across a quaint little village, not unlike your hometown, and a thick jungle.")
    input()
    print("Do you wish the go to the village or the jungle? ")
    vil_jun = int(input("\nType 1 for village, 2 for jungle, and any other number to learn more about your surrondings: "))
    if vil_jun == 1:
        vil_star()
def Starstruck():
    global star_dam 
    star_dam = 15
    global protag_fight_health
    protag_fight_health = 120
    global vil_fight_health
    vil_fight_health = 150
    #give intro
    #give player choice to go right or left
    #if left, give player choice to go into the village or jungle
    #when in village give player option to go to the seaside or talk with villagers (ends in same outcome, one just provides lore)
    #at seaside, you find two crying children, one boy and one girl, and a priest with a knife
    #you save the children and the priest explains that every 2 years the village has to sacrifice two children one boy and girl 
    #to a giant snake that lives in the ocean. You beat the snake and the townsfolk are so grateful that they give you a cool sword
    #You continue with your newfound wealth to a small village where Marx was last seen, you find clues of where marx was
    #if jungle, explore and find a hidden building
    #go into building or walk past it, If walk past you find a talking anteater that (if you give it food) joins your quest, you also battle a cultist
    #You find a small village where Marx was last seen, and you look for clues.
    #give player 3 choices where they think Marx went. if they answer wrong, they lose, if they answer right, they go to a bustling trade center
    #Inside the trade center there is a suspiciously empty stall. Player can investigate or walk past. If player investigates, they get kidnapped by an unrelated man and fails
    #iF PLAYER DOESN'T INVESTIGATE, they find a small shop that reads "Marx's Goods"
    #player has the option to confront or stalk out the store
    #both options end in player and marx in a playable battle
    #if the player has the anteater friend, Marx take 1/4 more damage from 2 attacks, if the player has the cool sword, they do 2 times more damage
    #player wins, marx mocks player, saying that killing him will never bring back the ones he killed
    #player gets option to spare marx, if marx is spare, he laughs and runs away, never to be of heard again
    #if player's doesn't spare, marx taunts the player with his dying breath, saying that their just like him
    print("\nPress enter to continue the dialogue.")
    print("You are", name[0], str(name[1])+". A strapping young",the_pronouns[4],"who has lived in comfort your entire life in your cozy little village. ")
    input()
    print("However, five years ago, your village was ruthlessly slaughtered and set ablaze, and you were the sole survivor. ")
    input()
    print("You escaped with burn wounds, and a conveniently vivid view of the", villian_pronouns[4],"that committed the act. ")
    input()
    print("It wasn't hard, after all,", villian_pronouns[0],"made sure you were the sole survivor so that you could tell the tale. I suppose it was foolish that", villian_pronouns[0],"told you",villian_pronouns[3],"name.\n")
    input()
    print(villian_name[0],villian_name[1])
    input()
    print("\n\nThat name has been stuck in your head for years, because as soon as you recovered, you became proficient in dueling and swordsmanship, and have traveled from continent to continent, looking for " + str(villian_pronouns[2])+".")
    input()
    print("And today, might just be the day. You know you're close to Marx, but you're at a fork in the road. Do you go left or right? ")
    left_right = int(input("\nType 1 for left, 2 for right: "))
    if left_right == 1:
        left_star()
        




#Introduces character options and uses the input function to allow to player to choose who they want to play as

def character_girl():
    global name
    gchar_choose = int(input("\n\nChoose your character!\n1. Ebony Starstruck: A young woman looking for the man who destroyed her home-village.\nPowers: None\nSkills: Dueling and Swordfighting\n2. Odessa Marjorie: A teenage fae seeking adventure.\nPowers: Flight and Hypnosis\nSkills: Social \n3. Lysandra Flyn: A pirate seeking fame and fortune\nPowers: Far-sight\nSkills: Fighting and Sailing\n"))
    while gchar_choose == 0 or gchar_choose > 3:
        gchar_choose = int(input("Please choose a number from 1-3: "))
    if gchar_choose == 1:
        name = ["Ebony", "Starstruck"]
        global villian_pronouns
        villian_pronouns = ["he", "his", "him", "his", "man"]
        
        global villian_name 
        villian_name = ["Cerberus", "Marx"]
        
        print("\nYou've chosen",name[0],name[1])
        input("Press Enter to begin ")
        Starstruck()
    if gchar_choose == 2:
        name = ["Odessa", "Marjorie"]
        print("You've chosen",name[0],name[1])
        input("Press Enter to begin ")
    if gchar_choose == 3:
        name = ["Lysandra", "Flyn"]
        print("You've chosen",name[0],name[1])
        input("Press Enter to begin ")
    
def character_man():
    global name
    gchar_choose = int(input("\n\nChose your character!\n1. Artemis Starstruck: A young man looking for the woman who destroyed his home-village.\nPowers: None\nSkills: Dueling and Swordfighting\n2. Ajax Marjorie: A teenage fae seeking adventure.\nPowers: Flight and Hypnosis\nSkills: Social \n3. Erix Flyn: A pirate seeking fame and fortune\nPowers: Far-sight\nSkills: Fighting and Sailing\n"))
    while gchar_choose < 1 or gchar_choose > 3:
        gchar_choose = int(input("Please choose a number from 1-3: "))
    if gchar_choose == 1:
        name = ["Artemis", "Starstruck"]
        global villian_pronouns
        villian_pronouns = ["she", "hers", "her", "her", "woman"]
        
        global villian_name 
        villian_name = ["Tempest", "Marx"]
        print("You've chosen",name[0],name[1])
        input("Press Enter to begin ")
        
        Starstruck()
    if gchar_choose == 2:
        name = ["Ajax", "Marjorie"]
        print("You've chosen",name[0],name[1])
        input("Press Enter to begin ")
    if gchar_choose == 3:
        name = ["Erix", "Flyn"]
        print("You've chosen",name[0],name[1])
        input("Press Enter to begin ")
    



        
#has the player choose the gender the want to play as
gender_choose = int(input("Choose your gender! \n\n1. Female\n2. Male\n"))
while gender_choose != 1 and gender_choose != 2:
    gender_choose = int(input("Please choose a number from 1-2: "))
    
    
    
    
#initiates the character selection and sets the pronouns
if gender_choose == 1:
   global the_pronouns
   the_pronouns = ["she", "hers", "her", "her", "woman"]
   
   character_girl()
else:
   the_pronouns = ["he", "his", "him", "his", "man"]
   character_man()



    
    

    