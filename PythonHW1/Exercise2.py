print("X      Y      Z")
print("___________________________")
def truth_table():
    for z in range(2):
        for y in range(2):
            for x in range(2):
                if not(x or y or z) == (not x and not y and not z):
                    print(x,"\t", y,"\t", z, " = True")
                else:
                    print (x,"\t", y,"\t", z, " = False")

truth_table()






