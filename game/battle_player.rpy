# Shirra's Ren'Py Battle Framework
# https://github.com/ShirraWhitefur/PyBattleFramework
# http://creativecommons.org/licenses/by-nc/3.0/

#  This file will contain initialization setup for the player, as well as all
# of the menus for selecting what action players will take, and then the
# actions, abilities, and items themselves, so as to keep things tidy.
#####################################################################
# Player Init Section
#####################################################################
init -50:
    $ player = DynamicCharacter("playername", color=(192, 64, 64, 255))
    $ playername = "SomethingFailed"
    $ player.Battle_Selected_Action = "battle_Player_Wait"
    $ player.Battle_Outcome = "end"
######
# Status Effects variables Initilization
#  This block handles status effects, including the check to see if it's on.
# EffectActive is probably going to be used mostly for the Screen/Frame/UI
# stuff, though it's been useful in handling how to make various (de)buffs code
# run smoother.
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
    $ player.Status_Clumsy_EffectActive = 0
    $ player.Status_Clumsy_Duration = 0
    $ player.Status_Clumsy_Strength = 0
    $ player.Status_Nimble_EffectActive = 0
    $ player.Status_Nimble_Duration = 0
    $ player.Status_Nimble_Strength = 0
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
    $ player.Status_EquipLoss_Weapon_Duration = 0
    $ player.Status_EquipLoss_Weapon_EffectActive = 0
    $ player.Status_EquipLoss_UpperBodyArmor_Duration = 0
    $ player.Status_EquipLoss_UpperBodyArmor_EffectActive = 0
    $ player.Status_EquipLoss_LowerBodyArmor_Duration = 0
    $ player.Status_EquipLoss_LowerBodyArmor_EffectActive = 0
    $ player.Status_EquipLoss_Necklace_Duration = 0
    $ player.Status_EquipLoss_Necklace_EffectActive = 0
    $ player.Status_EquipLoss_Ring_Duration = 0
    $ player.Status_EquipLoss_Ring_EffectActive = 0
######
# Equipment variables Initilization
    $ player.Equipment_Strength = 1
    $ player.Equipment_Precision = 1
    $ player.Equipment_Insight = 1
    $ player.Equipment_Deceit = 1
    $ player.Equipment_Vigor = 1
    $ player.Equipment_Spirit = 1
    $ player.Equipment_Resolve = 1
    $ player.Equipment_HealthPoints_Max = 1
    $ player.Equipment_AbilityPoints_Max = 1
    $ player.Equipment_WillPoints_Max = 1
    $ player.Equipment_Accuracy_Melee = 1
    $ player.Equipment_Accuracy_Ranged = 1
    $ player.Equipment_Armor_Physical = 1
    $ player.Equipment_Armor_Magic = 1
    $ player.Equipment_Armor_Will = 1
    $ player.Equipment_Damage_Bonus_Melee = 1
    $ player.Equipment_Damage_Bonus_Ranged = 1
    $ player.Equipment_Damage_Bonus_Magic = 1
    $ player.Equipment_Damage_Bonus_Will = 1
    $ player.Equipment_Dodge = 1
    $ player.Equipment_Initiative = 1
    $ player.Equipment_Weapon_Accuracy_Melee = 1
    $ player.Equipment_Weapon_Accuracy_Ranged = 1
    $ player.Equipment_Weapon_Damage_Melee_Max = 1
    $ player.Equipment_Weapon_Damage_Melee_Min = 1
    $ player.Equipment_Weapon_Damage_Ranged_Max = 1
    $ player.Equipment_Weapon_Damage_Ranged_Min = 1
    $ player.Equipment_Weapon_Damage_Magic_Max = 1
    $ player.Equipment_Weapon_Damage_Magic_Min = 1
    $ player.Equipment_Weapon_Damage_Will_Max = 1
    $ player.Equipment_Weapon_Damage_Will_Min = 1
######
# Equipment Slots and Weapon Type
#  These are what the player starts with.
    $ player.Equipment_Slot_Weapon_Name = no_weapon
    $ player.Equipment_Slot_Weapon_Name_Temp = no_weapon
    $ player.Equipment_Slot_Weapon_Name_Text = "Gear Init Failed."
    $ player.Equipment_Slot_Weapon_Accuracy_Type = "Melee"
    $ player.Equipment_Slot_Weapon_Damage_Type = "Melee"
    $ player.Equipment_Slot_UpperBodyArmor_Name = no_upper_armor
    $ player.Equipment_Slot_UpperBodyArmor_Name_Temp = no_upper_armor
    $ player.Equipment_Slot_UpperBodyArmor_Name_Text = "Gear Init Failed."
    $ player.Equipment_Slot_LowerBodyArmor_Name = no_lower_armor
    $ player.Equipment_Slot_LowerBodyArmor_Name_Temp = no_lower_armor
    $ player.Equipment_Slot_LowerBodyArmor_Name_Text = "Gear Init Failed."
    $ player.Equipment_Slot_Necklace_Name = no_necklace
    $ player.Equipment_Slot_Necklace_Name_Temp = no_necklace
    $ player.Equipment_Slot_Necklace_Name_Text = "Gear Init Failed."
    $ player.Equipment_Slot_Ring_Name = no_ring
    $ player.Equipment_Slot_Ring_Name_Temp = no_ring
    $ player.Equipment_Slot_Ring_Name_Text = "Gear Init Failed."
######
#  Equipment - Consumables.  Consider it a 'stock', and will handle the
# potions, grenades, and other one use items and non-rechargables (like wands.)
#  Also 'what the player starts with'.
    $ player.Equipment_Consumables_Potions_HP_Restore = 3
    $ player.Equipment_Consumables_Potions_AP_Restore = 2
    $ player.Equipment_Consumables_Potions_WP_Restore = 1
    $ player.Equipment_Currency = 5000
######
# Player's Base Statistics
# Just for quick reference..
#   Strength    Damage - Melee (% boost); Accuracy - Melee (# boost)
#   Precision   Damage - Ranged (% boost); Accuracy - Ranged (# boost)
#   Insight     Damage - Magic (% boost); Initiative (# boost)
#   Deceit      Damage - Will (% boost); Dodge (# boost)
#   Vigor       Max HP (% boost); Armor - Physical (% boost)
#   Spirit      Max AP (% boost); Armor - Magic (% boost)
#   Resolve     Max WP (% boost); Armor - Will (% boost)
#  Here, Dodge is being considered effectively 'Feint' or 'Bluff', faking
# someone out about where they'll think you'll be as opposed to where you end
# up.  .. At least that's how we explain it, so the two go to gether.
#  This is what the players start with.. and everything past is all calculated
# from these.
    $ player.Stats_Strength = 20
    $ player.Stats_Precision = 20
    $ player.Stats_Insight = 20
    $ player.Stats_Deceit = 20
    $ player.Stats_Vigor = 20
    $ player.Stats_Spirit = 20
    $ player.Stats_Resolve = 20
######
# Player's Calculated, Final Statistics
    $ player.X_Strength_X = player.Stats_Strength+player.Equipment_Strength+player.Status_Strengthen_Strength-player.Status_Weaken_Strength
    $ player.X_Precision_X = player.Stats_Precision+player.Equipment_Precision+player.Status_Nimble_Strength-player.Status_Clumsy_Strength
    $ player.X_Insight_X = player.Stats_Insight+player.Equipment_Insight
    $ player.X_Deceit_X = player.Stats_Deceit+player.Equipment_Deceit
    $ player.X_Vigor_X = player.Stats_Vigor+player.Equipment_Vigor
    $ player.X_Spirit_X = player.Stats_Spirit+player.Equipment_Spirit
    $ player.X_Resolve_X = player.Stats_Resolve+player.Equipment_Resolve
######
# Player's Base Attributes
#  Or bonuses and penalties.  Derived from Stats, we may want to be able to
# directly add to attributes seperate from the stats (as in, for the progression
# of a character.  We'll see if we reallly want that mess of code enough to deal
# with that idea later though, as it'd mean -another- fourteen variables to make
# for our 'bonus bonuses'.  Which just sounds silly.
#  Since we're going to need to work on balancing this somewhat 'on the fly', to
# make it easier to manipulate the system elsewhere to find that balance we will
# be using variables (over in battle_init) set on battle.Bonus_*, to work with
# our math, and allow us to 'fine tune' the system with far less fuss.
#
    $ player.Attribute_HealthPoints = (int(round((player.X_Vigor_X/battle.Bonus_HPAPWP_Max_Stat_Divisor))))+100
    $ player.Attribute_AbilityPoints = (int(round((player.X_Spirit_X/battle.Bonus_HPAPWP_Max_Stat_Divisor))))+100
    $ player.Attribute_WillPoints = (int(round((player.X_Resolve_X/battle.Bonus_HPAPWP_Max_Stat_Divisor))))+100
    $ player.Attribute_Accuracy_Melee = (int(round((player.X_Strength_X/battle.Bonus_Accuracy_Divisor))))
    $ player.Attribute_Accuracy_Ranged = (int(round((player.X_Precision_X/battle.Bonus_Accuracy_Divisor))))
    $ player.Attribute_Armor_Physical = (int(round((player.X_Vigor_X/battle.Bonus_Armor_Stat_Divisor))))+100
    $ player.Attribute_Armor_Magic = (int(round((player.X_Spirit_X/battle.Bonus_Armor_Stat_Divisor))))+100
    $ player.Attribute_Armor_Will = (int(round((player.X_Resolve_X/battle.Bonus_Armor_Stat_Divisor))))+100
    $ player.Attribute_Damage_Bonus_Melee = (int(round((player.X_Strength_X/battle.Bonus_Damage_Stat_Divisor))))+100
    $ player.Attribute_Damage_Bonus_Ranged = (int(round((player.X_Precision_X/battle.Bonus_Damage_Stat_Divisor))))+100
    $ player.Attribute_Damage_Bonus_Magic = (int(round((player.X_Insight_X/battle.Bonus_Damage_Stat_Divisor))))+100
    $ player.Attribute_Damage_Bonus_Will = (int(round((player.X_Deceit_X/battle.Bonus_Damage_Stat_Divisor))))+100
    $ player.Attribute_Dodge = (int(round((player.X_Deceit_X/battle.Bonus_Dodge_Divisor))))
    $ player.Attribute_Initiative = (int(round((player.X_Insight_X/battle.Bonus_Initiative_Divisor))))
######
# Player's Calculated, Final Attributes
#  Yes, status effects can end up being applied to both the stat -and- the
# attribute.  It's a matter of scale, and that stat checks will happen seperate
# of their derived abilities/bonuses.  +10 to a stat check can be a big boost,
# but it's only +1% to damage.  +10% to damage is nice, but that'd be a +100
# stat boost.  So they need duplication.  So +10 to the stat, +10 to the damage,
# +1 more to damage from that stat buff.  Easy and fairly reasonable.
#  Further.  All Attribute bonuses (aside from dodge and accuracy) are
# percentage multipliers, while all of equipment is flat, static bonuses.  This
# keeps attributes -always- relevant, while equipment is our biggest 'power
# creep' method.
    $ player.X_HealthPoints_Max_X = int(round((1 if (battle.Base_HealthPoints_Max+player.Equipment_HealthPoints_Max) < 1 else (battle.Base_HealthPoints_Max+player.Equipment_HealthPoints_Max))*((-99 if (player.Attribute_HealthPoints) < -99 else (player.Attribute_HealthPoints))*0.01)))
    $ player.X_HealthPoints_Current_X = player.X_HealthPoints_Max_X
    $ player.X_AbilityPoints_Max_X = int(round((1 if (battle.Base_AbilityPoints_Max+player.Equipment_AbilityPoints_Max) < 1 else (battle.Base_AbilityPoints_Max+player.Equipment_AbilityPoints_Max))*((-99 if (player.Attribute_AbilityPoints) < -99 else (player.Attribute_AbilityPoints))*0.01)))
    $ player.X_AbilityPoints_Current_X = player.X_AbilityPoints_Max_X
    $ player.X_WillPoints_Max_X = int(round((1 if (battle.Base_WillPoints_Max+player.Equipment_WillPoints_Max) < 1 else (battle.Base_WillPoints_Max+player.Equipment_WillPoints_Max))*((-99 if (player.Attribute_WillPoints) < -99 else (player.Attribute_WillPoints))*0.01)))
    $ player.X_WillPoints_Current_X = player.X_WillPoints_Max_X
    $ player.X_Accuracy_Melee_X = int(round(player.Attribute_Accuracy_Melee+player.Equipment_Accuracy_Melee))
    $ player.X_Accuracy_Ranged_X = int(round(player.Attribute_Accuracy_Ranged+player.Equipment_Accuracy_Ranged))
# For the time being, Block will increase not just Physical armor, but also Magic and Will.  This is to be discussed and debated.
    $ player.X_Armor_Physical_X = int(round((1 if (player.Equipment_Armor_Physical) < 1 else (player.Equipment_Armor_Physical))*((-99 if (player.Attribute_Armor_Physical+player.Status_Block_Strength) < -99 else (player.Attribute_Armor_Physical+player.Status_Block_Strength))*0.01)))
    $ player.X_Armor_Magic_X = int(round((1 if (player.Equipment_Armor_Magic) < 1 else (player.Equipment_Armor_Magic))*((-99 if (player.Attribute_Armor_Magic+player.Status_Block_Strength) < -99 else (player.Attribute_Armor_Magic+player.Status_Block_Strength))*0.01)))
    $ player.X_Armor_Will_X = int(round((1 if (player.Equipment_Armor_Will) < 1 else (player.Equipment_Armor_Will))*((-99 if (player.Attribute_Armor_Will+player.Status_Block_Strength) < -99 else (player.Attribute_Armor_Will+player.Status_Block_Strength))*0.01)))
    $ player.X_Dodge_X = player.Attribute_Dodge+player.Equipment_Dodge+player.Status_Haste_Strength+player.Status_Dodge_Strength-player.Status_Slow_Strength
    $ player.X_Initiative_X = player.Attribute_Initiative+player.Equipment_Initiative+player.Status_Haste_Strength-player.Status_Slow_Strength
    $ player.X_Damage_Bonus_Melee_Text_X = int(round((-99 if (player.Attribute_Damage_Bonus_Melee+player.Equipment_Damage_Bonus_Melee+player.Status_Strengthen_Strength-player.Status_Weaken_Strength) < -99 else (player.Attribute_Damage_Bonus_Melee+player.Equipment_Damage_Bonus_Melee+player.Status_Strengthen_Strength-player.Status_Weaken_Strength))))
    $ player.X_Damage_Bonus_Ranged_Text_X = int(round((-99 if (player.Attribute_Damage_Bonus_Ranged+player.Equipment_Damage_Bonus_Ranged+player.Status_Nimble_Strength-player.Status_Clumsy_Strength) < -99 else (player.Attribute_Damage_Bonus_Ranged+player.Equipment_Damage_Bonus_Ranged+player.Status_Nimble_Strength-player.Status_Clumsy_Strength))))
    $ player.X_Damage_Bonus_Magic_Text_X = int(round((-99 if (player.Attribute_Damage_Bonus_Magic+player.Equipment_Damage_Bonus_Magic) < -99 else (player.Attribute_Damage_Bonus_Magic+player.Equipment_Damage_Bonus_Magic))))
    $ player.X_Damage_Bonus_Will_Text_X = int(round((-99 if (player.Attribute_Damage_Bonus_Will+player.Equipment_Damage_Bonus_Will) < -99 else (player.Attribute_Damage_Bonus_Will+player.Equipment_Damage_Bonus_Will))))
    $ player.X_Damage_Bonus_Melee_X = (player.X_Damage_Bonus_Melee_Text_X)*0.01
    $ player.X_Damage_Bonus_Ranged_X = (player.X_Damage_Bonus_Ranged_Text_X)*0.01
    $ player.X_Damage_Bonus_Magic_X = (player.X_Damage_Bonus_Magic_Text_X)*0.01
    $ player.X_Damage_Bonus_Will_X = (player.X_Damage_Bonus_Will_Text_X)*0.01
    $ player.X_Weapon_Accuracy_Melee_X = int(round(player.Equipment_Weapon_Accuracy_Melee+player.X_Accuracy_Melee_X))
    $ player.X_Weapon_Accuracy_Ranged_X = int(round(player.Equipment_Weapon_Accuracy_Ranged+player.X_Accuracy_Ranged_X))
    $ player.X_Weapon_Damage_Melee_Max_X = int(round(player.Equipment_Weapon_Damage_Melee_Max*player.X_Damage_Bonus_Melee_X))
    $ player.X_Weapon_Damage_Melee_Min_X = int(round(player.Equipment_Weapon_Damage_Melee_Min*player.X_Damage_Bonus_Melee_X))
    $ player.X_Weapon_Damage_Ranged_Max_X = int(round(player.Equipment_Weapon_Damage_Ranged_Max*player.X_Damage_Bonus_Ranged_X))
    $ player.X_Weapon_Damage_Ranged_Min_X = int(round(player.Equipment_Weapon_Damage_Ranged_Min*player.X_Damage_Bonus_Ranged_X))
    $ player.X_Weapon_Damage_Magic_Max_X = int(round(player.Equipment_Weapon_Damage_Magic_Max*player.X_Damage_Bonus_Magic_X))
    $ player.X_Weapon_Damage_Magic_Min_X = int(round(player.Equipment_Weapon_Damage_Magic_Min*player.X_Damage_Bonus_Magic_X))
    $ player.X_Weapon_Damage_Will_Max_X = int(round(player.Equipment_Weapon_Damage_Will_Max*player.X_Damage_Bonus_Will_X))
    $ player.X_Weapon_Damage_Will_Min_X = int(round(player.Equipment_Weapon_Damage_Will_Min*player.X_Damage_Bonus_Will_X))


#####################################################################
# Player Menu Section
#####################################################################

label battle_Player_Menu:
    menu:
        "What will you do?"
        "Attack - [player.Equipment_Slot_Weapon_Damage_Type]":
            $ player.battle_selected_action = "battle_Player_Attack_Main_TypeCheck"
            return
        "Block":
            $ player.battle_selected_action = "battle_Player_Block"
            return
        "Dodge":
            $ player.battle_selected_action = "battle_Player_Dodge"
            return
        "Ability":
            jump battle_Player_Ability_Menu
        "Item":
            jump battle_Player_Item_Menu
        "Do Nothing":
            $ player.battle_selected_action = "battle_Player_Wait"
            return
# Debug - Definitely remove before normal play.
        "Debug - Use Regular UI":
            hide screen status_frame
            show screen fight(playername,enemy.name)
            jump battle_Player_Menu
        "Debug - Use Player Full Stats UI":
            hide screen fight
            show screen status_frame
            jump battle_Player_Menu

label battle_Player_Ability_Menu:
    menu:
        "Debuffs":
            jump battle_Player_Ability_Debuff_Menu
        "Buffs":
            jump battle_Player_Ability_Buff_Menu
        "Fire - 20 AP":
            if player.X_AbilityPoints_Current_X < 20:
                "Not enough AP!"
                jump battle_Player_Ability_Menu
            else:
                $ player.battle_selected_action = "battle_Player_Ability__Fire"
                return
        "Blizzard - 10 AP":
            if player.X_AbilityPoints_Current_X < 10:
                "Not enough AP!"
                jump battle_Player_Ability_Menu
            else:
                $ player.battle_selected_action = "battle_Player_Ability__Blizzard"
                return
        "Thunder - 30 AP":
            if player.X_AbilityPoints_Current_X < 30:
                "Not enough AP!"
                jump battle_Player_Ability_Menu
            else:
                $ player.battle_selected_action = "battle_Player_Ability__Thunder"
                return
        "Back":
            jump battle_Player_Menu

label battle_Player_Ability_Debuff_Menu:
    menu:
        "Poison - 5 AP":
            if player.X_AbilityPoints_Current_X < 5:
                "Not enough MP!"
                jump battle_Player_Ability_Debuff_Menu
            else:
                $ player.battle_selected_action = "battle_Player_Ability__Poison"
                return
        "Slow - 5 AP":
            if player.X_AbilityPoints_Current_X < 5:
                "Not enough MP!"
                jump battle_Player_Ability_Debuff_Menu
            else:
                $ player.battle_selected_action = "battle_Player_Ability__Slow"
                return
        "Weaken - 5 AP":
            if player.X_AbilityPoints_Current_X < 5:
                "Not enough MP!"
                jump battle_Player_Ability_Debuff_Menu
            else:
                $ player.battle_selected_action = "battle_Player_Ability__Weaken"
                return
        "Clumsy - 5 AP":
            if player.X_AbilityPoints_Current_X < 5:
                "Not enough MP!"
                jump battle_Player_Ability_Debuff_Menu
            else:
                $ player.battle_selected_action = "battle_Player_Ability__Clumsy"
                return
        "Paralyse - 5 AP":
            if player.X_AbilityPoints_Current_X < 5:
                "Not enough MP!"
                jump battle_Player_Ability_Debuff_Menu
            else:
                $ player.battle_selected_action = "battle_Player_Ability__Paralyse"
                return
        "Charm - 5 AP":
            if player.X_AbilityPoints_Current_X < 5:
                "Not enough MP!"
                jump battle_Player_Ability_Debuff_Menu
            else:
                $ player.battle_selected_action = "battle_Player_Ability__Charm"
                return
        "Sleep - 5 AP":
            if player.X_AbilityPoints_Current_X < 5:
                "Not enough MP!"
                jump battle_Player_Ability_Debuff_Menu
            else:
                $ player.battle_selected_action = "battle_Player_Ability__Sleep"
                return
        "Disarm - 5 AP":
            if player.X_AbilityPoints_Current_X < 5:
                "Not enough MP!"
                jump battle_Player_Ability_Debuff_Menu
            else:
                $ player.battle_selected_action = "battle_Player_Ability__Disarm"
                return
        "Remove their UpperBodyArmor - 5 AP":
            if player.X_AbilityPoints_Current_X < 5:
                "Not enough MP!"
                jump battle_Player_Ability_Debuff_Menu
            else:
                $ player.battle_selected_action = "battle_Player_Ability__UpperBodyArmorRemove"
                return
        "Back":
            jump battle_Player_Ability_Menu

label battle_Player_Ability_Buff_Menu:
    menu:
        "Regen - 5 AP":
            if player.X_AbilityPoints_Current_X < 5:
                "Not enough MP!"
                jump battle_Player_Ability_Buff_Menu
            else:
                $ player.battle_selected_action = "battle_Player_Ability__Regen"
                return
        "Haste - 5 AP":
            if player.X_AbilityPoints_Current_X < 5:
                "Not enough MP!"
                jump battle_Player_Ability_Buff_Menu
            else:
                $ player.battle_selected_action = "battle_Player_Ability__Haste"
                return
        "Strengthen - 5 AP":
            if player.X_AbilityPoints_Current_X < 5:
                "Not enough MP!"
                jump battle_Player_Ability_Buff_Menu
            else:
                $ player.battle_selected_action = "battle_Player_Ability__Strengthen"
                return
        "Nimble - 5 AP":
            if player.X_AbilityPoints_Current_X < 5:
                "Not enough MP!"
                jump battle_Player_Ability_Buff_Menu
            else:
                $ player.battle_selected_action = "battle_Player_Ability__Nimble"
                return
# Debug - Definitely remove before normal play.
        "Paralyze Self - 5 AP - Debug Test!":
            if player.X_AbilityPoints_Current_X < 5:
                "Not enough MP!"
                jump battle_Player_Ability_Buff_Menu
            else:
                $ player.battle_selected_action = "battle_Player_Ability__Paralyze_Self"
                return
        "Charm Self - 5 AP - Debug Test!":
            if player.X_AbilityPoints_Current_X < 5:
                "Not enough MP!"
                jump battle_Player_Ability_Buff_Menu
            else:
                $ player.battle_selected_action = "battle_Player_Ability__Charm_Self"
                return
        "Sleep Self - 5 AP - Debug Test!":
            if player.X_AbilityPoints_Current_X < 5:
                "Not enough MP!"
                jump battle_Player_Ability_Buff_Menu
            else:
                $ player.battle_selected_action = "battle_Player_Ability__Sleep_Self"
                return
        "Back":
            jump battle_Player_Ability_Menu

label battle_Player_Item_Menu:
    menu:
        "Healing Potion - [player.Equipment_Consumables_Potions_HP_Restore] Available.":
            if player.Equipment_Consumables_Potions_HP_Restore < 1:
                "No potions left!"
                jump battle_Player_Item_Menu
            else:
                $ player.battle_selected_action = "battle_Player_Item__Potion_HP"
                return
        "Ability Potion - [player.Equipment_Consumables_Potions_AP_Restore] Available.":
            if player.Equipment_Consumables_Potions_AP_Restore < 1:
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

#  This is our main attack, and changes how it interacts based on the defined
# pair of Types in the weapon.  You'll likely want to trim things of the debug
# related 'showing what the numbers do', and consider wether you want the
# weapon's attributes to include it's own attack miss/succeed, damage
# fail/succeed messages.

label battle_Player_Attack_Main_TypeCheck:
    "You attack [enemy.name!t] with your [player.Equipment_Slot_Weapon_Name_Text]"
    $player_roll_attack = renpy.random.randint(1,100)
    if player.Equipment_Slot_Weapon_Accuracy_Type == "Melee":
        if (player_roll_attack+player.X_Weapon_Accuracy_Melee_X)-enemy.X_Dodge_X > 50:
            "[enemy.name!t] was hit! ([player_roll_attack] + [player.X_Weapon_Accuracy_Melee_X] - [enemy.X_Dodge_X] vs 50)"
            call battle_Player_Attack_Main_Success
            return
        "[enemy.name!t] dodges the attack! ([player_roll_attack] + [player.X_Weapon_Accuracy_Melee_X] - [enemy.X_Dodge_X] vs 50)"
        return
    if player.Equipment_Slot_Weapon_Accuracy_Type == "Ranged":
        if (player_roll_attack+player.X_Weapon_Accuracy_Ranged_X)-enemy.X_Dodge_X > 50:
            "[enemy.name!t] was hit! ([player_roll_attack] + [player.X_Weapon_Accuracy_Ranged_X] - [enemy.X_Dodge_X] vs 50)"
            call battle_Player_Attack_Main_Success
            return
        "[enemy.name!t] dodges the attack! ([player_roll_attack] + [player.X_Weapon_Accuracy_Ranged_X] - [enemy.X_Dodge_X] vs 50)"
        return
    nar "You broke my system with a wierd accuracy type.  Stop that."
    jump end
        
label battle_Player_Attack_Main_Success:
    if player.Equipment_Slot_Weapon_Damage_Type == "Melee":
        $player_roll_damage = renpy.random.randint(player.X_Weapon_Damage_Melee_Min_X,player.X_Weapon_Damage_Melee_Max_X)
        $player_roll_damage_final = (player_roll_damage-enemy.X_Armor_Physical_X)
        if player_roll_damage_final < 1:
            "You hit, but do no damage.  ([player_roll_damage] - [enemy.X_Armor_Physical_X] = [player_roll_damage_final])"
            return
        call battle_call_Enemy_HP_Loss(player_roll_damage_final)
        "You land a solid blow, dealing [player_roll_damage_final] damage.  [enemy.name!t]'s HP at [enemy.X_HealthPoints_Current_X].  ([player_roll_damage] - [enemy.X_Armor_Physical_X])"
        return
    if player.Equipment_Slot_Weapon_Damage_Type == "Ranged":
        $player_roll_damage = renpy.random.randint(player.X_Weapon_Damage_Ranged_Min_X,player.X_Weapon_Damage_Ranged_Max_X)
        $player_roll_damage_final = (player_roll_damage-enemy.X_Armor_Physical_X)
        if player_roll_damage_final < 1:
            "You hit, but do no damage.  ([player_roll_damage] - [enemy.X_Armor_Physical_X] = [player_roll_damage_final])"
            return
        call battle_call_Enemy_HP_Loss(player_roll_damage_final)
        "You land a solid shot, dealing [player_roll_damage_final] damage.  [enemy.name!t]'s HP at [enemy.X_HealthPoints_Current_X].  ([player_roll_damage] - [enemy.X_Armor_Physical_X])"
        return
    if player.Equipment_Slot_Weapon_Damage_Type == "Magic":
        $player_roll_damage = renpy.random.randint(player.X_Weapon_Damage_Magic_Min_X,player.X_Weapon_Damage_Magic_Max_X)
        $player_roll_damage_final = (player_roll_damage-enemy.X_Armor_Magic_X)
        if player_roll_damage_final < 1:
            "You hit, but do no damage.  ([player_roll_damage] - [enemy.X_Armor_Magic_X] = [player_roll_damage_final])"
            return
        call battle_call_Enemy_HP_Loss(player_roll_damage_final)
        "You land a solid blast, dealing [player_roll_damage_final] damage.  [enemy.name!t]'s HP at [enemy.X_HealthPoints_Current_X].  ([player_roll_damage] - [enemy.X_Armor_Magic_X])"
        return
    if player.Equipment_Slot_Weapon_Damage_Type == "Will":
        $player_roll_damage = renpy.random.randint(player.X_Weapon_Damage_Will_Min_X,player.X_Weapon_Damage_Will_Max_X)
        $player_roll_damage_final = (player_roll_damage-enemy.X_Armor_Will_X)
        if player_roll_damage_final < 1:
            "You hit, but do no damage.  ([player_roll_damage] - [enemy.X_Armor_Will_X] = [player_roll_damage_final])"
            return
        call battle_call_Enemy_HP_Loss(player_roll_damage_final)
        "You land a solid blow, dealing [player_roll_damage_final] damage.  [enemy.name!t]'s HP at [enemy.X_HealthPoints_Current_X].  ([player_roll_damage] - [enemy.X_Armor_Will_X])"
        return
    nar "You broke my system with a wierd damage type.  Stop that."
    jump end

#  You may ask why we seperate the attack from the successful hit damage, but
# this is to allow for abilities that would do a single attack roll, but
# deliver damage of three seperate, 'standard' hits, and other things of that
# nature.

label battle_Player_Block:
    $ player.Status_Block_EffectActive = 1
# Change the level of block strength when the game system is figured out!
    $ player.Status_Block_Strength = 25
    call battle_call_Player_Armor_Recheck
    "You are actively blocking!"
    return

label battle_Player_Dodge:
    $ player.Status_Dodge_EffectActive = 1
# Change the level of dodge strength when the game system is figured out!
    $ player.Status_Dodge_Strength = 25
    call battle_call_Player_Dodge_Recheck
    "You are actively dodging!"
    return

label battle_Player_Ability__Fire:
    "You cast Fire on [enemy.name!t]!"
#  For reference, you're looking at "25 to 35 damage, plus bonuses"
    $player_roll_damage = renpy.random.randint(int(round(25*player.X_Damage_Bonus_Magic_X)),int(round(35*player.X_Damage_Bonus_Magic_X)))
    $player_roll_damage_final = (player_roll_damage-enemy.X_Armor_Magic_X)
    if player_roll_damage_final < 1:
        "Your magic hits, but does no damage.  ([player_roll_damage] - [enemy.X_Armor_Magic_X] = [player_roll_damage_final])"
        return
    call battle_call_Enemy_HP_Loss(player_roll_damage_final)
    call battle_call_Player_AP_Loss(20)
    "You sear them for [player_roll_damage_final] damage.  [enemy.name!t]'s HP at [enemy.X_HealthPoints_Current_X].  ([player_roll_damage] - [enemy.X_Armor_Magic_X] = [player_roll_damage_final])"
    return
   
label battle_Player_Ability__Blizzard:
    "You cast Blizzard on [enemy.name!t]!"
    $player_roll_damage = renpy.random.randint(int(round(15*player.X_Damage_Bonus_Magic_X)),int(round(25*player.X_Damage_Bonus_Magic_X)))
    $player_roll_damage_final = (player_roll_damage-enemy.X_Armor_Magic_X)
    if player_roll_damage_final < 1:
        "Your magic hits, but does no damage.  ([player_roll_damage] - [enemy.X_Armor_Magic_X] = [player_roll_damage_final])"
        return
    call battle_call_Enemy_HP_Loss(player_roll_damage_final)
    call battle_call_Player_AP_Loss(10)
    "You flashfreeze them for [player_roll_damage_final] damage.  [enemy.name!t]'s HP at [enemy.X_HealthPoints_Current_X].  ([player_roll_damage] - [enemy.X_Armor_Magic_X] = [player_roll_damage_final])"
    return

label battle_Player_Ability__Thunder:
    "You cast Thunder on [enemy.name!t]!"
    $player_roll_damage = renpy.random.randint(int(round(30*player.X_Damage_Bonus_Magic_X)),int(round(50*player.X_Damage_Bonus_Magic_X)))
    $player_roll_damage_final = (player_roll_damage-enemy.X_Armor_Magic_X)
    if player_roll_damage_final < 1:
        "Your magic hits, but does no damage.  ([player_roll_damage] - [enemy.X_Armor_Magic_X] = [player_roll_damage_final])"
        return
    call battle_call_Enemy_HP_Loss(player_roll_damage_final)
    call battle_call_Player_AP_Loss(30)
    "You zap them for [player_roll_damage_final] damage.  [enemy.name!t]'s HP at [enemy.X_HealthPoints_Current_X].  ([player_roll_damage] - [enemy.X_Armor_Magic_X] = [player_roll_damage_final])"
    return

label battle_Player_Ability__Poison:
    "You cast Poison on [enemy.name!t]!"
    $ enemy.Status_Poison_EffectActive = 1
    $ enemy.Status_Poison_Duration = renpy.random.randint(4,6)
    $ enemy.Status_Poison_Strength = renpy.random.randint(2,5)
    call battle_call_Player_AP_Loss(5)
    "You poison them for [enemy.Status_Poison_Duration] rounds, at [enemy.Status_Poison_Strength] strength."
    return

label battle_Player_Ability__Slow:
    "You cast Slow on [enemy.name!t]!"
    $ enemy.Status_Slow_EffectActive = 1
    $ enemy.Status_Slow_Duration = renpy.random.randint(4,6)
    $ enemy.Status_Slow_Strength = renpy.random.randint(2,5)
    call battle_call_Player_AP_Loss(5)
    "You slow them for [enemy.Status_Slow_Duration] rounds, at [enemy.Status_Slow_Strength] strength."
    return

label battle_Player_Ability__Weaken:
    "You cast Weaken on [enemy.name!t]!"
    $ enemy.Status_Weaken_EffectActive = 1
    $ enemy.Status_Weaken_Duration = renpy.random.randint(4,6)
    $ enemy.Status_Weaken_Strength = renpy.random.randint(2,5)
    call battle_call_Player_AP_Loss(5)
    "You weaken them for [enemy.Status_Weaken_Duration] rounds, at [enemy.Status_Weaken_Strength] strength."
    return

label battle_Player_Ability__Clumsy:
    "You cast Clumsy on [enemy.name!t]!"
    $ enemy.Status_Clumsy_EffectActive = 1
    $ enemy.Status_Clumsy_Duration = renpy.random.randint(4,6)
    $ enemy.Status_Clumsy_Strength = renpy.random.randint(2,5)
    call battle_call_Player_AP_Loss(5)
    "You make them Clumsy for [enemy.Status_Clumsy_Duration] rounds, at [enemy.Status_Clumsy_Strength] strength."
    return

label battle_Player_Ability__Paralyse:
    "You cast Paralyse on [enemy.name!t]!"
    $ enemy.Status_Paralyse_EffectActive = 1
    $ enemy.Status_Paralyse_Duration = renpy.random.randint(2,4)
    call battle_call_Player_AP_Loss(5)
    "You paralyse them for [enemy.Status_Paralyse_Duration] rounds."
    return

label battle_Player_Ability__Charm:
    "You cast Charm on [enemy.name!t]!"
    $ enemy.Status_Charm_EffectActive = 1
    $ enemy.Status_Charm_Duration = renpy.random.randint(2,4)
    call battle_call_Player_AP_Loss(5)
    "You charm them for [enemy.Status_Charm_Duration] rounds."
    return

label battle_Player_Ability__Sleep:
    "You cast Sleep on [enemy.name!t]!"
    $ enemy.Status_Sleep_EffectActive = 1
    $ enemy.Status_Sleep_Duration = renpy.random.randint(2,4)
    call battle_call_Player_AP_Loss(5)
    "You sleep them for [enemy.Status_Sleep_Duration] rounds."
    return

label battle_Player_Ability__Disarm:
    "You attempt to disarm [enemy.name!t]!"
    call battle_call_Player_AP_Loss(5)
    $player_roll_attack = renpy.random.randint(1,100)
    if player_roll_attack-enemy.X_Dodge_X > 50:
#  This particular check is to make sure we don't remove someone's gear twice,
# as that will -remove it permanently-.  Don't do that.  That's bad.  ^_^
        if enemy.Status_EquipLoss_Weapon_EffectActive == 0:
            call battle_call_Enemy_Status_EquipLoss_Weapon_Remove
        $ enemy.Status_EquipLoss_Weapon_EffectActive = 1
        $ enemy.Status_EquipLoss_Weapon_Duration = renpy.random.randint(2,4)
        "You disarm them for [enemy.Status_EquipLoss_Weapon_Duration] rounds.  ([player_roll_attack] - [enemy.X_Dodge_X] vs 50)"
        return
    "[enemy.name!t] dodges the attack! ([player_roll_attack] - [enemy.X_Dodge_X] vs 50)"
    return

label battle_Player_Ability__UpperBodyArmorRemove:
    "You attempt to remove [enemy.name!t]'s upper body armor!"
    call battle_call_Player_AP_Loss(5)
    $player_roll_attack = renpy.random.randint(1,100)
    if player_roll_attack-enemy.X_Dodge_X > 50:
#  This particular check is to make sure we don't remove someone's gear twice,
# as that will -remove it permanently-.  Don't do that.  That's bad.  ^_^
        if enemy.Status_EquipLoss_UpperBodyArmor_EffectActive == 0:
            call battle_call_Enemy_Status_EquipLoss_UpperBodyArmor_Remove
        $ enemy.Status_EquipLoss_UpperBodyArmor_EffectActive = 1
        $ enemy.Status_EquipLoss_UpperBodyArmor_Duration = renpy.random.randint(2,4)
        "You strip them of their upper body armor for [enemy.Status_EquipLoss_UpperBodyArmor_Duration] rounds.  ([player_roll_attack] - [enemy.X_Dodge_X] vs 50)"
        return
    "[enemy.name!t] dodges the attack! ([player_roll_attack] - [enemy.X_Dodge_X] vs 50)"
    return

label battle_Player_Ability__Regen:
    "You cast Regen on yourself!"
    $ player.Status_Regen_EffectActive = 1
    $ player.Status_Regen_Duration = renpy.random.randint(4,6)
    $ player.Status_Regen_Strength = renpy.random.randint(2,5)
    call battle_call_Player_AP_Loss(5)
    "You regen yourself for [player.Status_Regen_Duration] rounds, at [player.Status_Regen_Strength] strength."
    return

label battle_Player_Ability__Haste:
    "You cast Haste on yourself!"
    $ player.Status_Haste_EffectActive = 1
    $ player.Status_Haste_Duration = renpy.random.randint(4,6)
    $ player.Status_Haste_Strength = renpy.random.randint(2,5)
    call battle_call_Player_AP_Loss(5)
    "You haste yourself for [player.Status_Haste_Duration] rounds, at [player.Status_Haste_Strength] strength."
    return

label battle_Player_Ability__Strengthen:
    "You cast Strengthen on yourself!"
    $ player.Status_Strengthen_EffectActive = 1
    $ player.Status_Strengthen_Duration = renpy.random.randint(4,6)
    $ player.Status_Strengthen_Strength = renpy.random.randint(2,5)
    call battle_call_Player_AP_Loss(5)
    "You strengthen yourself them for [player.Status_Strengthen_Duration] rounds, at [player.Status_Strengthen_Strength] strength."
    return

label battle_Player_Ability__Nimble:
    "You cast Nimble on yourself!"
    $ player.Status_Nimble_EffectActive = 1
    $ player.Status_Nimble_Duration = renpy.random.randint(4,6)
    $ player.Status_Nimble_Strength = renpy.random.randint(2,5)
    call battle_call_Player_AP_Loss(5)
    "You make yourself more Nimble them for [player.Status_Nimble_Duration] rounds, at [player.Status_Nimble_Strength] strength."
    return

label battle_Player_Ability__Paralyze_Self:
    "You cast Paralyze on yourself! .. Why did you do that?"
    $ player.Status_Paralyse_EffectActive = 1
    $ player.Status_Paralyse_Duration = renpy.random.randint(2,4)
    call battle_call_Player_AP_Loss(5)
    "You paralyze yourself for [player.Status_Paralyse_Duration] rounds."
    return

label battle_Player_Ability__Charm_Self:
    "You cast Charm on yourself! .. Why did you do that?"
    $ player.Status_Charm_EffectActive = 1
    $ player.Status_Charm_Duration = renpy.random.randint(2,4)
    call battle_call_Player_AP_Loss(5)
    "You charm yourself for [player.Status_Charm_Duration] rounds."
    return

label battle_Player_Ability__Sleep_Self:
    "You cast Sleep on yourself! .. Why did you do that?"
    $ player.Status_Sleep_EffectActive = 1
    $ player.Status_Sleep_Duration = renpy.random.randint(2,4)
    call battle_call_Player_AP_Loss(5)
    "You sleep yourself for [player.Status_Sleep_Duration] rounds."
    return

label battle_Player_Item__Potion_HP:
    "You drink a potion!"
    $player_roll_damage_final = renpy.random.randint(20,40)
    call battle_call_Player_HP_Gain(player_roll_damage_final)
    $ player.Equipment_Consumables_Potions_HP_Restore -= 1
    "You heal [player_roll_damage_final] damage, and have [player.Equipment_Consumables_Potions_HP_Restore] left."
    return

label battle_Player_Item__Potion_AP:
    "You drink a potion!"
    $player_roll_damage_final = renpy.random.randint(15,30)
    call battle_call_Player_AP_Gain(player_roll_damage_final)
    $player_roll_damage = renpy.random.randint(5,15)
    call battle_call_Player_HP_Loss(player_roll_damage)
    $ player.Equipment_Consumables_Potions_AP_Restore -= 1
    "You regain [player_roll_damage_final] AP, but the potion burns away [player_roll_damage] HP of life in exchange.  You have [player.Equipment_Consumables_Potions_AP_Restore] of the mixture left."
    return

label battle_Player_Wait:
    "You decide to do nothing this turn."
    return

#  You may wish to cull the text from this, because the player is already
# informed of a skipped turn earlier.. but it's useful for the debug work.
label battle_Player_Skipped:
    "Your turn was skipped."
    return

