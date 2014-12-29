# Just a collection of little calls here.

#####################################################################
# Variable Min-Max Stops
#####################################################################

#  These are to keep the numbers 'tidy', and make it so your bars don't get all weird
# from negative numbers, keep people from overhealing, etc.  Several aren't needed
# yet, but it seemed a good idea to get them ready ahead of time.

label battle_call_Player_HP_Loss(hploss):
    if player.status_charm_duration > 0:
        "Taking damage breaks the Charm!"
        $ player.status_charm_duration = 0
    if player.status_sleep_duration > 0:
        "Taking damage wakes you from Sleep!"
        $ player.status_sleep_duration = 0
    $ player.hp_c -= hploss
    if player.hp_c < 0:
        $ player.hp_c = 0
    return

label battle_call_Player_HP_Gain(hpgain):
    $ player.hp_c += hpgain
    if player.hp_c > player.hp_m:
        $ player.hp_c = player.hp_m
    return

label battle_call_Player_AP_Loss(aploss):
    $ player.ap_c -= aploss
    if player.ap_c < 0:
        $ player.ap_c = 0
    return

label battle_call_Player_AP_Gain(apgain):
    $ player.ap_c += apgain
    if player.ap_c > player.ap_m:
        $ player.ap_c = player.ap_m
    return

label battle_call_Enemy_HP_Loss(hploss):
    if enemy.status_charm_duration > 0:
        "Taking damage breaks the Charm on [enemy.name!t]!"
        $ enemy.status_charm_duration = 0
    if enemy.status_sleep_duration > 0:
        "Taking damage wakes [enemy.name!t] from Sleep!"
        $ enemy.status_sleep_duration = 0
    $ enemy.hp_c -= hploss
    if enemy.hp_c < 0:
        $ enemy.hp_c = 0
    return

label battle_call_Enemy_HP_Gain(hpgain):
    $ enemy.hp_c += hpgain
    if enemy.hp_c > enemy.hp_m:
        $ enemy.hp_c = enemy.hp_m
    return

label battle_call_Enemy_AP_Loss(aploss):
    $ enemy.ap_c -= aploss
    if enemy.ap_c < 0:
        $ enemy.ap_c = 0
    return

label battle_call_Enemy_AP_Gain(apgain):
    $ enemy.ap_c += apgain
    if enemy.ap_c > enemy.ap_m:
        $ enemy.ap_c = enemy.ap_m
    return

#####################################################################
# Stat and Attribute Bonus Setting
#####################################################################

# These will be changed later, once the stat system and equipment system are in.

# For now though, it's basically
# Current (to be referenced almost everywhere) = (Base)+(Buffs)-(Debuffs)
# 'damage_max_current = (damage_max)+(strengthen.strength)-(weaken.strength)
# Accessed via a call anytime something would change the number, and thusly recalculated.

#####################################################################

