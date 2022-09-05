def find_quarter(x, y):
    if x > 0 and y > 0:
        print("It is the first quarter!")
    elif x < 0 and y > 0:
        print("It is the second quarter!")
    elif x < 0 and y < 0:
        print("It is the third quarter!")
    elif x > 0 and y < 0:
        print("It is the fourth quarter!")
    else:
        print("Inappropriate number. Please, chose anouther.")

find_quarter(245, -9)
find_quarter(-87, -97)
find_quarter(2.97, 42)
find_quarter(-67, 567)
find_quarter(0, 0)
find_quarter(0, 7)



