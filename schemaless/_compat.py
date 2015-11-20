import sys

PY2 = sys.version_info[0] == 2

if not PY2:
    iterkeys = lambda d: iter(d.keys())
    itervalues = lambda d: iter(d.values())
    iteritems = lambda d: iter(d.items())

def to_bytes(bytes_or_str, encoding='utf-8'):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode(encoding)
    else:
        value = bytes_or_str
    return value # Instance of bytes

def to_string(bytes_or_str, encoding='utf-8'):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode(encoding)
    else:
        value = bytes_or_str
    return value # Instance of bytes