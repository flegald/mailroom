#  _*_ coding:utf-8 _*_
"""A simple python program to keep track of names and donations."""
import sys
import io


GIFTER_DICT = {}

prompts = ["Would you like to 'Send a Thank you' or 'Create a Report'?", "Enter the donator name or press 'L' to see a list of previous names", "How much is the donation?"]
email_text = "Dear {},\nThank you so much for you donation of ${}. You are a good person.\n"


def main_controller():
    """Control flow of program."""
    begin = send_or_report()
    if begin is True:
        name = get_name()
        check_dict(name, GIFTER_DICT)
        ammt = get_ammt()
        update_dict(name, ammt)
        send_email(name, ammt)
        main_controller()
    elif begin is False:
        to_print = create_report()
        if to_print is False:
            main_controller()
        else:
            print_report(to_print)
            write_to_file(to_print)
            main_controller()


def prompt_usr(prompt):
    """Return the user response to a prompt."""
    try:
        input = raw_input
    except NameError:
        pass
    usr_answer = input('{} \n>>>>>> '.format(prompt))
    return usr_answer.lower()


def validator(usr_response):
    """Check the user answer."""
    usr_response = usr_response.lower()
    if usr_response == "send a thank you":
        return True
    elif usr_response == "create a report":
        return False
    elif usr_response == "q":
        sys.exit()
    else:
        return "error"


def send_or_report():
    """Send a thank you or create a report."""
    usr_response = prompt_usr(prompts[0])
    validate = validator(usr_response)
    if validate is True:
        return True
    elif validate is False:
        return False
    elif validate == "error":
        print("Please choose a valid option")
        send_or_report()


def get_name():
    """Get gifter name from user."""
    usr_response = prompt_usr(prompts[1])
    usr_response = usr_response.lower()
    if usr_response == "q":
        sys.exit()
    elif usr_response == "l":
        name_list = create_list(GIFTER_DICT)
        print name_list
        usr_response = prompt_usr(prompts[1])
        usr_response = usr_response.lower()
        return usr_response
    else:
        return usr_response


def check_dict(name, donate_dict):
    """Check to see if name exists in dictionary."""
    if name in donate_dict:
        return True
    else:
        donate_dict.update({str(name): {'name': str(name), 'total_ammt': 0, 'most_recent_ammt': 0, 'times_given': 0}})
        return False


def get_ammt():
    """Get donation ammount from user."""
    while True:
        try:
            usr_response = prompt_usr(prompts[2])
            usr_response = usr_response.lower()
            if usr_response == "q":
                sys.exit()
            return int(usr_response)
        except ValueError:
            print("Please type a full dollar ammount with no special characters")


def update_dict(name, ammt):
    """Update values for doner in dict."""
    temp_key = GIFTER_DICT.get(name)
    get_total = temp_key.get('total_ammt')
    total = int(get_total) + ammt
    get_total_times = temp_key.get('times_given')
    total_times = (get_total_times + 1)
    GIFTER_DICT.update({name: {'name': name, 'total_ammt': total, 'most_recent_ammt': ammt, 'times_given': total_times}})


def send_email(name, ammt):
    """Print out customized email text."""
    print email_text.format(name, ammt)
    return email_text.format(name, ammt)


def create_list(donate_dict):
    """Create a list of names that have given before."""
    if len(donate_dict) > 0:
        name_list = list(donate_dict.keys())
        return name_list
    else:
        print("There are no names")
        return False


def create_report():
    """Create a report of donaters."""
    if len(GIFTER_DICT) == 0:
        print("there is nothing to report")
        return False
    else:
        name_list = create_list(GIFTER_DICT)
        gifter_list = []
        for name in name_list:
            key = GIFTER_DICT.get(name)
            total = key.get("total_ammt")
            num_of_times = key.get("times_given")
            avg_donation = total / num_of_times
            gifter_list.append("Total:${} Name: {} Number of Times: {} Average:${}".format(int(total), name,  num_of_times, avg_donation))
        return gifter_list


def print_report(list):
    """Sort and print list."""
    sorted(list, reverse=True)
    for i in list:
        print i


def write_to_file(to_write):
    """Write list to readable txt file."""
    print("print")
    open_file = io.open("donate_track.txt", 'w')
    open_file.truncate()
    for i in to_write:
        print("writing: " + i)
        open_file.write(i.decode('utf-8'))
        open_file.write("\n".decode('utf-8'))
    open_file.close()

if __name__ == "__main__":
    main_controller()