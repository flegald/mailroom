import sys
gifter_dict = {}

email_text = "Dear {}, \n Thank you so much for your donation of ${}. You are one cool cat"


def validator(answer):
    if answer.lower() == "send a thank you":
        return True
    elif answer.lower() == "create a report":
        return False
    elif answer.lower == 'q':
        sys.exit()

def send_or_report():
    user_answer = raw_input("Would you like to 'Send a Thank You' or 'Create a Report'? (press 'q' at anytime to quit) \n >>>")
    if validator(user_answer):
        ask_name()
    elif validator(user_answer) == False:
        create_report(gifter_dict)

def ask_name():
    name_givenT = raw_input("Type gifter name or 'list' to see a list of gifters. \n >>>")
    if name_givenT.lower() == "list":
        print list(gifter_dict)
        ask_name()
    elif name_givenT.lower() == 'q':
        sys.exit()
    else:
        check_dic(name_givenT.lower())

def ask_ammt(name):
    update_name = name
    ammt_givenT = raw_input("How much is the donation? \n >>>")
    if ammt_givenT.lower == 'q':
        sys.exit()
    else:
        update_values(update_name, int(ammt_givenT))

def check_dic(name):
    if name in gifter_dict:
        ask_ammt(name)
    else:
        gifter_dict.update({name:{'total_ammt': 0, 'this_ammt': 0, 'times_given': 0 }})
        ask_ammt(name)

def update_values(name, ammt):
    temp_key = gifter_dict.get(name)
    get_total = temp_key.get('total_ammt')
    total = (int(get_total) + ammt)
    temp_total_given = gifter_dict.get(name)
    get_total_times = temp_total_given.get('times_given')
    total_times = (1 + get_total_times)
    gifter_dict.update({name: {'total_ammt': total, 'this_ammt': ammt, 'times_given': total_times}})
    print_email(name, ammt)

def print_email(name, ammt):
        print email_text.format(name, ammt)
        send_or_report()

def create_report(dict):
    gifter_list = list(gifter_dict.items())
    for gifter in gifter_list:
        print gifter

if __name__ == "__main__":
    send_or_report()