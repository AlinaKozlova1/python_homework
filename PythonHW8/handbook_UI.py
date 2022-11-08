import hb_searching as searching
import hb_controller as cont


def get_motive():
    reason = input(
        'If you would like to add a contact enter "1",\n'
        'if you want to search a someone number enter "2": ')
    return reason
            


def ask_name():
    name = input('Enter a name: ')
    return name


def ask_surname():
    surname = input('Enter a surname: ')
    return surname


def ask_phone_num():
    phone_num = input('Enter a phone number: ')
    return phone_num


def ask_description():
    description = input('You can add a description: ')
    return description

def ask_for_addition(phone_num, description):
    answer = ''
    while answer != 'no':
        answer = input(
            'Do you want to add phone number or description for this contact?'
            '\n(yes/no): ')
        if answer == 'yes':
                answer_2 = input('Do you want to add one more number(1)/description(2)?\n'
                    'or press any other key to exit: ')
                if answer_2 == '1':
                    phone_num.append(ask_phone_num())
                    print('---> the phone number has been added <---')
                elif answer_2 == '2':
                    description.append(ask_description())
                    print('---> the description has been added <---')
        elif answer == 'no':
            cont.ask_contact_correction()
        else:
            print('Enter "yes" or "no"')

                


# Searching module

def print_searched_contact(name_1, contact):
    print(f'\nThis was found according to "{name_1}" entry:\n{contact}')


def more_search():  # function checks if the user wants to search someone again
    answer_2 = ''
    while answer_2 != 'no':
        answer_2 = input('Do you want to find somebody else?'
                         '(yes/no): ')
        if answer_2 == 'yes':
            searching.search_contact()
        elif answer_2 == 'no':
            print('Okay!')
        else:
            print('Your answer must be "yes" or "no"')
