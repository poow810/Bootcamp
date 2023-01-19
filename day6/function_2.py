# debugging

def document_info(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional argument:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function

@document_info
def sub_int(x, y):
    return x - y


@document_info
def squares(n):
    return n * n


print(squares(5))
print(sub_int(7, 3))