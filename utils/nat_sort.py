# ---------------------------------------------------------
# natsort.py: Natural string sorting.
# ---------------------------------------------------------
#
# http://code.activestate.com/recipes/285264-natural-string-sorting/
#
# Credit to original authors: Seo Sanghyeon and Connelly Barnes,

def try_int(s):
    "Convert to integer if possible."
    try: return int(s)
    except: return s

def natsort_key(s):
    "Used internally to get a tuple by which s is sorted."
    import re
    return map(try_int, re.findall(r'(\d+|\D+)', s))

def natcmp(a, b):
    "Natural string comparison, case sensitive."
    return cmp(natsort_key(a), natsort_key(b))

def natcasecmp(a, b):
    "Natural string comparison, ignores case."
    return natcmp(a.lower(), b.lower())

def natsort(seq, cmp=natcmp):
    "In-place natural string sort."
    seq.sort(cmp)
    
def natsorted(seq, cmp=natcmp, key=None):
    "Returns a copy of seq, sorted by natural string sort."
    return sorted(seq, cmp, key)
