# Shirra's Ren'Py Battle Framework
# https://github.com/ShirraWhitefur/PyBattleFramework
# http://creativecommons.org/licenses/by-nc/3.0/

# Equipment Database - UpperBodyArmor
#  You might want to make an index of equipment sometime, just so you can find
# things once this gets unwieldy.  
#  Also! Remember, -every enemy needs equipment-.  You can use the same
# equipment pieces across multiple enemies.  In theory, this will save you some
# time in the long run, since you don't have to redefine the same axe over and
# over again.

# The first set in here should be 'No Equipment' for the slot.
init -99:
# UpperBodyArmor - No Armor Equipped - no_upper_armor
    $ no_upper_armor = Character("no_upper_armor")
    $ no_upper_armor.Equipment_Strength = 0
    $ no_upper_armor.Equipment_Precision = 0
    $ no_upper_armor.Equipment_Insight = 0
    $ no_upper_armor.Equipment_Deceit = 0
    $ no_upper_armor.Equipment_Vigor = 0
    $ no_upper_armor.Equipment_Spirit = 0
    $ no_upper_armor.Equipment_Resolve = 0
    $ no_upper_armor.Equipment_HealthPoints_Max = 0
    $ no_upper_armor.Equipment_AbilityPoints_Max = 0
    $ no_upper_armor.Equipment_WillPoints_Max = 0
    $ no_upper_armor.Equipment_Accuracy_Melee = 0
    $ no_upper_armor.Equipment_Accuracy_Ranged = 0
    $ no_upper_armor.Equipment_Armor_Physical = 0
    $ no_upper_armor.Equipment_Armor_Magic = 0
    $ no_upper_armor.Equipment_Armor_Will = 0
    $ no_upper_armor.Equipment_Damage_Bonus_Melee = 0
    $ no_upper_armor.Equipment_Damage_Bonus_Ranged = 0
    $ no_upper_armor.Equipment_Damage_Bonus_Magic = 0
    $ no_upper_armor.Equipment_Damage_Bonus_Will = 0
    $ no_upper_armor.Equipment_Dodge = 0
    $ no_upper_armor.Equipment_Initiative = 0
    $ no_upper_armor.Equipment_Slot_UpperBodyArmor_Name = no_upper_armor
    $ no_upper_armor.Equipment_Slot_UpperBodyArmor_Name_Text = "No Armor Equipped"
# UpperBodyArmor - Cloth Shirt - upper_cloth_shirt
    $ upper_cloth_shirt = Character("upper_cloth_shirt")
    $ upper_cloth_shirt.Equipment_Strength = 0
    $ upper_cloth_shirt.Equipment_Precision = 0
    $ upper_cloth_shirt.Equipment_Insight = 0
    $ upper_cloth_shirt.Equipment_Deceit = 0
    $ upper_cloth_shirt.Equipment_Vigor = 0
    $ upper_cloth_shirt.Equipment_Spirit = 0
    $ upper_cloth_shirt.Equipment_Resolve = 0
    $ upper_cloth_shirt.Equipment_HealthPoints_Max = 0
    $ upper_cloth_shirt.Equipment_AbilityPoints_Max = 0
    $ upper_cloth_shirt.Equipment_WillPoints_Max = 0
    $ upper_cloth_shirt.Equipment_Accuracy_Melee = 0
    $ upper_cloth_shirt.Equipment_Accuracy_Ranged = 0
    $ upper_cloth_shirt.Equipment_Armor_Physical = 1
    $ upper_cloth_shirt.Equipment_Armor_Magic = 1
    $ upper_cloth_shirt.Equipment_Armor_Will = 3
    $ upper_cloth_shirt.Equipment_Damage_Bonus_Melee = 0
    $ upper_cloth_shirt.Equipment_Damage_Bonus_Ranged = 0
    $ upper_cloth_shirt.Equipment_Damage_Bonus_Magic = 0
    $ upper_cloth_shirt.Equipment_Damage_Bonus_Will = 0
    $ upper_cloth_shirt.Equipment_Dodge = 2
    $ upper_cloth_shirt.Equipment_Initiative = 2
    $ upper_cloth_shirt.Equipment_Slot_UpperBodyArmor_Name = upper_cloth_shirt
    $ upper_cloth_shirt.Equipment_Slot_UpperBodyArmor_Name_Text = "Cloth Shirt"
# UpperBodyArmor - Chainmail Armor - upper_chain_armor
    $ upper_chain_armor = Character("upper_chain_armor")
    $ upper_chain_armor.Equipment_Strength = 0
    $ upper_chain_armor.Equipment_Precision = 0
    $ upper_chain_armor.Equipment_Insight = 0
    $ upper_chain_armor.Equipment_Deceit = 0
    $ upper_chain_armor.Equipment_Vigor = 0
    $ upper_chain_armor.Equipment_Spirit = 0
    $ upper_chain_armor.Equipment_Resolve = 0
    $ upper_chain_armor.Equipment_HealthPoints_Max = 5
    $ upper_chain_armor.Equipment_AbilityPoints_Max = 0
    $ upper_chain_armor.Equipment_WillPoints_Max = 0
    $ upper_chain_armor.Equipment_Accuracy_Melee = 0
    $ upper_chain_armor.Equipment_Accuracy_Ranged = 0
    $ upper_chain_armor.Equipment_Armor_Physical = 8
    $ upper_chain_armor.Equipment_Armor_Magic = 7
    $ upper_chain_armor.Equipment_Armor_Will = 4
    $ upper_chain_armor.Equipment_Damage_Bonus_Melee = 0
    $ upper_chain_armor.Equipment_Damage_Bonus_Ranged = 0
    $ upper_chain_armor.Equipment_Damage_Bonus_Magic = 0
    $ upper_chain_armor.Equipment_Damage_Bonus_Will = 0
    $ upper_chain_armor.Equipment_Dodge = 0
    $ upper_chain_armor.Equipment_Initiative = 0
    $ upper_chain_armor.Equipment_Slot_UpperBodyArmor_Name = upper_chain_armor
    $ upper_chain_armor.Equipment_Slot_UpperBodyArmor_Name_Text = "Chainmail Armor"
