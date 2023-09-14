# Adds packages to sys.path

import sys
libfolder = __path__ + "/lib"

if libfolder not in sys.path:
    sys.path.append(libfolder)
