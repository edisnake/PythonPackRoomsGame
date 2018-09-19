class Item:
    def __init__(self):
        """ Initialize the Item """
        self.name = None
        self.description = None

    def set_description(self, room_description):
        """ Set the Item's description """
        self.description = room_description

    def get_description(self):
        """ Get the Item's description """
        return self.description    

    def set_name(self, room_name):
        """ Set the Item's name """
        self.name = room_name

    def get_name(self):
        """ Get the Item's name """
        return self.name

    def describe(self):
        """ Describes the Item """
        print(self.name + " - " + self.description)

    def get_full_description(self):
        """ Returns the full Item description """
        return self.name + " - " + self.description
