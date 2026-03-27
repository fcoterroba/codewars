class Debugger(object):
    attribute_accesses = []
    method_calls = []


class Meta(type):
    def __new__(mcs, name, bases, namespace):
        for attr_name, attr_value in list(namespace.items()):
            if callable(attr_value) and not isinstance(attr_value, (staticmethod, classmethod)):
                namespace[attr_name] = mcs._wrap_method(attr_value)

        cls = super().__new__(mcs, name, bases, namespace)

        def __getattribute__(self, item):
            value = object.__getattribute__(self, item)
            if not item.startswith('__'):
                Debugger.attribute_accesses.append({
                    'action': 'get',
                    'class': type(self),
                    'attribute': item,
                    'value': value
                })
            return value

        def __setattr__(self, key, value):
            if not key.startswith('__'):
                Debugger.attribute_accesses.append({
                    'action': 'set',
                    'class': type(self),
                    'attribute': key,
                    'value': value
                })
            object.__setattr__(self, key, value)

        cls.__getattribute__ = __getattribute__
        cls.__setattr__ = __setattr__

        return cls

    @staticmethod
    def _wrap_method(method):
        def wrapper(*args, **kwargs):
            cls = type(args[0]) if args else None
            Debugger.method_calls.append({
                'class': cls,
                'method': method.__name__,
                'args': args,
                'kwargs': kwargs
            })
            return method(*args, **kwargs)
        wrapper.__name__ = method.__name__
        return wrapper

# original kata: https://www.codewars.com/kata/54bebed0d5b56c5b2600027f
# my solution: https://www.codewars.com/kata/reviews/54bec5636150e1db650000fe/groups/69c650f7c3e5b854d7eeca1f
