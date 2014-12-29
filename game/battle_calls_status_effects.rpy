# Status Effects file!
#  Paralyse, Charm, and Sleep, due to how they interrupt the action flow, will
# stay in battle.rpy as mostly if-else statements.

#####################################################################
# Status Effects - Player
#####################################################################

label battle_call_Player_Status_Check_Block:
# \/  Disabled for now, since it was to avoid issues with attributes getting
# \/ changed up oddly.  Overhaul should fix that.
#    if player.Status_Poison_Duration > 0:
#        if player.Status_Regen_Duration > 0:
#            $ player.Status_Poison_Duration = 0
#            $ player.Status_Regen_Duration = 0
#            "The Poison and Regen cancel each other out, leaving you normal."
#    if player.Status_Slow_Duration > 0:
#        if player.Status_Haste_Duration > 0:
#            $ player.Status_Slow_Duration = 0
#            $ player.Status_Haste_Duration = 0
#            "The Slow and Haste cancel each other out, leaving you normal."
#    if player.Status_Weaken_Duration > 0:
#        if player.Status_Strengthen_Duration > 0:
#            $ player.Status_Weaken_Duration = 0
#            $ player.Status_Strengthen_Duration = 0
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
            call battle_call_Player_Dodge_Recheck
            call battle_call_Player_Initiative_Recheck
            $ player.Status_Slow_Duration -= 1
            "Your dodge and initative are [player.Status_Slow_Strength] points worse due to slow.  [player.Status_Slow_Duration] rounds of Slow remaining."
            return
        if player.Status_Slow_Duration == 0:
            $ player.Status_Slow_EffectActive = 0
            $ player.Status_Slow_Strength = 0
            call battle_call_Player_Dodge_Recheck
            call battle_call_Player_Initiative_Recheck
            "You feel yourself speeding up to normal as Slow wears off."
    return

label battle_call_Player_Status_HasteCheck:
    if player.Status_Haste_EffectActive == 1:
        if player.Status_Haste_Duration > 0:
            "You are currently hasted!"
            call battle_call_Player_Dodge_Recheck
            call battle_call_Player_Initiative_Recheck
            $ player.Status_Haste_Duration -= 1
            "Your dodge and initiative are [player.Status_Haste_Strength] points better due to haste.  [player.Status_Haste_Duration] rounds of Haste remaining."
            return
        if player.Status_Haste_Duration == 0:
            $ player.Status_Haste_EffectActive = 0
            $ player.Status_Haste_Strength = 0
            call battle_call_Player_Dodge_Recheck
            call battle_call_Player_Initiative_Recheck
            "You feel yourself slowing down to normal as Haste wears off."
    return

label battle_call_Player_Status_WeakenCheck:
    if player.Status_Weaken_EffectActive == 1:
        if player.Status_Weaken_Duration > 0:
            "You are currently weakened!"
            call battle_call_Player_Damage_Melee_Recheck
            call battle_call_Player_Damage_Ranged_Recheck
            $ player.Status_Weaken_Duration -= 1
            "You damage is [player.Status_Weaken_Strength] points worse due to weaken.  [player.Status_Weaken_Duration] rounds of Weaken remaining."
            return
        if player.Status_Weaken_Duration == 0:
            $ player.Status_Weaken_EffectActive = 0
            $ player.Status_Weaken_Strength = 0
            call battle_call_Player_Damage_Melee_Recheck
            call battle_call_Player_Damage_Ranged_Recheck
            "You feel your strength returning to normal as Weaken wears off."
    return

label battle_call_Player_Status_StrengthenCheck:
    if player.Status_Strengthen_EffectActive == 1:
        if player.Status_Strengthen_Duration > 0:
            "You are currently strengthed!"
            call battle_call_Player_Damage_Melee_Recheck
            call battle_call_Player_Damage_Ranged_Recheck
            $ player.Status_Strengthen_Duration -= 1
            "You damage is [player.Status_Strengthen_Strength] points better due to strengthen.  [player.Status_Strengthen_Duration] rounds of Strengthen remaining."
            return
        if player.Status_Strengthen_Duration == 0:
            $ player.Status_Strengthen_EffectActive = 0
            $ player.Status_Strengthen_Strength = 0
            call battle_call_Player_Damage_Melee_Recheck
            call battle_call_Player_Damage_Ranged_Recheck
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
# \/  Disabled for now, since it was to avoid issues with attributes getting
# \/ changed up oddly.  Overhaul should fix that.
#    if enemy.Status_Poison_Duration > 0:
#        if enemy.Status_Regen_Duration > 0:
#            $ enemy.Status_Poison_Duration = 0
#            $ enemy.Status_Regen_Duration = 0
#            "The Poison and Regen cancel each other out, leaving [enemy.name!t] normal."
#    if enemy.Status_Slow_Duration > 0:
#        if enemy.Status_Haste_Duration > 0:
#            $ enemy.Status_Slow_Duration = 0
#            $ enemy.Status_Haste_Duration = 0
#            "The Slow and Haste cancel each other out, leaving [enemy.name!t] normal."
#    if enemy.Status_Weaken_Duration > 0:
#        if enemy.Status_Strengthen_Duration > 0:
#            $ enemy.Status_Weaken_Duration = 0
#            $ enemy.Status_Strengthen_Duration = 0
#            "The Weaken and Strengthen cancel each other out, leaving [enemy.name!t] normal."
    call battle_call_Enemy_Status_PoisonCheck
    call battle_call_Enemy_Status_RegenCheck
    call battle_call_Enemy_Status_SlowCheck
    call battle_call_Enemy_Status_HasteCheck
    call battle_call_Enemy_Status_WeakenCheck
    call battle_call_Enemy_Status_StrengthenCheck
    return

label battle_call_Enemy_Status_PoisonCheck:
    if enemy.Status_Poison_EffectActive == 1:
        if enemy.Status_Regen_Duration > 0:
            "[enemy.name!t] is currently poisoned!"
            call battle_call_Enemy_HP_Loss(enemy.Status_Poison_Strength)
            $ enemy.Status_Poison_Duration -= 1
            "[enemy.name!t] took [enemy.Status_Poison_Strength] damage from poison.  [enemy.name!t]'s HP at [enemy.X_HealthPoints_Current_X].  [enemy.Status_Poison_Duration] rounds of poison remaining."
            return
        if enemy.Status_Poison_Duration == 0:
            $ enemy.Status_Poison_EffectActive = 0
            $ enemy.Status_Poison_Strength = 0
            "[enemy.name!t] feels the poison fade from their body."
    return

label battle_call_Enemy_Status_RegenCheck:
    if enemy.Status_Regen_EffectActive == 1:
        if enemy.Status_Regen_Duration > 0:
            "[enemy.name!t] is currently regenerating!"
            call battle_call_Enemy_HP_Gain(enemy.Status_Regen_Strength)
            $ enemy.Status_Regen_Duration -= 1
            "[enemy.name!t] healed [enemy.Status_Regen_Strength] damage due to regeneration.  [enemy.name!t]'s HP at [enemy.X_HealthPoints_Current_X].  [enemy.Status_Regen_Duration] rounds of Regen remaining."
            return
        if enemy.Status_Regen_Duration == 0:
            $ enemy.Status_Regen_EffectActive = 0
            $ enemy.Status_Regen_Strength = 0
            "[enemy.name!t] feels the healing effects of Regen fade from their body."
    return

label battle_call_Enemy_Status_SlowCheck:
    if enemy.Status_Slow_EffectActive == 1:
        if enemy.Status_Slow_Duration > 0:
            "[enemy.name!t] is currently slowed!"
            call battle_call_Enemy_Dodge_Recheck
            call battle_call_Enemy_Initiative_Recheck
            $ enemy.Status_Slow_Duration -= 1
            "[enemy.name!t]'s dodge and initative are [enemy.Status_Slow_Strength] points worse due to slow.  [enemy.Status_Slow_Duration] rounds of Slow remaining."
            return
        if enemy.Status_Slow_Duration == 0:
            $ enemy.Status_Slow_EffectActive = 0
            $ enemy.Status_Slow_Strength = 0
            call battle_call_Enemy_Dodge_Recheck
            call battle_call_Enemy_Initiative_Recheck
            "[enemy.name!t] feels themself speeding up to normal as Slow wears off."
    return

label battle_call_Enemy_Status_HasteCheck:
    if enemy.Status_Haste_EffectActive == 1:
        if enemy.Status_Haste_Duration > 0:
            "[enemy.name!t] is currently hasted!"
            call battle_call_Enemy_Dodge_Recheck
            call battle_call_Enemy_Initiative_Recheck
            $ enemy.Status_Haste_Duration -= 1
            "[enemy.name!t]'s dodge and initiative are [enemy.Status_Haste_Strength] points better due to haste.  [enemy.Status_Haste_Duration] rounds of Haste remaining."
            return
        if enemy.Status_Haste_Duration == 0:
            $ enemy.Status_Haste_EffectActive = 0
            $ enemy.Status_Haste_Strength = 0
            call battle_call_Enemy_Dodge_Recheck
            call battle_call_Enemy_Initiative_Recheck
            "[enemy.name!t] feels themself slowing down to normal as Haste wears off."
    return

label battle_call_Enemy_Status_WeakenCheck:
    if enemy.Status_Weaken_EffectActive == 1:
        if enemy.Status_Weaken_Duration > 0:
            "[enemy.name!t] is currently weakened!"
            call battle_call_Enemy_Damage_Melee_Recheck
            call battle_call_Enemy_Damage_Ranged_Recheck
            $ enemy.Status_Weaken_Duration -= 1
            "[enemy.name!t]'s damage is [enemy.Status_Weaken_Strength] points worse due to weaken.  [enemy.Status_Weaken_Duration] rounds of Weaken remaining."
            return
        if enemy.Status_Weaken_Duration == 0:
            $ enemy.Status_Weaken_EffectActive = 0
            $ enemy.Status_Weaken_Strength = 0
            call battle_call_Enemy_Damage_Melee_Recheck
            call battle_call_Enemy_Damage_Ranged_Recheck
            "[enemy.name!t] feels their strength returning to normal as Weaken wears off."
    return

label battle_call_Enemy_Status_StrengthenCheck:
    if enemy.Status_Strengthen_EffectActive == 1:
        if enemy.Status_Strengthen_Duration > 0:
            "[enemy.name!t] is currently strengthed!"
            call battle_call_Enemy_Damage_Melee_Recheck
            call battle_call_Enemy_Damage_Ranged_Recheck
            $ enemy.Status_Strengthen_Duration -= 1
            "[enemy.name!t]'s damage is [enemy.Status_Strengthen_Strength] points better due to strengthen.  [enemy.Status_Strengthen_Duration] rounds of Strengthen remaining."
            return
        if enemy.Status_Strengthen_Duration == 0:
            $ enemy.Status_Strengthen_EffectActive = 0
            $ enemy.Status_Strengthen_Strength = 0
            call battle_call_Enemy_Damage_Melee_Recheck
            call battle_call_Enemy_Damage_Ranged_Recheck
            "[enemy.name!t] feel their strength returning to normal as Strengthen wears off."
    return


#label battle_call_Enemy_Status_EquipLoss_WeaponCheck:
#label battle_call_Enemy_Status_EquipLoss_ArmorCheck:

#label battle_call_Enemy_Status_Block:
#label battle_call_Enemy_Status_Dodge:
