import handbook_UI as ui


def search_contact():
    print('-------------------------')
    name = ui.ask_name()
    answer = check_contact(name)
    ui.print_searched_contact(name, answer)
    ui.more_search()


def check_contact(name):
    path = open('handbook_log.csv', 'r')
    for i in path:
        hb_name = i[0:len(name)]
        if hb_name == name:
            return i
    return 'There is no a person with this name:('



