from mcapi import *

from org.bukkit.event.block import BlockDamageEvent

remove_event_listeners()

@asynchronous()
def damage_event(e):
    player = e.getPlayer()
    health = player.getHealth()
    player.setHealth(health - 1)
    print("ow!")

listener = add_event_listener(BlockDamageEvent, damage_event)

