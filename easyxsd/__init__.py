try:                                                                            
    __version__ = \
        __import__('pkg_resources').get_distribution('easyxsd').version
except Exception:                                                               
     __version__ = 'unknown'

from easyxsd.utils import *
