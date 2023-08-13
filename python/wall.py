from mcapi import *

@asynchronous()
def cmd_wall(caller, params):
    if len(params) != 1:
        print("expected 1 parameter")
        return

    try:
        size = int(params[0])
    except ValueError:
        print("please give a number")
        return

    beginning = lookingat(caller)
    position = [beginning.x, beginning.y, beginning.z]
    for x in range(size):
        for y in range(size):
            setblock(position)
            position[0] += +1
        position[0] = beginning.x
        position[1] += 1


add_command('wall', cmd_wall)
