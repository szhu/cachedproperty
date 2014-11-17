@cachedproperty
===============

Python attributes are cached. Python property methods are lazy. Can't we have both?

`@cachedproperty` computes your attributes the first time they're accessed, because sometimes you'll never need to access them. It doubles as a dependency manager – no need to compute attributes in the correct order in `__init__`. (No circular dependencies, please!)

`@cachedproperty` is a decorator – use it just like `@property`:

```python
from cachedproperty import cachedproperty, ObjectWithCachedProperties

class NetworkUTCTime(ObjectWithCachedProperties):
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
```

...except code won't run more than once!

```python
>>> t = NetworkUTCTime()
>>> t.as_datetime
converting time from str to datetime
getting time from timeapi.org
datetime.datetime(2014, 11, 17, 9, 21, 27, tzinfo=tzutc())
>>> t.as_string
'2014-11-17T09:21:27+00:00'
>>> t.as_datetime
datetime.datetime(2014, 11, 17, 9, 21, 27, tzinfo=tzutc())
```
