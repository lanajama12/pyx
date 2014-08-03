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

"""
import string



def Template(template, **context):
    """
    Simple shortcut to `string.Template`, using safe_substitute method.

    Args:
        * template: raw string template follows `string.Template` rules.
        * context: context of the string template.

    Returns:
        Substituted string by merging raw string template and its context.
        i.e.
            Template('Hello ${name}', name='someone')  => 'Hello someone'
    """
    return string.Template(template).safe_substitute(**context)




