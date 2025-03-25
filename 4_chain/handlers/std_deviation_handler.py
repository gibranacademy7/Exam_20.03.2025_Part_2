import statistics
from .handler import Handler

class StdDeviationHandler(Handler):
    def handle(self, number_array, action):
        if action == "std_deviation":
            if len(number_array.numbers) > 1:
                calculated_std = statistics.stdev(number_array.numbers)
                number_array.std_deviation = calculated_std
                print(f"Standard deviation: {number_array.std_deviation}")
            else:
                print("Cannot calculate standard deviation with less than 2 numbers")
        else:
            return super().handle(number_array, action)
