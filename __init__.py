# Adds packages to sys.path

import sys
libfolder = __file__[:-11] + "/lib"

if libfolder not in sys.path:
    sys.path.append(libfolder)