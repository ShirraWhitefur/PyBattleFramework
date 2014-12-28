# If you're looking for the screen frame for the HP and such, check battle_screens.rpy
# If you're looking for the init's, head to battle_init.rpy
# If you're looking for some of the common calls we are been using, look inside battle_calls.rpy
#  If you're wondering why the victory/loss condition checks seem to be -all over- the bloody place,
# it's so that way our call/return functions line up properly.  I have no idea of a better way to do
# it.  There probably are several.

#####################################################################

label battle_start:
#  Reset the battle's round count to 0, since it's the start of a battle.  We don't have a need to track it right
# now, but it's there in case we need to make something like 'Merely -survive- for 5 rounds to 'win' the battle!'
    $ battle.roundcount = 0
# This brings out our "lovely" Name/HP/AP screen-frames in the corners.
    show screen fight(playername,enemy.name)


label battle_Begin_Round:
    $ battle.roundcount += 1
#  This is the start of every round.  We call the player menu, and let them select their actions, store it, and then
# go to Iniative Resolution and see who actually -acts- first.
    call battle_Player_Menu
    jump battle_Iniative_Resolution


label battle_Iniative_Resolution:
    $ player.roll_initiative = renpy.random.randint(1,100)+player.initiative_mod 
    $ enemy.roll_initiative = renpy.random.randint(1,100)+enemy.initiative_mod 
    if player.roll_initiative < enemy.roll_initiative:
        "[enemy.name!t] goes first.  Initiative - [playername!t] [player.roll_initiative] vs [enemy.name!t] [enemy.roll_initiative]"
#  This section for the enemy turn will include first firing any status effects and other things that are 'start of turn',
# picking out it's action, and executing it all in one go.
# Here, we make the calls that runs the status effects and start of turn things for the enemy, before moving onward.
        call battle_call_Enemy_Status_Check_Block
# Here, we make sure of any win/loss happening due to the previous round.. Just in case.
        if player.hp_c < 1:
            jump battle_Player_Loss_HP
        if enemy.hp_c < 1:
            jump battle_Player_Victory_HP
        call battle_Enemy_Turn
# Here, we make sure of any win/loss happening due to the enemy attack.
        if player.hp_c < 1:
            jump battle_Player_Loss_HP
        if enemy.hp_c < 1:
            jump battle_Player_Victory_HP
# Here, we make the calls that runs the status effects and start of turn things for the player, before moving onward.
        call battle_call_Player_Status_Check_Block
 # If any of these are true, need to skip the player's turn.
        if player.status_paralyse_duration > 0:
            "You are currently paralysed and cannot act!"
            $ player.status_paralyse_duration -= 1
            if player.status_paralyse_duration = 0:
                "You feel the paralysation wearing off, and will be normal next turn."
            if player.hp_c < 1:
                jump battle_Player_Loss_HP
            if enemy.hp_c < 1:
                jump battle_Player_Victory_HP
            jump battle_Begin_Round
        if player.status_charm_duration > 0:
            "You are currently charmed and cannot act!"
            $ player.status_charm_duration -= 1
            if player.status_charm_duration = 0:
                "You feel the charm wearing off, and will be normal next turn."
            if player.hp_c < 1:
                jump battle_Player_Loss_HP
            if enemy.hp_c < 1:
                jump battle_Player_Victory_HP
            jump battle_Begin_Round
        if player.status_sleep_duration > 0:
            "You are currently asleep and cannot act!"
            $ player.status_sleep_duration -= 1
            if player.status_sleep_duration = 0:
                "You feel the sleep wearing off, and will wake up next turn."
            if player.hp_c < 1:
                jump battle_Player_Loss_HP
            if enemy.hp_c < 1:
                jump battle_Player_Victory_HP
            jump battle_Begin_Round
# The player's turn..
        $PlayerBattleSelectedAction = player.battle_selected_action
        call expression PlayerBattleSelectedAction
# Here, we make sure of any win/loss happening due to the player's new attack.
        if player.hp_c < 1:
            jump battle_Player_Loss_HP
        if enemy.hp_c < 1:
            jump battle_Player_Victory_HP
# Round over, start new round!
        jump battle_Begin_Round
    else:
        "You go first.  Initiative - [playername!t] [player.roll_initiative] vs [enemy.name!t] [enemy.roll_initiative]"
# Here, we make the calls that runs the status effects and start of turn things for the player, before moving onward.
        call battle_call_Player_Status_Check_Block
 # If any of these are true, need to skip the player's turn.
        if player.status_paralyse_duration > 0:
            "You are currently paralysed and cannot act!"
            $ player.status_paralyse_duration -= 1
            if player.status_paralyse_duration = 0:
                "You feel the paralysation wearing off, and will be normal next turn."
# Here, we make the calls that runs the status effects and start of turn things for the enemy, before moving onward.
            call battle_call_Enemy_Status_Check_Block
            if player.hp_c < 1:
                jump battle_Player_Loss_HP
            if enemy.hp_c < 1:
                jump battle_Player_Victory_HP
            call battle_Enemy_Turn
            if player.hp_c < 1:
                jump battle_Player_Loss_HP
            if enemy.hp_c < 1:
                jump battle_Player_Victory_HP
            jump battle_Begin_Round
        if player.status_charm_duration > 0:
            "You are currently charmed and cannot act!"
            $ player.status_charm_duration -= 1
            if player.status_charm_duration = 0:
                "You feel the charm wearing off, and will be normal next turn."
# Here, we make the calls that runs the status effects and start of turn things for the enemy, before moving onward.
            call battle_call_Enemy_Status_Check_Block
            if player.hp_c < 1:
                jump battle_Player_Loss_HP
            if enemy.hp_c < 1:
                jump battle_Player_Victory_HP
            call battle_Enemy_Turn
            if player.hp_c < 1:
                jump battle_Player_Loss_HP
            if enemy.hp_c < 1:
                jump battle_Player_Victory_HP
            jump battle_Begin_Round
        if player.status_sleep_duration > 0:
            "You are currently asleep and cannot act!"
            $ player.status_sleep_duration -= 1
            if player.status_sleep_duration = 0:
                "You feel the sleep wearing off, and will wake up next turn."
# Here, we make the calls that runs the status effects and start of turn things for the enemy, before moving onward.
            call battle_call_Enemy_Status_Check_Block
            if player.hp_c < 1:
                jump battle_Player_Loss_HP
            if enemy.hp_c < 1:
                jump battle_Player_Victory_HP
            call battle_Enemy_Turn
            if player.hp_c < 1:
                jump battle_Player_Loss_HP
            if enemy.hp_c < 1:
                jump battle_Player_Victory_HP
            jump battle_Begin_Round
# The player's turn..
        $PlayerBattleSelectedAction = player.battle_selected_action
        call expression PlayerBattleSelectedAction
# Here, we make sure of any win/loss happening due to the player's new attack.
        if player.hp_c < 1:
            jump battle_Player_Loss_HP
        if enemy.hp_c < 1:
            jump battle_Player_Victory_HP
#  This section for the enemy turn will include first firing any status effects and other things that are 'start of turn',
# picking out it's action, and executing it all in one go.
# Here, we make the calls that runs the status effects and start of turn things for the enemy, before moving onward.
        call battle_call_Enemy_Status_Check_Block
        if player.hp_c < 1:
            jump battle_Player_Loss_HP
        if enemy.hp_c < 1:
            jump battle_Player_Victory_HP
        call battle_Enemy_Turn
# Here, we make sure of any win/loss happening due to the enemy attack.
        if player.hp_c < 1:
            jump battle_Player_Loss_HP
        if enemy.hp_c < 1:
            jump battle_Player_Victory_HP
# Round over, start new round!
        jump battle_Begin_Round

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

#####################################################################
# Enemy Turn Section
#####################################################################

label battle_Enemy_Turn:
 # If any of these are true, need to skip the enemy's turn.
    if enemy.status_paralyse_duration > 0:
        "[enemy.name!t] is currently paralysed and cannot act!"
        $ enemy.status_paralyse_duration -= 1
        if enemy.status_paralyse_duration < 1:
            "[enemy.name!t] feels the paralysation wearing off, and will be normal next turn."
        return
    if enemy.status_charm_duration > 0:
        "[enemy.name!t] is currently charmed and cannot act!"
        $ enemy.status_charm_duration -= 1
        if enemy.status_charm_duration = 0:
            "[enemy.name!t] feels the charm wearing off, and will be normal next turn."
        return
    if enemy.status_sleep_duration > 0:
        "[enemy.name!t] is currently asleep and cannot act!"
        $ enemy.status_sleep_duration -= 1
        if enemy.status_sleep_duration = 0:
            "[enemy.name!t] feels the sleep wearing off, and will wake up next turn."
        return
#  This calls up the list of actions this particular enemy can make, and with the call, picks one out randomly.
# Check them out either in battle_calls, or later, under the enemy's own .rpy file to adjust them.  Check out
# the start of battle_init.rpy to see how the weighted function is set up initially.
    $EnemyAttackList = enemy.attack_list
    call expression EnemyAttackList
    return



#####################################################################
# Enemy Action Section
#####################################################################

#  This section will most likely be split off into a seperate file for each enemy in later versions, to
# keep things 'tidy', since every enemy will have it's own unique attack text for every ability it uses.

label battle_Enemy_Attack_Melee:
    "[enemy.name!t] attacks you with an equally genericly named weapon!"
    $ enemy.roll_attack = renpy.random.randint(1,100)
    if enemy.roll_attack+enemy.accuracy_melee < 50:
        "You dodge the attack! ([enemy.roll_attack] + [enemy.accuracy_melee] vs 50)"
        return
    else:
        "You were hit! ([enemy.roll_attack] + [enemy.accuracy_melee] vs 50)"
        jump battle_Enemy_Attack_Melee_Success

label battle_Enemy_Attack_Melee_Success:
    $ enemy.roll_damage = renpy.random.randint(enemy.damage_melee_min,enemy.damage_melee_max)
    $ enemy.roll_damage_final = (enemy.roll_damage-player.armor)
    if enemy.roll_damage_final < 1:
        "[enemy.name!t] hits, but does no damage.  ([enemy.roll_damage] - [player.armor] = [enemy.roll_damage_final])"
        return
    else:
        call battle_call_Player_HP_Loss(enemy.roll_damage_final)
        "[enemy.name!t] lands a solid blow, dealing [enemy.roll_damage_final] damage.  [playername!t]'s HP at [player.hp_c].  ([enemy.roll_damage] - [player.armor])"
        return

label battle_Enemy_Ability__Fire:
#  The AP check for this is over in the Enemy action list itself, by picking lists that allow it.
# Check the enemy file itself for more info!
    "[enemy.name!t] casts Fire on you!"
    $ enemy.roll_damage_final = renpy.random.randint(25,35)
    call battle_call_Player_HP_Loss(enemy.roll_damage_final)
    call battle_call_Enemy_AP_Loss(20)
    "[enemy.name!t] sears you for [enemy.roll_damage_final] damage.  [playername!t]'s HP at [player.hp_c]."
    return

label battle_Enemy_Wait:
    "[enemy.name!t] decides to do nothing this turn."
    return

#####################################################################
# Win / Loss Section
#####################################################################

#  This will most likely just contain a variable storage on -how- you won/lost the fight, to be referenced
# back in the main VN proper.

label battle_Player_Loss_HP:
    $ player.battle_outcome = ename.battle_outcome_loss_hp
    "You lost the fight!"
    
    return

label battle_Player_Victory_HP:
    $ player.battle_outcome = ename.battle_outcome_victory_hp
    "You won the fight!"
    return


