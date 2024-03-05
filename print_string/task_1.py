class TaskOne:
    def __init__(self):
        self.input = ''

    def get_string(self, string):
        self.input = string
        return string

    def printString(self):
        return self.input.upper()


class Correction:
    def __init__(self):
        self.data = ''

    def get_string(self, string):
        self.data = input("Enter your data...")

    def printString(self):
        return self.data.upper()
