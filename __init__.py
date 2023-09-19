import sys
from pathlib import Path

"""Any module that imports this module gets import access to the modules  
in the 'lib' folder. 
(For development it is suggested to add the lib folder to the pythonpath, to
enable cde completion)
"""
cad_bundle_lib = Path(__file__).parent / Path("lib")

if cad_bundle_lib not in sys.path:
    sys.path.append(str(cad_bundle_lib))

