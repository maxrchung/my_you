from Locations.Lobby import Lobby

location = Lobby()
print("The girl ran away through the door.")

while True:
    com = location.get_input()
    location.process_command(com)
    