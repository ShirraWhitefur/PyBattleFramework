# Shirra's Ren'Py Battle Framework
# https://github.com/ShirraWhitefur/PyBattleFramework
# http://creativecommons.org/licenses/by-nc/3.0/

#  This file, like the other Enemy files, will contain most all of the things
# unique to the enemy, so it's all in one spot for easier reference.

#####################################################################
# Enemy Init Section
#####################################################################
init -25:
    $ Orc_Hero = Character("Orc Hero")
    $ Orc_Hero.name = "Orc Hero"
    $ Orc_Hero.Attack_List = "Attack_List_Orc_Hero"
    $ Orc_Hero.Battle_Outcomes_Loss_HP = "test02_orc_loss_hp"
    $ Orc_Hero.Battle_Outcomes_Victory_HP = "test02_orc_victory_hp"
    $ Orc_Hero.Stats_PlaceholderStrength = 0
    $ Orc_Hero.Attribute_HealthPoints = 120
    $ Orc_Hero.Attribute_AbilityPoints = 65
    $ Orc_Hero.Attribute_WillPoints = 100
    $ Orc_Hero.Attribute_Accuracy_Melee = 7
    $ Orc_Hero.Attribute_Accuracy_Ranged = 6
    $ Orc_Hero.Attribute_Armor_Physical = 3
    $ Orc_Hero.Attribute_Armor_Magic = 2
    $ Orc_Hero.Attribute_Armor_Will = 1
    $ Orc_Hero.Attribute_Damage_Bonus_Melee = 5
    $ Orc_Hero.Attribute_Damage_Bonus_Ranged = 1
    $ Orc_Hero.Attribute_Damage_Bonus_Magic = 1
    $ Orc_Hero.Attribute_Damage_Bonus_Will = 1
    $ Orc_Hero.Attribute_Dodge = 6
    $ Orc_Hero.Attribute_Initiative = 3
    $ Orc_Hero.Equipment_Slot_Weapon_Name = axe_orcish
    $ Orc_Hero.Equipment_Slot_UpperBodyArmor_Name = no_upper_armor
    $ Orc_Hero.Equipment_Slot_LowerBodyArmor_Name = lower_chain_armor
    $ Orc_Hero.Equipment_Slot_Necklace_Name = no_necklace
    $ Orc_Hero.Equipment_Slot_Ring_Name = no_ring
    $ Orc_Hero.Equipment_Consumables_Potions_HP_Restore = 1
    $ Orc_Hero.Equipment_Consumables_Potions_AP_Restore = 0
    $ Orc_Hero.Equipment_Consumables_Potions_WP_Restore = 0
    $ Orc_Hero.Equipment_Currency = 91

#####################################################################
# Enemy AI Section
#####################################################################
#  Here is where we make the effective 'AI' of our enemy.  Make conditions for
# things like being wounded but also having potions to heal, or perhaps if he's
# badly hurt he'll use a harder hitting attack.  Another helpful bit will be to
# remove unusable AP eating abilities from your attack list.  Especially as this
# is the only spot where it'll be checking to see if your enemy has enough AP to
# use the ability!
label Attack_List_Orc_Hero:
    if enemy.Equipment_Consumables_Potions_HP_Restore > 0:
        if enemy.X_HealthPoints_Current_X < enemy.X_HealthPoints_Max_X-30:
            $rand_choice = WeightedChoice([("battle_Orc_Hero_Attack_Main_TypeCheck", 0.15),
                                           ("battle_Orc_Hero_Item__Potion", 0.50),
                                           ("battle_Enemy_Dodge", 0.10),
                                           ("battle_Enemy_Block", 0.10),
                                           ("battle_Enemy_Wait", 0.15)])
            jump expression rand_choice
    if enemy.X_AbilityPoints_Current_X > 19:
        $rand_choice = WeightedChoice([("battle_Orc_Hero_Attack_Main_TypeCheck", 0.40),
                                       ("battle_Enemy_Ability__Fire", 0.30),
                                       ("battle_Enemy_Dodge", 0.10),
                                       ("battle_Enemy_Block", 0.10),
                                       ("battle_Enemy_Wait", 0.10)])
        jump expression rand_choice
    $rand_choice = WeightedChoice([("battle_Orc_Hero_Attack_Main_TypeCheck", 0.70),
                                   ("battle_Enemy_Dodge", 0.10),
                                   ("battle_Enemy_Block", 0.10),
                                   ("battle_Enemy_Wait", 0.10)])
    jump expression rand_choice
        
#####################################################################
# Enemy Action Section
#####################################################################

label battle_Orc_Hero_Item__Potion:
    "[enemy.name!t] drinks a potion!"
    $enemy_roll_damage_final = renpy.random.randint(20,40)
    call battle_call_Enemy_HP_Gain(enemy_roll_damage_final)
    $ enemy.Equipment_Consumables_Potions_HP_Restore -= 1
    "[enemy.name!t] heals [enemy_roll_damage_final] damage, and has [enemy.Equipment_Consumables_Potions_HP_Restore] left."
    return

#  Note, he's gonna look strange going screaming at people with a bow or wand.
# Really, stick to melee for him.
label battle_Orc_Hero_Attack_Main_TypeCheck:
    "[enemy.name!t] comes screaming at you with his [enemy.Equipment_Slot_Weapon_Name_Text]"
    $enemy_roll_attack = renpy.random.randint(1,100)
    if enemy.Equipment_Slot_Weapon_Accuracy_Type == "Melee":
        if (enemy_roll_attack+enemy.X_Weapon_Accuracy_Melee_X)-player.X_Dodge_X > 50:
            "You were hit! ([enemy_roll_attack] + [enemy.X_Weapon_Accuracy_Melee_X] - [player.X_Dodge_X] vs 50)"
            call battle_Orc_Hero_Attack_Main_Success
            return
        "You dodge the attack! ([enemy_roll_attack] + [enemy.X_Weapon_Accuracy_Melee_X] - [player.X_Dodge_X] vs 50)"
        return
    if enemy.Equipment_Slot_Weapon_Accuracy_Type == "Ranged":
        if (enemy_roll_attack+enemy.X_Weapon_Accuracy_Ranged_X)-player.X_Dodge_X > 50:
            "You were hit! ([enemy_roll_attack] + [enemy.X_Weapon_Accuracy_Melee_X] - [player.X_Dodge_X] vs 50)"
            call battle_Orc_Hero_Attack_Main_Success
            return
        "You dodge the attack! ([enemy_roll_attack] + [enemy.X_Weapon_Accuracy_Melee_X] - [player.X_Dodge_X] vs 50)"
        return
    nar "You broke my system with a wierd accuracy type.  Stop that."
    jump end
        
label battle_Orc_Hero_Attack_Main_Success:
    if enemy.Equipment_Slot_Weapon_Damage_Type == "Melee":
        $enemy_roll_damage = renpy.random.randint(enemy.X_Weapon_Damage_Melee_Min_X,enemy.X_Weapon_Damage_Melee_Max_X)
        $enemy_roll_damage_final = (enemy_roll_damage-player.X_Armor_Physical_X)
        if enemy_roll_damage_final < 1:
            "[enemy.name!t] hits, but does no damage, taking a moment to glare at your infuriating armor.  ([enemy_roll_damage] - [player.X_Armor_Physical_X] = [enemy_roll_damage_final])"
            return
        call battle_call_Player_HP_Loss(enemy_roll_damage_final)
        "[enemy.name!t] lands a solid blow, dealing [enemy_roll_damage_final] damage, the [enemy.Equipment_Slot_Weapon_Name_Text] biting into you through your armor.  [playername!t]'s HP at [player.X_HealthPoints_Current_X].  ([enemy_roll_damage] - [player.X_Armor_Physical_X])"
        return
    if enemy.Equipment_Slot_Weapon_Damage_Type == "Ranged":
        $enemy_roll_damage = renpy.random.randint(enemy.X_Weapon_Damage_Ranged_Min_X,enemy.X_Weapon_Damage_Ranged_Max_X)
        $enemy_roll_damage_final = (enemy_roll_damage-player.X_Armor_Physical_X)
        if enemy_roll_damage_final < 1:
            "[enemy.name!t] hits, but does no damage, taking a moment to glare at your infuriating armor.  ([enemy_roll_damage] - [player.X_Armor_Physical_X] = [enemy_roll_damage_final])"
            return
        call battle_call_Player_HP_Loss(enemy_roll_damage_final)
        "[enemy.name!t] lands a solid blow, dealing [enemy_roll_damage_final] damage, the [enemy.Equipment_Slot_Weapon_Name_Text] biting into you through your armor.  [playername!t]'s HP at [player.X_HealthPoints_Current_X].  ([enemy_roll_damage] - [player.X_Armor_Physical_X])"
        return
    if enemy.Equipment_Slot_Weapon_Damage_Type == "Magic":
        $enemy_roll_damage = renpy.random.randint(enemy.X_Weapon_Damage_Magic_Min_X,enemy.X_Weapon_Damage_Magic_Max_X)
        $enemy_roll_damage_final = (enemy_roll_damage-player.X_Armor_Magic_X)
        if enemy_roll_damage_final < 1:
            "[enemy.name!t] hits, but does no damage, taking a moment to glare at your infuriating armor.  ([enemy_roll_damage] - [player.X_Armor_Magic_X] = [enemy_roll_damage_final])"
            return
        call battle_call_Player_HP_Loss(enemy_roll_damage_final)
        "[enemy.name!t] lands a solid blow, dealing [enemy_roll_damage_final] damage, the [enemy.Equipment_Slot_Weapon_Name_Text] biting into you through your armor.  [playername!t]'s HP at [player.X_HealthPoints_Current_X].  ([enemy_roll_damage] - [player.X_Armor_Magic_X])"
        return
    if enemy.Equipment_Slot_Weapon_Damage_Type == "Will":
        $enemy_roll_damage = renpy.random.randint(enemy.X_Weapon_Damage_Will_Min_X,enemy.X_Weapon_Damage_Will_Max_X)
        $enemy_roll_damage_final = (enemy_roll_damage-player.X_Armor_Will_X)
        if enemy_roll_damage_final < 1:
            "[enemy.name!t] hits, but does no damage, taking a moment to glare at your infuriating armor.  ([enemy_roll_damage] - [player.X_Armor_Will_X] = [enemy_roll_damage_final])"
            return
        call battle_call_Player_HP_Loss(enemy_roll_damage_final)
        "[enemy.name!t] lands a solid blow, dealing [enemy_roll_damage_final] damage, the [enemy.Equipment_Slot_Weapon_Name_Text] biting into you through your armor.  [playername!t]'s HP at [player.X_HealthPoints_Current_X].  ([enemy_roll_damage] - [player.X_Armor_Will_X])"
        return
    nar "You broke my system with a wierd damage type.  Stop that."
    jump end
