#  This file, like the other Enemy files, will contain most all of the things unique
# to the enemy, so it's all in one spot for easier reference.

#####################################################################
# Enemy Init Section
#####################################################################
init:
    $ Orc_Hero = Character("Orc Hero")
    $ Orc_Hero.name = "Orc Hero"
    $ Orc_Hero.hp_c = 100
    $ Orc_Hero.hp_m = 100
    $ Orc_Hero.ap_c = 60
    $ Orc_Hero.ap_m = 60
    $ Orc_Hero.attack_list = "Attack_List_Orc_Hero"
    $ Orc_Hero.damage_melee_max = 10
    $ Orc_Hero.damage_melee_min = 2
    $ Orc_Hero.armor = 3
    $ Orc_Hero.accuracy_melee = 7
    $ Orc_Hero.dodge = 6
    $ Orc_Hero.initiative_mod = 3
    $ Orc_Hero.items_potions_hp = 1
    $ Orc_Hero.battle_outcome_loss_hp = "test02_orc_loss_hp"
    $ Orc_Hero.battle_outcome_victory_hp = "test02_orc_victory_hp"

#####################################################################
# Enemy AI Section
#####################################################################
#  Here is where we make the effective 'AI' of our enemy.  Make conditions for things like
# being wounded but also having potions to heal, or perhaps if he's badly hurt he'll use
# a harder hitting attack.  Another helpful bit will be to remove unusable AP eating
# abilities from your attack list.
label Attack_List_Orc_Hero:
    if enemy.items_potions_hp > 0:
        if enemy.hp_c < enemy.hp_m-30:
            $rand_choice = WeightedChoice([("battle_Orc_Hero_Attack_Melee", 0.20),
                                           ("battle_Orc_Hero_Item__Potion", 0.60),
                                           ("battle_Enemy_Wait", 0.20)])
            jump expression rand_choice
    if enemy.ap_c > 19:
        $rand_choice = WeightedChoice([("battle_Orc_Hero_Attack_Melee", 0.40),
                                       ("battle_Enemy_Ability__Fire", 0.30),
                                       ("battle_Enemy_Wait", 0.30)])
        jump expression rand_choice
    $rand_choice = WeightedChoice([("battle_Orc_Hero_Attack_Melee", 0.70),
                                   ("battle_Enemy_Wait", 0.30)])
    jump expression rand_choice
        
#####################################################################
# Enemy Action Section
#####################################################################

label battle_Orc_Hero_Attack_Melee:
    "[enemy.name!t] comes screaming at you with his axe!"
    $ enemy.roll_attack = renpy.random.randint(1,100)
    if enemy.roll_attack+enemy.accuracy_melee < 50:
        "You dodge the attack! ([enemy.roll_attack] + [enemy.accuracy_melee] vs 50)"
        return
    else:
        "You were hit! ([enemy.roll_attack] + [enemy.accuracy_melee] vs 50)"
        jump battle_Orc_Hero_Attack_Melee_Success

label battle_Orc_Hero_Attack_Melee_Success:
    $ enemy.roll_damage = renpy.random.randint(enemy.damage_melee_min,enemy.damage_melee_max)
    $ enemy.roll_damage_final = (enemy.roll_damage-player.armor)
    if enemy.roll_damage_final < 1:
        "[enemy.name!t] hits, but does no damage, taking a moment to glare at your infuriating armor.  ([enemy.roll_damage] - [player.armor] = [enemy.roll_damage_final])"
        return
    else:
        call battle_call_Player_HP_Loss(enemy.roll_damage_final)
        "[enemy.name!t] lands a solid blow, dealing [enemy.roll_damage_final] damage, the axe biting into you through your armor.  [playername!t]'s HP at [player.hp_c].  ([enemy.roll_damage] - [player.armor])"
        return

label battle_Orc_Hero_Item__Potion:
    "[enemy.name!t] drinks a potion!"
    $ enemy.roll_damage_final = renpy.random.randint(20,40)
    call battle_call_Enemy_HP_Gain(enemy.roll_damage_final)
    $ enemy.items_potions_hp -= 1
    "[enemy.name!t] heals [enemy.roll_damage_final] damage, and has [enemy.items_potions_hp] left."
    return
