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
    $ battle.Damage_Bonus_Min_Divisor = 10
    $ ename = "FailName"
#####################################################################
# Enemy Init Section
#####################################################################
    $ enemy = Character("Current Foe")
    $ enemy.name = "FailedEnemy"
    $ enemy.battle_selected_action = "battle_Enemy_Wait"
    $ enemy.Attack_List = "Attack_List_Goblin"
#  Base Stats - From these, when they're actually added and used, we'll get our
# base attributes.
    $ enemy.Stats_PlaceholderStrength = 0
#  Base attributes, to be derived from Stats.. when we add the stats in.
# The idea here being something like you set up Strength above, then set 
# player.Attribute_Damage_Bonus_Melee_Max = player.Stats_Strength/5, or something
# similar.  Set up an initialization/recheck call for players and enemies under
# battle calls.  There should be enough examples to know where and how to
# use it.
    $ enemy.Attribute_HealthPoints_Max = 5
    $ enemy.Attribute_AbilityPoints_Max = 5
    $ enemy.Attribute_WillPoints_Max = 5
    $ enemy.Attribute_Accuracy_Melee = 0
    $ enemy.Attribute_Accuracy_Ranged = 0
    $ enemy.Attribute_Armor_Physical = 0
    $ enemy.Attribute_Armor_Magic = 0
    $ enemy.Attribute_Armor_Will = 0
    $ enemy.Attribute_Damage_Bonus_Melee_Max = 0
    $ enemy.Attribute_Damage_Bonus_Ranged_Max = 0
    $ enemy.Attribute_Damage_Bonus_Magic_Max = 0
    $ enemy.Attribute_Damage_Bonus_Will_Max = 0
    $ enemy.Attribute_Dodge = 0
    $ enemy.Attribute_Initiative = 0
# Equipment.. which may be derived.. if we add in equipment properly.
    $ enemy.Equipment_HealthPoints_Max = 0
    $ enemy.Equipment_AbilityPoints_Max = 0
    $ enemy.Equipment_WillPoints_Max = 0
    $ enemy.Equipment_Accuracy_Melee = 0
    $ enemy.Equipment_Accuracy_Ranged = 0
    $ enemy.Equipment_Armor_Physical = 0
    $ enemy.Equipment_Armor_Magic = 0
    $ enemy.Equipment_Armor_Will = 0
    $ enemy.Equipment_Damage_Bonus_Melee_Max = 0
    $ enemy.Equipment_Damage_Bonus_Ranged_Max = 0
    $ enemy.Equipment_Damage_Bonus_Magic_Max = 0
    $ enemy.Equipment_Damage_Bonus_Will_Max = 0
    $ enemy.Equipment_Dodge = 0
    $ enemy.Equipment_Initiative = 0
    $ enemy.Equipment_Weapon_Accuracy_Melee = 0
    $ enemy.Equipment_Weapon_Accuracy_Ranged = 0
    $ enemy.Equipment_Weapon_Damage_Melee_Max = 5
    $ enemy.Equipment_Weapon_Damage_Melee_Min = 1
    $ enemy.Equipment_Weapon_Damage_Ranged_Max = 5
    $ enemy.Equipment_Weapon_Damage_Ranged_Min = 1
    $ enemy.Equipment_Weapon_Damage_Magic_Max = 5
    $ enemy.Equipment_Weapon_Damage_Magic_Min = 1
    $ enemy.Equipment_Weapon_Damage_Will_Max = 5
    $ enemy.Equipment_Weapon_Damage_Will_Min = 1
# Equipment Slots and Weapon Type
    $ enemy.Equipment_Slot_Weapon_Name = no_weapon
    $ enemy.Equipment_Slot_Weapon_Name_Text = "Gear Init Failed."
    $ enemy.Equipment_Slot_Weapon_Accuracy_Type = "Melee"
    $ enemy.Equipment_Slot_Weapon_Damage_Type = "Melee"
    $ enemy.Equipment_Slot_UpperBodyArmor_Name = no_upper_armor
    $ enemy.Equipment_Slot_UpperBodyArmor_Name_Text = "Gear Init Failed."
    $ enemy.Equipment_Slot_LowerBodyArmor_Name = no_lower_armor
    $ enemy.Equipment_Slot_LowerBodyArmor_Name_Text = "Gear Init Failed."
    $ enemy.Equipment_Slot_Necklace_Name = no_necklace
    $ enemy.Equipment_Slot_Necklace_Name_Text = "Gear Init Failed."
    $ enemy.Equipment_Slot_Ring_Name = no_ring
    $ enemy.Equipment_Slot_Ring_Name_Text = "Gear Init Failed."
#  Equipment - Consumables.  Consider it a 'stock', and will handle the
# potions, grenades, and other one use items and non-rechargables (like wands.)
    $ enemy.Equipment_Consumables_Potions_HP_Restore = 0
    $ enemy.Equipment_Consumables_Potions_AP_Restore = 0
    $ enemy.Equipment_Consumables_Potions_WP_Restore = 0
    $ enemy.Equipment_Currency = 0
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
# Enemy's Calculated Attributes
    $ enemy.X_HealthPoints_Current_X = 50
    $ enemy.X_HealthPoints_Max_X = 50
    $ enemy.X_AbilityPoints_Current_X = 30
    $ enemy.X_AbilityPoints_Max_X = 30
    $ enemy.X_WillPoints_Max_X = 0
    $ enemy.X_WillPoints_Current_X = 0
    $ enemy.X_PlaceholderStrength_X = 0
    $ enemy.X_Accuracy_Melee_X = 0
    $ enemy.X_Accuracy_Ranged_X = 0
    $ enemy.X_Armor_Physical_X = 0
    $ enemy.X_Armor_Magic_X = 0
    $ enemy.X_Armor_Will_X = 0
    $ enemy.X_Damage_Bonus_Melee_Max_X = 0
    $ enemy.X_Damage_Bonus_Melee_Min_X = 0
    $ enemy.X_Damage_Bonus_Ranged_Max_X = 0
    $ enemy.X_Damage_Bonus_Ranged_Min_X = 0
    $ enemy.X_Damage_Bonus_Magic_Max_X = 0
    $ enemy.X_Damage_Bonus_Magic_Min_X = 0
    $ enemy.X_Damage_Bonus_Will_Max_X = 0
    $ enemy.X_Damage_Bonus_Will_Min_X = 0
    $ enemy.X_Dodge_X = 0
    $ enemy.X_Initiative_X = 0
    $ enemy.X_Weapon_Accuracy_Melee_X = 0
    $ enemy.X_Weapon_Accuracy_Ranged_X = 0
    $ enemy.X_Weapon_Damage_Melee_Max_X = 0
    $ enemy.X_Weapon_Damage_Melee_Min_X = 0
    $ enemy.X_Weapon_Damage_Ranged_Max_X = 0
    $ enemy.X_Weapon_Damage_Ranged_Min_X = 0
    $ enemy.X_Weapon_Damage_Magic_Max_X = 0
    $ enemy.X_Weapon_Damage_Magic_Min_X = 0
    $ enemy.X_Weapon_Damage_Will_Max_X = 0
    $ enemy.X_Weapon_Damage_Will_Min_X = 0
