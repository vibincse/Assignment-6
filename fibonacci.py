# fibonacci.py
class Fibonacci:
    def __init__(self, value):
        if not isinstance(value, int):
            raise ValueError("Input must be an integer")
        self.value = value
        self.a, self.b = 0, 1
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > self.value:
            raise StopIteration

        if self.index == 0:
            self.index += 1
            return 0
        elif self.index == 1:
            self.index += 1
            return 1
        else:
            self.a, self.b = self.b, self.a + self.b
            self.index += 1
            return self.b


