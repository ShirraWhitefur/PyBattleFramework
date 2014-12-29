#  This file, like the other Enemy files, will contain most all of the things unique
# to the enemy, so it's all in one spot for easier reference.

#####################################################################
# Enemy Init Section
#####################################################################
init:
    $ Goblin = Character("Goblin")
    $ Goblin.name = "Goblin"
    $ Goblin.X_HealthPoints_Current_X = 50
    $ Goblin.X_HealthPoints_Max_X = 50
    $ Goblin.X_AbilityPoints_Current_X = 30
    $ Goblin.X_AbilityPoints_Max_X = 30
    $ Goblin.Attack_List = "Attack_List_Goblin"
    $ Goblin.X_Damage_Melee_Max_X = 5
    $ Goblin.X_Damage_Melee_Min_X = 1
    $ Goblin.X_Armor_Physical_X = 3
    $ Goblin.X_Accuracy_Melee_X = 7
    $ Goblin.X_Dodge_X = 6
    $ Goblin.X_Initiative_X = 1
    $ Goblin.Equipment_Consumables_Potions_HP_Restore = 0
    $ Goblin.Battle_Outcomes_Loss_HP = "test01_goblin_loss_hp"
    $ Goblin.Battle_Outcomes_Victory_HP = "test01_goblin_victory_hp"

#####################################################################
# Enemy AI Section
#####################################################################
#  Here is where we make the effective 'AI' of our enemy.  Make conditions for things like
# being wounded but also having potions to heal, or perhaps if he's badly hurt he'll use
# a harder hitting attack.  Another helpful bit will be to remove unusable AP eating
# abilities from your attack list.
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

