from mcapi import *
from mcapi import _commandMap


custom_commands = [name for name in _commandMap.getKnownCommands() 
                   if name.startswith("minecraftpyserver:") and not name.startswith("minecraftpyserver:py")]
for name in custom_commands:
    print "removing command: %s" % name
    cmd = get_command(name)
    if not cmd: 
        continue

    cmd.unregister(_commandMap)
    _commandMap.getKnownCommands().remove(name)
    for alias in cmd.getAliases():
        _commandMap.getKnownCommands().remove(alias)

remove_event_listeners()
