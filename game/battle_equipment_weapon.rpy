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
