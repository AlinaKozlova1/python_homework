def find_weekend():
    print('Is your day a weekend?')
    keep_going = True
    while keep_going:
        weekday = int(input("Enter a number of day of week: "))
        if 5 < weekday < 8:
            print("Yes, it's a weekend")
        elif 0 < weekday < 6:
            print("No, it's not a weekend")
        else:
            print("Sorry, your number is out of range.\
                \nPlease, enter any number from 1 to 7 and try again.")
        answer = input("Press any key to continue or enter 'stop' to leave: ")
        keep_going = (answer != "stop")

find_weekend()
