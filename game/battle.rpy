# If you're looking for the screen frame for the HP and such, check battle_screens.rpy
# If you're looking for the init's, head to battle_init.rpy
# If you're looking for some of the common calls we are been using, look inside battle_calls.rpy
# You'll find the Enemy's under battle_enemy_<name>.rpy
# And finally you'll find most of the player menu's and abilities under battle_player.rpy
#
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
#  Seriously considering taking and putting all the Paralysis/Sleep/Charm checks at the very start, before we do
# initiative, and have it so 'If you have any of these, you go last in the round, period', so as to decrease the
# amount of unneeded if-then branches with victory/loss checks.
    $player_initiative = renpy.random.randint(1,100)+player.X_Initiative_X 
    $enemy_initiative = renpy.random.randint(1,100)+enemy.X_Initiative_X 
    if player_initiative < enemy_initiative:
        "[enemy.name!t] goes first.  Initiative - [playername!t] [player_initiative] vs [enemy.name!t] [enemy_initiative]"
#  This section for the enemy turn will include first firing any status effects and other things that are 'start of turn',
# picking out it's action, and executing it all in one go.
# Here, we make the calls that runs the status effects and start of turn things for the enemy, before moving onward.
        call battle_call_Enemy_Status_Check_Block
# Here, we make sure of any win/loss happening due to the previous round.. Just in case.
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
# Here, we make the calls that runs the status effects and start of turn things for the player, before moving onward.
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
# Here, we make the calls that runs the status effects and start of turn things for the player, before moving onward.
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
#  This section for the enemy turn will include first firing any status effects and other things that are 'start of turn',
# picking out it's action, and executing it all in one go.
# Here, we make the calls that runs the status effects and start of turn things for the enemy, before moving onward.
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

#  This calls up the list of actions this particular enemy can make, and with the call, picks one out randomly.
# Check them out either in battle_calls, or later, under the enemy's own .rpy file to adjust them.  Check out
# the start of battle_init.rpy to see how the weighted function is set up initially.
    $EnemyAttackList = enemy.Attack_List
    call expression EnemyAttackList
    return

#####################################################################
# Enemy Action Section
#####################################################################

#  This section will most likely be split off into a seperate file for each enemy in later versions, to
# keep things 'tidy', since every enemy will have it's own unique attack text for every ability it uses.

label battle_Enemy_Attack_Melee:
    "[enemy.name!t] attacks you with an equally genericly named weapon!"
    $enemy_roll_attack = renpy.random.randint(1,100)
    if (enemy_roll_attack+enemy.X_Accuracy_Melee_X)-player.X_Dodge_X < 50:
        "You dodge the attack! ([enemy_roll_attack] + [enemy.X_Accuracy_Melee_X] - [player.X_Dodge_X] vs 50)"
        return
    else:
        "You were hit! ([enemy_roll_attack] + [enemy.X_Accuracy_Melee_X] - [player.X_Dodge_X] vs 50)"
        jump battle_Enemy_Attack_Melee_Success

label battle_Enemy_Attack_Melee_Success:
    $enemy_roll_damage = renpy.random.randint(enemy.X_Damage_Melee_Min_X,enemy.X_Damage_Melee_Max_X)
    $enemy_roll_damage_final = (enemy_roll_damage-player.X_Armor_Physical_X)
    if enemy_roll_damage_final < 1:
        "[enemy.name!t] hits, but does no damage.  ([enemy_roll_damage] - [player.X_Armor_Physical_X] = [enemy_roll_damage_final])"
        return
    else:
        call battle_call_Player_HP_Loss(enemy_roll_damage_final)
        "[enemy.name!t] lands a solid blow, dealing [enemy_roll_damage_final] damage.  [playername!t]'s HP at [player.X_HealthPoints_Current_X].  ([enemy_roll_damage] - [player.X_Armor_Physical_X])"
        return

label battle_Enemy_Ability__Fire:
#  The AP check for this is over in the Enemy action list itself, by picking lists that allow it.
# Check the enemy file itself for more info!
    "[enemy.name!t] casts Fire on you!"
    $enemy_roll_damage = renpy.random.randint(25,35)
    $enemy_roll_damage_final = (enemy_roll_damage-player.X_Armor_Magic_X)
    call battle_call_Player_HP_Loss(enemy_roll_damage_final)
    call battle_call_Enemy_AP_Loss(20)
    "[enemy.name!t] sears you for [enemy_roll_damage_final] damage.  [playername!t]'s HP at [player.X_HealthPoints_Current_X].  ([enemy_roll_damage] - [player.X_Armor_Magic_X])"
    return

label battle_Enemy_Wait:
    "[enemy.name!t] decides to do nothing this turn."
    return

label battle_Enemy_Skipped:
    "[enemy.name!t] turn was skipped."
    return

#####################################################################
# Win / Loss Section
#####################################################################

#  This will most likely just contain a variable storage on -how- you won/lost the fight, to be referenced
# back in the main VN proper.

label battle_Player_Loss_HP:
    $ player.Battle_Outcome = ename.Battle_Outcomes_Loss_HP
    "You lost the fight!"
    
    return

label battle_Player_Victory_HP:
    $ player.Battle_Outcome = ename.Battle_Outcomes_Victory_HP
    "You won the fight!"
    return


