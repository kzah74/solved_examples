import function_8_7
print(function_8_7.make_album('tim', 'programmer'))

from function_8_7 import make_album
variable = make_album('andrea', 'programmer', 5)
print(variable)

from function_8_7 import make_album as ma
print(ma('federica', 'beauty', 7))

import function_8_7 as f
print(f.make_album('simon', 'smart homes'))

from function_8_7 import *
variable = make_album('tim', 'programmer', 10)
print(variable)
