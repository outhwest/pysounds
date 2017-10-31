from sounds import Soundex

a = "Robert"
b = "Egbert"
c = "Rupert"
d = "Ashcraft"
e = "Ashcroft"
f = "Tymczak"

assert Soundex(a) == Soundex(c)
assert Soundex(a) != Soundex(b)
assert Soundex(b) != Soundex(c)
assert Soundex(d) == Soundex(e)
assert Soundex(d) == "A261"
assert Soundex(f) == "T522"
