'''
memory_utilities.py

General memory helpers
'''

import os
import sys

from logger import Logger

'''
Global definitions
'''
global_logger = Logger(__file__)


'''
Query disk space information for a directory in GB
'''
def get_dir_space(dir):

    stats = os.statvfs(dir)
    total = stats.f_frsize * stats.f_blocks
    free = stats.f_frsize * stats.f_bfree
    available = stats.f_frsize * stats.f_bavail    

    return total / 1e9, free / 1e9, available / 1e9
    
def show_dir_space(dir):
    
    msg = get_dir_space_descriptor(dir)
    global_logger.log('Directory memory stats for', dir, msg)

def get_dir_space_descriptor(dir):

    return 'Total: ' + str(total) + 'GB, free: ' + str(free) + 'GB, available: ' + str(avail) + 'GB'

    
    
