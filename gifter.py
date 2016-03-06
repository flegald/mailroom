# -*- coding:UTF-8 -*-

import sys
GIFTER_DICT = {}

email_text = "Dear {}, \n Thank you so much for your donation of ${}. You are one cool cat \n"
report_text = "Name: {} Total Donatations: {} Number of Times Donated: {}"

def validator(answer):
    if answer.lower() == "send a thank you":
        return True
    elif answer.lower() == "create a report":
        return False
    elif answer.lower() == 'q':
        sys.exit()
    else:
        print "Please choose one of the options"
        send_or_report()

def send_or_report():
    user_answer = raw_input("Would you like to 'Send a Thank You' or 'Create a Report'? (press 'q' at anytime to quit) \n >>>")
    if validator(user_answer):
        ask_name()
    elif validator(user_answer) == False:
        create_report(GIFTER_DICT)

    

def ask_name():
    name_givenT = raw_input("Type gifter name or 'list' to see a list of gifters. \n >>>")
    if name_givenT.lower() == "list":
        print list(GIFTER_DICT)
        ask_name()
    elif name_givenT.lower() == 'q':
        sys.exit()
    else:
        check_dic(name_givenT.lower())

def ask_ammt(name):
    update_name = name
    ammt_givenT = raw_input("How much is the donation? \n >>>")
    if ammt_givenT.lower() == 'q':
        sys.exit()
    elif ammt_givenT.isdigit() == False:
        print "Please enter only numbers with a full dollar ammount(no cent value)"
        ask_ammt(name)
    else:
        update_values(update_name, int(ammt_givenT))

def check_dic(name):
    if name in GIFTER_DICT:
        ask_ammt(name)
    else:
        GIFTER_DICT.update({name: {'name': name, 'total_ammt': 0, 'this_ammt': 0, 'times_given': 0 }})
        ask_ammt(name)

def update_values(name, ammt):
    temp_key = GIFTER_DICT.get(name)
    get_total = temp_key.get('total_ammt')
    total = (int(get_total) + ammt)
    temp_total_given = GIFTER_DICT.get(name)
    get_total_times = temp_total_given.get('times_given')
    total_times = (1 + get_total_times)
    GIFTER_DICT.update({name: {'name': name, 'total_ammt': total, 'this_ammt': ammt, 'times_given': total_times}})
    print_email(name, ammt)

def print_email(name, ammt):
        print email_text.format(name, ammt)
        send_or_report()

def create_report(dict):
    gifter_list = []
    for idx, gifter in enumerate(GIFTER_DICT):
        name = GIFTER_DICT[gifter].get("name")
        total = GIFTER_DICT[gifter].get("total_ammt")
        num_of_times = GIFTER_DICT[gifter].get("times_given")
        avg_donation = int(total)/int(num_of_times)
        gifter_list.append("Total:${} Name: {} Number of Times: {} Average:${}".format(int(total), name.upper(),  num_of_times, avg_donation))
    organize_list(gifter_list)

def organize_list(item):
    sorted(item, reverse=True)
    for gifter in item:
        print gifter
    send_or_report()

if __name__ == "__main__":
    send_or_report()