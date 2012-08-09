# -*- coding: utf-8 -*-
import logging

from functools import wraps
from timeit import default_timer as timer


logger = logging.getLogger(__name__)


__all__ = ('timeit', 'memorize',)


def timeit(func):
    """
    Decorator that logs the cost time of a function.
    """
    @wraps(func)
    def wrapped_func(*args, **kwargs):
        start  = timer()
        result = func(*args, **kwargs)
        cost   = timer() - start
        logger.debug('<method: %s> finished in %2.2f sec' % (func.__name__, cost))
        return result
    return wrapped_func


__cache__ = {}

def memorize(func, *args, **kwargs):
    """
    Simply memorize the calculated result :data:`func`. previously returned.

    Simply cached all calculated results from the decorated method/function into
    a global :data:`dict`.
    """
    @wraps(func)
    def wrapped_func(*args, **kwargs):
        if (len(args) > 0 and len(kwargs) > 0): 
            cacheKey = list(args)
            cacheKey.append(kwargs)
        elif (len(args) > 0): 
            cacheKey = args
        else:
            cacheKey = func.__name__
            
        global __cache__
        result = __cache__.get(cacheKey)
        if result is None:
            result = func(*args, **kwargs)
            __cache__[cacheKey] = result
        return result

    return wrapped_func
