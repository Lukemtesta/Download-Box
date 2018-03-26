'''
external_space.py

Tool to query mounted disk and system available diskspace on a Linux machine. 
Notifies when the disk space has exceeded a threshold
'''

import sys
import argparse
import traceback

from logger import Logger
from argument_parser import parse_arguments

from external_space_defines import *
from memory_utilities import *
from email_utilities import send_report, send_mail

'''
Global definitions
'''
global_logger = Logger(__file__)


'''
Main entry point
'''
if __name__ == "__main__":

    log_filename = global_logger.create_name_from_filename(__file__)

    global_logger.register_global_file(log_filename)
    global_logger.log('----- Starting -----')
    
    # Parse command line arguments
    cmdargs = parse_arguments()
    
    try:        

        _, _, canuse = get_dir_space(DIR_PATH_MOUNTED_DISK) 

        if(canuse < MIN_FREE_DISK_SPACE_ALLOWED_GB):
                        
            show_dir_space(DIR_PATH_MOUNTED_DISK)
            
            msg = 'Filespace exceeded. ' + get_dir_space_descriptor(DIR_PATH_MOUNTED_DISK) 

            if cmdargs.email:
                global_logger.log('Sending email to', cmdargs.email)
                send_mail(cmdargs.email, msg)
                send_mail(cmdargs.email, msgsys)
	
    except:        
        global_logger.log('Exception: ', sys.exc_info(), traceback.format_exc())
        if cmdargs.email:
            send_report(log_filename, cmdargs.email)
