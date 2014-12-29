# Status Effects file!
#  Paralyse, Charm, and Sleep, due to how they interrupt the action flow, will
# stay in battle.rpy as mostly if-else statements.

#####################################################################
# Status Effects - Player
#####################################################################

label battle_call_Player_Status_Check_Block:
# \/  Disabled for now, since it was to avoid issues with attributes getting
# \/ changed up oddly.  Overhaul should fix that.
#    if player.status_poison_duration > 0:
#        if player.status_regen_duration > 0:
#            $ player.status_poison_duration = 0
#            $ player.status_regen_duration = 0
#            "The Poison and Regen cancel each other out, leaving you normal."
#    if player.status_slow_duration > 0:
#        if player.status_haste_duration > 0:
#            $ player.status_slow_duration = 0
#            $ player.status_haste_duration = 0
#            "The Slow and Haste cancel each other out, leaving you normal."
#    if player.status_weaken_duration > 0:
#        if player.status_strengthen_duration > 0:
#            $ player.status_weaken_duration = 0
#            $ player.status_strengthen_duration = 0
#            "The Weaken and Strengthen cancel each other out, leaving you normal."
    call battle_call_Player_Status_PoisonCheck
    call battle_call_Player_Status_RegenCheck
    call battle_call_Player_Status_SlowCheck
    call battle_call_Player_Status_HasteCheck
    call battle_call_Player_Status_WeakenCheck
    call battle_call_Player_Status_StrengthenCheck
    return

label battle_call_Player_Status_PoisonCheck:
    if player.Status_Poison_EffectActive == 1:
        if player.Status_Regen_Duration > 0:
            "You are currently poisoned!"
            call battle_call_Player_HP_Loss(player.Status_Poison_Strength)
            $ player.Status_Poison_Duration -= 1
            "You took [player.Status_Poison_Strength] damage from poison.  [playername!t]'s HP at [player.X_HealthPoints_Current_X].  [player.Status_Poison_Duration] rounds of poison remaining."
            return
        if player.Status_Poison_Duration == 0:
            $ player.Status_Poison_EffectActive = 0
            $ player.Status_Poison_Strength = 0
            "You feel the poison fade from your body."
    return

label battle_call_Player_Status_RegenCheck:
    if player.Status_Regen_EffectActive == 1:
        if player.Status_Regen_Duration > 0:
            "You are currently regenerating!"
            call battle_call_Player_HP_Gain(player.Status_Regen_Strength)
            $ player.Status_Regen_Duration -= 1
            "You healed [player.Status_Regen_Strength] damage due to regeneration.  [playername!t]'s HP at [player.X_HealthPoints_Current_X].  [player.Status_Regen_Duration] rounds of Regen remaining."
            return
        if player.Status_Regen_Duration == 0:
            $ player.Status_Regen_EffectActive = 0
            $ player.Status_Regen_Strength = 0
            "You feel the healing effects of Regen fade from your body."
    return

label battle_call_Player_Status_SlowCheck:
    if player.Status_Slow_EffectActive == 1:
        if player.Status_Slow_Duration > 0:
            "You are currently slowed!"
            call battle_call_Dodge_Recheck
            call battle_call_Initiative_Recheck
            $ player.Status_Slow_Duration -= 1
            "Your dodge and initative are [player.Status_Slow_Strength] points worse due to slow.  [player.Status_Slow_Duration] rounds of Slow remaining."
            return
        if player.Status_Slow_Duration == 0:
            $ player.Status_Slow_EffectActive = 0
            $ player.Status_Slow_Strength = 0
            call battle_call_Dodge_Recheck
            call battle_call_Initiative_Recheck
            "You feel yourself speeding up to normal as Slow wears off."
    return

label battle_call_Player_Status_HasteCheck:
    if player.Status_Haste_EffectActive == 1:
        if player.Status_Haste_Duration > 0:
            "You are currently hasted!"
            call battle_call_Dodge_Recheck
            call battle_call_Initiative_Recheck
            $ player.Status_Haste_Duration -= 1
            "Your dodge and initiative are [player.Status_Haste_Strength] points better due to haste.  [player.Status_Haste_Duration] rounds of Haste remaining."
            return
        if player.Status_Haste_Duration == 0:
            $ player.Status_Haste_EffectActive = 0
            $ player.Status_Haste_Strength = 0
            call battle_call_Dodge_Recheck
            call battle_call_Initiative_Recheck
            "You feel yourself slowing down to normal as Haste wears off."
    return

label battle_call_Player_Status_WeakenCheck:
    if player.Status_Weaken_EffectActive == 1:
        if player.Status_Weaken_Duration > 0:
            "You are currently weakened!"
            call battle_call_Damage_Melee_Recheck
            call battle_call_Damage_Ranged_Recheck
            $ player.Status_Weaken_Duration -= 1
            "You damage is [player.Status_Weaken_Strength] points worse due to weaken.  [player.Status_Weaken_Duration] rounds of Weaken remaining."
            return
        if player.Status_Weaken_Duration == 0:
            $ player.Status_Weaken_EffectActive = 0
            $ player.Status_Weaken_Strength = 0
            call battle_call_Damage_Melee_Recheck
            call battle_call_Damage_Ranged_Recheck
            "You feel your strength returning to normal as Weaken wears off."
    return

label battle_call_Player_Status_StrengthenCheck:
    if player.Status_Strengthen_EffectActive == 1:
        if player.Status_Strengthen_Duration > 0:
            "You are currently strengthed!"
            call battle_call_Damage_Melee_Recheck
            call battle_call_Damage_Ranged_Recheck
            $ player.Status_Strengthen_Duration -= 1
            "You damage is [player.Status_Strengthen_Strength] points better due to strengthen.  [player.Status_Strengthen_Duration] rounds of Strengthen remaining."
            return
        if player.Status_Strengthen_Duration == 0:
            $ player.Status_Strengthen_EffectActive = 0
            $ player.Status_Strengthen_Strength = 0
            call battle_call_Damage_Melee_Recheck
            call battle_call_Damage_Ranged_Recheck
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
