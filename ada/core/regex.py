# -*- coding: utf-8 -*-
"""
Regular expression patterns & relative helpers.
"""
import re

from ada.core import consts


__all__ = ('email', 'latitude', 'longitude', 'geopt',
        'date', 'time', 'datetime', 'xmltime', 'ip', 'uuid'
        'sha1', 'sha256', 'youtube', 'url', 'image',
        'is_regex')


#============================== patterns ==============================
email       = re.compile(r'(?:^|\s)[-a-z0-9_.]+@(?:[-a-z0-9]+\.)+[a-z]{2,6}(?:\s|$)', re.IGNORECASE)
# Longitude & Latitude data for Google Maps
latitude    = re.compile(r'^-?([1-8]?[1-9]|[1-9]0)\.{1}\d{1,36}')
longitude   = re.compile(r'^-?([1]?[1-7][1-9]|[1]?[1-8][0]|[1-9]?[0-9])\.{1}\d{1,36}')
geopt       = re.compile(r'^-?([1-8]?[1-9]|[1-9]0)\.{1}\d{1,36}\,\s*-?([1]?[1-7][1-9]|[1]?[1-8][0]|[1-9]?[0-9])\.{1}\d{1,36}')

date        = re.compile(r'^(19[0-9][0-9]|20[0-9][0-9])(-)(0?[1-9]|1[0-2])(-)(0?[1-9]|[12][0-9]|3[01])$')
time        = re.compile(r'^(2[0-3]|[01]?[0-9]):([0-5]?[0-9]):([0-5]?[0-9])$')
datetime    = re.compile(r'^(19[0-9][0-9]|20[0-9][0-9])(-)(0?[1-9]|1[0-2])(-)(0?[1-9]|[12][0-9]|3[01])'
                        '\s(2[0-3]|[01]?[0-9]):([0-5]?[0-9]):([0-5]?[0-9])$')

xmltime     = re.compile(r'^(19[0-9][0-9]|20[0-9][0-9])(-)(0?[1-9]|1[0-2])(-)(0?[1-9]|[12][0-9]|3[01])'
                '(T)(0?[0-9]|1[1-9]|2[0-3])(:)(0?[0-9]|[1-5][0-9])(:)(0?[0-9]|[1-5][0-9])(\.\d{3}Z)$')

ip          = re.compile(r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)')
uuid        = re.compile(r'^(\w{8})-(\w{4})-(\w{4})-(\w{4})-(\w{12})$')

sha1        = re.compile(r'^\w{40}$')
sha256      = re.compile(r'^\w{64}$')
youtube     = re.compile(r'((http|https)://)?(www\.youtube\.com\/watch)(\?|#!)(v=.{11})(.*)')


class url:
    patterns = [
        re.compile("""([0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}|(((news|telnet|nttp|file|http|ftp|https)://)|(www|ftp)[-A-Za-z0-9]*\\.)[-A-Za-z0-9\\.]+)(:[0-9]*)?/[-A-Za-z0-9_\\$\\.\\+\\!\\*\\(\\),;:@&=\\?/~\\#\\%]*[^]'\\.}>\\),\\\"]"""),
        re.compile("([0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}|(((news|telnet|nttp|file|http|ftp|https)://)|(www|ftp)[-A-Za-z0-9]*\\.)[-A-Za-z0-9\\.]+)(:[0-9]*)?"),
        re.compile("(~/|/|\\./)([-A-Za-z0-9_\\$\\.\\+\\!\\*\\(\\),;:@&=\\?/~\\#\\%]|\\\\)+"),
        #re.compile("'\\<((mailto:)|)[-A-Za-z0-9\\.]+@[-A-Za-z0-9\\.]+"),
    ]

    @classmethod
    def match(cls, value):
        return cls.patterns[0].match(value) \
                or cls.patterns[1].match(value) \
                or cls.patterns[2].match(value)

    @classmethod
    def search(cls, value):
        return cls.patterns[0].match(value) \
                or cls.patterns[1].search(value) \
                or cls.patterns[2].search(value)



class image:

    exts = re.compile(r'(.*)(\.)(jpg|gif|png)$', re.IGNORECASE)

    @staticmethod
    def match(value):
        return url.match(value) and url.exts.match(value)

    @staticmethod
    def search(cls, value):
        return url.match(value) and image.exts.search(value)



#============================== common ==============================
def is_regex(pattern):
    """
    Check if `pattern` compiled :mod:`re` pattern.

    Args:
        * pattern: object to check.

    Returns:
        :data:`True` if :data:`pattern` is a compiled :mod:`re` expression, :data:`False` otherwise.
    """
    return type(pattern) is consts.RegexType
