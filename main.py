import pack

kitchen = pack.Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")

dinnigHall = pack.Room("Dining Hall")
dinnigHall.set_description("This is the dinning hall.")

ballroom = pack.Room("Ballroom")
ballroom.set_description("This is the ballroom.")


kitchen.link_room(dinnigHall, "south")
dinnigHall.link_room(kitchen, "north")
ballroom.link_room(dinnigHall, "east")
dinnigHall.link_room(ballroom, "west")

dave = pack.Enemy("Dave", "I'm a smelly zombie")
dave.set_conversation("I wanna eat brains...")
dave.set_weakness("cheese")
dinnigHall.set_character(dave) # aggregation example, an object inside another object

mike = pack.Enemy("Mike", "I'm a dangerous clown")
mike.set_conversation("Hey, this is mike yah...")
mike.set_weakness("cats")
kitchen.set_character(mike) # aggregation example, an object inside another object


# Available items to use in the rooms

item1 = pack.Item()
item1.set_description("This is good for breakfast!!!")
item1.set_name("cheese")
kitchen.set_item(item1)

item2 = pack.Item()
item2.set_description("These are nice pets!!!")
item2.set_name("cats")
dinnigHall.set_item(item2)

item3 = pack.Item()
item3.set_description("This is a delicious for breakfast!!!")
item3.set_name("cheese")
ballroom.set_item(item3)

# Default room
current_room = kitchen

finishGame = False
backpack = []

while finishGame == False:		
    #print("\n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    item_room = current_room.get_item()
    
    if inhabitant is not None:
        inhabitant.describe()

    if item_room is not None:
        print("Room's available item: " + item_room.get_name())
        
    command = input("> ")

    # Check whether a direction was typed
    if command in ['north', 'south', 'east', 'west']:
        current_room = current_room.move(command)

    elif command == 'talk' and inhabitant is not None:
        inhabitant.talk()

    elif command == 'fight' and inhabitant is not None:
        print("What will you fight with?")
        fight_with = input()

        if fight_with not in backpack:
            print("You don't have the item " + fight_with + " in your backpack")
            continue

        # if player loses the fight, the game ends
        if inhabitant.fight(fight_with) == False:
            finishGame = True
            print("You lose")
            print("Game Over")
        else:
            print("Hooray!, you won this fight!")
            print("You choosed " + item_room.get_full_description())
            print("Defeated enemies " + str(inhabitant.get_defeated_enemies()))
            
            if inhabitant.get_defeated_enemies() == 2:
                print("-----------------------------")
                print("  Excellent you won the Game  ")
                print("-----------------------------")
                current_room.character = None

    elif command == 'take':

        if item_room is not None:
            backpack.append(item_room.get_name())
            print("Item " + item_room.get_name() + " taken.")
            current_room.set_item(None)
        else:
            print("There's no available item in this room.") 

    elif command == 'exit':
        print("Good bye....\n")
        finishGame = True
    else:
        print("-Not valid command.-")   
