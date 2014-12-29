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
#  Please note, this is the work of only 5 days so far, and likely
# incredibly ineffecient!  .. Okay, it's made one professional programmer
# cross himself.  Lets just take that as a sign of respect for 'the evil
# codebeast that works despite sanity loss'.  ^_^
#


# The game starts here.
label start:

label firstmenu:
    scene bg test02
    menu:
        "Test 01 - Goblin Test Battle":
# This line tells the upcoming section what enemy information to pull.
            $ ename = Goblin
            jump test01_Battle

        "Test 02 - Orc Test Battle":
# This line tells the upcoming section what enemy information to pull.
            $ ename = Orc_Hero
            jump test01_Battle

        "Test 03 - Checking Init Variables":
            call test03_VariableCheck(no_weapon)
    return

label test01_Battle:
    nar "Here we go!"
    $ playername = renpy.input(_("What is your name?")) or _("Alex")
    player "My name is [playername!t]."
    "The foe is named [ename.name!t]"
# This line basically goes, 'Okay, lets import whatever enemy matches 'ename''
    call battle_call_Enemy_Data_Import
    call battle_start
    $playerbattleoutcome = player.Battle_Outcome
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

label test03_VariableCheck(weaponname):
    nar "Time to test variables."
    $ player.Equipment_Currency = weaponname.Equipment_Slot_Weapon_Name_Text
    nar "[player.Equipment_Currency] funds."
    nar "HP Max [player.X_HealthPoints_Max_X] ; HP Cur [player.X_HealthPoints_Current_X] ; AP Max [player.X_AbilityPoints_Max_X] ; AP Cur [player.X_AbilityPoints_Current_X] ; WP Max [player.X_WillPoints_Max_X] ; WP Cur [player.X_WillPoints_Current_X]"
    nar "Accuracy - Melee [player.X_Weapon_Accuracy_Melee_X] ; Accuracy - Ranged [player.X_Weapon_Accuracy_Ranged_X]"
    nar "Armor - Phys [player.X_Armor_Physical_X] ; Armor - Magic [player.X_Armor_Magic_X] ; Armor - Will [player.X_Armor_Will_X]"
    nar "Damage Melee [player.X_Weapon_Damage_Melee_Min_X] to [player.X_Weapon_Damage_Melee_Max_X] ; Damage Ranged [player.X_Weapon_Damage_Ranged_Min_X] to [player.X_Weapon_Damage_Ranged_Max_X] ; Damage Magic [player.X_Weapon_Damage_Magic_Min_X] to [player.X_Weapon_Damage_Magic_Max_X] ; Damage Will [player.X_Weapon_Damage_Will_Min_X] to [player.X_Weapon_Damage_Will_Max_X]"
    nar "Dodge [player.X_Dodge_X] ; Initiative Bonus [player.X_Initiative_X]"
    nar "[player.Equipment_Currency] funds."
    jump end

label end:
    "Done!"
    return

