from sounds import Soundex, Metaphone, isHomophone
from functools import partial

soundFromStart = partial(Soundex, start=True)

a = "Robert"
b = "Egbert"
c = "Rupert"
d = "Ashcraft"
e = "Ashcroft"
f = "Tymczak"
g = "fat"
h = "phat"

assert isHomophone(a,c)
assert not isHomophone(a,b)
assert not isHomophone(b,c)
assert isHomophone(d,e)

assert Soundex(d) == "A261"
assert Soundex(f) == "T522"
assert not isHomophone(g,h)

assert isHomophone(g,h,algorithm=soundFromStart)

assert isHomophone(d,e, algorithm=Metaphone)
assert isHomophone(a,b, algorithm=Metaphone)
assert isHomophone(g,h, algorithm=Metaphone)
