from functools import wraps

def parse_input_input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            print(f"Neither command entered, please enter one of: {args[1]}")
            return "nothing"                                                             #return some iterable to continue
        except KeyError:
            print(f"Command '{args[0]}' unsupported, please enter one of: {args[1]}")
            return "nothing"                                                             #return some iterable to continue   
        except Exception as e:
            print(f"{e}")                                                                   
            return "nothing"                                                             #return some iterable to continue
    return inner

@parse_input_input_error
def parse_input(user_input, cmd_dict):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    cmd_dict[cmd]                           #check if entered command correct (exists in commands list)
    return cmd, *args

def add_contact_input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Contacts incorrect or does not entered. Expected: add [username] [phone]"
        except Exception as e:
             return f"{e}"
    return inner

@add_contact_input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact_input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Contacts incorrect or does not entered. Expected: change [username] [phone]"
        except KeyError:
            return f"Contact '{args[0]}' does not exist in contact list."
        except Exception as e:
             return f"{e}"
    return inner

@change_contact_input_error
def change_contact(args, contacts):
    name, phone = args
    contacts.pop(name)
    contacts[name] = phone
    return "Contact updated."

def show_phone_input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return "Username does not entered. Expected: phone [username]"
        except KeyError:
            return f"Username '{args[0]}' does not exist in contact list."
        except Exception as e:
             return f"{e}"
    return inner

@show_phone_input_error  
def show_phone(args, contacts):
    name = args[0]
    return f"{name}: {contacts[name]}"

def show_all(contacts):
    contatct_list = [f"{key}: {contacts.get(key)}" for key in contacts.keys()] if len(contacts.keys()) > 0 else ["contact list is empty"]
    return contatct_list

def main():
    contacts = {}
    cmd_dict = {"close": "exit bot", "exit": "exit bot", "hello": "greeting - non functional command", "add": "adding new contact >>> add [username] [phone]", 
                "change": "update contact if exists >>> change [username] [phone]", "phone": "show contact if exists >>> phone [username]", 
                "all": "show all contacts if exists"}   
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input, cmd_dict)
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            for el in show_all(contacts):
                print(el, end="\n")

if __name__ == "__main__":
    main()