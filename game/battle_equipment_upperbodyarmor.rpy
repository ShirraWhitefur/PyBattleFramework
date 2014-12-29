# Equipment Database - UpperBodyArmor
#  You might want to make an index of equipment sometime, just so you can find
# things once this gets unwieldy.  
#  Also! Remember, -every enemy needs equipment-.  You can use the same
# equipment pieces across multiple enemies.  In theory, this will save you some
# time in the long run, since you don't have to redefine the same axe over and
# over again.

# The first set in here should be 'No Equipment' for the slot.
init:
# UpperBodyArmor - No Armor Equipped - no_upper_armor
    $ no_upper_armor = Character("no_upper_armor")
    $ no_upper_armor.Equipment_HealthPoints_Max = 0
    $ no_upper_armor.Equipment_AbilityPoints_Max = 0
    $ no_upper_armor.Equipment_WillPoints_Max = 0
    $ no_upper_armor.Equipment_Accuracy_Melee = 0
    $ no_upper_armor.Equipment_Accuracy_Ranged = 0
    $ no_upper_armor.Equipment_Armor_Physical = 0
    $ no_upper_armor.Equipment_Armor_Magic = 0
    $ no_upper_armor.Equipment_Armor_Will = 0
    $ no_upper_armor.Equipment_Damage_Bonus_Melee_Max = 0
    $ no_upper_armor.Equipment_Damage_Bonus_Ranged_Max = 0
    $ no_upper_armor.Equipment_Damage_Bonus_Magic_Max = 0
    $ no_upper_armor.Equipment_Damage_Bonus_Will_Max = 0
    $ no_upper_armor.Equipment_Dodge = 0
    $ no_upper_armor.Equipment_Initiative = 0
    $ no_upper_armor.Equipment_Slot_UpperBodyArmor_Name = "no_upper_armor"
    $ no_upper_armor.Equipment_Slot_UpperBodyArmor_Name_Text = "No Armor Equipped"
