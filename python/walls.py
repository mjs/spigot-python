from mcapi import *

def make_wall(start, xsize, ysize, zsize, mat):
    for x in range(xsize+1):
        for y in range(ysize+1):
            for z in range(zsize+1):
                pos = [start[0] + x, start[1] + y, start[2] + z]
                setblock(pos, type=mat)


@asynchronous()
def cmd_walls(caller, params):
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

    block = lookingat(caller)
    pos = [block.x, block.y, block.z]

    mat = Material.COBBLESTONE

    make_wall(pos, 0, sizey, sizez, mat)
    make_wall(pos, sizex, 0, sizez, mat)
    make_wall(pos, sizex, sizey, 0, mat)

    pos = [block.x + sizex, block.y, block.z]
    make_wall(pos, 0, sizey, sizez, mat)

    pos = [block.x, block.y + sizey, block.z]
    make_wall(pos, sizex, 0, sizez, mat)

    pos = [block.x, block.y, block.z + sizez]
    make_wall(pos, sizex, sizey, 0, mat)


add_command('walls', cmd_walls)
