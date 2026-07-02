# Built-in Modules

import math
import random

print(math.sqrt(16))
print(random.randint(1,10))

#Own Modules
#the new file ca be created in the name of modulespractice.py,then we have to import from that file.

from modulespractice import validate_status
print(validate_status(200,200))
print(validate_status(200,400))