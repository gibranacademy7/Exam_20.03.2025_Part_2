from .handler import Handler

class AverageHandler(Handler):
    def handle(self, number_array, action):
        if action == "average":
            calculated_average = sum(number_array.numbers) / len(number_array.numbers)
            number_array.average = calculated_average
            print(f"Average of numbers: {number_array.average}")
        else:
            return super().handle(number_array, action)
