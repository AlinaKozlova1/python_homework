def write_range ():
    try:
        number = int(input("Enter a number from 1 to 4: "))
        if number == 1:
            print ("the first quarter range => X∈(0; +∞), Y∈(0; +∞)")
        elif number == 2:
            print ("the second quarter range => X∈(0; -∞), Y∈(0; +∞)")
        elif number == 3:
            print ("the third quarter range => X∈(0; -∞), Y∈(0; -∞)")
        elif number == 4:
            print ("the fourth quarter range => X∈(0; +∞), Y∈(0; -∞)")
        else:
            print("Your number is out of range.")
    except ValueError:
        print("Enter a number!")

write_range()