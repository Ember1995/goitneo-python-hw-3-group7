from Field import Field
from datetime import datetime

class Birthday(Field):
    def __init__(self, birthday):
        try:
            self.date = datetime.strptime(birthday, "%d.%m.%Y")
            super().__init__(birthday)
        except ValueError:
            raise ValueError("Birthday must be in DD.MM.YYYY format.")
        
if __name__ == "__main__":
    try:
        birthday = Birthday("23/95/2034")
        print(f"Object created successfully: {birthday}")
    except Exception as e:
        print(f"{e}")
