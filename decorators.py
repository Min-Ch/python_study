from functools import wraps


def some_decorator(hi):
    def decorate(func):
        print(hi)
        print(func.__qualname__)
        print(func.__module__)

        @wraps(func)
        def wrapper(some):
            return func(some)
        return wrapper
    return decorate


def some_decorator_2(hello):
    def decorate(func):
        print(hello)
        print(func.__qualname__)
        print(func.__module__)

        @wraps(func)
        def wrapper(some):
            return func(some)
        return wrapper
    return decorate


@some_decorator('안녕하세요 첫번째 데코')
@some_decorator_2('안녕하세요 두번째 데코')
def some_func(some):
    print(some)


if __name__ == '__main__':
    some_func('123')
