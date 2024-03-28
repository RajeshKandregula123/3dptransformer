import os
import sys

# Add the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Add the 'lib' directory to the system path
lib_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lib'))
sys.path.append(lib_path)

# Add the 'models' directory to the system path
models_path = os.path.abspath(os.path.join(lib_path, 'models'))
sys.path.append(models_path)

# Add the 'utils' directory to the system path
utils_path = os.path.abspath(os.path.join(lib_path, 'utils'))
sys.path.append(utils_path)
