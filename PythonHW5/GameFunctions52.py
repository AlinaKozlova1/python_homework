def check_victory(A):
    win_array = tuple([[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7],
                 [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]])
    
    for i in win_array:
        for j in range(len(i)-2):
            if A[i[j]] == A[i[j + 1]] == A[i[j + 2]] != " . ":
                return 1
    return 0


def check_tie(A):
    for i in A:
        if A[i] == " . ":
            return 0
    return 2

def print_table(dict_):
    for i in range(1, 10):
        print(dict_[i], end=" ")
        if not i % 3:
            print("\t")

def switch_symbol(symbol):
    symbol = " o " if symbol == " x " else " x "
    return symbol