from logger import log as logging
from functools import wraps
import traceback


def disable_decorator(disable, /, *args, reason=None, notify=True, **kwargs):
    """Disable a decorator if a condition is met."""
    location = traceback.extract_stack()[-2]

    def null_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    def notification(decorator):
        if notify:
            logging.debug(f"Disabling the decorator: {decorator.__name__} (decoration at {location.filename}:{location.lineno}) because: {reason}")

    def nullify_decorator(decorator):
        notification(decorator)
        return null_decorator

    # For "static" condition checking.
    if isinstance(disable, bool):
        return nullify_decorator if disable else null_decorator

    # For "runtime" condition checking.
    assert callable(disable), f"Require a callable predicate: {disable =}"

    def conditionally_null_decorator(decorator):
        enabled_decorator = disable_decorator(False, reason=reason, notify=False)(decorator)
        disabled_decorator = disable_decorator(True, reason=reason, notify=False)(decorator)

        def conditional_decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                logging.debug("Inside the conditional decorator")
                runtime_disable = disable(*args, **kwargs)
                if runtime_disable:
                    notification(decorator)
                dec_func = disabled_decorator(func) if runtime_disable else enabled_decorator(func)
                return dec_func(*args, **kwargs)

            return wrapper

        return conditional_decorator

    return conditionally_null_decorator


if __name__ == "__main__":
    logging.getLogger().setLevel(logging.TRACE)


    def first_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("Inside the first decorator")
            return func(*args, **kwargs)

        return wrapper


    @disable_decorator(False, reason="Trying to enable")
    def second_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("Inside the second decorator")
            return func(*args, **kwargs)

        return wrapper


    @disable_decorator(True, reason="Trying to disable")
    def third_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("Inside the third decorator")
            return func(*args, **kwargs)

        return wrapper


    class Predicate:
        def __init__(self):
            self.value = None

        def __call__(self, *args, **kwargs):
            logging.debug("Calling predicate function.")
            return self.value

        def set_value(self, value):
            self.value = value


    predicate = Predicate()


    def example_function(*args, **kwargs):
        print("Hello World\n")


    def f0(*args, **kwargs):
        return example_function(*args, **kwargs)


    @first_decorator
    def f1(*args, **kwargs):
        return example_function(*args, **kwargs)


    @second_decorator
    def f2(*args, **kwargs):
        return example_function(*args, **kwargs)


    @third_decorator
    def f3(*args, **kwargs):
        return example_function(*args, **kwargs)


    @disable_decorator(predicate, reason="Trying to conditionally disable")
    def fourth_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("Inside the fourth decorator")
            return func(*args, **kwargs)

        return wrapper


    @fourth_decorator
    def f4(*args, **kwargs):
        return example_function(*args, **kwargs)


    for f in [f0, f1, f2, f3]:
        f()

    predicate.value = True
    f4()
    predicate.value = False
    f4()
