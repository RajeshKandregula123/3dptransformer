
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os.path as osp
import sys


def add_path(path):
    if path not in sys.path:
        sys.path.insert(0, path)

import os
this_dir = os.dirname(r'C:\Users\new user\Desktop\mvp-main\lib')
#lib_path = os.path.abspath(os.path.join(os.path.dirname(r'C:\Users\new user\Desktop\mvp-main\lib'), r'..', 'lib'))
#sys.path.append(lib_path)
lib_path = osp.join(this_dir, r'C:\Users\new user\Desktop\mvp-main\lib', 'lib')

#models_path = osp.join(this_dir, r'C:\Users\new user\Desktop\mvp-main\lib\models', 'models')
add_path(lib_path)
#add_path(models_path)
#sys.path.append(r'C:\Users\new user\Desktop\mvp-main\lib')
#sys.path.append(r'C:\Users\new user\Desktop\mvp-main\lib\models')








import os
import sys

# Add the parent directory to the system path
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(), '..')))

# Add the 'models' directory to the system path
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'models')))
