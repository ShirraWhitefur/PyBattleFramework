#  This file, like the other Enemy files, will contain most all of the things unique
# to the enemy, so it's all in one spot for easier reference.

#####################################################################
# Enemy Init Section
#####################################################################
init:
    $ Goblin = Character("Goblin")
    $ Goblin.name = "Goblin"
    $ Goblin.hp_c = 50
    $ Goblin.hp_m = 50
    $ Goblin.ap_c = 30
    $ Goblin.ap_m = 30
    $ Goblin.attack_list = "Attack_List_Goblin"
    $ Goblin.damage_melee_max = 5
    $ Goblin.damage_melee_min = 1
    $ Goblin.armor = 3
    $ Goblin.accuracy_melee = 7
    $ Goblin.dodge = 6
    $ Goblin.initiative_mod = 1
    $ Goblin.items_potions_hp = 0
    $ Goblin.battle_outcome_loss_hp = "test01_goblin_loss_hp"
    $ Goblin.battle_outcome_victory_hp = "test01_goblin_victory_hp"

#####################################################################
# Enemy AI Section
#####################################################################
#  Here is where we make the effective 'AI' of our enemy.  Make conditions for things like
# being wounded but also having potions to heal, or perhaps if he's badly hurt he'll use
# a harder hitting attack.  Another helpful bit will be to remove unusable AP eating
# abilities from your attack list.
label Attack_List_Goblin:
    if enemy.ap_c > 19:
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

