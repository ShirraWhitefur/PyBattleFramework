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
            jump test01_Battle

        "Test 02 - Orc Test Battle":
# This line tells the upcoming section what enemy information to pull.
            $ ename = Orc_Hero
            jump test01_Battle

        "Test 03 - Checking Init Variables":
            jump test03_VariableCheck
    return

label test01_Battle:
    nar "Here we go!"
    $ playername = renpy.input(_("What is your name?")) or _("Alex")
    player "My name is [playername!t]."
    "The foe is named [ename.name!t]"
#  This big block below is pulling the enemy information and copying it into the battle system, so you don't
# accidently mess up the original template.
    $ enemy = ename
    $ enemy.name = ename.name
    $ enemy.battle_selected_action = "battle_Enemy_Wait"
    $ enemy.Attack_List = ename.Attack_List
# And when in doubt, import in order..
    $ enemy.Stats_PlaceholderStrength = ename.Stats_PlaceholderStrength
    $ enemy.Attribute_HealthPoints_Max = ename.Attribute_HealthPoints_Max
    $ enemy.Attribute_AbilityPoints_Max = ename.Attribute_AbilityPoints_Max
    $ enemy.Attribute_WillPoints_Max = ename.Attribute_WillPoints_Max
    $ enemy.Attribute_Accuracy_Melee = ename.Attribute_Accuracy_Melee
    $ enemy.Attribute_Accuracy_Ranged = ename.Attribute_Accuracy_Ranged
    $ enemy.Attribute_Armor_Physical = ename.Attribute_Armor_Physical
    $ enemy.Attribute_Armor_Magic = ename.Attribute_Armor_Magic
    $ enemy.Attribute_Armor_Will = ename.Attribute_Armor_Will
    $ enemy.Attribute_Damage_Melee_Max = ename.Attribute_Damage_Melee_Max
    $ enemy.Attribute_Damage_Ranged_Max = ename.Attribute_Damage_Ranged_Max
    $ enemy.Attribute_Damage_Magic_Max = ename.Attribute_Damage_Magic_Max
    $ enemy.Attribute_Damage_Will_Max = ename.Attribute_Damage_Will_Max
    $ enemy.Attribute_Dodge = ename.Attribute_Dodge
    $ enemy.Attribute_Initiative = ename.Attribute_Initiative
    $ enemy.Equipment_HealthPoints_Max = ename.Equipment_HealthPoints_Max
    $ enemy.Equipment_AbilityPoints_Max = ename.Equipment_AbilityPoints_Max
    $ enemy.Equipment_WillPoints_Max = ename.Equipment_WillPoints_Max
    $ enemy.Equipment_Accuracy_Melee = ename.Equipment_Accuracy_Melee
    $ enemy.Equipment_Accuracy_Ranged = ename.Equipment_Accuracy_Ranged
    $ enemy.Equipment_Armor_Physical = ename.Equipment_Armor_Physical
    $ enemy.Equipment_Armor_Magic = ename.Equipment_Armor_Magic
    $ enemy.Equipment_Armor_Will = ename.Equipment_Armor_Will
    $ enemy.Equipment_Damage_Melee_Max = ename.Equipment_Damage_Melee_Max
    $ enemy.Equipment_Damage_Melee_Min = ename.Equipment_Damage_Melee_Min
    $ enemy.Equipment_Damage_Ranged_Max = ename.Equipment_Damage_Ranged_Max
    $ enemy.Equipment_Damage_Ranged_Min = ename.Equipment_Damage_Ranged_Min
    $ enemy.Equipment_Damage_Magic_Max = ename.Equipment_Damage_Magic_Max
    $ enemy.Equipment_Damage_Magic_Min = ename.Equipment_Damage_Magic_Min
    $ enemy.Equipment_Damage_Will_Max = ename.Equipment_Damage_Will_Max
    $ enemy.Equipment_Damage_Will_Min = ename.Equipment_Damage_Will_Min
    $ enemy.Equipment_Dodge = ename.Equipment_Dodge
    $ enemy.Equipment_Initiative = ename.Equipment_Initiative
    $ enemy.Equipment_Consumables_Potions_HP_Restore = ename.Equipment_Consumables_Potions_HP_Restore
    $ enemy.Equipment_Consumables_Potions_AP_Restore = ename.Equipment_Consumables_Potions_AP_Restore
    $ enemy.Equipment_Consumables_Potions_WP_Restore = ename.Equipment_Consumables_Potions_WP_Restore
# \/ This block is here, because evidently init: isn't -properly- initing them elsewhere, not completely.
# \/ Don't ask me, I don't know why not.
    $ enemy.Status_Poison_EffectActive = 0
    $ enemy.Status_Poison_Duration = 0
    $ enemy.Status_Poison_Strength = 0
    $ enemy.Status_Regen_EffectActive = 0
    $ enemy.Status_Regen_Duration = 0
    $ enemy.Status_Regen_Strength = 0
    $ enemy.Status_Slow_EffectActive = 0
    $ enemy.Status_Slow_Duration = 0
    $ enemy.Status_Slow_Strength = 0
    $ enemy.Status_Haste_EffectActive = 0
    $ enemy.Status_Haste_Duration = 0
    $ enemy.Status_Haste_Strength = 0
    $ enemy.Status_Weaken_EffectActive = 0
    $ enemy.Status_Weaken_Duration = 0
    $ enemy.Status_Weaken_Strength = 0
    $ enemy.Status_Strengthen_EffectActive = 0
    $ enemy.Status_Strengthen_Duration = 0
    $ enemy.Status_Strengthen_Strength = 0
    $ enemy.Status_Paralyse_EffectActive = 0
    $ enemy.Status_Paralyse_Duration = 0
    $ enemy.Status_Charm_EffectActive = 0
    $ enemy.Status_Charm_Duration = 0
    $ enemy.Status_Sleep_EffectActive = 0
    $ enemy.Status_Sleep_Duration = 0
    $ enemy.Status_Block_EffectActive = 0
    $ enemy.Status_Block_Strength = 0
    $ enemy.Status_Dodge_EffectActive = 0
    $ enemy.Status_Dodge_Strength = 0
# /\ Status effect inits.
    call battle_call_Enemy_Full_StartCheck
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

label test03_VariableCheck:
    nar "Time to test variables."
    nar "HP Max [player.X_HealthPoints_Max_X] ; HP Cur [player.X_HealthPoints_Current_X] ; AP Max [player.X_AbilityPoints_Max_X] ; AP Cur [player.X_AbilityPoints_Current_X] ; WP Max [player.X_WillPoints_Max_X] ; WP Cur [player.X_WillPoints_Current_X]"
    nar "Accuracy - Melee [player.X_Accuracy_Melee_X] ; Accuracy - Ranged [player.X_Accuracy_Ranged_X]"
    nar "Armor - Phys [player.X_Armor_Physical_X] ; Armor - Magic [player.X_Armor_Magic_X] ; Armor - Will [player.X_Armor_Will_X]"
    nar "Damage Melee [player.X_Damage_Melee_Min_X] to [player.X_Damage_Melee_Max_X] ; Damage Ranged [player.X_Damage_Ranged_Min_X] to [player.X_Damage_Ranged_Max_X] ; Damage Magic [player.X_Damage_Magic_Min_X] to [player.X_Damage_Magic_Max_X] ; Damage Will [player.X_Damage_Will_Min_X] to [player.X_Damage_Will_Max_X]"
    nar "Dodge [player.X_Dodge_X] ; Initiative Bonus [player.X_Initiative_X]"
    
    jump end

label end:
    "Done!"
    return
