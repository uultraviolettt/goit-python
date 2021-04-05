main_dict = {}


GREETING_COMMANDS = ("hello", "hey!",)
EXIT_COMMANDS = ("good bye", "close", "exit", "bye")
ADD_COMMANDS = ("add", "+")
SHOW_PHONE_COMMANDS = ("phone",)
SHOW_ALL_COMMANDS = ("show all",)


def input_error(func):
    def inner(str):
        try:
            return func(str)
        except ValueError:
            return "Give me name and phone after command, please"
        except KeyError:
            return "Sorry, give me correct name, please"
    return inner


def check_dict(func):
    def inner(str):
        if len(main_dict) == 0:
            return "Sorry, your phonebook is empty("
        else:
            return func(str)
    return inner


def exit_command(str):
    return "Good bye!"


@input_error
def add_command(str):
    name, phone = str.split(' ')
    main_dict[name] = phone
    return "Entry added succesfully!"


def greeting_command(str):
    return 'How can I help you?'


@check_dict
@input_error
def show_phone_command(str):
    return f'Name: {str}, phone: {main_dict[str]}'


@check_dict
@input_error
def show_all_command(str):
    result = ''
    for i in main_dict:
        result += f'Name: {i} Phone: {main_dict[i]}\n'
    return result


def non_command():
    return 'Sorry, i don`t know this command'


COMMANDS = {ADD_COMMANDS: add_command, GREETING_COMMANDS: greeting_command,
            SHOW_PHONE_COMMANDS: show_phone_command, SHOW_ALL_COMMANDS: show_all_command, EXIT_COMMANDS: exit_command}


def parse_data(command, list):
    for i in list:
        if command.startswith(i):
            return command.replace(i, '').strip()


def parse_command(command):
    for i in COMMANDS.keys():
        com = command.lower()
        if com.startswith(i):
            data = parse_data(command, i)
            return COMMANDS[i](data)
    return non_command()


def main():
    while True:
        command = input('Please, enter command:')
        result = parse_command(command)
        if result == 'Good bye!':
            print(result)
            break
        print(result)


if __name__ == '__main__':
    main()
