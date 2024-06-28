#Using a while loop to car game

command = " "
car_started = False

while True:
    command = input(">>>").lower()
    if command == "start":
        if car_started:
            print("Car already started!!!")
        else:
            car_started = True
            print("Car started.... Ready to go!!!")
    elif command == "stop":
        if not car_started:
            print("Car already stopped!!!")
        else:
            car_started = False
            print("car stopped")
    elif command == "help":
        print('''
start - to start the car
stop  to stop the car
quit - to exit game
''')
    elif command == "quit":
        print("Goodbye")
        break
    else:
        print("I don't understand this command")