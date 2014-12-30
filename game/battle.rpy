# Shirra's Ren'Py Battle Framework
# https://github.com/ShirraWhitefur/PyBattleFramework
# http://creativecommons.org/licenses/by-nc/3.0/

#  If you're looking for the screen frame for the HP and such, check
# battle_screens.rpy.  If you're looking for the init's, head to
# battle_init.rpy, as well as battle_player.rpy, and the battle_enemy*.rpy.
# If you're looking for some of the common calls we are been using, look inside
# battle_calls.rpy and battle_calls_status_effects.rpy
#  You'll find the Enemy's under battle_enemy_<name>.rpy, and most of the player
# menu's and abilities under battle_player.rpy.
#
#  If you're wondering why the victory/loss condition checks seem to be kinda
# frequent in the Turn Resolution, it's so that way our call/return functions
# line up properly.  I have no idea of a better way to do it, but it works for
# me!
#
# Init load order list
# -99 battle_equipment_*
# -75 battle_init
# -50 battle_player
# -25 battle_enemy_*

#####################################################################

label battle_start:
#  Reset the battle's round count to 0, since it's the start of a battle.  We
# don't have a need to track it right now, but it's there in case we need to
# make something like 'Merely -survive- for 5 rounds to 'win' the battle!'
    $ battle.roundcount = 0
# This brings out our "lovely" Name/HP/AP/etc screen-frames in the corners.
    show screen fight(playername,enemy.name)
#  I'm not saying I don't trust the equip code to get run properly elsewhere or
# anything like that, but I like to be thorough.  You'll probably want to remove
# the unnecessary call if you're sure you've been thorough, and save some
# processing time!
    call call_Player_Equipment_Slot_Initialize_All

label battle_Begin_Round:
    $ battle.roundcount += 1
#  This is the start of every round.  We call the player menu, and let them
# select their actions, store it, and then go to Turn Resolution and see who
# actually -acts- first.
    call battle_Player_Menu
    jump battle_Turn_Resolution


label battle_Turn_Resolution:
    $player_initiative = renpy.random.randint(1,100)+player.X_Initiative_X 
    $enemy_initiative = renpy.random.randint(1,100)+enemy.X_Initiative_X 
    if player_initiative < enemy_initiative:
        "[enemy.name!t] goes first.  Initiative - [playername!t] [player_initiative] vs [enemy.name!t] [enemy_initiative]"
#  This section for the enemy turn will include first firing any status effects
# and other things that are 'start of turn', picking out it's action, and
# executing it.
#  Here, we make the calls that runs the status effects and start of turn things
# for the enemy, before moving onward.
        call battle_call_Enemy_Status_Check_Block
#  Here, we make sure of any win/loss happening due to the previous round.. Just
# in case.
        if player.X_HealthPoints_Current_X < 1:
            jump battle_Player_Loss_HP
        if enemy.X_HealthPoints_Current_X < 1:
            jump battle_Player_Victory_HP
        call battle_Enemy_Turn
# Here, we make sure of any win/loss happening due to the enemy attack.
        if player.X_HealthPoints_Current_X < 1:
            jump battle_Player_Loss_HP
        if enemy.X_HealthPoints_Current_X < 1:
            jump battle_Player_Victory_HP
#  Here, we make the calls that runs the status effects and start of turn things
# for the player, before moving onward.
        call battle_call_Player_Status_Check_Block
        if player.Status_Paralyse_EffectActive == 1:
            "You are currently Paralysed and cannot act!"
            $ player.Status_Paralyse_Duration -= 1
            if player.Status_Paralyse_Duration == 0:
                $ player.Status_Paralyse_EffectActive = 0
                "You feel the Paralysation wearing off, and will be normal next turn."
            $ player.battle_selected_action = "battle_Player_Skipped"
        if player.Status_Charm_EffectActive == 1:
            "You are currently Charmed and cannot act!"
            $ player.Status_Charm_Duration -= 1
            if player.Status_Charm_Duration == 0:
                $ player.Status_Charm_EffectActive = 0
                "You feel the Charm wearing off, and will be normal next turn."
            $ player.battle_selected_action = "battle_Player_Skipped"
        if player.Status_Sleep_EffectActive == 1:
            "You are currently asleep and cannot act!"
            $ player.Status_Sleep_Duration -= 1
            if player.Status_Sleep_Duration == 0:
                $ player.Status_Sleep_EffectActive = 0
                "You feel the Sleep wearing off, and will wake up next turn."
            $ player.battle_selected_action = "battle_Player_Skipped"
# The player's turn..
        $PlayerBattleSelectedAction = player.battle_selected_action
        call expression PlayerBattleSelectedAction
# Here, we make sure of any win/loss happening due to the player's new attack.
        if player.X_HealthPoints_Current_X < 1:
            jump battle_Player_Loss_HP
        if enemy.X_HealthPoints_Current_X < 1:
            jump battle_Player_Victory_HP
# Round over, start new round!
        jump battle_Begin_Round
    else:
        "You go first.  Initiative - [playername!t] [player_initiative] vs [enemy.name!t] [enemy_initiative]"
#  Here, we make the calls that runs the status effects and start of turn things
# for the player, before moving onward.
        call battle_call_Player_Status_Check_Block
        if player.Status_Paralyse_EffectActive == 1:
            "You are currently Paralysed and cannot act!"
            $ player.Status_Paralyse_Duration -= 1
            if player.Status_Paralyse_Duration == 0:
                $ player.Status_Paralyse_EffectActive = 0
                "You feel the Paralysation wearing off, and will be normal next turn."
            $ player.battle_selected_action = "battle_Player_Skipped"
        if player.Status_Charm_EffectActive == 1:
            "You are currently Charmed and cannot act!"
            $ player.Status_Charm_Duration -= 1
            if player.Status_Charm_Duration == 0:
                $ player.Status_Charm_EffectActive = 0
                "You feel the Charm wearing off, and will be normal next turn."
            $ player.battle_selected_action = "battle_Player_Skipped"
        if player.Status_Sleep_EffectActive == 1:
            "You are currently asleep and cannot act!"
            $ player.Status_Sleep_Duration -= 1
            if player.Status_Sleep_Duration == 0:
                $ player.Status_Sleep_EffectActive = 0
                "You feel the Sleep wearing off, and will wake up next turn."
            $ player.battle_selected_action = "battle_Player_Skipped"
# The player's turn..
        $PlayerBattleSelectedAction = player.battle_selected_action
        call expression PlayerBattleSelectedAction
# Here, we make sure of any win/loss happening due to the player's new attack.
        if player.X_HealthPoints_Current_X < 1:
            jump battle_Player_Loss_HP
        if enemy.X_HealthPoints_Current_X < 1:
            jump battle_Player_Victory_HP
#  This section for the enemy turn will include first firing any status effects
# and other things that are 'start of turn', picking out it's action, and
# executing it.
#  Here, we make the calls that runs the status effects and start of turn things
# for the enemy, before moving onward.
        call battle_call_Enemy_Status_Check_Block
        if player.X_HealthPoints_Current_X < 1:
            jump battle_Player_Loss_HP
        if enemy.X_HealthPoints_Current_X < 1:
            jump battle_Player_Victory_HP
        call battle_Enemy_Turn
# Here, we make sure of any win/loss happening due to the enemy attack.
        if player.X_HealthPoints_Current_X < 1:
            jump battle_Player_Loss_HP
        if enemy.X_HealthPoints_Current_X < 1:
            jump battle_Player_Victory_HP
# Round over, start new round!
        jump battle_Begin_Round

#####################################################################
# Enemy Turn Section
#####################################################################

label battle_Enemy_Turn:
 # If any of these are true, need to skip the enemy's turn.
    if enemy.Status_Paralyse_EffectActive == 1:
        "[enemy.name!t] is currently paralysed and cannot act!"
        $ enemy.Status_Paralyse_Duration -= 1
        if enemy.Status_Paralyse_Duration == 0:
            $ enemy.Status_Paralyse_EffectActive = 0
            "[enemy.name!t] feels the paralysation wearing off, and will be normal next turn."
        jump battle_Enemy_Skipped
    if enemy.Status_Charm_EffectActive == 1:
        "[enemy.name!t] is currently charmed and cannot act!"
        $ enemy.Status_Charm_Duration -= 1
        if enemy.Status_Charm_Duration == 0:
            $ enemy.Status_Charm_EffectActive = 0
            "[enemy.name!t] feels the charm wearing off, and will be normal next turn."
        jump battle_Enemy_Skipped
    if enemy.Status_Sleep_EffectActive == 1:
        "[enemy.name!t] is currently asleep and cannot act!"
        $ enemy.Status_Sleep_Duration -= 1
        if enemy.Status_Sleep_Duration == 0:
            $ enemy.Status_Sleep_EffectActive = 0
            "[enemy.name!t] feels the sleep wearing off, and will wake up next turn."
        jump battle_Enemy_Skipped

#  This calls up the list of actions this particular enemy can make, and with
# the call, picks one out randomly. Check them out under the enemy's own .rpy
# file to adjust them.  Check out the start of battle_init.rpy to see how the
# weighted function is set up initially.
    $EnemyAttackList = enemy.Attack_List
    call expression EnemyAttackList
    return

#####################################################################
# Enemy Action Section
#####################################################################

#  This section contains only a few 'generic' actions currently, with the per
# enemy actions under their own .rpy files.  Likely in actual use, this will
# only contain skipped, and maybe block and dodge.  This keeps things tidy,
# since every enemy will usually have it's own unique attack text for every
# ability it uses.


label battle_Enemy_Attack_Main_TypeCheck_Success:
    $enemy_roll_damage = renpy.random.randint(enemy.X_Weapon_Damage_Melee_Min_X,enemy.X_Weapon_Damage_Melee_Max_X)
    $enemy_roll_damage_final = (enemy_roll_damage-player.X_Armor_Physical_X)
    if enemy_roll_damage_final < 1:
        "[enemy.name!t] hits, but does no damage.  ([enemy_roll_damage] - [player.X_Armor_Physical_X] = [enemy_roll_damage_final])"
        return
    else:
        call battle_call_Player_HP_Loss(enemy_roll_damage_final)
        "[enemy.name!t] lands a solid blow, dealing [enemy_roll_damage_final] damage.  [playername!t]'s HP at [player.X_HealthPoints_Current_X].  ([enemy_roll_damage] - [player.X_Armor_Physical_X])"
        return

label battle_Enemy_Attack_Main_TypeCheck:
    "[enemy.name!t] attacks you with their [enemy.Equipment_Slot_Weapon_Name_Text]"
    $enemy_roll_attack = renpy.random.randint(1,100)
    if enemy.Equipment_Slot_Weapon_Accuracy_Type == "Melee":
        if (enemy_roll_attack+enemy.X_Weapon_Accuracy_Melee_X)-player.X_Dodge_X > 50:
            "You were hit! ([enemy_roll_attack] + [enemy.X_Weapon_Accuracy_Melee_X] - [player.X_Dodge_X] vs 50)"
            call battle_Enemy_Attack_Main_Success
            return
        "You dodge the attack! ([enemy_roll_attack] + [enemy.X_Weapon_Accuracy_Melee_X] - [player.X_Dodge_X] vs 50)"
        return
    if enemy.Equipment_Slot_Weapon_Accuracy_Type == "Ranged":
        if (enemy_roll_attack+enemy.X_Weapon_Accuracy_Ranged_X)-player.X_Dodge_X > 50:
            "You were hit! ([enemy_roll_attack] + [enemy.X_Weapon_Accuracy_Melee_X] - [player.X_Dodge_X] vs 50)"
            call battle_Enemy_Attack_Main_Success
            return
        "You dodge the attack! ([enemy_roll_attack] + [enemy.X_Weapon_Accuracy_Melee_X] - [player.X_Dodge_X] vs 50)"
        return
    nar "You broke my system with a wierd accuracy type.  Stop that."
    jump end
        
label battle_Enemy_Attack_Main_Success:
    if enemy.Equipment_Slot_Weapon_Damage_Type == "Melee":
        $enemy_roll_damage = renpy.random.randint(enemy.X_Weapon_Damage_Melee_Min_X,enemy.X_Weapon_Damage_Melee_Max_X)
        $enemy_roll_damage_final = (enemy_roll_damage-player.X_Armor_Physical_X)
        if enemy_roll_damage_final < 1:
            "[enemy.name!t] hits, but does no damage.  ([enemy_roll_damage] - [player.X_Armor_Physical_X] = [enemy_roll_damage_final])"
            return
        call battle_call_Enemy_HP_Loss(enemy_roll_damage_final)
        "[enemy.name!t] lands a solid blow, dealing [enemy_roll_damage_final] damage.  [playername!t]'s HP at [player.X_HealthPoints_Current_X].  ([enemy_roll_damage] - [player.X_Armor_Physical_X])"
        return
    if enemy.Equipment_Slot_Weapon_Damage_Type == "Ranged":
        $enemy_roll_damage = renpy.random.randint(enemy.X_Weapon_Damage_Ranged_Min_X,enemy.X_Weapon_Damage_Ranged_Max_X)
        $enemy_roll_damage_final = (enemy_roll_damage-player.X_Armor_Physical_X)
        if enemy_roll_damage_final < 1:
            "[enemy.name!t] hits, but does no damage.  ([enemy_roll_damage] - [player.X_Armor_Physical_X] = [enemy_roll_damage_final])"
            return
        call battle_call_Enemy_HP_Loss(enemy_roll_damage_final)
        "[enemy.name!t] lands a solid blow, dealing [enemy_roll_damage_final] damage.  [playername!t]'s HP at [player.X_HealthPoints_Current_X].  ([enemy_roll_damage] - [player.X_Armor_Physical_X])"
        return
    if enemy.Equipment_Slot_Weapon_Damage_Type == "Magic":
        $enemy_roll_damage = renpy.random.randint(enemy.X_Weapon_Damage_Magic_Min_X,enemy.X_Weapon_Damage_Magic_Max_X)
        $enemy_roll_damage_final = (enemy_roll_damage-player.X_Armor_Magic_X)
        if enemy_roll_damage_final < 1:
            "[enemy.name!t] hits, but does no damage.  ([enemy_roll_damage] - [player.X_Armor_Magic_X] = [enemy_roll_damage_final])"
            return
        call battle_call_Enemy_HP_Loss(enemy_roll_damage_final)
        "[enemy.name!t] lands a solid blow, dealing [enemy_roll_damage_final] damage.  [playername!t]'s HP at [player.X_HealthPoints_Current_X].  ([enemy_roll_damage] - [player.X_Armor_Magic_X])"
        return
    if enemy.Equipment_Slot_Weapon_Damage_Type == "Will":
        $enemy_roll_damage = renpy.random.randint(enemy.X_Weapon_Damage_Will_Min_X,enemy.X_Weapon_Damage_Will_Max_X)
        $enemy_roll_damage_final = (enemy_roll_damage-player.X_Armor_Will_X)
        if enemy_roll_damage_final < 1:
            "[enemy.name!t] hits, but does no damage.  ([enemy_roll_damage] - [player.X_Armor_Will_X] = [enemy_roll_damage_final])"
            return
        call battle_call_Enemy_HP_Loss(enemy_roll_damage_final)
        "[enemy.name!t] lands a solid blow, dealing [enemy_roll_damage_final] damage.  [playername!t]'s HP at [player.X_HealthPoints_Current_X].  ([enemy_roll_damage] - [player.X_Armor_Will_X])"
        return
    nar "You broke my system with a wierd damage type.  Stop that."
    jump end

label battle_Enemy_Block:
    $ enemy.Status_Block_EffectActive = 1
# Change the level of block strength when the game system is figured out!
    $ enemy.Status_Block_Strength = 25
    call battle_call_Enemy_Armor_Recheck
    "[enemy.name!t] is actively blocking!"
    return

label battle_Enemy_Dodge:
    $ enemy.Status_Dodge_EffectActive = 1
# Change the level of dodge strength when the game system is figured out!
    $ enemy.Status_Dodge_Strength = 25
    call battle_call_Enemy_Dodge_Recheck
    "[enemy.name!t] is actively dodging!"
    return

label battle_Enemy_Wait:
    "[enemy.name!t] decides to do nothing this turn."
    return

label battle_Enemy_Skipped:
    "[enemy.name!t] turn was skipped."
    return

label battle_Enemy_Ability__Fire:
#  The AP check for this is over in the Enemy action list itself, by picking
# lists that allow it.  Check the enemy file itself for more info!  Do -not-
# forget to set the AP checks, or you'll have enemies casting into negative
# AP happily, and you'll just feel silly.
    "[enemy.name!t] casts Fire on you!"
    $enemy_roll_damage = renpy.random.randint((25+enemy.X_Damage_Bonus_Magic_Min_X),(35+enemy.X_Damage_Bonus_Magic_Max_X))
    $enemy_roll_damage_final = (enemy_roll_damage-player.X_Armor_Magic_X)
    if enemy_roll_damage_final < 1:
        "[enemy.name!t]'s magic hits, but does no damage.  ([enemy_roll_damage] - [player.X_Armor_Magic_X] = [enemy_roll_damage_final])"
        return
    call battle_call_Player_HP_Loss(enemy_roll_damage_final)
    call battle_call_Enemy_AP_Loss(20)
    "[enemy.name!t] sears you for [enemy_roll_damage_final] damage.  [playername!t]'s HP at [player.X_HealthPoints_Current_X].  ([enemy_roll_damage] - [player.X_Armor_Magic_X] = [enemy_roll_damage_final])"
    return


#####################################################################
# Win / Loss Section
#####################################################################

#  This contains the variable grab for -how- you won/lost the fight, as well as
# with which enemy, so you can have proper win/loss resolution.  This would also
# be what you'd follow towards to add experience and item rewards.

label battle_Player_Loss_HP:
    $ player.Battle_Outcome = ename.Battle_Outcomes_Loss_HP
    "You lost the fight!"
    return

label battle_Player_Victory_HP:
    $ player.Battle_Outcome = ename.Battle_Outcomes_Victory_HP
    "You won the fight!"
    return


