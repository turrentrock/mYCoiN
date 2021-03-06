import sys
from  glob import glob
import os

EXPECTED_DEPENDENCIES_PATH = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
assert(glob(EXPECTED_DEPENDENCIES_PATH+'/BlockChainPackage') != [])
if EXPECTED_DEPENDENCIES_PATH not in sys.path: 
    sys.path.append(EXPECTED_DEPENDENCIES_PATH)

import datetime
from collections import OrderedDict
import mongoengine

from typing import List, Set, Dict, Tuple, Optional