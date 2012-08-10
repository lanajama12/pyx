# -*- coding: utf-8 -*-
"""
Unified constants with cross-version (2.0 - 3.0) supports.
----------------------------

The constants defined in this module are:

.. data:: cwd

    Current working directory of the script, default is :data:`os.path.curdir`.
    By changing this value, all consequent :mod:`sirocco.core.system` operations 
    will be running under the updated value.


.. data:: UnicodeType

    Generic unicode type which support python 2 ~ 3.    


.. data:: StringType

    Generic string type which support python 2 ~ 3.


.. data:: RegexType

    Compiled :mod:`re` pattern type.


.. data:: maxint

    Maximum integer current system support, provided by :data:`sys.maxsize` in python 3,
    under python 2, the value is provied by :data:`sys.maxint`.

"""
import re
import sys
import types

"""
:hidden:
"""
ispy3   = (sys.version_info.major == 3)


#==========================================================================================
#   Removed Types@Python3 
#==========================================================================================
UnicodeType = ispy3 and str or getattr(types, 'UnicodeType')
StringType  = ispy3 and str or getattr(types, 'StringTypes')
RegexType   = type(re.compile(r'RegexType'))


#==========================================================================================
#   Self-Adaptive Constants for both Python2 and Python3 
#==========================================================================================
maxint = ispy3 and getattr(sys, 'maxsize') or getattr(sys, 'maxint')


#==========================================================================================
#   Self-Adaptive Lambdas for both Python2 and Python3 
#==========================================================================================
