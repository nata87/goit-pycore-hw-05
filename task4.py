def input_error(func):
    """
    Декоратор для обробки помилок введення користувача.
    Обробляє KeyError, ValueError, IndexError і повертає відповідні повідомлення.
    """
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return 'This contact does not exist.'
        except ValueError:
            return 'Give me name and phone please.'
        except IndexError:
            return 'Enter user name and phone.'
    return inner

@input_error
def add_contact(args, contacts):

    if len(args) != 2:
        raise ValueError
    name, phone = args
    contacts[name] = phone
    return f'Contact {name} added with phone {phone}.'

@input_error
def change_contact(args, contacts):

    if len(args) != 2:
        raise ValueError
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f'Contact {name} updated with new phone {phone}.'
    else:
        raise KeyError

@input_error
def show_phone(args, contacts):

    if len(args) != 1:
        raise IndexError
    name = args[0]
    return f'Phone number of {name}: {contacts[name]}'

@input_error
def show_all(contacts):

    if contacts:
        return '\n'.join([f'{name}: {phone}' for name, phone in contacts.items()])
    else:
        return 'No contacts available.'

def main():
    contacts = {}
    print('Welcome to the assistant bot!')
    while True:
        user_input = input('Enter a command: ')
        command, *args = user_input.strip().split(maxsplit=1)
        args = args[0].split() if args else []

        if command in ['close', 'exit']:
            print('Good bye!')
            break
        elif command == 'hello':
            print('How can I help you?')
        elif command == 'add':
            print(add_contact(args, contacts))
        elif command == 'change':
            print(change_contact(args, contacts))
        elif command == 'phone':
            print(show_phone(args, contacts))
        elif command == 'all':
            print(show_all(contacts))
        else:
            print('Invalid command.')

if __name__ == '__main__':
    main()
