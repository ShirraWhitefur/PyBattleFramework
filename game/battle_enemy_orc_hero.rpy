#  This file, like the other Enemy files, will contain most all of the things unique
# to the enemy, so it's all in one spot for easier reference.

#####################################################################
# Enemy Init Section
#####################################################################
init:
    $ Orc_Hero = Character("Orc Hero")
    $ Orc_Hero.name = "Orc Hero"
    $ Orc_Hero.Attack_List = "Attack_List_Orc_Hero"
    $ Orc_Hero.Battle_Outcomes_Loss_HP = "test02_orc_loss_hp"
    $ Orc_Hero.Battle_Outcomes_Victory_HP = "test02_orc_victory_hp"
    $ Orc_Hero.Stats_PlaceholderStrength = 0
    $ Orc_Hero.Attribute_HealthPoints_Max = 120
    $ Orc_Hero.Attribute_AbilityPoints_Max = 65
    $ Orc_Hero.Attribute_WillPoints_Max = 100
    $ Orc_Hero.Attribute_Accuracy_Melee = 7
    $ Orc_Hero.Attribute_Accuracy_Ranged = 6
    $ Orc_Hero.Attribute_Armor_Physical = 3
    $ Orc_Hero.Attribute_Armor_Magic = 2
    $ Orc_Hero.Attribute_Armor_Will = 1
    $ Orc_Hero.Attribute_Damage_Melee_Max = 5
    $ Orc_Hero.Attribute_Damage_Ranged_Max = 1
    $ Orc_Hero.Attribute_Damage_Magic_Max = 1
    $ Orc_Hero.Attribute_Damage_Will_Max = 1
    $ Orc_Hero.Attribute_Dodge = 6
    $ Orc_Hero.Attribute_Initiative = 3
    $ Orc_Hero.Equipment_HealthPoints_Max = 0
    $ Orc_Hero.Equipment_AbilityPoints_Max = 0
    $ Orc_Hero.Equipment_WillPoints_Max = 0
    $ Orc_Hero.Equipment_Accuracy_Melee = 0
    $ Orc_Hero.Equipment_Accuracy_Ranged = 0
    $ Orc_Hero.Equipment_Armor_Physical = 0
    $ Orc_Hero.Equipment_Armor_Magic = 0
    $ Orc_Hero.Equipment_Armor_Will = 0
    $ Orc_Hero.Equipment_Damage_Melee_Max = 10
    $ Orc_Hero.Equipment_Damage_Melee_Min = 2
    $ Orc_Hero.Equipment_Damage_Ranged_Max = 5
    $ Orc_Hero.Equipment_Damage_Ranged_Min = 1
    $ Orc_Hero.Equipment_Damage_Magic_Max = 2
    $ Orc_Hero.Equipment_Damage_Magic_Min = 1
    $ Orc_Hero.Equipment_Damage_Will_Max = 2
    $ Orc_Hero.Equipment_Damage_Will_Min = 1
    $ Orc_Hero.Equipment_Dodge = 0
    $ Orc_Hero.Equipment_Initiative = 0
    $ Orc_Hero.Equipment_Consumables_Potions_HP_Restore = 1
    $ Orc_Hero.Equipment_Consumables_Potions_AP_Restore = 0
    $ Orc_Hero.Equipment_Consumables_Potions_WP_Restore = 0

#####################################################################
# Enemy AI Section
#####################################################################
#  Here is where we make the effective 'AI' of our enemy.  Make conditions for things like
# being wounded but also having potions to heal, or perhaps if he's badly hurt he'll use
# a harder hitting attack.  Another helpful bit will be to remove unusable AP eating
# abilities from your attack list.
label Attack_List_Orc_Hero:
    if enemy.Equipment_Consumables_Potions_HP_Restore > 0:
        if enemy.X_HealthPoints_Current_X < enemy.X_HealthPoints_Max_X-30:
            $rand_choice = WeightedChoice([("battle_Orc_Hero_Attack_Melee", 0.20),
                                           ("battle_Orc_Hero_Item__Potion", 0.60),
                                           ("battle_Enemy_Wait", 0.20)])
            jump expression rand_choice
    if enemy.X_AbilityPoints_Current_X > 19:
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
    $enemy_roll_attack = renpy.random.randint(1,100)
    if (enemy_roll_attack+enemy.X_Accuracy_Melee_X)-player.X_Dodge_X < 50:
        "You dodge the attack! ([enemy_roll_attack] + [enemy.X_Accuracy_Melee_X] - [player.X_Dodge_X] vs 50)"
        return
    else:
        "You were hit! ([enemy_roll_attack] + [enemy.X_Accuracy_Melee_X] - [player.X_Dodge_X] vs 50)"
        jump battle_Orc_Hero_Attack_Melee_Success

label battle_Orc_Hero_Attack_Melee_Success:
    $enemy_roll_damage = renpy.random.randint(enemy.X_Damage_Melee_Min_X,enemy.X_Damage_Melee_Max_X)
    $enemy_roll_damage_final = (enemy_roll_damage-player.X_Armor_Physical_X)
    if enemy_roll_damage_final < 1:
        "[enemy.name!t] hits, but does no damage, taking a moment to glare at your infuriating armor.  ([enemy_roll_damage] - [player.X_Armor_Physical_X] = [enemy_roll_damage_final])"
        return
    else:
        call battle_call_Player_HP_Loss(enemy_roll_damage_final)
        "[enemy.name!t] lands a solid blow, dealing [enemy_roll_damage_final] damage, the axe biting into you through your armor.  [playername!t]'s HP at [player.X_HealthPoints_Current_X].  ([enemy_roll_damage] - [player.X_Armor_Magic_X])"
        return

label battle_Orc_Hero_Item__Potion:
    "[enemy.name!t] drinks a potion!"
    $ enemy.roll_damage_final = renpy.random.randint(20,40)
    call battle_call_Enemy_HP_Gain(enemy.roll_damage_final)
    $ enemy.Equipment_Consumables_Potions_HP_Restore -= 1
    "[enemy.name!t] heals [enemy.roll_damage_final] damage, and has [enemy.Equipment_Consumables_Potions_HP_Restore] left."
    return
