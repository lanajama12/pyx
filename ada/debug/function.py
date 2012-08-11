# -*- coding: utf-8 -*-
"""
Common debug tools set.
=======================
"""
import inspect

from functools import wraps
from timeit import default_timer as timer

from ada.debug.logger import get as getLogger


__all__ = ('attr', 'timeit', 'traceback')


logger = getLogger(__name__)


def attr(**context):
    """
    Decorator that add attributes into func.

    Added attributes can be access outside via function's `func_dict` property.
    """
    #TODO(Jim Zhan) FIXME
    def decorator(func):
        def wrapped_func(*args, **kwargs):
            for key, value in context.items():
                print key, value
            return func(*args, **kwargs)
        return wraps(func)(decorator)
    return decorator


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



def traceback(frame, parent=False):
    """Pick frame info from current caller's `frame`.

    Args:
        * frame: :type:`frame` instance, use :func:`inspect.currentframe`.
        * parent: whether to get outer frame (caller) traceback info, :data:`False` by default.

    Returns:
        :class:`inspect.Trackback` instance from :data:`frame` or its parent frame.
    """
    # Traceback(filename='<stdin>', lineno=1, function='<module>', code_context=None, index=None)
    if parent is True:
        # frame itself will always be placed @ the first index of its outerframes.
        outers = inspect.getouterframes(frame)
        traceback = (len(outers) == 1) and None or inspect.getframeinfo(outers[1][0])
    else:
        traceback = inspect.getframeinfo(frame)
    return traceback
