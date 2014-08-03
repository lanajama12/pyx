# -*- coding: utf-8 -*-
import logging

from functools import wraps


__all__ = ('memorize',)


logger = logging.getLogger(__name__)



__cache__ = {}

def memorize(func):
    """
    Simply memorize the calculated result :data:`func`. previously returned.

    Simply cached all calculated results from the decorated method/function into
    a global `dict`.
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
