def flatten_list(func):
    def wrapper(*args):
        flat_list = []
        for item in args:
            if type(item) is list:
                for in_item in item:
                    flat_list.append(in_item)
            else:
                flat_list.append(item)
        print(flat_list)
        result = func(*flat_list)
        return result
    return wrapper


def convert_string_to_int(func):
    def wrapper(*args):
        converted_list = []
        for item in args:
            if isinstance(item, str):
                if item.isdigit():
                    converted_list.append(int(item))
                else:
                    converted_list.append(item)
                continue
            converted_list.append(item)
        print(converted_list)
        result = func(*converted_list)
        return result
    return wrapper


def filter_integers(func):
    def wrapper(*args):
        filtered_list = list(filter(lambda x: isinstance(x, int), args))
        print(filtered_list)
        result = func(*filtered_list)
        return result
    return wrapper


@flatten_list
@convert_string_to_int
@filter_integers
def integer_sum(*args):
    return sum(args)


args = [True, "1", "2", -0.9, 4, [5, "hi", "3"]]
print(integer_sum(*args))
# print(integer_sum(*args))
