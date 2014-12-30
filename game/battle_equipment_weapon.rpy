# Shirra's Ren'Py Battle Framework
# https://github.com/ShirraWhitefur/PyBattleFramework
# http://creativecommons.org/licenses/by-nc/3.0/

# Equipment Database - Weapons
#  You might want to make an index of equipment sometime, just so you can find
# things once this gets unwieldy.  
#  Also! Remember, -every enemy needs equipment-.  You can use the same
# equipment pieces across multiple enemies.  In theory, this will save you some
# time in the long run, since you don't have to redefine the same axe over and
# over again.

# The first set in here should be 'No Equipment' for the slot.
init -99:
# Weapon - No Weapon Equipped - Bare Hands - no_weapon
    $ no_weapon = Character("no_weapon")
    $ no_weapon.Equipment_HealthPoints_Max = 0
    $ no_weapon.Equipment_AbilityPoints_Max = 0
    $ no_weapon.Equipment_WillPoints_Max = 0
    $ no_weapon.Equipment_Accuracy_Melee = 0
    $ no_weapon.Equipment_Accuracy_Ranged = 0
    $ no_weapon.Equipment_Armor_Physical = 0
    $ no_weapon.Equipment_Armor_Magic = 0
    $ no_weapon.Equipment_Armor_Will = 0
    $ no_weapon.Equipment_Damage_Bonus_Melee_Max = 0
    $ no_weapon.Equipment_Damage_Bonus_Ranged_Max = 0
    $ no_weapon.Equipment_Damage_Bonus_Magic_Max = 0
    $ no_weapon.Equipment_Damage_Bonus_Will_Max = 0
    $ no_weapon.Equipment_Dodge = 0
    $ no_weapon.Equipment_Initiative = 0
    $ no_weapon.Equipment_Weapon_Accuracy_Melee = 0
    $ no_weapon.Equipment_Weapon_Accuracy_Ranged = 0
    $ no_weapon.Equipment_Weapon_Damage_Melee_Max = 5
    $ no_weapon.Equipment_Weapon_Damage_Melee_Min = 1
    $ no_weapon.Equipment_Weapon_Damage_Ranged_Max = 5
    $ no_weapon.Equipment_Weapon_Damage_Ranged_Min = 1
    $ no_weapon.Equipment_Weapon_Damage_Magic_Max = 5
    $ no_weapon.Equipment_Weapon_Damage_Magic_Min = 1
    $ no_weapon.Equipment_Weapon_Damage_Will_Max = 5
    $ no_weapon.Equipment_Weapon_Damage_Will_Min = 1
    $ no_weapon.Equipment_Slot_Weapon_Name = no_weapon
    $ no_weapon.Equipment_Slot_Weapon_Name_Text = "No Weapon Equipped - Bare Hands"
    $ no_weapon.Equipment_Slot_Weapon_Accuracy_Type = "Melee"
    $ no_weapon.Equipment_Slot_Weapon_Damage_Type = "Melee"
# Weapon - Axe, Orcish - axe_orcish
    $ axe_orcish = Character("axe_orcish")
    $ axe_orcish.Equipment_HealthPoints_Max = 0
    $ axe_orcish.Equipment_AbilityPoints_Max = 0
    $ axe_orcish.Equipment_WillPoints_Max = 0
    $ axe_orcish.Equipment_Accuracy_Melee = 0
    $ axe_orcish.Equipment_Accuracy_Ranged = 0
    $ axe_orcish.Equipment_Armor_Physical = 0
    $ axe_orcish.Equipment_Armor_Magic = 0
    $ axe_orcish.Equipment_Armor_Will = 0
    $ axe_orcish.Equipment_Damage_Bonus_Melee_Max = 0
    $ axe_orcish.Equipment_Damage_Bonus_Ranged_Max = 0
    $ axe_orcish.Equipment_Damage_Bonus_Magic_Max = 0
    $ axe_orcish.Equipment_Damage_Bonus_Will_Max = 0
    $ axe_orcish.Equipment_Dodge = 0
    $ axe_orcish.Equipment_Initiative = 0
    $ axe_orcish.Equipment_Weapon_Accuracy_Melee = 2
    $ axe_orcish.Equipment_Weapon_Accuracy_Ranged = 0
    $ axe_orcish.Equipment_Weapon_Damage_Melee_Max = 12
    $ axe_orcish.Equipment_Weapon_Damage_Melee_Min = 2
    $ axe_orcish.Equipment_Weapon_Damage_Ranged_Max = 5
    $ axe_orcish.Equipment_Weapon_Damage_Ranged_Min = 1
    $ axe_orcish.Equipment_Weapon_Damage_Magic_Max = 5
    $ axe_orcish.Equipment_Weapon_Damage_Magic_Min = 1
    $ axe_orcish.Equipment_Weapon_Damage_Will_Max = 5
    $ axe_orcish.Equipment_Weapon_Damage_Will_Min = 1
    $ axe_orcish.Equipment_Slot_Weapon_Name = axe_orcish
    $ axe_orcish.Equipment_Slot_Weapon_Name_Text = "Orcish Axe"
    $ axe_orcish.Equipment_Slot_Weapon_Accuracy_Type = "Melee"
    $ axe_orcish.Equipment_Slot_Weapon_Damage_Type = "Melee"
# Weapon - Sword, Adventurer's - sword_adventurers
    $ sword_adventurers = Character("sword_adventurers")
    $ sword_adventurers.Equipment_HealthPoints_Max = 2
    $ sword_adventurers.Equipment_AbilityPoints_Max = 0
    $ sword_adventurers.Equipment_WillPoints_Max = 0
    $ sword_adventurers.Equipment_Accuracy_Melee = 0
    $ sword_adventurers.Equipment_Accuracy_Ranged = 0
    $ sword_adventurers.Equipment_Armor_Physical = 0
    $ sword_adventurers.Equipment_Armor_Magic = 0
    $ sword_adventurers.Equipment_Armor_Will = 0
    $ sword_adventurers.Equipment_Damage_Bonus_Melee_Max = 2
    $ sword_adventurers.Equipment_Damage_Bonus_Ranged_Max = 0
    $ sword_adventurers.Equipment_Damage_Bonus_Magic_Max = 0
    $ sword_adventurers.Equipment_Damage_Bonus_Will_Max = 0
    $ sword_adventurers.Equipment_Dodge = 0
    $ sword_adventurers.Equipment_Initiative = 0
    $ sword_adventurers.Equipment_Weapon_Accuracy_Melee = 5
    $ sword_adventurers.Equipment_Weapon_Accuracy_Ranged = 0
    $ sword_adventurers.Equipment_Weapon_Damage_Melee_Max = 15
    $ sword_adventurers.Equipment_Weapon_Damage_Melee_Min = 3
    $ sword_adventurers.Equipment_Weapon_Damage_Ranged_Max = 5
    $ sword_adventurers.Equipment_Weapon_Damage_Ranged_Min = 1
    $ sword_adventurers.Equipment_Weapon_Damage_Magic_Max = 5
    $ sword_adventurers.Equipment_Weapon_Damage_Magic_Min = 1
    $ sword_adventurers.Equipment_Weapon_Damage_Will_Max = 5
    $ sword_adventurers.Equipment_Weapon_Damage_Will_Min = 1
    $ sword_adventurers.Equipment_Slot_Weapon_Name = sword_adventurers
    $ sword_adventurers.Equipment_Slot_Weapon_Name_Text = "Adventurer's Sword"
    $ sword_adventurers.Equipment_Slot_Weapon_Accuracy_Type = "Melee"
    $ sword_adventurers.Equipment_Slot_Weapon_Damage_Type = "Melee"
# Weapon - Bow, Short - bow_short
    $ bow_short = Character("bow_short")
    $ bow_short.Equipment_HealthPoints_Max = 0
    $ bow_short.Equipment_AbilityPoints_Max = 0
    $ bow_short.Equipment_WillPoints_Max = 0
    $ bow_short.Equipment_Accuracy_Melee = 0
    $ bow_short.Equipment_Accuracy_Ranged = 0
    $ bow_short.Equipment_Armor_Physical = 0
    $ bow_short.Equipment_Armor_Magic = 0
    $ bow_short.Equipment_Armor_Will = 0
    $ bow_short.Equipment_Damage_Bonus_Melee_Max = 0
    $ bow_short.Equipment_Damage_Bonus_Ranged_Max = 10
    $ bow_short.Equipment_Damage_Bonus_Magic_Max = 0
    $ bow_short.Equipment_Damage_Bonus_Will_Max = 0
    $ bow_short.Equipment_Dodge = 0
    $ bow_short.Equipment_Initiative = 0
    $ bow_short.Equipment_Weapon_Accuracy_Melee = 0
    $ bow_short.Equipment_Weapon_Accuracy_Ranged = 10
    $ bow_short.Equipment_Weapon_Damage_Melee_Max = 5
    $ bow_short.Equipment_Weapon_Damage_Melee_Min = 1
    $ bow_short.Equipment_Weapon_Damage_Ranged_Max = 10
    $ bow_short.Equipment_Weapon_Damage_Ranged_Min = 5
    $ bow_short.Equipment_Weapon_Damage_Magic_Max = 5
    $ bow_short.Equipment_Weapon_Damage_Magic_Min = 1
    $ bow_short.Equipment_Weapon_Damage_Will_Max = 5
    $ bow_short.Equipment_Weapon_Damage_Will_Min = 1
    $ bow_short.Equipment_Slot_Weapon_Name = bow_short
    $ bow_short.Equipment_Slot_Weapon_Name_Text = "Short Bow"
    $ bow_short.Equipment_Slot_Weapon_Accuracy_Type = "Ranged"
    $ bow_short.Equipment_Slot_Weapon_Damage_Type = "Ranged"
# Weapon - Wand of the Firemage - wand_firemage
    $ wand_firemage = Character("wand_firemage")
    $ wand_firemage.Equipment_HealthPoints_Max = 0
    $ wand_firemage.Equipment_AbilityPoints_Max = 20
    $ wand_firemage.Equipment_WillPoints_Max = 0
    $ wand_firemage.Equipment_Accuracy_Melee = 0
    $ wand_firemage.Equipment_Accuracy_Ranged = 5
    $ wand_firemage.Equipment_Armor_Physical = 0
    $ wand_firemage.Equipment_Armor_Magic = 0
    $ wand_firemage.Equipment_Armor_Will = 0
    $ wand_firemage.Equipment_Damage_Bonus_Melee_Max = 0
    $ wand_firemage.Equipment_Damage_Bonus_Ranged_Max = 0
    $ wand_firemage.Equipment_Damage_Bonus_Magic_Max = 10
    $ wand_firemage.Equipment_Damage_Bonus_Will_Max = 0
    $ wand_firemage.Equipment_Dodge = 0
    $ wand_firemage.Equipment_Initiative = 0
    $ wand_firemage.Equipment_Weapon_Accuracy_Melee = 0
    $ wand_firemage.Equipment_Weapon_Accuracy_Ranged = 0
    $ wand_firemage.Equipment_Weapon_Damage_Melee_Max = 5
    $ wand_firemage.Equipment_Weapon_Damage_Melee_Min = 1
    $ wand_firemage.Equipment_Weapon_Damage_Ranged_Max = 5
    $ wand_firemage.Equipment_Weapon_Damage_Ranged_Min = 1
    $ wand_firemage.Equipment_Weapon_Damage_Magic_Max = 30
    $ wand_firemage.Equipment_Weapon_Damage_Magic_Min = 10
    $ wand_firemage.Equipment_Weapon_Damage_Will_Max = 5
    $ wand_firemage.Equipment_Weapon_Damage_Will_Min = 1
    $ wand_firemage.Equipment_Slot_Weapon_Name = wand_firemage
    $ wand_firemage.Equipment_Slot_Weapon_Name_Text = "Wand of the Firemage"
    $ wand_firemage.Equipment_Slot_Weapon_Accuracy_Type = "Ranged"
    $ wand_firemage.Equipment_Slot_Weapon_Damage_Type = "Magic"
