import model_complex as mc
import model_franction as mf
import view
x = 0
y = 0
sign = 0


def start():
    global x
    global y
    global sign
    x = view.get_value()
    y = view.get_value()
    sign = view.get_sign()
    res = check_num(x, y)
    view.view_data(x, y, sign, res)


def complex_calc():
    if sign == "-":
        return mc.get_complex_subtraction(x, y)
    elif sign == "+":
        return mc.get_complex_sum(x, y)
    elif sign == "*":
        return mc.get_complex_multiplication(x, y)
    elif sign == "/":
        return mc.get_complex_divion(x, y)
    else:
        print("Wrong sign")
        return "---"


def franction_calc():
    list_1 = mf.make_franction_list(x)
    list_2 = mf.make_franction_list(y)
    if sign == "-":
        return mf.get_franction_subtraction(list_1, list_2)
    elif sign == "+":
        return mf.get_franction_sum(list_1, list_2)
    elif sign == "*":
        return mf.get_franction_multiplication(list_1, list_2)
    elif sign == "/":
        return mf.get_franction_dividion(list_1, list_2)
    else:
        print("Wrong sign")
        return '---'


def check_num(num_1, num_2):
    if type(num_1) == complex and type(num_2) == complex:
        return complex_calc()
    else:
        return franction_calc()
