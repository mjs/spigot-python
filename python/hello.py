from mcapi import *

@asynchronous()
def cmd_hello(*args):
    print "hello there"

add_command('hello', cmd_hello)
