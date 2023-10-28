from mcapi import *
from time import sleep
from random import random

from org.bukkit.event.block import BlockDamageEvent
from org.bukkit.inventory import ItemStack


remove_event_listeners()

def block_damage_event(e):
    block = e.getBlock()
    world = block.getWorld()

    if random() < 0.5:
        world.spawnEntity(block.getLocation(), EntityType.PRIMED_TNT)
    else:
        item = ItemStack(Material.GOLDEN_CARROT)
        world.dropItemNaturally(block.getLocation(), item, None)


listener = add_event_listener(BlockDamageEvent, block_damage_event)

