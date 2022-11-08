def num_logger(us):
    with open("handbook_log.csv", "a") as file: 
        for value in us.values(): # adds every value from 'users' dict in the file
            file.write('{}\t'.format(value))
        file.write('\n')
        