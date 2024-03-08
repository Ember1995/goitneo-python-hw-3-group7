from models import *
from decorators import *

@input_error
def add_contact(args, book):
    name, phone, *optional_args = args
    birthday = optional_args[0] if optional_args else None
    new_record = Record(name)
    new_record.add_phone(phone)
    if birthday:
        new_record.add_birthday(birthday)
    book.add_record(new_record)
    return f"Contact {name} added with phone number {phone}{' and birthday ' + birthday if birthday else ''}."

@input_error
def change_contact(args, book):
    name = args[0]
    if name not in book.data:
        raise KeyError()
    record = book.data[name]

    print("Select parameter to change:\n1. Phone\n2. Birthday")
    parameter = input("Enter parameter number: ")

    if parameter == "1":
        print("Select action:\n1. Add new phone\n2. Change existing phone\n3. Delete phone")
        action = input("Enter action number: ")

        if action == "1":
            new_phone = input("Enter new phone number: ")
            record.add_phone(new_phone)
            return f"New phone number {new_phone} added for {name}."

        elif action == "2":
            print(f"Select a phone for {name} to change:")
            for i, phone in enumerate(record.phones, start=1):
                print(f"{i}. {phone.value}")
            index = int(input("Enter phone number index: ")) - 1
            if 0 <= index < len(record.phones):
                new_phone = input("Enter new phone number: ")
                old_phone = record.phones[index].value
                record.edit_phone(old_phone, new_phone)
                return f"Phone number for {name} changed from {old_phone} to {new_phone}."
            else:
                return "Invalid index. Put the initial command again."

        elif action == "3":
            if len(record.phones) == 1:
                return "Cannot delete the only phone number. Each contact must have at least one phone number."

            print("Select a phone to delete:")
            for i, phone in enumerate(record.phones, start=1):
                print(f"{i}. {phone.value}")
            index = int(input("Enter phone number index: ")) - 1
            if 0 <= index < len(record.phones):
                record.remove_phone(record.phones[index].value)
                return f"Phone number removed for {name}."
        else:
            return "Invalid index. Put the initial command again."

    elif parameter == "2":
        new_birthday = input("Enter new birthday in DD.MM.YYYY format: ")
        record.add_birthday(new_birthday)
        return f"Birthday for {name} changed to {new_birthday}."

    else:
        return "Invalid index. Put the initial command again."

@input_error
def add_birthday(args, book):
    name, birthday = args
    if name in book.data:
        record = book.data[name]
        record.add_birthday(birthday)
        return f"Birthday {birthday} added for {name}."
    else:
        raise KeyError()

@input_error    
def show_phone(args, book):
    name, = args
    if name in book.data:
        record = book.data[name]
        phones = '; '.join([phone.value for phone in record.phones])
        return phones
    else:
        raise KeyError(f"Contact with name '{name}' not found.")

@input_error
def show_birthday(args, book):
    name, = args
    if name in book.data and book.data[name].birthday:
        return f"{name}'s birthday is on {book.data[name].birthday.value}."
    else:
        raise KeyError()

def show_all(book):
    contacts_info = []
    for name, record in book.data.items():
        phones = ', '.join(phone.value for phone in getattr(record, 'phones', []))
        birthday = f", birthday: {record.birthday.value}" if getattr(record, 'birthday', None) else ""
        contacts_info.append(f"Name: {name}, phones: {phones}{birthday}")
    return '\n'.join(contacts_info)
    
if __name__ == "__main__":
    pass
