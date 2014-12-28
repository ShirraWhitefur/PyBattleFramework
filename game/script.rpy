# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image bg test02 = "bg02.jpg"

# Declare characters used by this game.
define nar = Character('Narrator', color="#c8ffc8")

#####################################################################
# Quick Notes from Shirra Whitefur about this mess.
#####################################################################
#  You'll find that we like to split up the various sections into quite a
# few files, for the sake of sanity and organization.  We just find it a
# lot easier to -find- what we're hunting for, if they're not super-huge.
#
#  You should also, -hopefully-, if we've done it all right, find that
# all the calls and returns line up, so you can call the battle from in the
# midst of your VN and properly return to it.
#
#  Please note, this is the work of only 3 days so far, and likely
# incredibly ineffecient!
#


# The game starts here.
label start:

label firstmenu:
    scene bg test02
    menu:
        "Test 01 - Goblin Test Battle":
# This line tells the upcoming section what enemy information to pull.
            $ ename = Goblin
            jump test01_Goblin

        "Test 02 - Orc Test Battle":
# This line tells the upcoming section what enemy information to pull.
            $ ename = Orc_Hero
            jump test02_Orc

        "Test 03 - The same as the first, for now.":
            $ ename = Goblin
            jump test01_Goblin
    return

label test01_Goblin:
    nar "Here we go!"
    $ playername = renpy.input(_("What is your name?")) or _("Alex")
    player "My name is [playername!t]."
    "The foe is named [ename.name!t]"
#  This big block below is pulling the enemy information and copying it into the battle system, so you don't
# accidently mess up the original template.
    $ enemy = ename
    $ enemy.name = ename.name
    $ enemy.hp_c = ename.hp_c
    $ enemy.hp_m = ename.hp_m
    $ enemy.ap_c = ename.ap_c
    $ enemy.ap_m = ename.ap_m
    $ enemy.attack_list = ename.attack_list
    $ enemy.damage_melee_max = ename.damage_melee_max
    $ enemy.damage_melee_min = ename.damage_melee_min
    $ enemy.armor = ename.armor
    $ enemy.accuracy_melee = ename.accuracy_melee
    $ enemy.dodge = ename.dodge
    $ enemy.initiative_mod = ename.initiative_mod
    $ enemy.items_potions_hp = ename.items_potions_hp
    $ enemy.roll_attack = 0
    $ enemy.roll_damage = 0
    $ enemy.roll_damage_final = 0
    $ enemy.roll_initiative = 0
    $ enemy.battle_selected_action = "battle_Enemy_Wait"
# \/ This block is here, because evidently init: isn't -properly- initing them elsewhere, not completely.
# \/ Don't ask me, I don't know why not.
    $ enemy.status_poison_duration = 0
    $ enemy.status_poison_strength = 0
    $ enemy.status_regen_duration = 0
    $ enemy.status_regen_strength = 0
    $ enemy.status_slow_duration = 0
    $ enemy.status_slow_strength = 0
    $ enemy.status_haste_duration = 0
    $ enemy.status_haste_strength = 0
    $ enemy.status_weaken_duration = 0
    $ enemy.status_weaken_strength = 0
    $ enemy.status_strengthen_duration = 0
    $ enemy.status_strengthen_strength = 0
    $ enemy.status_paralyse_duration = 0
    $ enemy.status_charm_duration = 0
    $ enemy.status_sleep_duration = 0
    $ enemy.initiative_mod_temp = 0
    $ enemy.dodge_temp = 0
    $ enemy.damage_melee_max_temp = 0
    $ enemy.damage_melee_min_temp = 0
# /\ Status effect inits.
    call battle_start
    $playerbattleoutcome = player.battle_outcome
    jump expression playerbattleoutcome

label test01_goblin_loss_hp:
# This hides our "lovely" Name/HP/AP screen-frames.
    hide screen fight
    nar "And so you lost to the power of the evil tester goblin."
    jump end

label test01_goblin_victory_hp:
# This hides our "lovely" Name/HP/AP screen-frames.
    hide screen fight
    nar "And so you triumphed over the evil tester goblin."
    jump end

label test02_Orc:
    nar "Here we go!"
    $ playername = renpy.input(_("What is your name?")) or _("Alex")
    player "My name is [playername!t]."
    "The foe is named [ename.name!t]"
#  This big block below is pulling the enemy information and copying it into the battle system, so you don't
# accidently mess up the original template.
    $ enemy = ename
    $ enemy.name = ename.name
    $ enemy.hp_c = ename.hp_c
    $ enemy.hp_m = ename.hp_m
    $ enemy.ap_c = ename.ap_c
    $ enemy.ap_m = ename.ap_m
    $ enemy.attack_list = ename.attack_list
    $ enemy.damage_melee_max = ename.damage_melee_max
    $ enemy.damage_melee_min = ename.damage_melee_min
    $ enemy.armor = ename.armor
    $ enemy.accuracy_melee = ename.accuracy_melee
    $ enemy.dodge = ename.dodge
    $ enemy.initiative_mod = ename.initiative_mod
    $ enemy.items_potions_hp = ename.items_potions_hp
    $ enemy.roll_attack = 0
    $ enemy.roll_damage = 0
    $ enemy.roll_damage_final = 0
    $ enemy.roll_initiative = 0
    $ enemy.battle_selected_action = "battle_Enemy_Wait"
# \/ This block is here, because evidently init: isn't -properly- initing them elsewhere, not completely.
# \/ Don't ask me, I don't know why not.
    $ enemy.status_poison_duration = 0
    $ enemy.status_poison_strength = 0
    $ enemy.status_regen_duration = 0
    $ enemy.status_regen_strength = 0
    $ enemy.status_slow_duration = 0
    $ enemy.status_slow_strength = 0
    $ enemy.status_haste_duration = 0
    $ enemy.status_haste_strength = 0
    $ enemy.status_weaken_duration = 0
    $ enemy.status_weaken_strength = 0
    $ enemy.status_strengthen_duration = 0
    $ enemy.status_strengthen_strength = 0
    $ enemy.status_paralyse_duration = 0
    $ enemy.status_charm_duration = 0
    $ enemy.status_sleep_duration = 0
    $ enemy.initiative_mod_temp = 0
    $ enemy.dodge_temp = 0
    $ enemy.damage_melee_max_temp = 0
    $ enemy.damage_melee_min_temp = 0
# /\ Status effect inits.
    call battle_start
    $playerbattleoutcome = player.battle_outcome
    jump expression playerbattleoutcome

label test02_orc_loss_hp:
# This hides our "lovely" Name/HP/AP screen-frames.
    hide screen fight
    nar "And so you lost to the power of the evil tester orc."
    jump end

label test02_orc_victory_hp:
# This hides our "lovely" Name/HP/AP screen-frames.
    hide screen fight
    nar "And so you triumphed over the evil tester orc."
    jump end

label end:
    "Done!"
    return

