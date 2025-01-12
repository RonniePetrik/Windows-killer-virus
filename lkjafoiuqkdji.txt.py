#!/usr/bin/python

import time
import string
import os
import random
time.sleep(1.89)
proceed_input = input('This is malware, and it will delete your operating system, do you want to continue? yes/no')


while True:
    if proceed_input == ('no'):
        print('program stopped')
        break
    else:
        print('DO YOU REALLY WANT TO CONTINUE, THIS WILL DELETE YOUR OS.')
        proceed_input_2 = input('yes/no')
        if proceed_input_2 == input('no'):
            print('program stopped')
            break
        else:
            file_path = 'Windows'
            os.remove(file_path)
            
            
            
            
           
