# Shirra's Ren'Py Battle Framework
# https://github.com/ShirraWhitefur/PyBattleFramework
# http://creativecommons.org/licenses/by-nc/3.0/

# Equipment Database - Ring
#  You might want to make an index of equipment sometime, just so you can find
# things once this gets unwieldy.  
#  Also! Remember, -every enemy needs equipment-.  You can use the same
# equipment pieces across multiple enemies.  In theory, this will save you some
# time in the long run, since you don't have to redefine the same axe over and
# over again.

# The first set in here should be 'No Equipment' for the slot.
init -99:
# Ring - No Ring Worn - no_ring
    $ no_ring = Character("no_ring")
    $ no_ring.Equipment_HealthPoints_Max = 0
    $ no_ring.Equipment_AbilityPoints_Max = 0
    $ no_ring.Equipment_WillPoints_Max = 0
    $ no_ring.Equipment_Accuracy_Melee = 0
    $ no_ring.Equipment_Accuracy_Ranged = 0
    $ no_ring.Equipment_Armor_Physical = 0
    $ no_ring.Equipment_Armor_Magic = 0
    $ no_ring.Equipment_Armor_Will = 0
    $ no_ring.Equipment_Damage_Bonus_Melee_Max = 0
    $ no_ring.Equipment_Damage_Bonus_Ranged_Max = 0
    $ no_ring.Equipment_Damage_Bonus_Magic_Max = 0
    $ no_ring.Equipment_Damage_Bonus_Will_Max = 0
    $ no_ring.Equipment_Dodge = 0
    $ no_ring.Equipment_Initiative = 0
    $ no_ring.Equipment_Slot_Ring_Name = no_ring
    $ no_ring.Equipment_Slot_Ring_Name_Text = "No Ring Worn"
# Ring - Ring of Magic Power - ring_magic_power
    $ ring_magic_power = Character("ring_magic_power")
    $ ring_magic_power.Equipment_HealthPoints_Max = 0
    $ ring_magic_power.Equipment_AbilityPoints_Max = 0
    $ ring_magic_power.Equipment_WillPoints_Max = 0
    $ ring_magic_power.Equipment_Accuracy_Melee = 0
    $ ring_magic_power.Equipment_Accuracy_Ranged = 0
    $ ring_magic_power.Equipment_Armor_Physical = 0
    $ ring_magic_power.Equipment_Armor_Magic = 0
    $ ring_magic_power.Equipment_Armor_Will = 0
    $ ring_magic_power.Equipment_Damage_Bonus_Melee_Max = 0
    $ ring_magic_power.Equipment_Damage_Bonus_Ranged_Max = 0
    $ ring_magic_power.Equipment_Damage_Bonus_Magic_Max = 25
    $ ring_magic_power.Equipment_Damage_Bonus_Will_Max = 0
    $ ring_magic_power.Equipment_Dodge = 0
    $ ring_magic_power.Equipment_Initiative = 0
    $ ring_magic_power.Equipment_Slot_Ring_Name = ring_magic_power
    $ ring_magic_power.Equipment_Slot_Ring_Name_Text = "Ring of Magic Power"
# Ring - Ring of Accuracy - ring_accuracy
    $ ring_accuracy = Character("ring_accuracy")
    $ ring_accuracy.Equipment_HealthPoints_Max = 0
    $ ring_accuracy.Equipment_AbilityPoints_Max = 0
    $ ring_accuracy.Equipment_WillPoints_Max = 0
    $ ring_accuracy.Equipment_Accuracy_Melee = 10
    $ ring_accuracy.Equipment_Accuracy_Ranged = 10
    $ ring_accuracy.Equipment_Armor_Physical = 0
    $ ring_accuracy.Equipment_Armor_Magic = 0
    $ ring_accuracy.Equipment_Armor_Will = 0
    $ ring_accuracy.Equipment_Damage_Bonus_Melee_Max = 0
    $ ring_accuracy.Equipment_Damage_Bonus_Ranged_Max = 0
    $ ring_accuracy.Equipment_Damage_Bonus_Magic_Max = 0
    $ ring_accuracy.Equipment_Damage_Bonus_Will_Max = 0
    $ ring_accuracy.Equipment_Dodge = 0
    $ ring_accuracy.Equipment_Initiative = 0
    $ ring_accuracy.Equipment_Slot_Ring_Name = ring_accuracy
    $ ring_accuracy.Equipment_Slot_Ring_Name_Text = "Ring of Accuracy"
