import handbook_UI as ui
import handbook_adding as adding
import hb_searching as searching


def start():
    motive = ui.get_motive()
    if motive == '1':
        ask_new_contact()
    elif motive == '2':
        searching.search_contact()
    else:
        print('Sorry, there is no such operation:(')


contact_name = '-'
contact_surname = '-'
contact_phone_num = []
contact_description = []


def ask_new_contact():
    print('-------------------------')
    global contact_name
    global contact_surname
    global contact_phone_num
    global contact_description
    contact_name = ui.ask_name()
    contact_surname = ui.ask_surname()
    contact_phone_num.append(ui.ask_phone_num())
    contact_description.append(ui.ask_description())
    ask_contact_correction()
    ui.ask_for_addition(contact_phone_num, contact_description)
    adding.add_new_contact(
                contact_name, contact_surname, contact_phone_num, contact_description)
   


def ask_contact_correction():
    answer = ''
    while answer != 'yes':
        answer = input(
            f'\n{contact_name}\t{contact_surname}\t{contact_phone_num}\t{contact_description}\n'
            '\nIs entered data correct?(yes/no) - ')
        if answer == 'no':
            answer_2 = input(
                'Do you want to change something?\n'
                '(yes/no): ')
            if answer_2 == 'yes':
                change_contact()
            # if answer_2 == 'yes':
            #     contact_phone_num.append(ui.ask_phone_num())
            # elif answer_2 == '2':
            #     contact_description.append(ui.ask_description())
            # elif answer_2 == '3':
            #     change_contact()
            # else:
            #     print('Okay~')
            else:
                print('Your answer must be "yes" or "no"')
        elif answer == 'yes':
            print('Okay')
        else:
            print('Your answer must be "yes" or "no"')


def change_contact():
    global contact_name
    global contact_surname
    global contact_phone_num
    global contact_description
    answ = int(input('What would you like to change:\n'
                     '1 - name\n2 - surname\n3 - phone number\n4 - description\n'
                     'or press any other key to exit without changes: '))
    if answ == 1:
        contact_name = ui.ask_name()
    elif answ == 2:
        contact_surname = ui.ask_surname()
    elif answ == 3:
        contact_phone_num.pop()
        contact_phone_num.append(ui.ask_phone_num())
    elif answ == 4:
        contact_description.pop()
        contact_description.append(ui.ask_description())
    else:
        print('fine~')
