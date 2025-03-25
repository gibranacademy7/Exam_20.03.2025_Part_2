from .handler import Handler

class SortHandler(Handler):
    def handle(self, number_array, action):
        if action == "sort":
            number_array.numbers = sorted(number_array.numbers)
            print(f"Sorted array: {number_array.numbers}")
        else:
            return super().handle(number_array, action)
