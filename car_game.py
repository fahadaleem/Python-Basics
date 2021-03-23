## car game
## commands in this game
## help to list the commands
## start - to start the car
## stop - to stop the car
## quit - to exit

is_stop = False
is_start = False
while True:
    command = input(">").lower()
    if command == "help":
        print('''
    start - to start the car
    stop - to stop the car
    quit - to exit''')
    elif command == "start" and not is_start:
        is_start = True
        print("Car started!..... Ready to go!")
    elif command == "start" and is_start:
        print("Car is already started!")
        continue
    elif command == "stop" and not is_stop:
        is_stop = True
        print("Car Stopped!")
    elif command == "stop" and is_stop:
        print("Car is already Stopped!")
        continue
    elif command == "quit":
        break
    else:
        print("I don't understand what you want...")
    