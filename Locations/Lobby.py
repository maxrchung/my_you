from .Location import Location

class Lobby(Location):
    def __init__(self):
        super().__init__()
        self.has_lobby_key = False

    def setup_commands(self):
        self.coms = dict.fromkeys(["check door", "open door", "examine door", "go to door"], self.check_door)
        self.coms.update(dict.fromkeys(["look around", "where am i"], self.look_around))
        self.coms.update(dict.fromkeys(["go to trash can", "go to trash", "check trash"], self.check_trash))

    def check_door(self):
        if self.has_lobby_key:
            if self.confirm_action("You have key. Do you wanna use key?"):
                print("Okay you unlocked the door.")
            else:
                print("Okay you don't use it then. Why?")
        else:
            print("The door is locked. Maybe you should find a key.")

    def look_around(self):
        print("You appear to be in the lobby. There's a trash can. You should go in there.")

    def check_trash(self):
        if self.has_lobby_key:
                print("Lol, you already picked up the key bro. There's nothing else here.")
        else:
            if self.confirm_action("There's a key! Do you want to pick it up?"):
                self.has_lobby_key = True
                print("Alright swagger you got a key.")
            else:
                print("Okay the key will be rotting away in the trash can until you pick it up.")