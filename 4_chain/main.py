from number_array import NumberArray
from handlers.sort_handler import SortHandler
from handlers.multiply_handler import MultiplyHandler
from handlers.average_handler import AverageHandler
from handlers.std_deviation_handler import StdDeviationHandler

def main():
    size = int(input("Enter the size of the array: "))
    number_array = NumberArray(size)

    print(f"Original array: {number_array.numbers}")


    sort_handler = SortHandler()
    multiply_handler = MultiplyHandler(sort_handler)
    average_handler = AverageHandler(multiply_handler)
    std_handler = StdDeviationHandler(average_handler)


    actions = ["sort", "multiply", "average", "std_deviation"]
    for action in actions:
        user_choice = input(f"{action.capitalize()} the array? (yes/no): ").strip().lower()
        if user_choice == "yes":
            std_handler.handle(number_array, action)

    print(f"Final array: {number_array.numbers}")
    print("\nStored Statistics:")
    if number_array.average is not None:
        print(f"Average: {number_array.average}")
    if number_array.std_deviation is not None:
        print(f"Standard Deviation: {number_array.std_deviation}")

if __name__ == "__main__":
    main()
