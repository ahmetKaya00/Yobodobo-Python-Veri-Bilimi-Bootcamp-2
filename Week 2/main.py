import hesap as h
from hesap import topla

import math
import random
import requests

print(math.sqrt(16))
print(math.pi)

print(random.randint(1,6))

r = requests.get("https://www.google.com")
print(r.status_code)

print(h.topla(3,5))
print(h.carp(3,5))
print(h.PI)