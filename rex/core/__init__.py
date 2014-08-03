# -*- coding: utf-8 -*-
#
# Copyright 2012 Jim Zhan.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#   http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Foundamental core module.
"""

__all__ = ('Object',)


class Object:                  
    """Plain Object class with auto getter/setter support.
    """
    def __init__(self, *args, **kwargs):
        self.__dict__.update(**kwargs)  


    def __iter__(self):        
        for key, value in vars(self).items():
            yield key, value   
