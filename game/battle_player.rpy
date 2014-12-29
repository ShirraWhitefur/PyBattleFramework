#  This file will contain initialization setup for the player, as well as all
# of the menus for selecting what action players will take, and then the
# actions, abilities, and items themselves, so as to keep things tidy.
#####################################################################
# Player Init Section
#####################################################################
init:
    $ player = DynamicCharacter("playername", color=(192, 64, 64, 255))
    $ playername = "SomethingFailed"
    $ player.Battle_Selected_Action = "battle_Player_Wait"
# Base Stats - From these, when they're actually added and used, we'll get our base attributes.
    $ player.Stats_PlaceholderStrength = 0
# Base attributes, to be derived from Stats.. when we add the stats in.
    $ player.Attribute_HealthPoints_Max = 295
    $ player.Attribute_AbilityPoints_Max = 292
    $ player.Attribute_WillPoints_Max = 290
    $ player.Attribute_Accuracy_Melee = 5
    $ player.Attribute_Accuracy_Ranged = 5
    $ player.Attribute_Armor_Physical = 1
    $ player.Attribute_Armor_Magic = 1
    $ player.Attribute_Armor_Will = 1
    $ player.Attribute_Damage_Melee_Max = 10
    $ player.Attribute_Damage_Ranged_Max = 10
    $ player.Attribute_Damage_Magic_Max = 10
    $ player.Attribute_Damage_Will_Max = 10
    $ player.Attribute_Dodge = 5
    $ player.Attribute_Initiative = 5
# Equipment.. which may be derived.. if we add in equipment properly.
    $ player.Equipment_HealthPoints_Max = 5
    $ player.Equipment_AbilityPoints_Max = 8
    $ player.Equipment_WillPoints_Max = 10
    $ player.Equipment_Accuracy_Melee = 4
    $ player.Equipment_Accuracy_Ranged = 4
    $ player.Equipment_Armor_Physical = 2
    $ player.Equipment_Armor_Magic = 2
    $ player.Equipment_Armor_Will = 2
    $ player.Equipment_Damage_Melee_Max = 10
    $ player.Equipment_Damage_Melee_Min = 1
    $ player.Equipment_Damage_Ranged_Max = 10
    $ player.Equipment_Damage_Ranged_Min = 1
    $ player.Equipment_Damage_Magic_Max = 10
    $ player.Equipment_Damage_Magic_Min = 1
    $ player.Equipment_Damage_Will_Max = 10
    $ player.Equipment_Damage_Will_Min = 1
    $ player.Equipment_Dodge = 4
    $ player.Equipment_Initiative = 4
#  Equipment - Consumables.  Consider it a 'stock', and will handle the
# potions, grenades, and other one use items and non-rechargables (like wands.)
    $ player.Equipment_Consumables_Potions_HP_Restore = 3
    $ player.Equipment_Consumables_Potions_AP_Restore = 2
    $ player.Equipment_Consumables_Potions_WP_Restore = 1
#  This block handles status effects, including the check to see if it's on.
# EffectActive is probably going to be used mostly for the Screen/Frame/UI
# stuff.
    $ player.Status_Poison_EffectActive = 0
    $ player.Status_Poison_Duration = 0
    $ player.Status_Poison_Strength = 0
    $ player.Status_Regen_EffectActive = 0
    $ player.Status_Regen_Duration = 0
    $ player.Status_Regen_Strength = 0
    $ player.Status_Slow_EffectActive = 0
    $ player.Status_Slow_Duration = 0
    $ player.Status_Slow_Strength = 0
    $ player.Status_Haste_EffectActive = 0
    $ player.Status_Haste_Duration = 0
    $ player.Status_Haste_Strength = 0
    $ player.Status_Weaken_EffectActive = 0
    $ player.Status_Weaken_Duration = 0
    $ player.Status_Weaken_Strength = 0
    $ player.Status_Strengthen_EffectActive = 0
    $ player.Status_Strengthen_Duration = 0
    $ player.Status_Strengthen_Strength = 0
    $ player.Status_Paralyse_EffectActive = 0
    $ player.Status_Paralyse_Duration = 0
    $ player.Status_Charm_EffectActive = 0
    $ player.Status_Charm_Duration = 0
    $ player.Status_Sleep_EffectActive = 0
    $ player.Status_Sleep_Duration = 0
    $ player.Status_Block_EffectActive = 0
    $ player.Status_Block_Strength = 0
    $ player.Status_Dodge_EffectActive = 0
    $ player.Status_Dodge_Strength = 0
# Player's Calculated Attributes
    $ player.X_HealthPoints_Max_X = player.Attribute_HealthPoints_Max+player.Equipment_HealthPoints_Max
    $ player.X_HealthPoints_Current_X = player.X_HealthPoints_Max_X
    $ player.X_AbilityPoints_Max_X = player.Attribute_AbilityPoints_Max+player.Equipment_AbilityPoints_Max
    $ player.X_AbilityPoints_Current_X = player.X_AbilityPoints_Max_X
    $ player.X_WillPoints_Max_X = player.Attribute_WillPoints_Max+player.Equipment_WillPoints_Max
    $ player.X_WillPoints_Current_X = player.X_WillPoints_Max_X
    $ player.X_PlaceholderStrength_X = player.Stats_PlaceholderStrength
    $ player.X_Accuracy_Melee_X = player.Attribute_Accuracy_Melee+player.Equipment_Accuracy_Melee
    $ player.X_Accuracy_Ranged_X = player.Attribute_Accuracy_Ranged+player.Equipment_Accuracy_Ranged
    $ player.X_Armor_Physical_X = player.Attribute_Armor_Physical+player.Equipment_Armor_Physical+player.Status_Block_Strength
    $ player.X_Armor_Magic_X = player.Attribute_Armor_Magic+player.Equipment_Armor_Magic+player.Status_Block_Strength
    $ player.X_Armor_Will_X = player.Attribute_Armor_Will+player.Equipment_Armor_Will
    $ player.X_Damage_Melee_Max_X = player.Equipment_Damage_Melee_Max+player.Attribute_Damage_Melee_Max+player.Status_Strengthen_Strength-player.Status_Weaken_Strength
    $ player.X_Damage_Melee_Min_X = player.Equipment_Damage_Melee_Min+(round(player.Attribute_Damage_Melee_Max/10,0))+(round(player.Status_Strengthen_Strength/10,0))-(round(player.Status_Weaken_Strength/10,0))
    $ player.X_Damage_Ranged_Max_X = player.Equipment_Damage_Ranged_Max+player.Attribute_Damage_Ranged_Max+player.Status_Strengthen_Strength-player.Status_Weaken_Strength
    $ player.X_Damage_Ranged_Min_X = player.Equipment_Damage_Ranged_Min+(round(player.Attribute_Damage_Ranged_Max/10,0))+(round(player.Status_Strengthen_Strength/10,0))-(round(player.Status_Weaken_Strength/10,0))
    $ player.X_Damage_Magic_Max_X = player.Equipment_Damage_Magic_Max+player.Attribute_Damage_Magic_Max
    $ player.X_Damage_Magic_Min_X = player.Equipment_Damage_Magic_Min+(round(player.Attribute_Damage_Magic_Max/10,0))
    $ player.X_Damage_Will_Max_X = player.Equipment_Damage_Will_Max+player.Attribute_Damage_Will_Max
    $ player.X_Damage_Will_Min_X = player.Equipment_Damage_Will_Min+(round(player.Attribute_Damage_Will_Max/10,0))
    $ player.X_Dodge_X = player.Attribute_Dodge+player.Equipment_Dodge+player.Status_Haste_Strength+player.Status_Dodge_Strength-player.Status_Slow_Strength
    $ player.X_Initiative_X = player.Attribute_Initiative+player.Equipment_Initiative+player.Status_Haste_Strength-player.Status_Slow_Strength
# Extra bits.  Trying to obsolete these.
    $ player.roll_attack = 0
    $ player.roll_damage = 0
    $ player.roll_damage_final = 0
    $ player.roll_initiative = 0

#####################################################################
# Player Menu Section
#####################################################################

label battle_Player_Menu:
    menu:
        "What will you do?"
        "Attack - Melee":
            $ player.battle_selected_action = "battle_Player_Attack_Melee"
            return
# \/  Not done - Need to redo status effects and stats -completely- to pull in 'real' and 'temp'
# \/ numbers to work from, so we don't get abnormal math results from effects toggling on and off.
#        "Block":
#            $ player.battle_selected_action = "battle_Player_Block"
#            return
#        "Dodge":
#            $ player.battle_selected_action = "battle_Player_Dodge"
#            return
        "Ability":
            jump battle_Player_Ability_Menu
        "Item":
            jump battle_Player_Item_Menu
        "Do Nothing":
            $ player.battle_selected_action = "battle_Player_Wait"
            return

label battle_Player_Ability_Menu:
    menu:
        "Debuffs":
            jump battle_Player_Ability_Debuff_Menu
        "Buffs":
            jump battle_Player_Ability_Buff_Menu
        "Fire - 20 AP":
            if player.ap_c < 20:
                "Not enough MP!"
                jump battle_Player_Ability_Menu
            else:
                $ player.battle_selected_action = "battle_Player_Ability__Fire"
                return
        "Blizzard - 10 AP":
            if player.ap_c < 10:
                "Not enough MP!"
                jump battle_Player_Ability_Menu
            else:
                $ player.battle_selected_action = "battle_Player_Ability__Blizzard"
                return
        "Thunder - 30 AP":
            if player.ap_c < 30:
                "Not enough MP!"
                jump battle_Player_Ability_Menu
            else:
                $ player.battle_selected_action = "battle_Player_Ability__Thunder"
                return
        "Back":
            jump battle_Player_Menu

label battle_Player_Ability_Debuff_Menu:
    menu:
        "Poison - 5 AP":
            if player.ap_c < 5:
                "Not enough MP!"
                jump battle_Player_Ability_Menu
            else:
                $ player.battle_selected_action = "battle_Player_Ability__Poison"
                return
        "Slow - 5 AP":
            if player.ap_c < 5:
                "Not enough MP!"
                jump battle_Player_Ability_Menu
            else:
                $ player.battle_selected_action = "battle_Player_Ability__Slow"
                return
        "Weaken - 5 AP":
            if player.ap_c < 5:
                "Not enough MP!"
                jump battle_Player_Ability_Menu
            else:
                $ player.battle_selected_action = "battle_Player_Ability__Weaken"
                return
        "Paralyze - 5 AP":
            if player.ap_c < 5:
                "Not enough MP!"
                jump battle_Player_Ability_Menu
            else:
                $ player.battle_selected_action = "battle_Player_Ability__Paralyze"
                return
        "Charm - 5 AP":
            if player.ap_c < 5:
                "Not enough MP!"
                jump battle_Player_Ability_Menu
            else:
                $ player.battle_selected_action = "battle_Player_Ability__Charm"
                return
        "Sleep - 5 AP":
            if player.ap_c < 5:
                "Not enough MP!"
                jump battle_Player_Ability_Menu
            else:
                $ player.battle_selected_action = "battle_Player_Ability__Sleep"
                return
        "Back":
            jump battle_Player_Menu

label battle_Player_Ability_Buff_Menu:
    menu:
        "Regen - 5 AP":
            if player.ap_c < 5:
                "Not enough MP!"
                jump battle_Player_Ability_Menu
            else:
                $ player.battle_selected_action = "battle_Player_Ability__Regen"
                return
        "Haste - 5 AP":
            if player.ap_c < 5:
                "Not enough MP!"
                jump battle_Player_Ability_Menu
            else:
                $ player.battle_selected_action = "battle_Player_Ability__Haste"
                return
        "Strengthen - 5 AP":
            if player.ap_c < 5:
                "Not enough MP!"
                jump battle_Player_Ability_Menu
            else:
                $ player.battle_selected_action = "battle_Player_Ability__Strengthen"
                return
        "Paralyze Self - 5 AP - Debug Test!":
            if player.ap_c < 5:
                "Not enough MP!"
                jump battle_Player_Ability_Menu
            else:
                $ player.battle_selected_action = "battle_Player_Ability__Paralyze_Self"
                return
        "Charm Self - 5 AP - Debug Test!":
            if player.ap_c < 5:
                "Not enough MP!"
                jump battle_Player_Ability_Menu
            else:
                $ player.battle_selected_action = "battle_Player_Ability__Charm_Self"
                return
        "Sleep Self - 5 AP - Debug Test!":
            if player.ap_c < 5:
                "Not enough MP!"
                jump battle_Player_Ability_Menu
            else:
                $ player.battle_selected_action = "battle_Player_Ability__Sleep_Self"
                return
        "Back":
            jump battle_Player_Menu

label battle_Player_Item_Menu:
    menu:
        "Healing Potion - [player.items_potions_hp] Available.":
            if player.items_potions_hp < 1:
                "No potions left!"
                jump battle_Player_Item_Menu
            else:
                $ player.battle_selected_action = "battle_Player_Item__Potion_HP"
                return
        "Ability Potion - [player.items_potions_ap] Available.":
            if player.items_potions_ap < 1:
                "No potions left!"
                jump battle_Player_Item_Menu
            else:
                $ player.battle_selected_action = "battle_Player_Item__Potion_AP"
                return
        "Back":
            jump battle_Player_Menu

#####################################################################
# Player Action Section
#####################################################################

label battle_Player_Attack_Melee:
    "You attack [enemy.name!t] with your weapon of generic name!"
    $ player.roll_attack = renpy.random.randint(1,100)
    if player.roll_attack+player.accuracy_melee < 50:
        "[enemy.name!t] dodges the attack! ([player.roll_attack] + [player.accuracy_melee] vs 50)"
        return
    else:
        "[enemy.name!t] was hit! ([player.roll_attack] + [player.accuracy_melee] vs 50)"
        jump battle_Player_Attack_Melee_Success

#  You may ask why we seperate the attack from the successful hit damage, but this is to allow for
# abilities that would do a single attack roll, but deliver damage of three seperate, 'standard'
# hits, and other things of that nature.

label battle_Player_Attack_Melee_Success:
    $ player.roll_damage = renpy.random.randint(player.damage_melee_min,player.damage_melee_max)
    $ player.roll_damage_final = (player.roll_damage-enemy.armor)
    if player.roll_damage_final < 1:
        "You hit, but do no damage.  ([player.roll_damage] - [enemy.armor] = [player.roll_damage_final])"
        return
    else:
        call battle_call_Enemy_HP_Loss(player.roll_damage_final)
        "You land a solid blow, dealing [player.roll_damage_final] damage.  [enemy.name!t]'s HP at [enemy.hp_c].  ([player.roll_damage] - [enemy.armor])"
        return

label battle_Player_Ability__Fire:
    "You cast Fire on [enemy.name!t]!"
    $ player.roll_damage_final = renpy.random.randint(25,35)
    call battle_call_Enemy_HP_Loss(player.roll_damage_final)
    call battle_call_Player_AP_Loss(20)
    "You sear them for [player.roll_damage_final] damage.  [enemy.name!t]'s HP at [enemy.hp_c]."
    return
   
label battle_Player_Ability__Blizzard:
    "You cast Blizzard on [enemy.name!t]!"
    $ player.roll_damage_final = renpy.random.randint(15,25)
    call battle_call_Enemy_HP_Loss(player.roll_damage_final)
    call battle_call_Player_AP_Loss(10)
    "You flashfreeze them for [player.roll_damage_final] damage.  [enemy.name!t]'s HP at [enemy.hp_c]."
    return

label battle_Player_Ability__Thunder:
    "You cast Thunder on [enemy.name!t]!"
    $ player.roll_damage_final = renpy.random.randint(30,50)
    call battle_call_Enemy_HP_Loss(player.roll_damage_final)
    call battle_call_Player_AP_Loss(30)
    "You zap them for [player.roll_damage_final] damage.  [enemy.name!t]'s HP at [enemy.hp_c]."
    return

label battle_Player_Ability__Poison:
    "You cast Poison on [enemy.name!t]!"
    $ enemy.status_poison_duration = renpy.random.randint(4,6)
    $ enemy.status_poison_strength = renpy.random.randint(2,5)
    call battle_call_Player_AP_Loss(5)
    "You poison them for [enemy.status_poison_duration] rounds, at [enemy.status_poison_strength] strength."
    return

label battle_Player_Ability__Slow:
    "You cast Slow on [enemy.name!t]!"
    $ enemy.status_slow_duration = renpy.random.randint(4,6)
    $ enemy.status_slow_strength = renpy.random.randint(2,5)
    call battle_call_Player_AP_Loss(5)
    "You slow them for [enemy.status_slow_duration] rounds, at [enemy.status_slow_strength] strength."
    return

label battle_Player_Ability__Weaken:
    "You cast Weaken on [enemy.name!t]!"
    $ enemy.status_weaken_duration = renpy.random.randint(4,6)
    $ enemy.status_weaken_strength = renpy.random.randint(2,5)
    call battle_call_Player_AP_Loss(5)
    "You weaken them for [enemy.status_weaken_duration] rounds, at [enemy.status_weaken_strength] strength."
    return

label battle_Player_Ability__Paralyze:
    "You cast Paralyze on [enemy.name!t]!"
    $ enemy.status_paralyze_duration = renpy.random.randint(2,4)
    call battle_call_Player_AP_Loss(5)
    "You paralyze them for [enemy.status_paralyze_duration] rounds."
    return

label battle_Player_Ability__Charm:
    "You cast Charm on [enemy.name!t]!"
    $ enemy.status_charm_duration = renpy.random.randint(2,4)
    call battle_call_Player_AP_Loss(5)
    "You charm them for [enemy.status_charm_duration] rounds."
    return

label battle_Player_Ability__Sleep:
    "You cast Sleep on [enemy.name!t]!"
    $ enemy.status_sleep_duration = renpy.random.randint(2,4)
    call battle_call_Player_AP_Loss(5)
    "You sleep them for [enemy.status_sleep_duration] rounds."
    return

label battle_Player_Ability__Regen:
    "You cast Regen on yourself!"
    $ player.status_regen_duration = renpy.random.randint(4,6)
    $ player.status_regen_strength = renpy.random.randint(2,5)
    call battle_call_Player_AP_Loss(5)
    "You regen yourself for [player.status_regen_duration] rounds, at [player.status_regen_strength] strength."
    return

label battle_Player_Ability__Haste:
    "You cast Haste on yourself!"
    $ player.status_haste_duration = renpy.random.randint(4,6)
    $ player.status_haste_strength = renpy.random.randint(2,5)
    call battle_call_Player_AP_Loss(5)
    "You haste yourself for [player.status_haste_duration] rounds, at [player.status_haste_strength] strength."
    return

label battle_Player_Ability__Strengthen:
    "You cast Strengthen on yourself!"
    $ player.status_strengthen_duration = renpy.random.randint(4,6)
    $ player.status_strengthen_strength = renpy.random.randint(2,5)
    call battle_call_Player_AP_Loss(5)
    "You strengthen yourself them for [player.status_strengthen_duration] rounds, at [player.status_strengthen_strength] strength."
    return

label battle_Player_Ability__Paralyze_Self:
    "You cast Paralyze on yourself! .. Why did you do that?"
    $ player.status_paralyze_duration = renpy.random.randint(2,4)
    call battle_call_Player_AP_Loss(5)
    "You paralyze yourself for [player.status_paralyze_duration] rounds."
    return

label battle_Player_Ability__Charm_Self:
    "You cast Charm on yourself! .. Why did you do that?"
    $ player.status_charm_duration = renpy.random.randint(2,4)
    call battle_call_Player_AP_Loss(5)
    "You charm yourself for [player.status_charm_duration] rounds."
    return

label battle_Player_Ability__Sleep_Self:
    "You cast Sleep on yourself! .. Why did you do that?"
    $ player.status_sleep_duration = renpy.random.randint(2,4)
    call battle_call_Player_AP_Loss(5)
    "You sleep yourself for [player.status_sleep_duration] rounds."
    return

label battle_Player_Item__Potion_HP:
    "You drink a potion!"
    $ player.roll_damage_final = renpy.random.randint(20,40)
    call battle_call_Player_HP_Gain(player.roll_damage_final)
    $ player.items_potions_hp -= 1
    "You heal [player.roll_damage_final] damage, and have [player.items_potions_hp] left."
    return

label battle_Player_Item__Potion_AP:
    "You drink a potion!"
    $ player.roll_damage_final = renpy.random.randint(15,30)
    call battle_call_Player_AP_Gain(player.roll_damage_final)
    $ player.roll_damage = renpy.random.randint(5,15)
    call battle_call_Player_HP_Loss(player.roll_damage)
    $ player.items_potions_ap -= 1
    "You regain [player.roll_damage_final] AP, but the potion burns away [player.roll_damage] HP of life in exchange.  You have [player.items_potions_ap] of the mixture left."
    return

label battle_Player_Wait:
    "You decide to do nothing this turn."
    return

