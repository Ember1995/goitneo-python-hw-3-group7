from Field import Field

class Phone(Field):
    def __init__(self, phone):
        if phone is not None and phone != '':
            if len(phone) != 10 or not phone.isdigit():
                raise ValueError("Phone must consist of 10 digits.")
        super().__init__(phone)

if __name__ == "__main__":
    try:
        phone = Phone("not 10 digits")
        print(f"Object created successfully: {phone}")
    except Exception as e:
        print(f"{e}")

