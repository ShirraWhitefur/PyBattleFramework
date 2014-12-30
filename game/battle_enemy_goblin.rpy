#  This file, like the other Enemy files, will contain most all of the things
# unique to the enemy, so it's all in one spot for easier reference.

#####################################################################
# Enemy Init Section
#####################################################################
init -25:
    $ Goblin = Character("Goblin")
    $ Goblin.name = "Goblin"
    $ Goblin.Attack_List = "Attack_List_Goblin"
    $ Goblin.Battle_Outcomes_Loss_HP = "test01_goblin_loss_hp"
    $ Goblin.Battle_Outcomes_Victory_HP = "test01_goblin_victory_hp"
    $ Goblin.Stats_PlaceholderStrength = 0
    $ Goblin.Attribute_HealthPoints_Max = 50
    $ Goblin.Attribute_AbilityPoints_Max = 30
    $ Goblin.Attribute_WillPoints_Max = 100
    $ Goblin.Attribute_Accuracy_Melee = 7
    $ Goblin.Attribute_Accuracy_Ranged = 6
    $ Goblin.Attribute_Armor_Physical = 3
    $ Goblin.Attribute_Armor_Magic = 2
    $ Goblin.Attribute_Armor_Will = 1
    $ Goblin.Attribute_Damage_Bonus_Melee_Max = 3
    $ Goblin.Attribute_Damage_Bonus_Ranged_Max = 1
    $ Goblin.Attribute_Damage_Bonus_Magic_Max = 1
    $ Goblin.Attribute_Damage_Bonus_Will_Max = 1
    $ Goblin.Attribute_Dodge = 6
    $ Goblin.Attribute_Initiative = 1
    $ Goblin.Equipment_Slot_Weapon_Name = no_weapon
    $ Goblin.Equipment_Slot_UpperBodyArmor_Name = no_upper_armor
    $ Goblin.Equipment_Slot_LowerBodyArmor_Name = no_lower_armor
    $ Goblin.Equipment_Slot_Necklace_Name = no_necklace
    $ Goblin.Equipment_Slot_Ring_Name = no_ring
    $ Goblin.Equipment_Consumables_Potions_HP_Restore = 0
    $ Goblin.Equipment_Consumables_Potions_AP_Restore = 0
    $ Goblin.Equipment_Consumables_Potions_WP_Restore = 0

#####################################################################
# Enemy AI Section
#####################################################################
#  Here is where we make the effective 'AI' of our enemy.  Make conditions for
# things like being wounded but also having potions to heal, or perhaps if he's
# badly hurt he'll use a harder hitting attack.  Another helpful bit will be to
# remove unusable AP eating abilities from your attack list.  Especially as this
# is the only spot where it'll be checking to see if your enemy has enough AP to
# use the ability!
label Attack_List_Goblin:
    if enemy.X_AbilityPoints_Current_X > 19:
        $rand_choice = WeightedChoice([("battle_Enemy_Attack_Melee", 0.40),
                                       ("battle_Enemy_Ability__Fire", 0.30),
                                       ("battle_Enemy_Wait", 0.30)])
        jump expression rand_choice
    $rand_choice = WeightedChoice([("battle_Enemy_Attack_Melee", 0.70),
                                   ("battle_Enemy_Wait", 0.30)])
    jump expression rand_choice
        
#####################################################################
# Enemy Action Section
#####################################################################

