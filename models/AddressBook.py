from collections import UserDict
from collections import defaultdict
from datetime import datetime

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)
            
    def delete(self, name):
        if name in self.data:
            del self.data[name]
            
    def get_birthdays_per_week(self):
        today = datetime.today().date()
        birthdays = defaultdict(list)
        day_names = {
            0: "Monday", 
            1: "Tuesday", 
            2: "Wednesday", 
            3: "Thursday", 
            4: "Friday", 
            5: "Saturday", 
            6: "Sunday"
            }

        for name, record in self.data.items():
            if record.birthday:
                birthday_date = datetime.strptime(record.birthday.value, "%d.%m.%Y").date()
                birthday_this_year = birthday_date.replace(year=today.year)

                if birthday_this_year < today:
                    birthday_this_year = birthday_this_year.replace(year=today.year + 1)

                delta_days = (birthday_this_year - today).days

                if 0 <= delta_days < 7:
                    day_of_week = birthday_this_year.weekday()

                    if day_of_week in [5, 6]: 
                        day_of_week = 0

                    birthdays[day_names[day_of_week]].append(name)

        if not birthdays: 
            print("No birthdays next week.")
        else:
            for day, names in birthdays.items():
                print(f"{day}: {', '.join(names)}")

if __name__ == "__main__":
   pass