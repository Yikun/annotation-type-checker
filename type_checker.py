import inspect
import functools
import typing


# We could also add `allow_list` to allow user enable the checkers on specific args
# type checker on every input args (except arg in block_list)
# Will raise TypeError when args type is unmatched.
def type_checker(block_list=['return']):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kw):
            # Get all input args name and value
            # like: OrderedDict([('self', <Demo...>), ('a', 1), ('b', 2)])
            kv = inspect.signature(func).bind(self, *args, **kw).arguments
            hints = typing.get_type_hints(func)
            for k, t in hints.items():
                if block_list and k in block_list:
                    # skip `self` type check
                    continue
                # Get annotation type from annotaions, __annotations__ like:
                # {'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}
                v = kv.get(k)
                # Raise the TypeError when input value is not match with type
                if not isinstance(v, t):
                    raise TypeError("The type of %s should be a %s type" % (k, t))
            return func(self, *args, **kw)
        return wrapper
    return decorator
