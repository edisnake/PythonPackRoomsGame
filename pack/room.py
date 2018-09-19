class Room():
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None        
        
    def set_description(self, room_description):
        self.description = room_description

    def get_description(self):
        return self.description    

    def set_name(self, room_name):
        self.name = room_name

    def get_name(self):
        return self.name

    def describe(self): 
        print(self.description)

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
        #print( self.name + " linked rooms :" + repr(self.linked_rooms) )

    def get_details(self):
        print('-----------------------')
        print(self.get_name())
        print('-----------------------')
        self.describe()
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print( "The " + room.get_name() + " room is at " + direction)    

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
        return self

    def set_character(self, room_character):
        self.character = room_character

    def get_character(self):
        return self.character

    def set_item(self, room_item):
        self.item = room_item

    def get_item(self):
        return self.item
    
