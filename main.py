# Imports of required files.
import site
# Defining the project path for imports.
site.addsitedir('/')
# Continued import of required files.
from functions.init import *
from functions.config import *

# Viewing program information.
init()
# Start of the configuration required to generate one or more passwords.
config()