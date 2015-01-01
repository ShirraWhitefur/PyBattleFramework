# Shirra's Ren'Py Battle Framework
# https://github.com/ShirraWhitefur/PyBattleFramework
# http://creativecommons.org/licenses/by-nc/3.0/

# Equipment Database - LowerBodyArmor
#  You might want to make an index of equipment sometime, just so you can find
# things once this gets unwieldy.  
#  Also! Remember, -every enemy needs equipment-.  You can use the same
# equipment pieces across multiple enemies.  In theory, this will save you some
# time in the long run, since you don't have to redefine the same axe over and
# over again.

# The first set in here should be 'No Equipment' for the slot.
init -99:
# LowerBodyArmor - No Armor Equipped - no_lower_armor
    $ no_lower_armor = Character("no_lower_armor")
    $ no_lower_armor.Equipment_HealthPoints_Max = 0
    $ no_lower_armor.Equipment_AbilityPoints_Max = 0
    $ no_lower_armor.Equipment_WillPoints_Max = 0
    $ no_lower_armor.Equipment_Accuracy_Melee = 0
    $ no_lower_armor.Equipment_Accuracy_Ranged = 0
    $ no_lower_armor.Equipment_Armor_Physical = 0
    $ no_lower_armor.Equipment_Armor_Magic = 0
    $ no_lower_armor.Equipment_Armor_Will = 0
    $ no_lower_armor.Equipment_Damage_Bonus_Melee = 0
    $ no_lower_armor.Equipment_Damage_Bonus_Ranged = 0
    $ no_lower_armor.Equipment_Damage_Bonus_Magic = 0
    $ no_lower_armor.Equipment_Damage_Bonus_Will = 0
    $ no_lower_armor.Equipment_Dodge = 0
    $ no_lower_armor.Equipment_Initiative = 0
    $ no_lower_armor.Equipment_Slot_LowerBodyArmor_Name = no_lower_armor
    $ no_lower_armor.Equipment_Slot_LowerBodyArmor_Name_Text = "No Armor Equipped"
# LowerBodyArmor - Ragged Leather Armor - lower_leather_rags
    $ lower_leather_rags = Character("lower_leather_rags")
    $ lower_leather_rags.Equipment_HealthPoints_Max = 0
    $ lower_leather_rags.Equipment_AbilityPoints_Max = 0
    $ lower_leather_rags.Equipment_WillPoints_Max = 0
    $ lower_leather_rags.Equipment_Accuracy_Melee = 0
    $ lower_leather_rags.Equipment_Accuracy_Ranged = 0
    $ lower_leather_rags.Equipment_Armor_Physical = 2
    $ lower_leather_rags.Equipment_Armor_Magic = 1
    $ lower_leather_rags.Equipment_Armor_Will = 1
    $ lower_leather_rags.Equipment_Damage_Bonus_Melee = 0
    $ lower_leather_rags.Equipment_Damage_Bonus_Ranged = 0
    $ lower_leather_rags.Equipment_Damage_Bonus_Magic = 0
    $ lower_leather_rags.Equipment_Damage_Bonus_Will = 0
    $ lower_leather_rags.Equipment_Dodge = 1
    $ lower_leather_rags.Equipment_Initiative = 1
    $ lower_leather_rags.Equipment_Slot_LowerBodyArmor_Name = lower_leather_rags
    $ lower_leather_rags.Equipment_Slot_LowerBodyArmor_Name_Text = "Ragged Leather Armor"
# LowerBodyArmor - Chainmail Leggings - lower_chain_armor
    $ lower_chain_armor = Character("lower_chain_armor")
    $ lower_chain_armor.Equipment_HealthPoints_Max = 0
    $ lower_chain_armor.Equipment_AbilityPoints_Max = 0
    $ lower_chain_armor.Equipment_WillPoints_Max = 0
    $ lower_chain_armor.Equipment_Accuracy_Melee = 0
    $ lower_chain_armor.Equipment_Accuracy_Ranged = 0
    $ lower_chain_armor.Equipment_Armor_Physical = 8
    $ lower_chain_armor.Equipment_Armor_Magic = 7
    $ lower_chain_armor.Equipment_Armor_Will = 4
    $ lower_chain_armor.Equipment_Damage_Bonus_Melee = 0
    $ lower_chain_armor.Equipment_Damage_Bonus_Ranged = 0
    $ lower_chain_armor.Equipment_Damage_Bonus_Magic = 0
    $ lower_chain_armor.Equipment_Damage_Bonus_Will = 0
    $ lower_chain_armor.Equipment_Dodge = 0
    $ lower_chain_armor.Equipment_Initiative = 0
    $ lower_chain_armor.Equipment_Slot_LowerBodyArmor_Name = lower_chain_armor
    $ lower_chain_armor.Equipment_Slot_LowerBodyArmor_Name_Text = "Chainmail Leggings"

