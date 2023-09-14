import sys

newlib = __file__[:-11] + "/lib"

if newlib not in sys.path:
    sys.path.append(newlib)
