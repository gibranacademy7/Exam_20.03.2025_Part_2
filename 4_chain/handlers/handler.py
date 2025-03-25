class Handler:
    def __init__(self, next_handler=None):
        self._next_handler = next_handler

    def handle(self, number_array, action):
        if self._next_handler:
            return self._next_handler.handle(number_array, action)
        return number_array
