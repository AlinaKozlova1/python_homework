import logger


def view_data(a, b, sign, result):
    logger.expression_logger(a, b, sign, result)
    print(f"{a} {sign} {b} = {result}")


def get_value():
    try:
        num = input("value = ")
        return complex(num)
    except ValueError:
        return str(num)


def get_sign():
    return input("sign: ")
