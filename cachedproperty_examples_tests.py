from cachedproperty import cachedproperty, ObjectWithCachedProperties
from time import sleep


class DirectoryContact(object):
    '''
    Look, so many repetitive operations!

    >>> jane = DirectoryContact("Jane Doe")
    >>> jane.name
    fetching contact name...
    'Jane Doe'
    >>> jane.first_name
    parsing contact name...
    fetching contact name...
    'Jane'

    >>> john = DirectoryContact("John Smith")
    >>> john.first_name
    parsing contact name...
    fetching contact name...
    'John'
    >>> john.name
    fetching contact name...
    'John Smith'
    '''

    def __init__(self, name_that_would_have_been_fetched):
        self.name_that_would_have_been_fetched = name_that_would_have_been_fetched

    def get_name(self):
        print "fetching contact name..."
        sleep(0.2)  # wow such time expensive our server is so slow
        return self.name_that_would_have_been_fetched

    @property
    def name(self):
        return self.get_name()

    @property
    def name_parts(self):
        print "parsing contact name..."
        sleep(0.2)  # oh my god this algorithm is so inefficient
        parts = self.name.split(' ', 1)
        if len(parts) < 2:
            parts.append(None)
        return parts

    @property
    def first_name(self):
        return self.name_parts[0]

    @property
    def last_name(self):
        return self.name_parts[1]


class CachedDirectoryContact(ObjectWithCachedProperties):
    '''
    Look, less many repetitive operations!

    >>> jane = CachedDirectoryContact("Jane Doe")
    >>> jane.name
    fetching contact name...
    'Jane Doe'
    >>> jane.first_name
    parsing contact name...
    'Jane'

    >>> john = CachedDirectoryContact("John Smith")
    >>> john.first_name
    parsing contact name...
    fetching contact name...
    'John'
    >>> john.name
    'John Smith'
    '''

    def __init__(self, name_that_would_have_been_fetched):
        self.name_that_would_have_been_fetched = name_that_would_have_been_fetched
        self.init_property_caches()

    def get_name(self):
        print "fetching contact name..."
        sleep(0.2)  # wow such time expensive our server is so slow
        return self.name_that_would_have_been_fetched

    @cachedproperty
    def name(self):
        return self.get_name()

    @cachedproperty
    def name_parts(self):
        print "parsing contact name..."
        sleep(0.2)  # oh my god this algorithm is so inefficient
        parts = self.name.split(' ', 1)
        if len(parts) < 2:
            parts.append(None)
        return parts

    @cachedproperty
    def first_name(self):
        return self.name_parts[0]

    @cachedproperty
    def last_name(self):
        return self.name_parts[1]


class NetworkUTCTime(ObjectWithCachedProperties):
    '''
    Perhaps a more realistic example (but not much more realistic)
    '''

    @cachedproperty
    def as_string(self):
        from urllib2 import urlopen
        print "getting time from timeapi.org"
        response = urlopen('http://www.timeapi.org/utc/now')
        return response.read()

    @cachedproperty
    def as_datetime(self):
        print "converting time from str to datetime"
        from dateutil.parser import parse
        return parse(self.as_string)
