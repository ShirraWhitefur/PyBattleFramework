# Shirra's Ren'Py Battle Framework
# https://github.com/ShirraWhitefur/PyBattleFramework
# http://creativecommons.org/licenses/by-nc/3.0/

#  We have to initialize a whole mess of variables for this system to work
# nicely, and the enemy needs a full set of them.  The enemy here though is
# representing the -current- enemy, loaded into memory, a copy of one from the
# enemy files.  Those are effectively a template.  To set up the enemies, make
# their own files and names for them, rather than messing with this one, beyond
# customizing things to include whatever stat system and other changes you want
# to make across the board.
#  Also, anything with .* style variables on it is being set up as a character
# because.. well it's the only way I could make it work.  So yes.  Battle is a
# character.

# The following init python section is from Asceai on the forums
# ' http://lemmasoft.renai.us/forums/viewtopic.php?p=323010#p323010 '
# It's used to power our enemy AI system!
init python:-100
    def WeightedChoice(choices):
        """
        @param choices: A list of (choice, weight) tuples. Returns a random
        choice (using renpy.random as the random number generator)
        """
        totalweight = 0.0
        for choice, weight in choices:
            totalweight += weight
        randval = renpy.random.random() * totalweight
        for choice, weight in choices:
            if randval <= weight:
                return choice
            else:
                randval -= weight

init -75:
    $ battle = Character("BattleSettings")
    $ battle.roundcount = 0
    $ battle.EquipGearName = "no_weapon"
#  Multipliers for the Stats to Attributes (bonuses) math, to make the system
# easier to quickly tweak.
    $ battle.Base_HealthPoints_Max = 50
    $ battle.Base_AbilityPoints_Max = 30
    $ battle.Base_WillPoints_Max = 50
    $ battle.Bonus_Damage_Stat_Divisor = 10
    $ battle.Bonus_Armor_Stat_Divisor = 10
    $ battle.Bonus_HPAPWP_Max_Stat_Divisor = 10
    $ battle.Bonus_Accuracy_Divisor = 5
    $ battle.Bonus_Dodge_Divisor = 5
    $ battle.Bonus_Initiative_Divisor = 5
#
    $ ename = "FailName"
#####################################################################
# Enemy Init Section
#####################################################################
    $ enemy = Character("Current Foe")
    $ enemy.name = "FailedEnemy"
    $ enemy.battle_selected_action = "battle_Enemy_Wait"
    $ enemy.Attack_List = "Attack_List_Goblin"
######
# Status Effects
#  This block handles status effects, including the check to see if it's on.
# EffectActive is probably going to be used mostly for the Screen/Frame/UI
# stuff.
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
######
# Equipment Initilization
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
# Equipment Slots and Weapon Type
    $ enemy.Equipment_Slot_Weapon_Name = no_weapon
    $ enemy.Equipment_Slot_Weapon_Name_Temp = no_weapon
    $ enemy.Equipment_Slot_Weapon_Name_Text = "Gear Init Failed."
    $ enemy.Equipment_Slot_Weapon_Accuracy_Type = "Melee"
    $ enemy.Equipment_Slot_Weapon_Damage_Type = "Melee"
    $ enemy.Equipment_Slot_UpperBodyArmor_Name = no_upper_armor
    $ enemy.Equipment_Slot_UpperBodyArmor_Name_Temp = no_upper_armor
    $ enemy.Equipment_Slot_UpperBodyArmor_Name_Text = "Gear Init Failed."
    $ enemy.Equipment_Slot_LowerBodyArmor_Name = no_lower_armor
    $ enemy.Equipment_Slot_LowerBodyArmor_Name_Temp = no_lower_armor
    $ enemy.Equipment_Slot_LowerBodyArmor_Name_Text = "Gear Init Failed."
    $ enemy.Equipment_Slot_Necklace_Name = no_necklace
    $ enemy.Equipment_Slot_Necklace_Name_Temp = no_necklace
    $ enemy.Equipment_Slot_Necklace_Name_Text = "Gear Init Failed."
    $ enemy.Equipment_Slot_Ring_Name = no_ring
    $ enemy.Equipment_Slot_Ring_Name_Temp = no_ring
    $ enemy.Equipment_Slot_Ring_Name_Text = "Gear Init Failed."
######
#  Equipment - Consumables.  Consider it a 'stock', and will handle the
# potions, grenades, and other one use items and non-rechargables (like wands.)
    $ enemy.Equipment_Consumables_Potions_HP_Restore = 3
    $ enemy.Equipment_Consumables_Potions_AP_Restore = 2
    $ enemy.Equipment_Consumables_Potions_WP_Restore = 1
    $ enemy.Equipment_Currency = 5000
######
# Enemy's Base Statistics
# Just for quick reference..
#   Strength    Damage - Melee (percentage boost); Accuracy - Melee (integer boost)
#   Precision   Damage - Ranged (percentage boost); Accuracy - Ranged (integer boost)
#   Insight     Damage - Magic (percentage boost); Initiative (integer boost)
#   Deceit      Damage - Will (percentage boost); Dodge (integar boost)
#   Vigor       Max HP (percentage boost); Armor - Physical (percentage boost)
#   Spirit      Max AP (percentage boost); Armor - Magic (percentage boost)
#   Resolve     Max WP (percentage boost); Armor - Will (percentage boost)
#  Here, Dodge is being considered effectively 'Feint' or 'Bluff', faking
# someone out about where they'll think you'll be as opposed to where you end
# up.  .. At least that's how we explain it, so the two go to gether.
    $ enemy.Stats_Strength = 20
    $ enemy.Stats_Precision = 20
    $ enemy.Stats_Insight = 20
    $ enemy.Stats_Deceit = 20
    $ enemy.Stats_Vigor = 20
    $ enemy.Stats_Spirit = 20
    $ enemy.Stats_Resolve = 20
######
# Enemy's Calculated, Final Statistics
    $ enemy.X_Strength_X = enemy.Stats_Strength+enemy.Equipment_Strength+enemy.Status_Strengthen_Strength-enemy.Status_Weaken_Strength
    $ enemy.X_Precision_X = enemy.Stats_Precision+enemy.Equipment_Precision+enemy.Status_Nimble_Strength-enemy.Status_Clumsy_Strength
    $ enemy.X_Insight_X = enemy.Stats_Insight+enemy.Equipment_Insight
    $ enemy.X_Deceit_X = enemy.Stats_Deceit+enemy.Equipment_Deceit
    $ enemy.X_Vigor_X = enemy.Stats_Vigor+enemy.Equipment_Vigor
    $ enemy.X_Spirit_X = enemy.Stats_Spirit+enemy.Equipment_Spirit
    $ enemy.X_Resolve_X = enemy.Stats_Resolve+enemy.Equipment_Resolve
######
# Enemy's Base Attributes
# Or bonuses and penalties.  Derived from Stats, we may want to be able to
# directly add to attributes seperate from the stats (as in, for the progression
# of a character.  We'll see if we reallly want that mess of code to deal with
# though later.
#  Since we're going to need to work on balancing this somewhat 'on the fly', to
# make it easier to manipulate the system elsewhere to find that balance we will
# be using variables (over in battle_init) set on battle.Bonus_*, to work with
# our math.  
#
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
######
# Enemy's Calculated, Final Attributes
#  Yes, status effects can end up being applied to both the stat -and- the
# attribute.  It's a matter of scale, and that stat checks will happen seperate
# of their derived abilities/bonuses.  +10 to a stat check can be a big boost,
# but it's only +1% to damage.  +10% to damage is nice, but that'd be a +100
# stat boost.  So they need duplication.  So +10 to the stat, +10 to the damage,
# +1 more to damage from that stat buff.  Easy and fairly reasonable.
#  Further.  All Attribute bonuses (aside from dodge and accuracy) are
# percentage multipliers, while all of equipment is flat, static bonuses.  This
# keeps attributes -always- relevant, while equipment is our biggest 'power
# creep' method.
    $ enemy.X_HealthPoints_Max_X = int(round((1 if (battle.Base_HealthPoints_Max+enemy.Equipment_HealthPoints_Max) < 1 else (battle.Base_HealthPoints_Max+enemy.Equipment_HealthPoints_Max))*((-99 if (enemy.Attribute_HealthPoints) < -99 else (enemy.Attribute_HealthPoints))*0.01)))
    $ enemy.X_HealthPoints_Current_X = enemy.X_HealthPoints_Max_X
    $ enemy.X_AbilityPoints_Max_X = int(round((1 if (battle.Base_AbilityPoints_Max+enemy.Equipment_AbilityPoints_Max) < 1 else (battle.Base_AbilityPoints_Max+enemy.Equipment_AbilityPoints_Max))*((-99 if (enemy.Attribute_AbilityPoints) < -99 else (enemy.Attribute_AbilityPoints))*0.01)))
    $ enemy.X_AbilityPoints_Current_X = enemy.X_AbilityPoints_Max_X
    $ enemy.X_WillPoints_Max_X = int(round((1 if (battle.Base_WillPoints_Max+enemy.Equipment_WillPoints_Max) < 1 else (battle.Base_WillPoints_Max+enemy.Equipment_WillPoints_Max))*((-99 if (enemy.Attribute_WillPoints) < -99 else (enemy.Attribute_WillPoints))*0.01)))
    $ enemy.X_WillPoints_Current_X = enemy.X_WillPoints_Max_X
    $ enemy.X_Accuracy_Melee_X = enemy.Attribute_Accuracy_Melee+enemy.Equipment_Accuracy_Melee
    $ enemy.X_Accuracy_Ranged_X = enemy.Attribute_Accuracy_Ranged+enemy.Equipment_Accuracy_Ranged
# For the time being, Block will increase not just Physical armor, but also Magic and Will.  This is to be discussed and debated.
    $ enemy.X_Armor_Physical_X = int(round((1 if (enemy.Equipment_Armor_Physical) < 1 else (enemy.Equipment_Armor_Physical))*((-99 if (enemy.Attribute_Armor_Physical+enemy.Status_Block_Strength) < -99 else (enemy.Attribute_Armor_Physical+enemy.Status_Block_Strength))*0.01)))
    $ enemy.X_Armor_Magic_X = int(round((1 if (enemy.Equipment_Armor_Magic) < 1 else (enemy.Equipment_Armor_Magic))*((-99 if (enemy.Attribute_Armor_Magic+enemy.Status_Block_Strength) < -99 else (enemy.Attribute_Armor_Magic+enemy.Status_Block_Strength))*0.01)))
    $ enemy.X_Armor_Will_X = int(round((1 if (enemy.Equipment_Armor_Will) < 1 else (enemy.Equipment_Armor_Will))*((-99 if (enemy.Attribute_Armor_Will+enemy.Status_Block_Strength) < -99 else (enemy.Attribute_Armor_Will+enemy.Status_Block_Strength))*0.01)))
    $ enemy.X_Dodge_X = enemy.Attribute_Dodge+enemy.Equipment_Dodge+enemy.Status_Haste_Strength+enemy.Status_Dodge_Strength-enemy.Status_Slow_Strength
    $ enemy.X_Initiative_X = enemy.Attribute_Initiative+enemy.Equipment_Initiative+enemy.Status_Haste_Strength-enemy.Status_Slow_Strength
    $ enemy.X_Damage_Bonus_Melee_Text_X = int(round((-99 if (enemy.Attribute_Damage_Bonus_Melee+enemy.Equipment_Damage_Bonus_Melee+enemy.Status_Strengthen_Strength-enemy.Status_Weaken_Strength) < -99 else (enemy.Attribute_Damage_Bonus_Melee+enemy.Equipment_Damage_Bonus_Melee+enemy.Status_Strengthen_Strength-enemy.Status_Weaken_Strength))))
    $ enemy.X_Damage_Bonus_Ranged_Text_X = int(round((-99 if (enemy.Attribute_Damage_Bonus_Ranged+enemy.Equipment_Damage_Bonus_Ranged+enemy.Status_Nimble_Strength-enemy.Status_Clumsy_Strength) < -99 else (enemy.Attribute_Damage_Bonus_Ranged+enemy.Equipment_Damage_Bonus_Ranged+enemy.Status_Nimble_Strength-enemy.Status_Clumsy_Strength))))
    $ enemy.X_Damage_Bonus_Magic_Text_X = int(round((-99 if (enemy.Attribute_Damage_Bonus_Magic+enemy.Equipment_Damage_Bonus_Magic) < -99 else (enemy.Attribute_Damage_Bonus_Magic+enemy.Equipment_Damage_Bonus_Magic))))
    $ enemy.X_Damage_Bonus_Will_Text_X = int(round((-99 if (enemy.Attribute_Damage_Bonus_Will+enemy.Equipment_Damage_Bonus_Will) < -99 else (enemy.Attribute_Damage_Bonus_Will+enemy.Equipment_Damage_Bonus_Will))))
    $ enemy.X_Damage_Bonus_Melee_X = (enemy.X_Damage_Bonus_Melee_Text_X)*0.01
    $ enemy.X_Damage_Bonus_Ranged_X = (enemy.X_Damage_Bonus_Ranged_Text_X)*0.01
    $ enemy.X_Damage_Bonus_Magic_X = (enemy.X_Damage_Bonus_Magic_Text_X)*0.01
    $ enemy.X_Damage_Bonus_Will_X = (enemy.X_Damage_Bonus_Will_Text_X)*0.01
    $ enemy.X_Weapon_Accuracy_Melee_X = int(round(enemy.Equipment_Weapon_Accuracy_Melee+enemy.X_Accuracy_Melee_X))
    $ enemy.X_Weapon_Accuracy_Ranged_X = int(round(enemy.Equipment_Weapon_Accuracy_Ranged+enemy.X_Accuracy_Ranged_X))
    $ enemy.X_Weapon_Damage_Melee_Max_X = int(round(enemy.Equipment_Weapon_Damage_Melee_Max*enemy.X_Damage_Bonus_Melee_X))
    $ enemy.X_Weapon_Damage_Melee_Min_X = int(round(enemy.Equipment_Weapon_Damage_Melee_Min*enemy.X_Damage_Bonus_Melee_X))
    $ enemy.X_Weapon_Damage_Ranged_Max_X = int(round(enemy.Equipment_Weapon_Damage_Ranged_Max*enemy.X_Damage_Bonus_Ranged_X))
    $ enemy.X_Weapon_Damage_Ranged_Min_X = int(round(enemy.Equipment_Weapon_Damage_Ranged_Min*enemy.X_Damage_Bonus_Ranged_X))
    $ enemy.X_Weapon_Damage_Magic_Max_X = int(round(enemy.Equipment_Weapon_Damage_Magic_Max*enemy.X_Damage_Bonus_Magic_X))
    $ enemy.X_Weapon_Damage_Magic_Min_X = int(round(enemy.Equipment_Weapon_Damage_Magic_Min*enemy.X_Damage_Bonus_Magic_X))
    $ enemy.X_Weapon_Damage_Will_Max_X = int(round(enemy.Equipment_Weapon_Damage_Will_Max*enemy.X_Damage_Bonus_Will_X))
    $ enemy.X_Weapon_Damage_Will_Min_X = int(round(enemy.Equipment_Weapon_Damage_Will_Min*enemy.X_Damage_Bonus_Will_X))

