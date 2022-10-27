#  3 Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def rle_encode(data):
    encoding_list = ''
    previos_char = ''
    count = 1

    if not data:
        return ''
    for char in data:
        if char != previos_char:
            if previos_char:
                encoding_list += str(count) + previos_char
            previos_char = char
            count = 1
        else:
            count += 1
    else:
        encoding_list += str(count) + previos_char
        print(encoding_list)
        return encoding_list


def rle_decode(data):
    decoding_list = ''
    count = 1
    for char in data:
        if char.isdigit():
            count *= char
        else:
            decoding_list += char * int(count)
            count = 1
    print(decoding_list)
    return decoding_list



data1 = rle_encode('AAAABBCCCCCCCDDD')
data2 = rle_decode(data1)

