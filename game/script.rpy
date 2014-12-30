# Shirra's Ren'Py Battle Framework
# https://github.com/ShirraWhitefur/PyBattleFramework
# http://creativecommons.org/licenses/by-nc/3.0/

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
#  _MOST_ notes are going to end up starting in battle.rpy.
#
#  You should also, -hopefully-, if we've done it all right, find that
# all the calls and returns line up, so you can call the battle from in the
# midst of your VN and properly return to it.
#
#  Please note, this is work is likely incredibly ineffecient!  .. Okay, it's
# made one professional programmer cross himself.  Lets just take that as a
# sign of respect for 'the evil codebeast that works despite sanity loss'.  ^_^
#

# The game starts here.
label start:
    scene bg test02
    jump Framework_Test_Start

label Framework_Test_Start:
    nar "Welcome to Shirra's Ren'Py Battle Framework!\n This is a basic functionality demo, for a battle system done in style somewhat like Monster Girl Quest.\n It handles a One on One battle set up only, with quite a few options.  You will likely get more use out of digging into the .rpy code and looking over the comments.  Still, it's always good to see how things actually function in use.\n In any case, lets move on to the important bit!"
    $ playername = renpy.input(_("What is your name?")) or _("Nameless Wanderer")
    player "My name is [playername!t]."
#  Here's a quick bit to make our equipment variables on player match the gear
# named, and set current HP/etc to max.  Good for initial startup of the game.
    call call_Player_Equipment_Slot_Initialize_All
    call battle_call_Player_HP_AP_WP_Current_To_Max_Set
    nar "Wonderful!  Lets get you situated."
    nar "Our testing area isn't exactly 'very furnished', but it should do well enough."
    jump Framework_Test_Room_Clearing

label Framework_Test_Room_Clearing:
    nar "Welcome to the clearing."
    menu:
        nar "Choose where you're going next."
        "Plains of battle":
            jump Framework_Test_Room_Plains_of_Battle
        "Curiously placed vendors":
            jump Framework_Test_Room_Vendor_Tent
        "Campsite - to get some rest":
            jump Framework_Test_Campsite_Rest
        "A wayward mirror - to inspect yourself":
            jump Framework_Test_Mirror_Status
        "Enough of this, time to quit!":
            nar "Enjoy yourself out there!"
            jump end

label Framework_Test_Room_Plains_of_Battle:
    nar "Alas, the plains are particularly empty, with only two foes wandering around on it.  A lowly goblin archer, and a stronger orcish hero."
    menu:
        nar "Who would you like to test your mettle against?"
        "Goblin Archer":
# This line tells the upcoming section what enemy information to pull.
            $ ename = Goblin
            call Framework_Test_Plains_of_Battle_Enemy_Encounter
            nar "Finished with that, you head back to the clearing."
            jump Framework_Test_Room_Clearing
        "Orc Hero":
# This line tells the upcoming section what enemy information to pull.
            $ ename = Orc_Hero
            call Framework_Test_Plains_of_Battle_Enemy_Encounter
            nar "Finished with that, you head back to the clearing."
            jump Framework_Test_Room_Clearing
        "Return to the clearing":
            nar "You decide the clearing is just a better place to be than a battle, and head back."
            jump Framework_Test_Room_Clearing

label Framework_Test_Plains_of_Battle_Enemy_Encounter:
    nar "The foe you will face is [ename.name!t]"
# This line basically goes, 'Okay, lets import whatever enemy matches 'ename''
    call battle_call_Enemy_Data_Import
    call battle_start
    $playerbattleoutcome = player.Battle_Outcome
    jump expression playerbattleoutcome

label test01_goblin_loss_hp:
# This hides our "lovely" Name/HP/AP screen-frames.
    hide screen fight
    nar "And so you lost to the power of the evil testing goblin.  Game over!"
    jump end

label test01_goblin_victory_hp:
# This hides our "lovely" Name/HP/AP screen-frames.
    hide screen fight
    $ player.Equipment_Currency += enemy.Equipment_Currency
    nar "And so you triumphed over the evil testing goblin.  He was carrying [enemy.Equipment_Currency] coins, and unsurprisingly, you 'heroically' scavange it from them, leaving you with [player.Equipment_Currency] coins."
    return

label test02_orc_loss_hp:
# This hides our "lovely" Name/HP/AP screen-frames.
    hide screen fight
    nar "And so you lost to the power of the evil testing orc.  Game over!"
    jump end

label test02_orc_victory_hp:
# This hides our "lovely" Name/HP/AP screen-frames.
    hide screen fight
    $ player.Equipment_Currency += enemy.Equipment_Currency
    nar "And so you triumphed over the evil testing orc.  He was carrying [enemy.Equipment_Currency] coins, and unsurprisingly, you 'heroically' scavange it from them, leaving you with [player.Equipment_Currency] coins."
    return

label Framework_Test_Room_Vendor_Tent:
    nar "Definitely a curious place to set up a tent and your wares, but it's a demo.  What do you expect?"
    jump Framework_Test_Room_Vendor_Menu

label Framework_Test_Room_Vendor_Menu:
    menu:
        nar "Who would you like to purchase from?"
        "Weapon vendor":
            jump Framework_Test_Room_Vendor_Weapon_Menu
        "Armor vendor":
            jump Framework_Test_Room_Vendor_Armor_Menu
        "Jewelry vendor":
            jump Framework_Test_Room_Vendor_Jewelry_Menu
        "Return to the clearing":
            nar "Deciding you've had enough of strangely placed vendors, you head back to the clearing."
            jump Framework_Test_Room_Clearing

label Framework_Test_Room_Vendor_Weapon_Menu:
    menu:
        nar "You are wielding [player.Equipment_Slot_Weapon_Name_Text], and have [player.Equipment_Currency] coins."
        "Weapon - No Weapon - Free!":
            call call_Player_Equipment_Slot_Unequip_Weapon(player.Equipment_Slot_Weapon_Name)
            nar "Weapon unequipped!"
            jump Framework_Test_Room_Vendor_Weapon_Menu
        "Weapon - Orcish Axe - 100 coins":
            $ player.Equipment_Currency -= 100
            call call_Player_Equipment_Slot_Equip_Weapon(axe_orcish)
            nar "Weapon equipped!  [player.Equipment_Currency] coins remaining."
            jump Framework_Test_Room_Vendor_Weapon_Menu
        "Weapon - Adventurer's Sword - 300 coins":
            $ player.Equipment_Currency -= 300
            call call_Player_Equipment_Slot_Equip_Weapon(sword_adventurers)
            nar "Weapon equipped!  [player.Equipment_Currency] coins remaining."
            jump Framework_Test_Room_Vendor_Weapon_Menu
        "Weapon - Short Bow - 500 coins":
            $ player.Equipment_Currency -= 500
            call call_Player_Equipment_Slot_Equip_Weapon(bow_short)
            nar "Weapon equipped!  [player.Equipment_Currency] coins remaining."
            jump Framework_Test_Room_Vendor_Weapon_Menu
        "Weapon - Wand of the Firemage - 1000 coins":
            $ player.Equipment_Currency -= 1000
            call call_Player_Equipment_Slot_Equip_Weapon(wand_firemage)
            nar "Weapon equipped!  [player.Equipment_Currency] coins remaining."
            jump Framework_Test_Room_Vendor_Weapon_Menu
        "Don't change your weapon":
            jump Framework_Test_Room_Vendor_Menu

label Framework_Test_Room_Vendor_Armor_Menu:
    menu:
        nar "You are wearing [player.Equipment_Slot_UpperBodyArmor_Name_Text] on your torso, and [player.Equipment_Slot_LowerBodyArmor_Name_Text] on your legs.  You have [player.Equipment_Currency] coins."
        "Torso - No Armor - Free!":
            call call_Player_Equipment_Slot_Unequip_UpperBodyArmor(player.Equipment_Slot_UpperBodyArmor_Name)
            nar "Armor unequipped!"
            jump Framework_Test_Room_Vendor_Armor_Menu
        "Legs - No Armor - Free!":
            call call_Player_Equipment_Slot_Unequip_LowerBodyArmor(player.Equipment_Slot_LowerBodyArmor_Name)
            nar "Armor unequipped!"
            jump Framework_Test_Room_Vendor_Armor_Menu
        "Torso - Cloth Shirt - 100 coins":
            $ player.Equipment_Currency -= 100
            call call_Player_Equipment_Slot_Equip_UpperBodyArmor(upper_cloth_shirt)
            nar "Armor equipped!  [player.Equipment_Currency] coins remaining."
            jump Framework_Test_Room_Vendor_Armor_Menu
        "Legs - Ragged Leather Armor - 300 coins":
            $ player.Equipment_Currency -= 300
            call call_Player_Equipment_Slot_Equip_LowerBodyArmor(lower_leather_rags)
            nar "Armor equipped!  [player.Equipment_Currency] coins remaining."
            jump Framework_Test_Room_Vendor_Armor_Menu
        "Legs - Chain Armor - 500 coins":
            $ player.Equipment_Currency -= 500
            call call_Player_Equipment_Slot_Equip_LowerBodyArmor(lower_chain_armor)
            nar "Armor equipped!  [player.Equipment_Currency] coins remaining."
            jump Framework_Test_Room_Vendor_Armor_Menu
        "Torso - Chain Armor - 1000 coins":
            $ player.Equipment_Currency -= 1000
            call call_Player_Equipment_Slot_Equip_UpperBodyArmor(upper_chain_armor)
            nar "Armor equipped!  [player.Equipment_Currency] coins remaining."
            jump Framework_Test_Room_Vendor_Armor_Menu
        "Don't change your armor":
            jump Framework_Test_Room_Vendor_Menu

label Framework_Test_Room_Vendor_Jewelry_Menu:
    menu:
        nar "You are wearing [player.Equipment_Slot_Necklace_Name_Text] on your neck, and [player.Equipment_Slot_Ring_Name_Text] on your finger.  You have [player.Equipment_Currency] coins."
        "Neck - No Necklace - Free!":
            call call_Player_Equipment_Slot_Unequip_Necklace(player.Equipment_Slot_Necklace_Name)
            nar "Necklace unequipped!"
            jump Framework_Test_Room_Vendor_Jewelry_Menu
        "Finger - No Ring - Free!":
            call call_Player_Equipment_Slot_Unequip_Ring(player.Equipment_Slot_Ring_Name)
            nar "Ring unequipped!"
            jump Framework_Test_Room_Vendor_Jewelry_Menu
        "Neck - Necklace of Frail Dodging - 100 coins":
            $ player.Equipment_Currency -= 100
            call call_Player_Equipment_Slot_Equip_Necklace(necklace_frail_dodge)
            nar "Necklace equipped!  [player.Equipment_Currency] coins remaining."
            jump Framework_Test_Room_Vendor_Jewelry_Menu
        "Neck - Necklace of Health - 300 coins":
            $ player.Equipment_Currency -= 300
            call call_Player_Equipment_Slot_Equip_Necklace(necklace_health)
            nar "Necklace equipped!  [player.Equipment_Currency] coins remaining."
            jump Framework_Test_Room_Vendor_Jewelry_Menu
        "Finger - Ring of Accuracy - 500 coins":
            $ player.Equipment_Currency -= 500
            call call_Player_Equipment_Slot_Equip_Ring(ring_accuracy)
            nar "Ring equipped!  [player.Equipment_Currency] coins remaining."
            jump Framework_Test_Room_Vendor_Jewelry_Menu
        "Finger - Ring of Magic Power - 1000 coins":
            $ player.Equipment_Currency -= 1000
            call call_Player_Equipment_Slot_Equip_Ring(ring_magic_power)
            nar "Ring equipped!  [player.Equipment_Currency] coins remaining."
            jump Framework_Test_Room_Vendor_Jewelry_Menu
        "Don't change your jewelry":
            jump Framework_Test_Room_Vendor_Menu

label Framework_Test_Campsite_Rest:
    call battle_call_Player_HP_AP_WP_Current_To_Max_Set
    nar "You settled down for a rest, and wake up feeling restored.  HP/AP/Will recovered!"
    jump Framework_Test_Room_Clearing

label Framework_Test_Mirror_Status:
    nar "You peer into the mirror and look yourself over."
    show screen status_frame
    nar "Egads, that's one ugly status screen."
    nar "Well, at least it's functional though."
    hide screen status_frame
    nar "Right, that's enough of that, back to the clearing."
    jump Framework_Test_Room_Clearing

label end:
    "Done!"
    return
