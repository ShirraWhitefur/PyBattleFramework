# Shirra's Ren'Py Battle Framework
# https://github.com/ShirraWhitefur/PyBattleFramework
# http://creativecommons.org/licenses/by-nc/3.0/

#  This file, like the other Enemy files, will contain most all of the things
# unique to the enemy, so it's all in one spot for easier reference.

#####################################################################
# Enemy Init Section
#####################################################################
init -25:
    $ Status_Blob = Character("Status Blob")
    $ Status_Blob.name = "The Wobbling Status Blob"
    $ Status_Blob.Attack_List = "Attack_List_Status_Blob"
    $ Status_Blob.Battle_Outcomes_Loss_HP = "test03_status_blob_loss_hp"
    $ Status_Blob.Battle_Outcomes_Victory_HP = "test03_status_blob_victory_hp"
    $ Status_Blob.Stats_Strength = 250
    $ Status_Blob.Stats_Precision = 250
    $ Status_Blob.Stats_Insight = 250
    $ Status_Blob.Stats_Deceit = 250
    $ Status_Blob.Stats_Vigor = 250
    $ Status_Blob.Stats_Spirit = 250
    $ Status_Blob.Stats_Resolve = 250
    $ Status_Blob.Equipment_Slot_Weapon_Name = no_weapon
    $ Status_Blob.Equipment_Slot_UpperBodyArmor_Name = no_upper_armor
    $ Status_Blob.Equipment_Slot_LowerBodyArmor_Name = lower_chain_armor
    $ Status_Blob.Equipment_Slot_Necklace_Name = no_necklace
    $ Status_Blob.Equipment_Slot_Ring_Name = ring_status_blob
    $ Status_Blob.Equipment_Consumables_Potions_HP_Restore = 0
    $ Status_Blob.Equipment_Consumables_Potions_AP_Restore = 0
    $ Status_Blob.Equipment_Consumables_Potions_WP_Restore = 0
    $ Status_Blob.Equipment_Currency = 160

#####################################################################
# Enemy AI Section
#####################################################################
#  Here is where we make the effective 'AI' of our enemy.  Make conditions for
# things like being wounded but also having potions to heal, or perhaps if he's
# badly hurt he'll use a harder hitting attack.  Another helpful bit will be to
# remove unusable AP eating abilities from your attack list.  Especially as this
# is the only spot where it'll be checking to see if your enemy has enough AP to
# use the ability!
label Attack_List_Status_Blob:
    if enemy.X_AbilityPoints_Current_X > 4:
        $rand_choice = WeightedChoice([("battle_Status_Blob_Attack_Main_TypeCheck", 0.5),
                                        ("battle_Status_Blob_Ability__StatusALL", 0.15),
                                        ("battle_Enemy_Ability__Poison", 0.10),
                                        ("battle_Enemy_Ability__Slow", 0.10),
                                        ("battle_Enemy_Ability__Weaken", 0.10),
                                        ("battle_Enemy_Ability__Clumsy", 0.10),
                                        ("battle_Enemy_Ability__Paralyse", 0.7),
                                        ("battle_Enemy_Ability__Charm", 0.7),
                                        ("battle_Enemy_Ability__Sleep", 0.7),
                                        ("battle_Enemy_Ability__Disarm", 0.7),
                                        ("battle_Enemy_Ability__UpperBodyArmorRemove", 0.7),
                                        ("battle_Enemy_Dodge", 0.03),
                                        ("battle_Enemy_Block", 0.03),
                                        ("battle_Enemy_Wait", 0.04)])
        jump expression rand_choice
    $rand_choice = WeightedChoice([("battle_Status_Blob_Attack_Main_TypeCheck", 0.75),
                                        ("battle_Enemy_Dodge", 0.05),
                                        ("battle_Enemy_Block", 0.15),
                                        ("battle_Enemy_Wait", 0.05)])
    jump expression rand_choice

#####################################################################
# Enemy Action Section
#####################################################################


#  It's a blob.  It melee's. 
# Really, stick to melee for them.
label battle_Status_Blob_Attack_Main_TypeCheck:
    "[enemy.name!t] schlorps and slaps at you with tendrils of ick."
    $enemy_roll_attack = renpy.random.randint(1,100)
    if enemy.Equipment_Slot_Weapon_Accuracy_Type == "Melee":
        if (enemy_roll_attack+enemy.X_Weapon_Accuracy_Melee_X)-player.X_Dodge_X > 50:
            "You were hit! ([enemy_roll_attack] + [enemy.X_Weapon_Accuracy_Melee_X] - [player.X_Dodge_X] vs 50)"
            call battle_Status_Blob_Attack_Main_Success
            return
        "You dodge the attack! ([enemy_roll_attack] + [enemy.X_Weapon_Accuracy_Melee_X] - [player.X_Dodge_X] vs 50)"
        return
    if enemy.Equipment_Slot_Weapon_Accuracy_Type == "Ranged":
        if (enemy_roll_attack+enemy.X_Weapon_Accuracy_Ranged_X)-player.X_Dodge_X > 50:
            "You were hit! ([enemy_roll_attack] + [enemy.X_Weapon_Accuracy_Melee_X] - [player.X_Dodge_X] vs 50)"
            call battle_Status_Blob_Attack_Main_Success
            return
        "You dodge the attack! ([enemy_roll_attack] + [enemy.X_Weapon_Accuracy_Melee_X] - [player.X_Dodge_X] vs 50)"
        return
    nar "You broke my system with a wierd accuracy type.  Stop that."
    jump end
        
label battle_Status_Blob_Attack_Main_Success:
    if enemy.Equipment_Slot_Weapon_Damage_Type == "Melee":
        $enemy_roll_damage = renpy.random.randint(enemy.X_Weapon_Damage_Melee_Min_X,enemy.X_Weapon_Damage_Melee_Max_X)
        $enemy_roll_damage_final = (enemy_roll_damage-player.X_Armor_Physical_X)
        if enemy_roll_damage_final < 1:
            "[enemy.name!t] hits, but does no damage, just leaving an icky trail on your armor.  ([enemy_roll_damage] - [player.X_Armor_Physical_X] = [enemy_roll_damage_final])"
            return
        call battle_call_Player_HP_Loss(enemy_roll_damage_final)
        "[enemy.name!t] smashes you around with an icky pseudopod, dealing [enemy_roll_damage_final] damage.  [playername!t]'s HP at [player.X_HealthPoints_Current_X].  ([enemy_roll_damage] - [player.X_Armor_Physical_X])"
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

label battle_Status_Blob_Ability__StatusALL:
    "[enemy.name!t] attempts to bowl you over and flow over you!"
    call battle_call_Enemy_AP_Loss(5)
    $enemy_roll_attack = renpy.random.randint(1,100)
    if enemy_roll_attack-player.X_Dodge_X < 50:
        "[playername!t] dodges the attack!  So incredibly lucky!  ([enemy_roll_attack] - [player.X_Dodge_X] vs 50)"
        return
    $ player.Status_Poison_EffectActive = 1
    $ player.Status_Poison_Duration = renpy.random.randint(4,6)
    $ player.Status_Poison_Strength = renpy.random.randint(2,5)
    "[enemy.name!t] poisons you for [player.Status_Poison_Duration] rounds, at [player.Status_Poison_Strength] strength."
    $ player.Status_Slow_EffectActive = 1
    $ player.Status_Slow_Duration = renpy.random.randint(4,6)
    $ player.Status_Slow_Strength = renpy.random.randint(2,5)
    "[enemy.name!t] slows you for [player.Status_Slow_Duration] rounds, at [player.Status_Slow_Strength] strength."
    $ player.Status_Weaken_EffectActive = 1
    $ player.Status_Weaken_Duration = renpy.random.randint(4,6)
    $ player.Status_Weaken_Strength = renpy.random.randint(2,5)
    "[enemy.name!t] weakens you for [player.Status_Weaken_Duration] rounds, at [player.Status_Weaken_Strength] strength."
    $ player.Status_Clumsy_EffectActive = 1
    $ player.Status_Clumsy_Duration = renpy.random.randint(4,6)
    $ player.Status_Clumsy_Strength = renpy.random.randint(2,5)
    "[enemy.name!t] makes you Clumsy for [player.Status_Clumsy_Duration] rounds, at [player.Status_Clumsy_Strength] strength."
    $ player.Status_Paralyse_EffectActive = 1
    $ player.Status_Paralyse_Duration = renpy.random.randint(2,4)
    "[enemy.name!t] paralyses you for [player.Status_Paralyse_Duration] rounds."
    $ player.Status_Charm_EffectActive = 1
    $ player.Status_Charm_Duration = renpy.random.randint(2,4)
    "[enemy.name!t] charms you for [player.Status_Charm_Duration] rounds."
    $ player.Status_Sleep_EffectActive = 1
    $ player.Status_Sleep_Duration = renpy.random.randint(2,4)
    "[enemy.name!t] sleeps you for [player.Status_Sleep_Duration] rounds."
    if player.Status_EquipLoss_Weapon_EffectActive == 0:
        call battle_call_Enemy_Status_EquipLoss_Weapon_Remove
    $ player.Status_EquipLoss_Weapon_EffectActive = 1
    $ player.Status_EquipLoss_Weapon_Duration = renpy.random.randint(2,4)
    "[enemy.name!t] disarms you for [player.Status_EquipLoss_Weapon_Duration] rounds.  ([enemy_roll_attack] - [player.X_Dodge_X] vs 50)"
    if player.Status_EquipLoss_UpperBodyArmor_EffectActive == 0:
        call battle_call_Enemy_Status_EquipLoss_UpperBodyArmor_Remove
    $ player.Status_EquipLoss_UpperBodyArmor_EffectActive = 1
    $ player.Status_EquipLoss_UpperBodyArmor_Duration = renpy.random.randint(2,4)
    "[enemy.name!t] strips you of your upper body armor for [player.Status_EquipLoss_UpperBodyArmor_Duration] rounds.  ([enemy_roll_attack] - [player.X_Dodge_X] vs 50)"
    "Good grief.  That was just bloody mean, wasn't it?"
    return
