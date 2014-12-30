# Shirra's Ren'Py Battle Framework
# https://github.com/ShirraWhitefur/PyBattleFramework
# http://creativecommons.org/licenses/by-nc/3.0/

# Equipment Database - Necklace
#  You might want to make an index of equipment sometime, just so you can find
# things once this gets unwieldy.  
#  Also! Remember, -every enemy needs equipment-.  You can use the same
# equipment pieces across multiple enemies.  In theory, this will save you some
# time in the long run, since you don't have to redefine the same axe over and
# over again.

# The first set in here should be 'No Equipment' for the slot.
init -99:
# Necklace - No Necklace Worn - no_necklace
    $ no_necklace = Character("no_necklace")
    $ no_necklace.Equipment_HealthPoints_Max = 0
    $ no_necklace.Equipment_AbilityPoints_Max = 0
    $ no_necklace.Equipment_WillPoints_Max = 0
    $ no_necklace.Equipment_Accuracy_Melee = 0
    $ no_necklace.Equipment_Accuracy_Ranged = 0
    $ no_necklace.Equipment_Armor_Physical = 0
    $ no_necklace.Equipment_Armor_Magic = 0
    $ no_necklace.Equipment_Armor_Will = 0
    $ no_necklace.Equipment_Damage_Bonus_Melee_Max = 0
    $ no_necklace.Equipment_Damage_Bonus_Ranged_Max = 0
    $ no_necklace.Equipment_Damage_Bonus_Magic_Max = 0
    $ no_necklace.Equipment_Damage_Bonus_Will_Max = 0
    $ no_necklace.Equipment_Dodge = 0
    $ no_necklace.Equipment_Initiative = 0
    $ no_necklace.Equipment_Slot_Necklace_Name = no_necklace
    $ no_necklace.Equipment_Slot_Necklace_Name_Text = "No Necklace Worn"
# Necklace - Necklace of Health - necklace_health
    $ necklace_health = Character("necklace_health")
    $ necklace_health.Equipment_HealthPoints_Max = 40
    $ necklace_health.Equipment_AbilityPoints_Max = 0
    $ necklace_health.Equipment_WillPoints_Max = 0
    $ necklace_health.Equipment_Accuracy_Melee = 0
    $ necklace_health.Equipment_Accuracy_Ranged = 0
    $ necklace_health.Equipment_Armor_Physical = 0
    $ necklace_health.Equipment_Armor_Magic = 0
    $ necklace_health.Equipment_Armor_Will = 0
    $ necklace_health.Equipment_Damage_Bonus_Melee_Max = 0
    $ necklace_health.Equipment_Damage_Bonus_Ranged_Max = 0
    $ necklace_health.Equipment_Damage_Bonus_Magic_Max = 0
    $ necklace_health.Equipment_Damage_Bonus_Will_Max = 0
    $ necklace_health.Equipment_Dodge = 0
    $ necklace_health.Equipment_Initiative = 0
    $ necklace_health.Equipment_Slot_Necklace_Name = necklace_health
    $ necklace_health.Equipment_Slot_Necklace_Name_Text = "Necklace of Health"
# Necklace - Necklace of Frail Dodging - necklace_frail_dodge
    $ necklace_frail_dodge = Character("necklace_frail_dodge")
    $ necklace_frail_dodge.Equipment_HealthPoints_Max = -40
    $ necklace_frail_dodge.Equipment_AbilityPoints_Max = 0
    $ necklace_frail_dodge.Equipment_WillPoints_Max = 0
    $ necklace_frail_dodge.Equipment_Accuracy_Melee = 0
    $ necklace_frail_dodge.Equipment_Accuracy_Ranged = 0
    $ necklace_frail_dodge.Equipment_Armor_Physical = 0
    $ necklace_frail_dodge.Equipment_Armor_Magic = 0
    $ necklace_frail_dodge.Equipment_Armor_Will = 0
    $ necklace_frail_dodge.Equipment_Damage_Bonus_Melee_Max = 0
    $ necklace_frail_dodge.Equipment_Damage_Bonus_Ranged_Max = 0
    $ necklace_frail_dodge.Equipment_Damage_Bonus_Magic_Max = 0
    $ necklace_frail_dodge.Equipment_Damage_Bonus_Will_Max = 0
    $ necklace_frail_dodge.Equipment_Dodge = 12
    $ necklace_frail_dodge.Equipment_Initiative = 0
    $ necklace_frail_dodge.Equipment_Slot_Necklace_Name = necklace_frail_dodge
    $ necklace_frail_dodge.Equipment_Slot_Necklace_Name_Text = "Necklace of Frail Dodging"
