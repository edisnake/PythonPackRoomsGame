# Python Pack Rooms Game

This is a script game project which involves python pack structure creation and object-oriented design implementation. 

The Game is about three rooms among which you can move, each room has a character who you can talk or fight and each character has a weakness you can use to win the fight.

## Server Dependencies

Python 3.6 or greater


## Install and Usage

	1. Clone the repository
		https://github.com/edisnake/PythonPackRoomsGame.git
	
	2. In the command line go to project cloned folder and run the script
		python main.py
		
	3. Type the operation direction or action you want to perform.
		
		Some general considerations:
		
		- Kitchen is the default room
		
		- If you want to move to a next room, then you can type one of the following commands (without quotes):
			"north", "south", "east" or "west"
		
		- If you want to talk with the character in the current room, then you can type "talk" to get character's conversation 
		
		- If you want to fight with the character in the current room,
			then you can type "fight" next you will have to type which item (weapon) to use as long as it's in your backpack.
		
		- If you can fight maybe you should type "take" first, 
			because this way you can save the room's item in your backpack and use it to fight.
		
		- You win the game when defeating 2 characters (enemies). You lose if you choose a wrong item to fight
		
		- Finally, if you want to exit the game, just type "exit"


## Author

Edwuin Gutierrez
edwinguti86@gmail.com


## License

Copyright(c) 2018
MIT License
