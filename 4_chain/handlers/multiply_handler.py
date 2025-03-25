from .handler import Handler

class MultiplyHandler(Handler):
    def handle(self, number_array, action):
        if action == "multiply":
            factor = int(input("Enter the multiplication factor: "))
            number_array.numbers = [num * factor for num in number_array.numbers]
            print(f"Array after multiplication: {number_array.numbers}")
        else:
            return super().handle(number_array, action)
