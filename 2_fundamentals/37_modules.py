# Modules - any .py file is a module you can import.
# dog.py sits in this same folder and defines bark().

import dog
dog.bark()

from dog import bark
bark()

# Standard library modules
import math
from math import sqrt
print(math.pi, sqrt(4))

# Modules in a sub-folder (a package) are imported with dots:
#   from lib import dog      (needs a lib/ folder containing dog.py)
