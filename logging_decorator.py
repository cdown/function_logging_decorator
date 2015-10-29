from contextlib import wraps

def log_when_called(logger):
    '''
    Wrap a function so that it logs when called.
    '''
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            output_args = ', '.join(map(repr, args))
            if kwargs:
                output_args += ', ' + ', '.join(
                    '%s=%r' % (key, value) for key, value in kwargs.items()
                )

            logger.debug('Calling %s(%s)', func.__name__, output_args)
            return func(*args, **kwargs)
        return wrapper
    return decorator
