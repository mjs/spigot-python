from mcapi import *
from time import sleep
from random import randint

from org.bukkit.event.block import BlockDamageEvent
from org.bukkit.event.player import PlayerInteractEntityEvent

remove_event_listeners()

@asynchronous()
def damage_event(e):
    player = e.getPlayer()
    health = player.getHealth()
    player.setHealth(health - 1)
    #b = e.getBlock()

listener = add_event_listener(BlockDamageEvent, damage_event)

#@asynchronous()
#def interact_event(e):
    #yell("interact")

#listener = add_event_listener(PlayerInteractEntityEvent, interact_event)
