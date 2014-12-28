# Just a collection of little calls here.

#####################################################################
# Status Effects - Player
#####################################################################

label battle_call_Player_Status_Check_Block:
    if player.status_poison_duration > 0:
        if player.status_regen_duration > 0:
            $ player.status_poison_duration = 0
            $ player.status_regen_duration = 0
            "The Poison and Regen cancel each other out, leaving you normal."
    if player.status_slow_duration > 0:
        if player.status_haste_duration > 0:
            $ player.status_slow_duration = 0
            $ player.status_haste_duration = 0
            "The Slow and Haste cancel each other out, leaving you normal."
    if player.status_weaken_duration > 0:
        if player.status_strengthen_duration > 0:
            $ player.status_weaken_duration = 0
            $ player.status_strengthen_duration = 0
            "The Weaken and Strengthen cancel each other out, leaving you normal."
    call battle_call_Player_Status_PoisonCheck
    call battle_call_Player_Status_RegenCheck
    call battle_call_Player_Status_SlowCheck
    call battle_call_Player_Status_HasteCheck
    call battle_call_Player_Status_WeakenCheck
    call battle_call_Player_Status_StrengthenCheck
    return

label battle_call_Player_Status_PoisonCheck:
    if player.status_poison_duration > 0:
        "You are currently poisoned!"
        call battle_call_Player_HP_Loss(player.status_poison_strength)
        $ player.status_poison_duration -= 1
        "You took [player.status_poison_strength] damage from poison.  [playername!t]'s HP at [player.hp_c]."
        return
    else:
        if player.status_poison_strength > 0:
            $ player.status_poison_strength = 0
            "You feel the poison fade from your body."
        return

label battle_call_Player_Status_RegenCheck:
    if player.status_regen_duration > 0:
        "You are currently regenerating!"
        call battle_call_Player_HP_Gain(player.status_regen_strength)
        $ player.status_regen_duration -= 1
        "You healed [player.status_regen_strength] damage due to regeneration.  [playername!t]'s HP at [player.hp_c]."
        return
    else:
        if player.status_regen_strength > 0:
            $ player.status_regen_strength = 0
            "You feel the healing effects of Regen fade from your body."
        return

label battle_call_Player_Status_SlowCheck:
    if player.status_slow_duration > 0:
        "You are currently slowed!"
        if player.initiative_mod_temp == 0:
            $ player.initiative_mod_temp = player.initiative_mod
            $ player.dodge_temp = player.dodge
            $ player.initiative_mod -= player.status_slow_strength
            $ player.dodge -= player.status_slow_strength
        $ player.status_slow_duration -= 1
        "Your dodge and initative are [player.status_slow_strength] points worse due to slow."
        return
    else:
        if player.status_slow_strength > 0:
            $ player.initiative_mod = player.initiative_mod_temp
            $ player.dodge = player.dodge_temp
            $ player.status_slow_strength = 0
            "You feel yourself speeding up to normal as Slow wears off."
        return

label battle_call_Player_Status_HasteCheck:
    if player.status_haste_duration > 0:
        "You are currently hasted!"
        if player.initiative_mod_temp == 0:
            $ player.initiative_mod_temp = player.initiative_mod
            $ player.dodge_temp = player.dodge
            $ player.initiative_mod += player.status_haste_strength
            $ player.dodge += player.status_haste_strength
        $ player.status_haste_duration -= 1
        "Your dodge and initiative are [player.status_haste_strength] points better due to haste."
        return
    else:
        if player.status_haste_strength > 0:
            $ player.initiative_mod = player.initiative_mod_temp
            $ player.dodge = player.dodge_temp
            $ player.status_haste_strength = 0
            "You feel yourself slowing down to normal as Haste wears off."
        return

label battle_call_Player_Status_WeakenCheck:
    if player.status_weaken_duration > 0:
        "You are currently weakened!"
        if player.damage_melee_max_temp == 0:
            $ player.damage_melee_max_temp = player.damage_melee_max
            $ player.damage_melee_min_temp = player.damage_melee_min
            $ player.damage_melee_min -= player.status_weaken_strength/2
            if player.damage_melee_min < 1:
                $ player.damage_melee_min = 1
            $ player.damage_melee_min -= player.status_weaken_strength
            if player.damage_melee_max < player.damage_melee_min:
                $ player.damage_melee_max = player.damage_melee_min
        $ player.status_weaken_duration -= 1
        "You damage is [player.status_weaken_strength] points worse due to weaken."
        return
    else:
        if player.status_weaken_strength > 0:
            $ player.damage_melee_max = player.damage_melee_max_temp
            $ player.damage_melee_min = player.damage_melee_min_temp
            $ player.status_weaken_strength = 0
            "You feel your strength returning to normal as Weaken wears off."
        return

label battle_call_Player_Status_StrengthenCheck:
    if player.status_strengthen_duration > 0:
        "You are currently strengthed!"
        if player.damage_melee_max_temp == 0:
            $ player.damage_melee_max_temp = player.damage_melee_max
            $ player.damage_melee_min_temp = player.damage_melee_min
            $ player.damage_melee_min += player.status_strengthen_strength/2
            $ player.damage_melee_max += player.status_strengthen_strength
        $ player.status_strengthen_duration -= 1
        "You damage is [player.status_strengthen_strength] points better due to strengthen."
        return
    else:
        if player.status_strengthen_strength > 0:
            $ player.damage_melee_max = player.damage_melee_max_temp
            $ player.damage_melee_min = player.damage_melee_min_temp
            $ player.status_strengthen_strength = 0
            "You feel your strength returning to normal as Strengthen wears off."
        return

#label battle_call_Player_Status_EquipLoss_WeaponCheck:
#label battle_call_Player_Status_EquipLoss_ArmorCheck:

#label battle_call_Player_Status_Block:
#label battle_call_Player_Status_Dodge:

#####################################################################
# Status Effects - Enemy
#####################################################################

label battle_call_Enemy_Status_Check_Block:
    if enemy.status_poison_duration > 0:
        if enemy.status_regen_duration > 0:
            $ enemy.status_poison_duration = 0
            $ enemy.status_regen_duration = 0
            "The Poison and Regen cancel each other out, leaving [enemy.name!t] normal."
    if enemy.status_slow_duration > 0:
        if enemy.status_haste_duration > 0:
            $ enemy.status_slow_duration = 0
            $ enemy.status_haste_duration = 0
            "The Slow and Haste cancel each other out, leaving [enemy.name!t] normal."
    if enemy.status_weaken_duration > 0:
        if enemy.status_strengthen_duration > 0:
            $ enemy.status_weaken_duration = 0
            $ enemy.status_strengthen_duration = 0
            "The Weaken and Strengthen cancel each other out, leaving [enemy.name!t] normal."
    call battle_call_Enemy_Status_PoisonCheck
    call battle_call_Enemy_Status_RegenCheck
    call battle_call_Enemy_Status_SlowCheck
    call battle_call_Enemy_Status_HasteCheck
    call battle_call_Enemy_Status_WeakenCheck
    call battle_call_Enemy_Status_StrengthenCheck
    return

label battle_call_Enemy_Status_PoisonCheck:
    if enemy.status_poison_duration > 0:
        "[enemy.name!t] is currently poisoned!"
        call battle_call_Enemy_HP_Loss(enemy.status_poison_strength)
        $ enemy.status_poison_duration -= 1
        "[enemy.name!t] took [enemy.status_poison_strength] damage from poison.  [enemy.name!t]'s HP at [enemy.hp_c]."
        return
    else:
        if enemy.status_poison_strength > 0:
            $ enemy.status_poison_strength = 0
            "[enemy.name!t] feels the poison fade from their body."
        return

label battle_call_Enemy_Status_RegenCheck:
    if enemy.status_regen_duration > 0:
        "[enemy.name!t] is currently regenerating!"
        call battle_call_Enemy_HP_Gain(enemy.status_regen_strength)
        $ enemy.status_regen_duration -= 1
        "[enemy.name!t] healed [enemy.status_regen_strength] damage due to regeneration.  [enemy.name!t]'s HP at [enemy.hp_c]."
        return
    else:
        if enemy.status_regen_strength > 0:
            $ enemy.status_regen_strength = 0
            "[enemy.name!t] feels the healing effects of Regen fade from their body."
        return

label battle_call_Enemy_Status_SlowCheck:
    if enemy.status_slow_duration > 0:
        "[enemy.name!t] is currently slowed!"
        if enemy.initiative_mod_temp == 0:
            $ enemy.initiative_mod_temp = enemy.initiative_mod
            $ enemy.dodge_temp = enemy.dodge
            $ enemy.initiative_mod -= enemy.status_slow_strength
            $ enemy.dodge -= enemy.status_slow_strength
        $ enemy.status_slow_duration -= 1
        "[enemy.name!t]'s dodge and initative are [enemy.status_slow_strength] points worse due to slow."
        return
    else:
        if enemy.status_slow_strength > 0:
            $ enemy.initiative_mod = enemy.initiative_mod_temp
            $ enemy.dodge = enemy.dodge_temp
            $ enemy.status_slow_strength = 0
            "[enemy.name!t] feels themself speeding up to normal as Slow wears off."
        return

label battle_call_Enemy_Status_HasteCheck:
    if enemy.status_haste_duration > 0:
        "[enemy.name!t] is currently hasted!"
        if enemy.initiative_mod_temp == 0:
            $ enemy.initiative_mod_temp = enemy.initiative_mod
            $ enemy.dodge_temp = enemy.dodge
            $ enemy.initiative_mod += enemy.status_haste_strength
            $ enemy.dodge += enemy.status_haste_strength
        $ enemy.status_haste_duration -= 1
        "[enemy.name!t]'s dodge and initiative are [enemy.status_haste_strength] points better due to haste."
        return
    else:
        if enemy.status_haste_strength > 0:
            $ enemy.initiative_mod = enemy.initiative_mod_temp
            $ enemy.dodge = enemy.dodge_temp
            $ enemy.status_haste_strength = 0
            "[enemy.name!t] feels themself slowing down to normal as Haste wears off."
        return

label battle_call_Enemy_Status_WeakenCheck:
    if enemy.status_weaken_duration > 0:
        "[enemy.name!t] is currently weakened!"
        if enemy.damage_melee_max_temp == 0:
            $ enemy.damage_melee_max_temp = enemy.damage_melee_max
            $ enemy.damage_melee_min_temp = enemy.damage_melee_min
            $ enemy.damage_melee_min -= enemy.status_weaken_strength/2
            if enemy.damage_melee_min < 1:
                $ enemy.damage_melee_min = 1
            $ enemy.damage_melee_min -= enemy.status_weaken_strength
            if enemy.damage_melee_max < enemy.damage_melee_min:
                $ enemy.damage_melee_max = enemy.damage_melee_min
        $ enemy.status_weaken_duration -= 1
        "[enemy.name!t]'s damage is [enemy.status_weaken_strength] points worse due to weaken."
        return
    else:
        if enemy.status_weaken_strength > 0:
            $ enemy.damage_melee_max = enemy.damage_melee_max_temp
            $ enemy.damage_melee_min = enemy.damage_melee_min_temp
            $ enemy.status_weaken_strength = 0
            "[enemy.name!t] feels their strength returning to normal as Weaken wears off."
        return

label battle_call_Enemy_Status_StrengthenCheck:
    if enemy.status_strengthen_duration > 0:
        "[enemy.name!t] is currently strengthed!"
        if enemy.damage_melee_max_temp == 0:
            $ enemy.damage_melee_max_temp = enemy.damage_melee_max
            $ enemy.damage_melee_min_temp = enemy.damage_melee_min
            $ enemy.damage_melee_min += enemy.status_strengthen_strength/2
            $ enemy.damage_melee_max += enemy.status_strengthen_strength
        $ enemy.status_strengthen_duration -= 1
        "[enemy.name!t]'s damage is [enemy.status_strengthen_strength] points better due to strengthen."
        return
    else:
        if enemy.status_strengthen_strength > 0:
            $ enemy.damage_melee_max = enemy.damage_melee_max_temp
            $ enemy.damage_melee_min = enemy.damage_melee_min_temp
            $ enemy.status_strengthen_strength = 0
            "[enemy.name!t] feel their strength returning to normal as Strengthen wears off."
        return

#label battle_call_Enemy_Status_EquipLoss_WeaponCheck:
#label battle_call_Enemy_Status_EquipLoss_ArmorCheck:


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

