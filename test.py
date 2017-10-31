from sounds import Soundex

a = "Robert"
b = "Egbert"
c = "Rupert"

assert Soundex(a) == Soundex(c)
assert Soundex(a) != Soundex(b)
assert Soundex(b) != Soundex(c)
