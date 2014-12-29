# Just a collection of little calls here.

#####################################################################
# Variable Min-Max Stops
#####################################################################

#  These are to keep the numbers 'tidy', and make it so your bars don't get all weird
# from negative numbers, keep people from overhealing, etc.  Several aren't needed
# yet, but it seemed a good idea to get them ready ahead of time.

label battle_call_Player_HP_Loss(hploss):
    if player.Status_Charm_EffectActive == 1:
        "Taking damage breaks the Charm!"
        $ player.Status_Charm_EffectActive = 0
        $ player.Status_Charm_Duration = 0
    if player.Status_Sleep_EffectActive == 1:
        "Taking damage wakes you from Sleep!"
        $ player.Status_Sleep_EffectActive = 0
        $ player.Status_Sleep_Duration = 0
    $ player.X_HealthPoints_Current_X -= hploss
    if player.X_HealthPoints_Current_X < 0:
        $ player.X_HealthPoints_Current_X = 0
    return

label battle_call_Player_HP_Gain(hpgain):
    $ player.X_HealthPoints_Current_X += hpgain
    if player.X_HealthPoints_Current_X > player.X_HealthPoints_Max_X:
        $ player.X_HealthPoints_Current_X = player.X_HealthPoints_Max_X
    return

label battle_call_Player_AP_Loss(aploss):
    $ player.X_AbilityPoints_Current_X -= aploss
    if player.X_AbilityPoints_Current_X < 0:
        $ player.X_AbilityPoints_Current_X = 0
    return

label battle_call_Player_AP_Gain(apgain):
    $ player.X_AbilityPoints_Current_X += apgain
    if player.X_AbilityPoints_Current_X > player.X_AbilityPoints_Max_X:
        $ player.X_AbilityPoints_Current_X = player.X_AbilityPoints_Max_X
    return

label battle_call_Player_WP_Loss(wploss):
    $ player.X_WillPoints_Current_X -= wploss
    if player.X_WillPoints_Current_X < 0:
        $ player.X_WillPoints_Current_X = 0
    return

label battle_call_Player_WP_Gain(apgain):
    $ player.X_WillPoints_Current_X += wpgain
    if player.X_WillPoints_Current_X > player.X_WillPoints_Max_X:
        $ player.X_WillPoints_Current_X = player.X_WillPoints_Max_X
    return

label battle_call_Enemy_HP_Loss(hploss):
    if enemy.Status_Charm_Duration > 0:
        "Taking damage breaks the Charm on [enemy.name!t]!"
        $ enemy.Status_Charm_Duration = 0
    if enemy.Status_Sleep_Duration > 0:
        "Taking damage wakes [enemy.name!t] from Sleep!"
        $ enemy.Status_Sleep_Duration = 0
    $ enemy.X_HealthPoints_Current_X -= hploss
    if enemy.X_HealthPoints_Current_X < 0:
        $ enemy.X_HealthPoints_Current_X = 0
    return

label battle_call_Enemy_HP_Gain(hpgain):
    $ enemy.X_HealthPoints_Current_X += hpgain
    if enemy.X_HealthPoints_Current_X > enemy.X_HealthPoints_Max_X:
        $ enemy.X_HealthPoints_Current_X = enemy.X_HealthPoints_Max_X
    return

label battle_call_Enemy_AP_Loss(aploss):
    $ enemy.X_AbilityPoints_Current_X -= aploss
    if enemy.X_AbilityPoints_Current_X < 0:
        $ enemy.X_AbilityPoints_Current_X = 0
    return

label battle_call_Enemy_AP_Gain(apgain):
    $ enemy.X_AbilityPoints_Current_X += apgain
    if enemy.X_AbilityPoints_Current_X > enemy.X_AbilityPoints_Max_X:
        $ enemy.X_AbilityPoints_Current_X = enemy.X_AbilityPoints_Max_X
    return

#####################################################################
# Stat and Attribute Bonus Setting
#####################################################################

# These will be changed later, once the stat system and equipment system are in.

# For now though, it's basically
# Current (to be referenced almost everywhere) = (Base)+(Buffs)-(Debuffs)
# 'damage_max_current = (damage_max)+(strengthen.strength)-(weaken.strength)
# Accessed via a call anytime something would change the number, and thusly recalculated.

label battle_call_Full_Recheck:
    call battle_call_HP_AP_WP_Max_Recheck
    call battle_call_Accuracy_Recheck
    call battle_call_Armor_Recheck
    call battle_call_Damage_Melee_Recheck
    call battle_call_Damage_Ranged_Recheck
    call battle_call_Damage_Magic_Recheck
    call battle_call_Damage_Will_Recheck
    call battle_call_Dodge_Recheck
    call battle_call_Initiative_Recheck
    return

label battle_call_HP_AP_WP_Max_Recheck:
    $ player.X_HealthPoints_Max_X = player.Attribute_HealthPoints_Max+player.Equipment_HealthPoints_Max
    $ player.X_AbilityPoints_Max_X = player.Attribute_AbilityPoints_Max+player.Equipment_AbilityPoints_Max
    $ player.X_WillPoints_Max_X = player.Attribute_WillPoints_Max+player.Equipment_WillPoints_Max
    return

label battle_call_Accuracy_Recheck:
    $ player.X_Accuracy_Melee_X = player.Attribute_Accuracy_Melee+player.Equipment_Accuracy_Melee
    $ player.X_Accuracy_Ranged_X = player.Attribute_Accuracy_Ranged+player.Equipment_Accuracy_Ranged
    return

label battle_call_Armor_Recheck:
    $ player.X_Armor_Physical_X = player.Attribute_Armor_Physical+player.Equipment_Armor_Physical+player.Status_Block_Strength
    $ player.X_Armor_Magic_X = player.Attribute_Armor_Magic+player.Equipment_Armor_Magic+player.Status_Block_Strength
    $ player.X_Armor_Will_X = player.Attribute_Armor_Will+player.Equipment_Armor_Will
    return

label battle_call_Damage_Melee_Recheck:
    $ player.X_Damage_Melee_Max_X = player.Equipment_Damage_Melee_Max+player.Attribute_Damage_Melee_Max+player.Status_Strengthen_Strength-player.Status_Weaken_Strength
    $ player.X_Damage_Melee_Min_X = int(player.Equipment_Damage_Melee_Min+(round(player.Attribute_Damage_Melee_Max/10,0))+(round(player.Status_Strengthen_Strength/10,0))-(round(player.Status_Weaken_Strength/10,0)))
    return

label battle_call_Damage_Ranged_Recheck:
    $ player.X_Damage_Ranged_Max_X = player.Equipment_Damage_Ranged_Max+player.Attribute_Damage_Ranged_Max+player.Status_Strengthen_Strength-player.Status_Weaken_Strength
    $ player.X_Damage_Ranged_Min_X = int(player.Equipment_Damage_Ranged_Min+(round(player.Attribute_Damage_Ranged_Max/10,0))+(round(player.Status_Strengthen_Strength/10,0))-(round(player.Status_Weaken_Strength/10,0)))
    return

label battle_call_Damage_Magic_Recheck:
    $ player.X_Damage_Magic_Max_X = player.Equipment_Damage_Magic_Max+player.Attribute_Damage_Magic_Max
    $ player.X_Damage_Magic_Min_X = int(player.Equipment_Damage_Magic_Min+(round(player.Attribute_Damage_Magic_Max/10,0)))
    return

label battle_call_Damage_Will_Recheck:
    $ player.X_Damage_Will_Max_X = player.Equipment_Damage_Will_Max+player.Attribute_Damage_Will_Max
    $ player.X_Damage_Will_Min_X = int(player.Equipment_Damage_Will_Min+(round(player.Attribute_Damage_Will_Max/10,0)))
    return

label battle_call_Dodge_Recheck:
    $ player.X_Dodge_X = player.Attribute_Dodge+player.Equipment_Dodge+player.Status_Haste_Strength+player.Status_Dodge_Strength-player.Status_Slow_Strength
    return

label battle_call_Initiative_Recheck:
    $ player.X_Initiative_X = player.Attribute_Initiative+player.Equipment_Initiative+player.Status_Haste_Strength-player.Status_Slow_Strength
    return

#####################################################################

