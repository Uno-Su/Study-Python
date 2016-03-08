from functools import wraps
def injectuser(default_user):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if 'user'not in kwargs.keys():
                kwargs['user'] = default_user
            print("this function is {0}".format(fn.__name__))
            print("this doc is {0}".format(fn.__doc__))
            ret = fn(*args,**kwargs)
            return ret
        return wrapper
    return inner

@injectuser('swb')
def do_somethings(*args,**kwargs):
    '''This function is used for decribition
    '''
    print(kwargs.get('user'))

do_somethings()