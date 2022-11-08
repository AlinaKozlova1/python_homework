import handbook_UI as ui
import hg_logger as log

users = {}


def add_new_contact(name, surname, phone, descrip):
    global users
    users['name'] = name
    users['surname'] = surname
    users['phone number'] = phone
    users['description'] = descrip
    log.num_logger(users)
    print('Your contact has been added successfully!')
