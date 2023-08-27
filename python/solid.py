from mcapi import *


@asynchronous()
def cmd_solid(caller, params):
    if len(params) != 3:
        print("expected 3 parameter")
        return

    try:
        sizex = int(params[0])
        sizey = int(params[1])
        sizez = int(params[2])
    except ValueError:
        print("please give a number")
        return

    beginning = lookingat(caller)
    position = [beginning.x, beginning.y, beginning.z]
    for x in range(sizex):
        for y in range(sizey):
            for z in range(sizez):
                setblock(position, type = Material.CHERRY_PLANKS)
                position[2] += 1
            position[2] = beginning.z
            position[1] += 1
        position[1] = beginning.y
        position[0] += 1


add_command('solid', cmd_solid)
