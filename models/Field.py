class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
        
if __name__ == "__main__":
    try:
        field = Field("test")
        print(f"Object created successfully: {field}")
    except Exception as e:
        print(f"{e}")
