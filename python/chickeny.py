from mcapi import *
from time import sleep
from random import randint

from org.bukkit.event.player import PlayerJoinEvent

@asynchronous()
def join_event(e):
    player = e.getPlayer()
    player_location = location(player)
    player_location.y += 20
    yell("A chickeny hello to player %s" % (player.getName(),))
    for i in range(10):
        spawn(player_location)

listener = add_event_listener(PlayerJoinEvent, join_event)
