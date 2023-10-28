from mcapi import *
from time import sleep
from random import choice

from org.bukkit import World
from org.bukkit.event.block import BlockDamageEvent
from org.bukkit.inventory import ItemStack

remove_event_listeners()

#JOHN_WICK = [Material.BARRIER, Material.GOAT_HORN, Material.FIREWORK_ROCKET, Material.GLASS_BOTTLE]

#@asynchronous()
def block_damage_event(e):

    block = e.getBlock()
    block.setType(Material.TNT)


listener = add_event_listener(BlockDamageEvent, block_damage_event)







#def block_damage_event(e):
    #item = ItemStack(choice(JOHN_WICK))

    #block = e.getBlock()
    #world = block.getWorld()
    #world.dropItem(block.getLocation(), item, None)


#listener = add_event_listener(BlockDamageEvent, block_damage_event)
