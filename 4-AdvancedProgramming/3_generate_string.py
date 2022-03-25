def generate_string(string, frequency):
    for chr in string:
        yield chr * frequency


class GenerateString:
    def __init__(self, string, frequency):
        self.string = string
        self.frequency = frequency
        self.char = 0
        self.new_string = ''

    def __iter__(self):
        self.char = 0
        self.new_string = ''
        return self

    def __next__(self):
        try:
            self.new_string = self.string[self.char] * self.frequency
            self.char += 1
            return self.new_string
        except Exception:
            raise StopIteration


string = "hello"
frequency = 3

function_result = generate_string(string, frequency)
print("".join(list(function_result)))
class_result = GenerateString(string, frequency)
print(class_result)
print("".join(list(class_result)))
