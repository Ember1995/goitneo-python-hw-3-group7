from Field import Field

class Name(Field):
    def __init__(self, name):
        if not name:
            raise ValueError("Name cannot be empty")
        super().__init__(name)
              
if __name__ == "__main__":
    try:
        name = Name("")
        print(f"Object created successfully: {name}")
    except Exception as e:
        print(f"{e}")