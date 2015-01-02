# Shirra's Ren'Py Battle Framework
# https://github.com/ShirraWhitefur/PyBattleFramework
# http://creativecommons.org/licenses/by-nc/3.0/

# Just a collection of battle system calls here.
# If you're looking for status effects, try battle_calls_status_effects
# Or equipment, try battle_calls_equipment

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
    call battle_call_Player_Stat_Recheck
    call battle_call_Player_Ability_Recheck
    call battle_call_Player_Full_Recheck
    call battle_call_Player_HP_AP_WP_Current_To_Max_Set

label battle_call_Player_Full_Recheck:
    call battle_call_Player_Stat_Recheck
    call battle_call_Player_HP_AP_WP_Max_Recheck
    call battle_call_Player_Accuracy_Recheck
    call battle_call_Player_Armor_Recheck
    call battle_call_Player_Damage_Bonus_Recheck
    call battle_call_Player_Dodge_Recheck
    call battle_call_Player_Initiative_Recheck
    call battle_call_Player_Weapon_Accuracy_Recheck
    call battle_call_Player_Weapon_Damage_Recheck
    return

label battle_call_Player_Stat_Recheck:
    $ player.X_Strength_X = player.Stats_Strength+player.Equipment_Strength+player.Status_Strengthen_Strength-player.Status_Weaken_Strength
    $ player.X_Precision_X = player.Stats_Precision+player.Equipment_Precision+player.Status_Nimble_Strength-player.Status_Clumsy_Strength
    $ player.X_Insight_X = player.Stats_Insight+player.Equipment_Insight
    $ player.X_Deceit_X = player.Stats_Deceit+player.Equipment_Deceit
    $ player.X_Vigor_X = player.Stats_Vigor+player.Equipment_Vigor
    $ player.X_Spirit_X = player.Stats_Spirit+player.Equipment_Spirit
    $ player.X_Resolve_X = player.Stats_Resolve+player.Equipment_Resolve

label battle_call_Player_Ability_Recheck:
    $ player.Attribute_HealthPoints = (int(round((player.X_Vigor_X/battle.Bonus_HPAPWP_Max_Stat_Divisor))))+100
    $ player.Attribute_AbilityPoints = (int(round((player.X_Spirit_X/battle.Bonus_HPAPWP_Max_Stat_Divisor))))+100
    $ player.Attribute_WillPoints = (int(round((player.X_Resolve_X/battle.Bonus_HPAPWP_Max_Stat_Divisor))))+100
    $ player.Attribute_Accuracy_Melee = (int(round((player.X_Strength_X/battle.Bonus_Accuracy_Divisor))))
    $ player.Attribute_Accuracy_Ranged = (int(round((player.X_Precision_X/battle.Bonus_Accuracy_Divisor))))
    $ player.Attribute_Armor_Physical = (int(round((player.X_Vigor_X/battle.Bonus_Armor_Stat_Divisor))))+100
    $ player.Attribute_Armor_Magic = (int(round((player.X_Spirit_X/battle.Bonus_Armor_Stat_Divisor))))+100
    $ player.Attribute_Armor_Will = (int(round((player.X_Resolve_X/battle.Bonus_Armor_Stat_Divisor))))+100
    $ player.Attribute_Damage_Bonus_Melee = (int(round((player.X_Strength_X/battle.Bonus_Damage_Stat_Divisor))))+100
    $ player.Attribute_Damage_Bonus_Ranged = (int(round((player.X_Precision_X/battle.Bonus_Damage_Stat_Divisor))))+100
    $ player.Attribute_Damage_Bonus_Magic = (int(round((player.X_Insight_X/battle.Bonus_Damage_Stat_Divisor))))+100
    $ player.Attribute_Damage_Bonus_Will = (int(round((player.X_Deceit_X/battle.Bonus_Damage_Stat_Divisor))))+100
    $ player.Attribute_Dodge = (int(round((player.X_Deceit_X/battle.Bonus_Dodge_Divisor))))
    $ player.Attribute_Initiative = (int(round((player.X_Insight_X/battle.Bonus_Initiative_Divisor))))

label battle_call_Player_HP_AP_WP_Max_Recheck:
    $ player.X_Vigor_X = player.Stats_Vigor+player.Equipment_Vigor
    $ player.X_Spirit_X = player.Stats_Spirit+player.Equipment_Spirit
    $ player.X_Resolve_X = player.Stats_Resolve+player.Equipment_Resolve
    $ player.Attribute_HealthPoints = (int(round((player.X_Vigor_X/battle.Bonus_HPAPWP_Max_Stat_Divisor))))+100
    $ player.Attribute_AbilityPoints = (int(round((player.X_Spirit_X/battle.Bonus_HPAPWP_Max_Stat_Divisor))))+100
    $ player.Attribute_WillPoints = (int(round((player.X_Resolve_X/battle.Bonus_HPAPWP_Max_Stat_Divisor))))+100
    $ player.X_HealthPoints_Max_X = int(round((1 if (battle.Base_HealthPoints_Max+player.Equipment_HealthPoints_Max) < 1 else (battle.Base_HealthPoints_Max+player.Equipment_HealthPoints_Max))*((-99 if (player.Attribute_HealthPoints) < -99 else (player.Attribute_HealthPoints))*0.01)))
    $ player.X_AbilityPoints_Max_X = int(round((1 if (battle.Base_AbilityPoints_Max+player.Equipment_AbilityPoints_Max) < 1 else (battle.Base_AbilityPoints_Max+player.Equipment_AbilityPoints_Max))*((-99 if (player.Attribute_AbilityPoints) < -99 else (player.Attribute_AbilityPoints))*0.01)))
    $ player.X_WillPoints_Max_X = int(round((1 if (battle.Base_WillPoints_Max+player.Equipment_WillPoints_Max) < 1 else (battle.Base_WillPoints_Max+player.Equipment_WillPoints_Max))*((-99 if (player.Attribute_WillPoints) < -99 else (player.Attribute_WillPoints))*0.01)))
    return

label battle_call_Player_HP_AP_WP_Current_To_Max_Set:
    $ player.X_HealthPoints_Current_X = player.X_HealthPoints_Max_X
    $ player.X_AbilityPoints_Current_X = player.X_AbilityPoints_Max_X
    $ player.X_WillPoints_Current_X = player.X_WillPoints_Max_X

label battle_call_Player_Accuracy_Recheck:
    $ player.X_Strength_X = player.Stats_Strength+player.Equipment_Strength+player.Status_Strengthen_Strength-player.Status_Weaken_Strength
    $ player.X_Precision_X = player.Stats_Precision+player.Equipment_Precision+player.Status_Nimble_Strength-player.Status_Clumsy_Strength
    $ player.Attribute_Accuracy_Melee = (int(round((player.X_Strength_X/battle.Bonus_Accuracy_Divisor))))
    $ player.Attribute_Accuracy_Ranged = (int(round((player.X_Precision_X/battle.Bonus_Accuracy_Divisor))))
    $ player.X_Accuracy_Melee_X = int(round(player.Attribute_Accuracy_Melee+player.Equipment_Accuracy_Melee))
    $ player.X_Accuracy_Ranged_X = int(round(player.Attribute_Accuracy_Ranged+player.Equipment_Accuracy_Ranged))
    $ player.X_Weapon_Accuracy_Melee_X = int(round(player.Equipment_Weapon_Accuracy_Melee+player.X_Accuracy_Melee_X))
    $ player.X_Weapon_Accuracy_Ranged_X = int(round(player.Equipment_Weapon_Accuracy_Ranged+player.X_Accuracy_Ranged_X))
    return

label battle_call_Player_Armor_Recheck:
    $ player.X_Vigor_X = player.Stats_Vigor+player.Equipment_Vigor
    $ player.X_Spirit_X = player.Stats_Spirit+player.Equipment_Spirit
    $ player.X_Resolve_X = player.Stats_Resolve+player.Equipment_Resolve
    $ player.Attribute_Armor_Physical = (int(round((player.X_Vigor_X/battle.Bonus_Armor_Stat_Divisor))))+100
    $ player.Attribute_Armor_Magic = (int(round((player.X_Spirit_X/battle.Bonus_Armor_Stat_Divisor))))+100
    $ player.Attribute_Armor_Will = (int(round((player.X_Resolve_X/battle.Bonus_Armor_Stat_Divisor))))+100
    $ player.X_Armor_Physical_X = int(round((1 if (player.Equipment_Armor_Physical) < 1 else (player.Equipment_Armor_Physical))*((-99 if (player.Attribute_Armor_Physical+player.Status_Block_Strength) < -99 else (player.Attribute_Armor_Physical+player.Status_Block_Strength))*0.01)))
    $ player.X_Armor_Magic_X = int(round((1 if (player.Equipment_Armor_Magic) < 1 else (player.Equipment_Armor_Magic))*((-99 if (player.Attribute_Armor_Magic+player.Status_Block_Strength) < -99 else (player.Attribute_Armor_Magic+player.Status_Block_Strength))*0.01)))
    $ player.X_Armor_Will_X = int(round((1 if (player.Equipment_Armor_Will) < 1 else (player.Equipment_Armor_Will))*((-99 if (player.Attribute_Armor_Will+player.Status_Block_Strength) < -99 else (player.Attribute_Armor_Will+player.Status_Block_Strength))*0.01)))
    return

label battle_call_Player_Damage_Bonus_Recheck:
    $ player.X_Strength_X = player.Stats_Strength+player.Equipment_Strength+player.Status_Strengthen_Strength-player.Status_Weaken_Strength
    $ player.X_Precision_X = player.Stats_Precision+player.Equipment_Precision+player.Status_Nimble_Strength-player.Status_Clumsy_Strength
    $ player.X_Insight_X = player.Stats_Insight+player.Equipment_Insight
    $ player.X_Deceit_X = player.Stats_Deceit+player.Equipment_Deceit
    $ player.Attribute_Damage_Bonus_Melee = (int(round((player.X_Strength_X/battle.Bonus_Damage_Stat_Divisor))))+100
    $ player.Attribute_Damage_Bonus_Ranged = (int(round((player.X_Precision_X/battle.Bonus_Damage_Stat_Divisor))))+100
    $ player.Attribute_Damage_Bonus_Magic = (int(round((player.X_Insight_X/battle.Bonus_Damage_Stat_Divisor))))+100
    $ player.Attribute_Damage_Bonus_Will = (int(round((player.X_Deceit_X/battle.Bonus_Damage_Stat_Divisor))))+100
    $ player.X_Damage_Bonus_Melee_Text_X = int(round((-99 if (player.Attribute_Damage_Bonus_Melee+player.Equipment_Damage_Bonus_Melee+player.Status_Strengthen_Strength-player.Status_Weaken_Strength) < -99 else (player.Attribute_Damage_Bonus_Melee+player.Equipment_Damage_Bonus_Melee+player.Status_Strengthen_Strength-player.Status_Weaken_Strength))))
    $ player.X_Damage_Bonus_Ranged_Text_X = int(round((-99 if (player.Attribute_Damage_Bonus_Ranged+player.Equipment_Damage_Bonus_Ranged+player.Status_Nimble_Strength-player.Status_Clumsy_Strength) < -99 else (player.Attribute_Damage_Bonus_Ranged+player.Equipment_Damage_Bonus_Ranged+player.Status_Nimble_Strength-player.Status_Clumsy_Strength))))
    $ player.X_Damage_Bonus_Magic_Text_X = int(round((-99 if (player.Attribute_Damage_Bonus_Magic+player.Equipment_Damage_Bonus_Magic) < -99 else (player.Attribute_Damage_Bonus_Magic+player.Equipment_Damage_Bonus_Magic))))
    $ player.X_Damage_Bonus_Will_Text_X = int(round((-99 if (player.Attribute_Damage_Bonus_Will+player.Equipment_Damage_Bonus_Will) < -99 else (player.Attribute_Damage_Bonus_Will+player.Equipment_Damage_Bonus_Will))))
    $ player.X_Damage_Bonus_Melee_X = (player.X_Damage_Bonus_Melee_Text_X)*0.01
    $ player.X_Damage_Bonus_Ranged_X = (player.X_Damage_Bonus_Ranged_Text_X)*0.01
    $ player.X_Damage_Bonus_Magic_X = (player.X_Damage_Bonus_Magic_Text_X)*0.01
    $ player.X_Damage_Bonus_Will_X = (player.X_Damage_Bonus_Will_Text_X)*0.01
    return

label battle_call_Player_Dodge_Recheck:
    $ player.X_Deceit_X = player.Stats_Deceit+player.Equipment_Deceit
    $ player.Attribute_Dodge = (int(round((player.X_Deceit_X/battle.Bonus_Dodge_Divisor))))
    $ player.X_Dodge_X = player.Attribute_Dodge+player.Equipment_Dodge+player.Status_Haste_Strength+player.Status_Dodge_Strength-player.Status_Slow_Strength
    return

label battle_call_Player_Initiative_Recheck:
    $ player.X_Insight_X = player.Stats_Insight+player.Equipment_Insight
    $ player.Attribute_Initiative = (int(round((player.X_Insight_X/battle.Bonus_Initiative_Divisor))))
    $ player.X_Initiative_X = player.Attribute_Initiative+player.Equipment_Initiative+player.Status_Haste_Strength-player.Status_Slow_Strength
    return

label battle_call_Player_Weapon_Accuracy_Recheck:
    $ player.X_Weapon_Accuracy_Melee_X = player.Attribute_Accuracy_Melee+player.Equipment_Weapon_Accuracy_Melee+player.Equipment_Accuracy_Melee
    $ player.X_Weapon_Accuracy_Ranged_X = player.Attribute_Accuracy_Ranged+player.Equipment_Weapon_Accuracy_Ranged+player.Equipment_Accuracy_Ranged

label battle_call_Player_Weapon_Damage_Recheck:
    $ player.X_Weapon_Damage_Melee_Max_X = int(round(player.Equipment_Weapon_Damage_Melee_Max*player.X_Damage_Bonus_Melee_X))
    $ player.X_Weapon_Damage_Melee_Min_X = int(round(player.Equipment_Weapon_Damage_Melee_Min*player.X_Damage_Bonus_Melee_X))
    $ player.X_Weapon_Damage_Ranged_Max_X = int(round(player.Equipment_Weapon_Damage_Ranged_Max*player.X_Damage_Bonus_Ranged_X))
    $ player.X_Weapon_Damage_Ranged_Min_X = int(round(player.Equipment_Weapon_Damage_Ranged_Min*player.X_Damage_Bonus_Ranged_X))
    $ player.X_Weapon_Damage_Magic_Max_X = int(round(player.Equipment_Weapon_Damage_Magic_Max*player.X_Damage_Bonus_Magic_X))
    $ player.X_Weapon_Damage_Magic_Min_X = int(round(player.Equipment_Weapon_Damage_Magic_Min*player.X_Damage_Bonus_Magic_X))
    $ player.X_Weapon_Damage_Will_Max_X = int(round(player.Equipment_Weapon_Damage_Will_Max*player.X_Damage_Bonus_Will_X))
    $ player.X_Weapon_Damage_Will_Min_X = int(round(player.Equipment_Weapon_Damage_Will_Min*player.X_Damage_Bonus_Will_X))
    return

##### - Enemy Set

label battle_call_Enemy_Full_StartCheck:
    call battle_call_Enemy_Stat_Recheck
    call battle_call_Enemy_Ability_Recheck
    call battle_call_Enemy_Full_Recheck
    call battle_call_Enemy_HP_AP_WP_Current_To_Max_Set

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

label battle_call_Enemy_Stat_Recheck:
    $ enemy.X_Strength_X = enemy.Stats_Strength+enemy.Equipment_Strength+enemy.Status_Strengthen_Strength-enemy.Status_Weaken_Strength
    $ enemy.X_Precision_X = enemy.Stats_Precision+enemy.Equipment_Precision+enemy.Status_Nimble_Strength-enemy.Status_Clumsy_Strength
    $ enemy.X_Insight_X = enemy.Stats_Insight+enemy.Equipment_Insight
    $ enemy.X_Deceit_X = enemy.Stats_Deceit+enemy.Equipment_Deceit
    $ enemy.X_Vigor_X = enemy.Stats_Vigor+enemy.Equipment_Vigor
    $ enemy.X_Spirit_X = enemy.Stats_Spirit+enemy.Equipment_Spirit
    $ enemy.X_Resolve_X = enemy.Stats_Resolve+enemy.Equipment_Resolve

label battle_call_Enemy_Ability_Recheck:
    $ enemy.Attribute_HealthPoints = (int(round((enemy.X_Vigor_X/battle.Bonus_HPAPWP_Max_Stat_Divisor))))+100
    $ enemy.Attribute_AbilityPoints = (int(round((enemy.X_Spirit_X/battle.Bonus_HPAPWP_Max_Stat_Divisor))))+100
    $ enemy.Attribute_WillPoints = (int(round((enemy.X_Resolve_X/battle.Bonus_HPAPWP_Max_Stat_Divisor))))+100
    $ enemy.Attribute_Accuracy_Melee = (int(round((enemy.X_Strength_X/battle.Bonus_Accuracy_Divisor))))
    $ enemy.Attribute_Accuracy_Ranged = (int(round((enemy.X_Precision_X/battle.Bonus_Accuracy_Divisor))))
    $ enemy.Attribute_Armor_Physical = (int(round((enemy.X_Vigor_X/battle.Bonus_Armor_Stat_Divisor))))+100
    $ enemy.Attribute_Armor_Magic = (int(round((enemy.X_Spirit_X/battle.Bonus_Armor_Stat_Divisor))))+100
    $ enemy.Attribute_Armor_Will = (int(round((enemy.X_Resolve_X/battle.Bonus_Armor_Stat_Divisor))))+100
    $ enemy.Attribute_Damage_Bonus_Melee = (int(round((enemy.X_Strength_X/battle.Bonus_Damage_Stat_Divisor))))+100
    $ enemy.Attribute_Damage_Bonus_Ranged = (int(round((enemy.X_Precision_X/battle.Bonus_Damage_Stat_Divisor))))+100
    $ enemy.Attribute_Damage_Bonus_Magic = (int(round((enemy.X_Insight_X/battle.Bonus_Damage_Stat_Divisor))))+100
    $ enemy.Attribute_Damage_Bonus_Will = (int(round((enemy.X_Deceit_X/battle.Bonus_Damage_Stat_Divisor))))+100
    $ enemy.Attribute_Dodge = (int(round((enemy.X_Deceit_X/battle.Bonus_Dodge_Divisor))))
    $ enemy.Attribute_Initiative = (int(round((enemy.X_Insight_X/battle.Bonus_Initiative_Divisor))))

label battle_call_Enemy_HP_AP_WP_Max_Recheck:
    $ enemy.X_Vigor_X = enemy.Stats_Vigor+enemy.Equipment_Vigor
    $ enemy.X_Spirit_X = enemy.Stats_Spirit+enemy.Equipment_Spirit
    $ enemy.X_Resolve_X = enemy.Stats_Resolve+enemy.Equipment_Resolve
    $ enemy.Attribute_HealthPoints = (int(round((enemy.X_Vigor_X/battle.Bonus_HPAPWP_Max_Stat_Divisor))))+100
    $ enemy.Attribute_AbilityPoints = (int(round((enemy.X_Spirit_X/battle.Bonus_HPAPWP_Max_Stat_Divisor))))+100
    $ enemy.Attribute_WillPoints = (int(round((enemy.X_Resolve_X/battle.Bonus_HPAPWP_Max_Stat_Divisor))))+100
    $ enemy.X_HealthPoints_Max_X = int(round((1 if (battle.Base_HealthPoints_Max+enemy.Equipment_HealthPoints_Max) < 1 else (battle.Base_HealthPoints_Max+enemy.Equipment_HealthPoints_Max))*((-99 if (enemy.Attribute_HealthPoints) < -99 else (enemy.Attribute_HealthPoints))*0.01)))
    $ enemy.X_AbilityPoints_Max_X = int(round((1 if (battle.Base_AbilityPoints_Max+enemy.Equipment_AbilityPoints_Max) < 1 else (battle.Base_AbilityPoints_Max+enemy.Equipment_AbilityPoints_Max))*((-99 if (enemy.Attribute_AbilityPoints) < -99 else (enemy.Attribute_AbilityPoints))*0.01)))
    $ enemy.X_WillPoints_Max_X = int(round((1 if (battle.Base_WillPoints_Max+enemy.Equipment_WillPoints_Max) < 1 else (battle.Base_WillPoints_Max+enemy.Equipment_WillPoints_Max))*((-99 if (enemy.Attribute_WillPoints) < -99 else (enemy.Attribute_WillPoints))*0.01)))
    return

label battle_call_Enemy_HP_AP_WP_Current_To_Max_Set:
    $ enemy.X_HealthPoints_Current_X = enemy.X_HealthPoints_Max_X
    $ enemy.X_AbilityPoints_Current_X = enemy.X_AbilityPoints_Max_X
    $ enemy.X_WillPoints_Current_X = enemy.X_WillPoints_Max_X

label battle_call_Enemy_Accuracy_Recheck:
    $ enemy.X_Strength_X = enemy.Stats_Strength+enemy.Equipment_Strength+enemy.Status_Strengthen_Strength-enemy.Status_Weaken_Strength
    $ enemy.X_Precision_X = enemy.Stats_Precision+enemy.Equipment_Precision+enemy.Status_Nimble_Strength-enemy.Status_Clumsy_Strength
    $ enemy.Attribute_Accuracy_Melee = (int(round((enemy.X_Strength_X/battle.Bonus_Accuracy_Divisor))))
    $ enemy.Attribute_Accuracy_Ranged = (int(round((enemy.X_Precision_X/battle.Bonus_Accuracy_Divisor))))
    $ enemy.X_Accuracy_Melee_X = int(round(enemy.Attribute_Accuracy_Melee+enemy.Equipment_Accuracy_Melee))
    $ enemy.X_Accuracy_Ranged_X = int(round(enemy.Attribute_Accuracy_Ranged+enemy.Equipment_Accuracy_Ranged))
    $ enemy.X_Weapon_Accuracy_Melee_X = int(round(enemy.Equipment_Weapon_Accuracy_Melee+enemy.X_Accuracy_Melee_X))
    $ enemy.X_Weapon_Accuracy_Ranged_X = int(round(enemy.Equipment_Weapon_Accuracy_Ranged+enemy.X_Accuracy_Ranged_X))
    return

label battle_call_Enemy_Armor_Recheck:
    $ enemy.X_Vigor_X = enemy.Stats_Vigor+enemy.Equipment_Vigor
    $ enemy.X_Spirit_X = enemy.Stats_Spirit+enemy.Equipment_Spirit
    $ enemy.X_Resolve_X = enemy.Stats_Resolve+enemy.Equipment_Resolve
    $ enemy.Attribute_Armor_Physical = (int(round((enemy.X_Vigor_X/battle.Bonus_Armor_Stat_Divisor))))+100
    $ enemy.Attribute_Armor_Magic = (int(round((enemy.X_Spirit_X/battle.Bonus_Armor_Stat_Divisor))))+100
    $ enemy.Attribute_Armor_Will = (int(round((enemy.X_Resolve_X/battle.Bonus_Armor_Stat_Divisor))))+100
    $ enemy.X_Armor_Physical_X = int(round((1 if (enemy.Equipment_Armor_Physical) < 1 else (enemy.Equipment_Armor_Physical))*((-99 if (enemy.Attribute_Armor_Physical+enemy.Status_Block_Strength) < -99 else (enemy.Attribute_Armor_Physical+enemy.Status_Block_Strength))*0.01)))
    $ enemy.X_Armor_Magic_X = int(round((1 if (enemy.Equipment_Armor_Magic) < 1 else (enemy.Equipment_Armor_Magic))*((-99 if (enemy.Attribute_Armor_Magic+enemy.Status_Block_Strength) < -99 else (enemy.Attribute_Armor_Magic+enemy.Status_Block_Strength))*0.01)))
    $ enemy.X_Armor_Will_X = int(round((1 if (enemy.Equipment_Armor_Will) < 1 else (enemy.Equipment_Armor_Will))*((-99 if (enemy.Attribute_Armor_Will+enemy.Status_Block_Strength) < -99 else (enemy.Attribute_Armor_Will+enemy.Status_Block_Strength))*0.01)))
    return

label battle_call_Enemy_Damage_Bonus_Recheck:
    $ enemy.X_Strength_X = enemy.Stats_Strength+enemy.Equipment_Strength+enemy.Status_Strengthen_Strength-enemy.Status_Weaken_Strength
    $ enemy.X_Precision_X = enemy.Stats_Precision+enemy.Equipment_Precision+enemy.Status_Nimble_Strength-enemy.Status_Clumsy_Strength
    $ enemy.X_Insight_X = enemy.Stats_Insight+enemy.Equipment_Insight
    $ enemy.X_Deceit_X = enemy.Stats_Deceit+enemy.Equipment_Deceit
    $ enemy.Attribute_Damage_Bonus_Melee = (int(round((enemy.X_Strength_X/battle.Bonus_Damage_Stat_Divisor))))+100
    $ enemy.Attribute_Damage_Bonus_Ranged = (int(round((enemy.X_Precision_X/battle.Bonus_Damage_Stat_Divisor))))+100
    $ enemy.Attribute_Damage_Bonus_Magic = (int(round((enemy.X_Insight_X/battle.Bonus_Damage_Stat_Divisor))))+100
    $ enemy.Attribute_Damage_Bonus_Will = (int(round((enemy.X_Deceit_X/battle.Bonus_Damage_Stat_Divisor))))+100
    $ enemy.X_Damage_Bonus_Melee_Text_X = int(round((-99 if (enemy.Attribute_Damage_Bonus_Melee+enemy.Equipment_Damage_Bonus_Melee+enemy.Status_Strengthen_Strength-enemy.Status_Weaken_Strength) < -99 else (enemy.Attribute_Damage_Bonus_Melee+enemy.Equipment_Damage_Bonus_Melee+enemy.Status_Strengthen_Strength-enemy.Status_Weaken_Strength))))
    $ enemy.X_Damage_Bonus_Ranged_Text_X = int(round((-99 if (enemy.Attribute_Damage_Bonus_Ranged+enemy.Equipment_Damage_Bonus_Ranged+enemy.Status_Nimble_Strength-enemy.Status_Clumsy_Strength) < -99 else (enemy.Attribute_Damage_Bonus_Ranged+enemy.Equipment_Damage_Bonus_Ranged+enemy.Status_Nimble_Strength-enemy.Status_Clumsy_Strength))))
    $ enemy.X_Damage_Bonus_Magic_Text_X = int(round((-99 if (enemy.Attribute_Damage_Bonus_Magic+enemy.Equipment_Damage_Bonus_Magic) < -99 else (enemy.Attribute_Damage_Bonus_Magic+enemy.Equipment_Damage_Bonus_Magic))))
    $ enemy.X_Damage_Bonus_Will_Text_X = int(round((-99 if (enemy.Attribute_Damage_Bonus_Will+enemy.Equipment_Damage_Bonus_Will) < -99 else (enemy.Attribute_Damage_Bonus_Will+enemy.Equipment_Damage_Bonus_Will))))
    $ enemy.X_Damage_Bonus_Melee_X = (enemy.X_Damage_Bonus_Melee_Text_X)*0.01
    $ enemy.X_Damage_Bonus_Ranged_X = (enemy.X_Damage_Bonus_Ranged_Text_X)*0.01
    $ enemy.X_Damage_Bonus_Magic_X = (enemy.X_Damage_Bonus_Magic_Text_X)*0.01
    $ enemy.X_Damage_Bonus_Will_X = (enemy.X_Damage_Bonus_Will_Text_X)*0.01
    return

label battle_call_Enemy_Dodge_Recheck:
    $ enemy.X_Deceit_X = enemy.Stats_Deceit+enemy.Equipment_Deceit
    $ enemy.Attribute_Dodge = (int(round((enemy.X_Deceit_X/battle.Bonus_Dodge_Divisor))))
    $ enemy.X_Dodge_X = enemy.Attribute_Dodge+enemy.Equipment_Dodge+enemy.Status_Haste_Strength+enemy.Status_Dodge_Strength-enemy.Status_Slow_Strength
    return

label battle_call_Enemy_Initiative_Recheck:
    $ enemy.X_Insight_X = enemy.Stats_Insight+enemy.Equipment_Insight
    $ enemy.Attribute_Initiative = (int(round((enemy.X_Insight_X/battle.Bonus_Initiative_Divisor))))
    $ enemy.X_Initiative_X = enemy.Attribute_Initiative+enemy.Equipment_Initiative+enemy.Status_Haste_Strength-enemy.Status_Slow_Strength
    return

label battle_call_Enemy_Weapon_Accuracy_Recheck:
    $ enemy.X_Weapon_Accuracy_Melee_X = enemy.Attribute_Accuracy_Melee+enemy.Equipment_Weapon_Accuracy_Melee+enemy.Equipment_Accuracy_Melee
    $ enemy.X_Weapon_Accuracy_Ranged_X = enemy.Attribute_Accuracy_Ranged+enemy.Equipment_Weapon_Accuracy_Ranged+enemy.Equipment_Accuracy_Ranged

label battle_call_Enemy_Weapon_Damage_Recheck:
    $ enemy.X_Weapon_Damage_Melee_Max_X = int(round(enemy.Equipment_Weapon_Damage_Melee_Max*enemy.X_Damage_Bonus_Melee_X))
    $ enemy.X_Weapon_Damage_Melee_Min_X = int(round(enemy.Equipment_Weapon_Damage_Melee_Min*enemy.X_Damage_Bonus_Melee_X))
    $ enemy.X_Weapon_Damage_Ranged_Max_X = int(round(enemy.Equipment_Weapon_Damage_Ranged_Max*enemy.X_Damage_Bonus_Ranged_X))
    $ enemy.X_Weapon_Damage_Ranged_Min_X = int(round(enemy.Equipment_Weapon_Damage_Ranged_Min*enemy.X_Damage_Bonus_Ranged_X))
    $ enemy.X_Weapon_Damage_Magic_Max_X = int(round(enemy.Equipment_Weapon_Damage_Magic_Max*enemy.X_Damage_Bonus_Magic_X))
    $ enemy.X_Weapon_Damage_Magic_Min_X = int(round(enemy.Equipment_Weapon_Damage_Magic_Min*enemy.X_Damage_Bonus_Magic_X))
    $ enemy.X_Weapon_Damage_Will_Max_X = int(round(enemy.Equipment_Weapon_Damage_Will_Max*enemy.X_Damage_Bonus_Will_X))
    $ enemy.X_Weapon_Damage_Will_Min_X = int(round(enemy.Equipment_Weapon_Damage_Will_Min*enemy.X_Damage_Bonus_Will_X))
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
    $ enemy.Status_Clumsy_EffectActive = 0
    $ enemy.Status_Clumsy_Duration = 0
    $ enemy.Status_Clumsy_Strength = 0
    $ enemy.Status_Nimble_EffectActive = 0
    $ enemy.Status_Nimble_Duration = 0
    $ enemy.Status_Nimble_Strength = 0
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
    $ enemy.Status_EquipLoss_Weapon_Duration = 0
    $ enemy.Status_EquipLoss_Weapon_EffectActive = 0
    $ enemy.Status_EquipLoss_UpperBodyArmor_Duration = 0
    $ enemy.Status_EquipLoss_UpperBodyArmor_EffectActive = 0
    $ enemy.Status_EquipLoss_LowerBodyArmor_Duration = 0
    $ enemy.Status_EquipLoss_LowerBodyArmor_EffectActive = 0
    $ enemy.Status_EquipLoss_Necklace_Duration = 0
    $ enemy.Status_EquipLoss_Necklace_EffectActive = 0
    $ enemy.Status_EquipLoss_Ring_Duration = 0
    $ enemy.Status_EquipLoss_Ring_EffectActive = 0
# /\ Status effect inits.
# \/ Temporary inits to let the rest of the calculations fire in order.
#    Pretend I didn't do some silly recursive actions. x.x
    $ enemy.Equipment_Strength = 1
    $ enemy.Equipment_Precision = 1
    $ enemy.Equipment_Insight = 1
    $ enemy.Equipment_Deceit = 1
    $ enemy.Equipment_Vigor = 1
    $ enemy.Equipment_Spirit = 1
    $ enemy.Equipment_Resolve = 1
    $ enemy.Equipment_HealthPoints_Max = 1
    $ enemy.Equipment_AbilityPoints_Max = 1
    $ enemy.Equipment_WillPoints_Max = 1
    $ enemy.Equipment_Accuracy_Melee = 1
    $ enemy.Equipment_Accuracy_Ranged = 1
    $ enemy.Equipment_Armor_Physical = 1
    $ enemy.Equipment_Armor_Magic = 1
    $ enemy.Equipment_Armor_Will = 1
    $ enemy.Equipment_Damage_Bonus_Melee = 1
    $ enemy.Equipment_Damage_Bonus_Ranged = 1
    $ enemy.Equipment_Damage_Bonus_Magic = 1
    $ enemy.Equipment_Damage_Bonus_Will = 1
    $ enemy.Equipment_Dodge = 1
    $ enemy.Equipment_Initiative = 1
    $ enemy.Equipment_Weapon_Accuracy_Melee = 1
    $ enemy.Equipment_Weapon_Accuracy_Ranged = 1
    $ enemy.Equipment_Weapon_Damage_Melee_Max = 1
    $ enemy.Equipment_Weapon_Damage_Melee_Min = 1
    $ enemy.Equipment_Weapon_Damage_Ranged_Max = 1
    $ enemy.Equipment_Weapon_Damage_Ranged_Min = 1
    $ enemy.Equipment_Weapon_Damage_Magic_Max = 1
    $ enemy.Equipment_Weapon_Damage_Magic_Min = 1
    $ enemy.Equipment_Weapon_Damage_Will_Max = 1
    $ enemy.Equipment_Weapon_Damage_Will_Min = 1
# And the rest.
    $ enemy.Stats_Strength = ename.Stats_Strength
    $ enemy.Stats_Precision = ename.Stats_Precision
    $ enemy.Stats_Insight = ename.Stats_Insight
    $ enemy.Stats_Deceit = ename.Stats_Deceit
    $ enemy.Stats_Vigor = ename.Stats_Vigor
    $ enemy.Stats_Spirit = ename.Stats_Spirit
    $ enemy.Stats_Resolve = ename.Stats_Resolve
    $ enemy.Equipment_Slot_Weapon_Name = ename.Equipment_Slot_Weapon_Name
    $ enemy.Equipment_Slot_UpperBodyArmor_Name = ename.Equipment_Slot_UpperBodyArmor_Name
    $ enemy.Equipment_Slot_LowerBodyArmor_Name = ename.Equipment_Slot_LowerBodyArmor_Name
    $ enemy.Equipment_Slot_Necklace_Name = ename.Equipment_Slot_Necklace_Name
    $ enemy.Equipment_Slot_Ring_Name = ename.Equipment_Slot_Ring_Name
    $ enemy.Equipment_Consumables_Potions_HP_Restore = ename.Equipment_Consumables_Potions_HP_Restore
    $ enemy.Equipment_Consumables_Potions_AP_Restore = ename.Equipment_Consumables_Potions_AP_Restore
    $ enemy.Equipment_Consumables_Potions_WP_Restore = ename.Equipment_Consumables_Potions_WP_Restore
    $ enemy.Equipment_Currency = ename.Equipment_Currency
#  This line basically tells the game to go 'Okay, now calculate all the
# variables based on the data we've imported.  Saves us a mess of lines here.
    call battle_call_Enemy_Stat_Recheck
    call battle_call_Enemy_Ability_Recheck
    call call_Enemy_Equipment_Slot_Initialize_All
    call battle_call_Enemy_HP_AP_WP_Current_To_Max_Set
    return
