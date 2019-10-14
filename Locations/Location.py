class Location:
    def __init__(self):
        self.setup_commands()
        self.confirm_action_yes = ["yes", "ye", "y", "yup", "sure", "okay", "alright"]

    def setup_commands(self):
        self.coms = {}

    def process_command(self, com):
        if com in self.coms:
            self.coms[com]()
        else:
            print("What do you mean?")
        print()
        
    def get_input(self):
        com = input("You: ").strip().lower()
        return com

    def confirm_action(self, msg):
        print(msg)
        com = self.get_input()
        if com in self.confirm_action_yes:
            return True
        return False