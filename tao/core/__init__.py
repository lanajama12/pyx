# -*- coding: utf-8 -*-
"""

"""

class Object:                  
    """Plain Object class with auto getter/setter support.
    """
    def __init__(self, *args, **kwargs):
        self.__dict__.update(**kwargs)  


    def __iter__(self):        
        for key, value in vars(self).items():
            yield key, value   
