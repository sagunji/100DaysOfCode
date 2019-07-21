from functools import wraps


def make_html(element):
    def wrapper(func):
        def value():
            return "<{}>{}</{}>".format(element, func(), element)

        return value

    return wrapper

