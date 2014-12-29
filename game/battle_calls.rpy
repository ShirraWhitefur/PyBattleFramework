# Just a collection of little calls here.

#####################################################################
# Variable Min-Max Stops
#####################################################################

#  These are to keep the numbers 'tidy', and make it so your bars don't get all
# weird from negative numbers, keep people from overhealing, etc.  Several
# aren't needed yet, but it seemed a good idea to get them ready ahead of time.

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
# These will be changed later, once the stat system is in.

# For now though, it's basically
# Current (to be referenced almost everywhere) = (Base)+(Buffs)-(Debuffs)
# 'damage_max_current = (damage_max)+(strengthen.strength)-(weaken.strength)
#  Accessed via a call anytime something would change the number, and thusly
# recalculated.  This makes it much easier to handle our (de)buffs and equipment
# changes safely, and correct any possible 'issues' that came up.

label battle_call_Player_Full_StartCheck:
# call battle_call_Player_Initial_Equip
    call battle_call_Player_Full_Recheck
    call battle_call_Player_HP_AP_WP_Current_to_Max_Set

label battle_call_Player_Full_Recheck:
    call battle_call_Player_HP_AP_WP_Max_Recheck
    call battle_call_Player_Accuracy_Recheck
    call battle_call_Player_Armor_Recheck
    call battle_call_Player_Damage_Bonus_Recheck
    call battle_call_Player_Dodge_Recheck
    call battle_call_Player_Initiative_Recheck
    call battle_call_Player_Weapon_Accuracy_Recheck
    call battle_call_Player_Weapon_Damage_Recheck
    return

# call battle_call_Player_Initial_Equip

label battle_call_Player_HP_AP_WP_Max_Recheck:
    $ player.X_HealthPoints_Max_X = player.Attribute_HealthPoints_Max+player.Equipment_HealthPoints_Max
    $ player.X_AbilityPoints_Max_X = player.Attribute_AbilityPoints_Max+player.Equipment_AbilityPoints_Max
    $ player.X_WillPoints_Max_X = player.Attribute_WillPoints_Max+player.Equipment_WillPoints_Max
    return

label battle_call_Player_HP_AP_WP_Current_To_Max_Set:
    $ player.X_HealthPoints_Current_X = player.X_HealthPoints_Max_X
    $ player.X_AbilityPoints_Current_X = player.X_AbilityPoints_Max_X
    $ player.X_WillPoints_Current_X = player.X_WillPoints_Max_X

label battle_call_Player_Accuracy_Recheck:
    $ player.X_Weapon_Accuracy_Melee_X = player.Attribute_Accuracy_Melee+player.Equipment_Weapon_Accuracy_Melee
    $ player.X_Weapon_Accuracy_Ranged_X = player.Attribute_Accuracy_Ranged+player.Equipment_Weapon_Accuracy_Ranged
    return

label battle_call_Player_Armor_Recheck:
    $ player.X_Armor_Physical_X = player.Attribute_Armor_Physical+player.Equipment_Armor_Physical+player.Status_Block_Strength
    $ player.X_Armor_Magic_X = player.Attribute_Armor_Magic+player.Equipment_Armor_Magic+player.Status_Block_Strength
    $ player.X_Armor_Will_X = player.Attribute_Armor_Will+player.Equipment_Armor_Will
    return

label battle_call_Player_Damage_Bonus_Recheck:
    $ player.X_Damage_Bonus_Melee_Max_X = player.Attribute_Damage_Bonus_Melee_Max+player.Equipment_Damage_Bonus_Melee_Max+player.Status_Strengthen_Strength-player.Status_Weaken_Strength
    $ player.X_Damage_Bonus_Ranged_Max_X = player.Attribute_Damage_Bonus_Ranged_Max+player.Equipment_Damage_Bonus_Ranged_Max+player.Status_Strengthen_Strength-player.Status_Weaken_Strength
    $ player.X_Damage_Bonus_Magic_Max_X = player.Attribute_Damage_Bonus_Magic_Max+player.Equipment_Damage_Bonus_Magic_Max
    $ player.X_Damage_Bonus_Will_Max_X = player.Attribute_Damage_Bonus_Will_Max+player.Equipment_Damage_Bonus_Will_Max
    return

label battle_call_Player_Dodge_Recheck:
    $ player.X_Dodge_X = player.Attribute_Dodge+player.Equipment_Dodge+player.Status_Haste_Strength+player.Status_Dodge_Strength-player.Status_Slow_Strength
    return

label battle_call_Player_Initiative_Recheck:
    $ player.X_Initiative_X = player.Attribute_Initiative+player.Equipment_Initiative+player.Status_Haste_Strength-player.Status_Slow_Strength
    return

label battle_call_Player_Weapon_Accuracy_Recheck:
    $ player.X_Weapon_Accuracy_Melee_X = player.Attribute_Accuracy_Melee+player.Equipment_Weapon_Accuracy_Melee+player.Equipment_Accuracy_Melee
    $ player.X_Weapon_Accuracy_Ranged_X = player.Attribute_Accuracy_Ranged+player.Equipment_Weapon_Accuracy_Ranged+player.Equipment_Accuracy_Ranged

label battle_call_Player_Weapon_Damage_Recheck:
    $ player.X_Weapon_Damage_Melee_Max_X = player.Equipment_Weapon_Damage_Melee_Max+player.Attribute_Damage_Bonus_Melee_Max+player.Equipment_Damage_Bonus_Melee_Max+player.Status_Strengthen_Strength-player.Status_Weaken_Strength
    $ player.X_Weapon_Damage_Melee_Min_X = int(player.Equipment_Weapon_Damage_Melee_Min+(round(player.Attribute_Damage_Bonus_Melee_Max/10,0))+(round(player.Equipment_Damage_Bonus_Melee_Max/10,0))+(round(player.Status_Strengthen_Strength/10,0))-(round(player.Status_Weaken_Strength/10,0)))
    $ player.X_Weapon_Damage_Ranged_Max_X = player.Equipment_Weapon_Damage_Ranged_Max+player.Attribute_Damage_Bonus_Ranged_Max+player.Equipment_Damage_Bonus_Ranged_Max+player.Status_Strengthen_Strength-player.Status_Weaken_Strength
    $ player.X_Weapon_Damage_Ranged_Min_X = int(player.Equipment_Weapon_Damage_Ranged_Min+(round(player.Attribute_Damage_Bonus_Ranged_Max/10,0))+(round(player.Equipment_Damage_Bonus_Ranged_Max/10,0))+(round(player.Status_Strengthen_Strength/10,0))-(round(player.Status_Weaken_Strength/10,0)))
    $ player.X_Weapon_Damage_Magic_Max_X = player.Equipment_Weapon_Damage_Magic_Max+player.Attribute_Damage_Bonus_Magic_Max+player.Equipment_Damage_Bonus_Magic_Max
    $ player.X_Weapon_Damage_Magic_Min_X = int(player.Equipment_Weapon_Damage_Magic_Min+(round(player.Attribute_Damage_Bonus_Magic_Max/10,0)))+(round(player.Equipment_Damage_Bonus_Magic_Max/10,0))
    $ player.X_Weapon_Damage_Will_Max_X = player.Equipment_Weapon_Damage_Will_Max+player.Attribute_Damage_Bonus_Will_Max+player.Equipment_Damage_Bonus_Will_Max
    $ player.X_Weapon_Damage_Will_Min_X = int(player.Equipment_Weapon_Damage_Will_Min+(round(player.Attribute_Damage_Bonus_Will_Max/10,0))+(round(player.Equipment_Damage_Bonus_Will_Max/10,0)))
    return

##### - Enemy Set

label battle_call_Enemy_Full_StartCheck:
# call battle_call_Enemy_Initial_Equip
    call battle_call_Enemy_Full_Recheck
    call battle_call_Enemy_HP_AP_WP_Current_to_Max_Set

label battle_call_Enemy_Full_Recheck:
    call battle_call_Enemy_HP_AP_WP_Max_Recheck
    call battle_call_Enemy_Accuracy_Recheck
    call battle_call_Enemy_Armor_Recheck
    call battle_call_Enemy_Damage_Bonus_Recheck
    call battle_call_Enemy_Dodge_Recheck
    call battle_call_Enemy_Initiative_Recheck
    call battle_call_Enemy_Weapon_Accuracy_Recheck
    call battle_call_Enemy_Weapon_Damage_Recheck
    return

# label battle_call_Enemy_Initial_Equip:

label battle_call_Enemy_HP_AP_WP_Max_Recheck:
    $ enemy.X_HealthPoints_Max_X = enemy.Attribute_HealthPoints_Max+enemy.Equipment_HealthPoints_Max
    $ enemy.X_AbilityPoints_Max_X = enemy.Attribute_AbilityPoints_Max+enemy.Equipment_AbilityPoints_Max
    $ enemy.X_WillPoints_Max_X = enemy.Attribute_WillPoints_Max+enemy.Equipment_WillPoints_Max
    return

label battle_call_Enemy_HP_AP_WP_Current_to_Max_Set:
    $ enemy.X_HealthPoints_Current_X = enemy.X_HealthPoints_Max_X
    $ enemy.X_AbilityPoints_Current_X = enemy.X_AbilityPoints_Max_X
    $ enemy.X_WillPoints_Current_X = enemy.X_WillPoints_Max_X

label battle_call_Enemy_Accuracy_Recheck:
    $ enemy.X_Accuracy_Melee_X = enemy.Attribute_Accuracy_Melee+enemy.Equipment_Accuracy_Melee
    $ enemy.X_Accuracy_Ranged_X = enemy.Attribute_Accuracy_Ranged+enemy.Equipment_Accuracy_Ranged
    return

label battle_call_Enemy_Armor_Recheck:
    $ enemy.X_Armor_Physical_X = enemy.Attribute_Armor_Physical+enemy.Equipment_Armor_Physical+enemy.Status_Block_Strength
    $ enemy.X_Armor_Magic_X = enemy.Attribute_Armor_Magic+enemy.Equipment_Armor_Magic+enemy.Status_Block_Strength
    $ enemy.X_Armor_Will_X = enemy.Attribute_Armor_Will+enemy.Equipment_Armor_Will
    return

label battle_call_Enemy_Damage_Bonus_Recheck:
    $ enemy.X_Damage_Bonus_Melee_Max_X = enemy.Attribute_Damage_Bonus_Melee_Max+enemy.Equipment_Damage_Bonus_Melee_Max+enemy.Status_Strengthen_Strength-enemy.Status_Weaken_Strength
    $ enemy.X_Damage_Bonus_Ranged_Max_X = enemy.Attribute_Damage_Bonus_Ranged_Max+enemy.Equipment_Damage_Bonus_Ranged_Max+enemy.Status_Strengthen_Strength-enemy.Status_Weaken_Strength
    $ enemy.X_Damage_Bonus_Magic_Max_X = enemy.Attribute_Damage_Bonus_Magic_Max+enemy.Equipment_Damage_Bonus_Magic_Max
    $ enemy.X_Damage_Bonus_Will_Max_X = enemy.Attribute_Damage_Bonus_Will_Max+enemy.Equipment_Damage_Bonus_Will_Max
    return

label battle_call_Enemy_Dodge_Recheck:
    $ enemy.X_Dodge_X = enemy.Attribute_Dodge+enemy.Equipment_Dodge+enemy.Status_Haste_Strength+enemy.Status_Dodge_Strength-enemy.Status_Slow_Strength
    return

label battle_call_Enemy_Initiative_Recheck:
    $ enemy.X_Initiative_X = enemy.Attribute_Initiative+enemy.Equipment_Initiative+enemy.Status_Haste_Strength-enemy.Status_Slow_Strength
    return

label battle_call_Enemy_Weapon_Accuracy_Recheck:
    $ enemy.X_Weapon_Accuracy_Melee_X = enemy.Attribute_Accuracy_Melee+enemy.Equipment_Weapon_Accuracy_Melee+enemy.Equipment_Accuracy_Melee
    $ enemy.X_Weapon_Accuracy_Ranged_X = enemy.Attribute_Accuracy_Ranged+enemy.Equipment_Weapon_Accuracy_Ranged+enemy.Equipment_Accuracy_Ranged

label battle_call_Enemy_Weapon_Damage_Recheck:
    $ enemy.X_Weapon_Damage_Melee_Max_X = enemy.Equipment_Weapon_Damage_Melee_Max+enemy.Attribute_Damage_Bonus_Melee_Max+enemy.Equipment_Damage_Bonus_Melee_Max+enemy.Status_Strengthen_Strength-enemy.Status_Weaken_Strength
    $ enemy.X_Weapon_Damage_Melee_Min_X = int(enemy.Equipment_Weapon_Damage_Melee_Min+(round(enemy.Attribute_Damage_Bonus_Melee_Max/10,0))+(round(enemy.Equipment_Damage_Bonus_Melee_Max/10,0))+(round(enemy.Status_Strengthen_Strength/10,0))-(round(enemy.Status_Weaken_Strength/10,0)))
    $ enemy.X_Weapon_Damage_Ranged_Max_X = enemy.Equipment_Weapon_Damage_Ranged_Max+enemy.Attribute_Damage_Bonus_Ranged_Max+enemy.Equipment_Damage_Bonus_Ranged_Max+enemy.Status_Strengthen_Strength-enemy.Status_Weaken_Strength
    $ enemy.X_Weapon_Damage_Ranged_Min_X = int(enemy.Equipment_Weapon_Damage_Ranged_Min+(round(enemy.Attribute_Damage_Bonus_Ranged_Max/10,0))+(round(enemy.Equipment_Damage_Bonus_Ranged_Max/10,0))+(round(enemy.Status_Strengthen_Strength/10,0))-(round(enemy.Status_Weaken_Strength/10,0)))
    $ enemy.X_Weapon_Damage_Magic_Max_X = enemy.Equipment_Weapon_Damage_Magic_Max+enemy.Attribute_Damage_Bonus_Magic_Max+enemy.Equipment_Damage_Bonus_Magic_Max
    $ enemy.X_Weapon_Damage_Magic_Min_X = int(enemy.Equipment_Weapon_Damage_Magic_Min+(round(enemy.Attribute_Damage_Bonus_Magic_Max/10,0)))+(round(enemy.Equipment_Damage_Bonus_Magic_Max/10,0))
    $ enemy.X_Weapon_Damage_Will_Max_X = enemy.Equipment_Weapon_Damage_Will_Max+enemy.Attribute_Damage_Bonus_Will_Max+enemy.Equipment_Damage_Bonus_Will_Max
    $ enemy.X_Weapon_Damage_Will_Min_X = int(enemy.Equipment_Weapon_Damage_Will_Min+(round(enemy.Attribute_Damage_Bonus_Will_Max/10,0))+(round(enemy.Equipment_Damage_Bonus_Will_Max/10,0)))
    return

#####################################################################
# Enemy Data import and initialization
#####################################################################
# Make sure you set that ename variable!

label battle_call_Enemy_Data_Import:
#  This big block below is pulling the enemy information and copying it into the
# battle system, so you don't accidently mess up the original template.
    $ enemy = ename
    $ enemy.name = ename.name
    $ enemy.battle_selected_action = "battle_Enemy_Wait"
    $ enemy.Attack_List = ename.Attack_List
# And when in doubt, import in order..
    $ enemy.Stats_PlaceholderStrength = ename.Stats_PlaceholderStrength
    $ enemy.Attribute_HealthPoints_Max = ename.Attribute_HealthPoints_Max
    $ enemy.Attribute_AbilityPoints_Max = ename.Attribute_AbilityPoints_Max
    $ enemy.Attribute_WillPoints_Max = ename.Attribute_WillPoints_Max
    $ enemy.Attribute_Accuracy_Melee = ename.Attribute_Accuracy_Melee
    $ enemy.Attribute_Accuracy_Ranged = ename.Attribute_Accuracy_Ranged
    $ enemy.Attribute_Armor_Physical = ename.Attribute_Armor_Physical
    $ enemy.Attribute_Armor_Magic = ename.Attribute_Armor_Magic
    $ enemy.Attribute_Armor_Will = ename.Attribute_Armor_Will
    $ enemy.Attribute_Damage_Bonus_Melee_Max = ename.Attribute_Damage_Bonus_Melee_Max
    $ enemy.Attribute_Damage_Bonus_Ranged_Max = ename.Attribute_Damage_Bonus_Ranged_Max
    $ enemy.Attribute_Damage_Bonus_Magic_Max = ename.Attribute_Damage_Bonus_Magic_Max
    $ enemy.Attribute_Damage_Bonus_Will_Max = ename.Attribute_Damage_Bonus_Will_Max
    $ enemy.Attribute_Dodge = ename.Attribute_Dodge
    $ enemy.Attribute_Initiative = ename.Attribute_Initiative
    $ enemy.Equipment_Slot_Weapon_Name = ename.Equipment_Slot_Weapon_Name
    $ enemy.Equipment_Slot_UpperBodyArmor_Name = ename.Equipment_Slot_UpperBodyArmor_Name
    $ enemy.Equipment_Slot_LowerBodyArmor_Name = ename.Equipment_Slot_LowerBodyArmor_Name
    $ enemy.Equipment_Slot_Necklace_Name = ename.Equipment_Slot_Necklace_Name
    $ enemy.Equipment_Slot_Ring_Name = ename.Equipment_Slot_Ring_Name
    $ enemy.Equipment_Consumables_Potions_HP_Restore = ename.Equipment_Consumables_Potions_HP_Restore
    $ enemy.Equipment_Consumables_Potions_AP_Restore = ename.Equipment_Consumables_Potions_AP_Restore
    $ enemy.Equipment_Consumables_Potions_WP_Restore = ename.Equipment_Consumables_Potions_WP_Restore
# \/  This block is here, because evidently init: isn't -properly- initing them
# \/ elsewhere, not completely.  Don't ask me, I don't know why it's not.
    $ enemy.Status_Poison_EffectActive = 0
    $ enemy.Status_Poison_Duration = 0
    $ enemy.Status_Poison_Strength = 0
    $ enemy.Status_Regen_EffectActive = 0
    $ enemy.Status_Regen_Duration = 0
    $ enemy.Status_Regen_Strength = 0
    $ enemy.Status_Slow_EffectActive = 0
    $ enemy.Status_Slow_Duration = 0
    $ enemy.Status_Slow_Strength = 0
    $ enemy.Status_Haste_EffectActive = 0
    $ enemy.Status_Haste_Duration = 0
    $ enemy.Status_Haste_Strength = 0
    $ enemy.Status_Weaken_EffectActive = 0
    $ enemy.Status_Weaken_Duration = 0
    $ enemy.Status_Weaken_Strength = 0
    $ enemy.Status_Strengthen_EffectActive = 0
    $ enemy.Status_Strengthen_Duration = 0
    $ enemy.Status_Strengthen_Strength = 0
    $ enemy.Status_Paralyse_EffectActive = 0
    $ enemy.Status_Paralyse_Duration = 0
    $ enemy.Status_Charm_EffectActive = 0
    $ enemy.Status_Charm_Duration = 0
    $ enemy.Status_Sleep_EffectActive = 0
    $ enemy.Status_Sleep_Duration = 0
    $ enemy.Status_Block_EffectActive = 0
    $ enemy.Status_Block_Strength = 0
    $ enemy.Status_Dodge_EffectActive = 0
    $ enemy.Status_Dodge_Strength = 0
# /\ Status effect inits.
#  This line basically tells the game to go 'Okay, now calculate all the
# variables based on the data we've imported.  Saves us a mess of lines here.
    call call_Enemy_Equipment_Slot_Initialize_All
    call battle_call_Enemy_Full_StartCheck
    return
