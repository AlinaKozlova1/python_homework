print("X      Y      Z")
print("___________________________")
def truth_table(x, y, z):
    if not(x or y or z) == (not x) or (not y) or (not z):
        print(x,"\t", y,"\t", z, " = True")
    else:
        print (x,"\t", y,"\t", z, " = False")

truth_table(True, True, True)
truth_table(True, True, False)
truth_table(False, False, False)
truth_table(False, True, False)
truth_table(True, False, False)
truth_table(False, True, True)
truth_table(False, False, True)
truth_table(True, False, True)






