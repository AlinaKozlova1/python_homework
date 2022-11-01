from datetime import datetime as dt


def expression_logger(a, b, sign, result):
    time = dt.now().strftime("%H:%M")
    with open("log.csv", "a") as file:
        file.write("{}: {}{}{} = {}\n".format(time, a, sign, b, result))
