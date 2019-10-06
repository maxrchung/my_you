has_lobby_key = False
location = "lobby"
print("The girl ran away through the door.")

def get_input():
    com = input("You: ").strip().lower()
    return com

def check_phrase(com, phrases):
    is_phrase = com in phrases
    return is_phrase

def confirm_action(msg):
    print(msg)
    com = get_input()
    if check_phrase(com, ["yes", "ye", "y", "yup", "sure", "okay", "alright"]):
        return True
    return False
    

while True:
    com = get_input()
    if location == "lobby":
        if check_phrase(com, ["check door", "open door", "examine door", "go to door"]):
            if has_lobby_key:
                if confirm_action("You have key. Do you wanna use key?"):
                    print("Okay you unlocked the door.")
                    location = "next_room"
                else:
                    print("Okay you don't use it then. Why?")

            else:
                print("The door is locked. Maybe you should find a key.")

        elif check_phrase(com, ["look around", "where am i"]):
            print("You appear to be in the lobby. There's a trash can. You should go in there.")
            
        elif check_phrase(com, ["go to trash can", "go to trash", "check trash"]):
            if has_lobby_key:
                print("Lol, you already picked up the key bro. There's nothing else here.")

            else:
                if confirm_action("There's a key! Do you want to pick it up?"):
                    has_lobby_key = True
                    print("Alright swagger you got a key.")
                else:
                    print("Okay the key will be rotting away in the trash can until you pick it up.")

        else:
            print("What do you mean?")

    print()
    