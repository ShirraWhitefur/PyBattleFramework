# Shirra's Ren'Py Battle Framework
# https://github.com/ShirraWhitefur/PyBattleFramework
# http://creativecommons.org/licenses/by-nc/3.0/

# This is where any Screen/UI elements for battle will end up.

#  This is called with your player name and enemy name, appearing on the left
# and right upper corners.
screen fight(pname,ename):
    use battle_frame(pname)
    use battle_frame2(ename)
    use battle_frame_status_effects
    use battle_frame2_status_effects
    use battle_frame_equipped_overview
    use battle_frame2_equipped_overview

screen battle_frame(pname):
    frame xfill(False) yminimum(None) background(None) xpos 0.01 ypos 0.005:
# Player name ends up here..
        text (pname) size 20
    frame xfill(False) yminimum(None) background(None) xpos 0.01 ypos 0.045:
        hbox:
            vbox:
                text ("HP") xalign 1.0 size 20
                text ("AP") xalign 1.0 size 20
                text ("WP") xalign 1.0 size 20
            vbox:
                bar value player.X_HealthPoints_Current_X range player.X_HealthPoints_Max_X xmaximum 150
                bar value player.X_AbilityPoints_Current_X range player.X_AbilityPoints_Max_X xmaximum 150
                bar value player.X_WillPoints_Current_X range player.X_WillPoints_Max_X xmaximum 150
            vbox:
                text ("%d/%d" % (player.X_HealthPoints_Current_X, player.X_HealthPoints_Max_X)) xalign 0.5 size 20
                text ("%d/%d" % (player.X_AbilityPoints_Current_X, player.X_AbilityPoints_Max_X)) xalign 0.5 size 20
                text ("%d/%d" % (player.X_WillPoints_Current_X, player.X_WillPoints_Max_X)) xalign 0.5 size 20
# \/  This section is somewhat of a 'debug' section.  Primarily being used
# \/ currently to show our (de)buffs and help track for errors in the code, it
# \/ also serves as an example of how to set up statements to track the various
# \/ (de)buffs, so you can then use it for triggering pretty status icons in the
# \/ nifty UI you will undoubtedly make to replace this mess!  ^_^  It would
# \/ probably be wise to call this with a seperate screen command..
screen battle_frame_status_effects:
    frame xfill(False) yminimum(None) background(None) xpos 0.01 ypos 0.175:
            hbox:
                vbox:
                        text ("Buff1 -") xalign 1.0 size 12
                        text ("Buff2 -") xalign 1.0 size 12
                        text ("Debuff1 -") xalign 1.0 size 12
                        text ("Debuff2 -") xalign 1.0 size 12
                vbox:
                    hbox:
                        text (" ") size 12
                        if player.Status_Regen_EffectActive == 1:
                            text (" Regen ") size 12
                        if player.Status_Haste_EffectActive == 1:
                            text (" Haste ") size 12
                        if player.Status_Strengthen_EffectActive == 1:
                            text (" Strength ") size 12
                        if player.Status_Nimble_EffectActive == 1:
                            text (" Nimble ") size 12
                    hbox:
                        text (" ") size 12
                        if player.Status_Block_EffectActive == 1:
                            text (" Block ") size 12
                        if player.Status_Dodge_EffectActive == 1:
                            text (" Dodge ") size 12
                    hbox:
                        text (" ") size 12
                        if player.Status_Poison_EffectActive == 1:
                            text (" Poison ") size 12
                        if player.Status_Slow_EffectActive == 1:
                            text (" Slow ") size 12
                        if player.Status_Weaken_EffectActive == 1:
                            text (" Weaken ") size 12
                        if player.Status_Clumsy_EffectActive == 1:
                            text (" Clumsy ") size 12
                    hbox:
                        if player.Status_Paralyse_EffectActive == 1:
                            text (" Paralyse ") size 12
                        if player.Status_Charm_EffectActive == 1:
                            text (" Charm ") size 12
                        if player.Status_Sleep_EffectActive == 1:
                            text (" Sleep ") size 12
# /\ The end of the 'status block'
# \/  This section is definitely a debug section, to make sure that the items
# \/ are being properly equipped.  You'll probably want to just delete this,
# \/ unless you need it to test your work.
screen battle_frame_equipped_overview:
    frame xfill(False) yminimum(None) background(None) xpos 0.01 ypos 0.27:
            hbox:
                vbox:
                        text ("Weapon -") xalign 1.0 size 12
                        text (" ") xalign 1.0 size 12
                        text ("UpperArmor -") xalign 1.0 size 12
                        text ("LowerArmor -") xalign 1.0 size 12
                        text ("Necklace -") xalign 1.0 size 12
                        text ("Ring -") xalign 1.0 size 12
                vbox:
                        text ("[player.Equipment_Slot_Weapon_Name_Text]") size 12
                        text ("Acc - [player.Equipment_Slot_Weapon_Accuracy_Type] - Dmg - [player.Equipment_Slot_Weapon_Damage_Type]") size 12
                        text ("[player.Equipment_Slot_UpperBodyArmor_Name_Text]") size 12
                        text ("[player.Equipment_Slot_LowerBodyArmor_Name_Text]") size 12
                        text ("[player.Equipment_Slot_Necklace_Name_Text]") size 12
                        text ("[player.Equipment_Slot_Ring_Name_Text]") size 12
# /\ The end of the 'equipment block'

#  If you don't like the (very bad) 'mirrored' effect, remove the xalign's, then
# tinker with the xpos's until you get it on screen in the spot you want!
# Didn't invert the bar's because.. need custom images for it not to look wrong.
# If you -do- want inverted bars, bar_invert 1 is where you start, followed by
# http://www.renpy.org/doc/html/style_properties.html#bar-style-properties for
# the rest of your properties to define the left and right bar displayables.
screen battle_frame2(ename):
    frame xfill(False) yminimum(None) background(None) xpos 0.99 ypos 0.005 xalign 1.0:
# Enemy name ends up here..
        text (ename) size 20
    frame xfill(False) yminimum(None) background(None) xpos 0.99 ypos 0.045 xalign 1.0:
        hbox: # (name, "HP", bar) from (level, hp, maxhp)
            vbox:
                text ("HP") xalign 1.0 size 20
                text ("AP") xalign 1.0 size 20
                text ("WP") xalign 1.0 size 20
            vbox:
                bar value enemy.X_HealthPoints_Current_X range enemy.X_HealthPoints_Max_X xmaximum 150
                bar value enemy.X_AbilityPoints_Current_X range enemy.X_AbilityPoints_Max_X xmaximum 150
                bar value enemy.X_WillPoints_Current_X range enemy.X_WillPoints_Max_X xmaximum 150
            vbox:
                text ("%d/%d" % (enemy.X_HealthPoints_Current_X, enemy.X_HealthPoints_Max_X)) xalign 0.5 size 20
                text ("%d/%d" % (enemy.X_AbilityPoints_Current_X, enemy.X_AbilityPoints_Max_X)) xalign 0.5 size 20
                text ("%d/%d" % (enemy.X_WillPoints_Current_X, enemy.X_WillPoints_Max_X)) xalign 0.5 size 20
# \/  This section is somewhat of a 'debug' section.  Primarily being used
# \/ currently to show our (de)buffs and help track for errors in the code, it
# \/ also serves as an example of how to set up statements to track the various
# \/ (de)buffs, so you can then use it for triggering pretty status icons in the
# \/ nifty UI you will undoubtedly make to replace this mess!  ^_^  It would
# \/ probably be wise to call this with a seperate screen command..
screen battle_frame2_status_effects:
    frame xfill(False) yminimum(None) background(None) xpos 0.99 ypos 0.175 xalign 1.0:
            hbox:
                vbox xalign 1.0:
                    hbox:
                        text (" ") size 12
                        if enemy.Status_Regen_EffectActive == 1:
                            text (" Regen ") size 12
                        if enemy.Status_Haste_EffectActive == 1:
                            text (" Haste ") size 12
                        if enemy.Status_Strengthen_EffectActive == 1:
                            text (" Strength ") size 12
                        if enemy.Status_Nimble_EffectActive == 1:
                            text (" Nimble ") size 12
                    hbox:
                        text (" ") size 12
                        if enemy.Status_Block_EffectActive == 1:
                            text (" Block ") size 12
                        if enemy.Status_Dodge_EffectActive == 1:
                            text (" Dodge ") size 12
                    hbox:
                        text (" ") size 12
                        if enemy.Status_Poison_EffectActive == 1:
                            text (" Poison ") size 12
                        if enemy.Status_Slow_EffectActive == 1:
                            text (" Slow ") size 12
                        if enemy.Status_Weaken_EffectActive == 1:
                            text (" Weaken ") size 12
                        if enemy.Status_Clumsy_EffectActive == 1:
                            text (" Clumsy ") size 12
                    hbox:
                        if enemy.Status_Paralyse_EffectActive == 1:
                            text (" Paralyse ") size 12
                        if enemy.Status_Charm_EffectActive == 1:
                            text (" Charm ") size 12
                        if enemy.Status_Sleep_EffectActive == 1:
                            text (" Sleep ") size 12
                vbox xalign 1.0:
                        text ("- Buff1") xalign 0.0 size 12
                        text ("- Buff2") xalign 0.0 size 12
                        text ("- Debuff1") xalign 0.0 size 12
                        text ("- Debuff2") xalign 0.0 size 12
# /\ The end of the 'status block'
# \/  This section is definitely a debug section, to make sure that the items
# \/ are being properly equipped.  You'll probably want to just delete this,
# \/ unless you need it to test your work.
screen battle_frame2_equipped_overview:
    frame xfill(False) yminimum(None) background(None) xpos 0.99 ypos 0.27 xalign 1.0:
            hbox:
                vbox xalign 1.0:
                        text ("[enemy.Equipment_Slot_Weapon_Name_Text]") size 12
                        text ("Acc - [enemy.Equipment_Slot_Weapon_Accuracy_Type] - Dmg - [enemy.Equipment_Slot_Weapon_Damage_Type]") size 12
                        text ("[enemy.Equipment_Slot_UpperBodyArmor_Name_Text]") size 12
                        text ("[enemy.Equipment_Slot_LowerBodyArmor_Name_Text]") size 12
                        text ("[enemy.Equipment_Slot_Necklace_Name_Text]") size 12
                        text ("[enemy.Equipment_Slot_Ring_Name_Text]") size 12
                vbox xalign 1.0:
                        text ("- Weapon") xalign 0.0 size 12
                        text (" ") xalign 0.0 size 12
                        text ("- UpperArmor") xalign 0.0 size 12
                        text ("- LowerArmor") xalign 0.0 size 12
                        text ("- Necklace") xalign 0.0 size 12
                        text ("- Ring") xalign 0.0 size 12
# /\ The end of the 'equipment block'

#####################################################################
# Really Ugly Status Screen
#####################################################################

screen status_frame:
    use status_frame_main
    use status_frame_equipment
    use status_frame_stats
    use status_frame_final

screen status_frame_main:
    frame xfill(False) yminimum(None) background(None) xpos 0.01 ypos 0.005:
# Player name ends up here..
        text (playername) size 20
    frame xfill(False) yminimum(None) background(None) xpos 0.01 ypos 0.045:
        hbox:
            vbox:
                text ("HP") xalign 1.0 size 20
                text ("AP") xalign 1.0 size 20
                text ("WP") xalign 1.0 size 20
            vbox:
                bar value player.X_HealthPoints_Current_X range player.X_HealthPoints_Max_X xmaximum 150
                bar value player.X_AbilityPoints_Current_X range player.X_AbilityPoints_Max_X xmaximum 150
                bar value player.X_WillPoints_Current_X range player.X_WillPoints_Max_X xmaximum 150
            vbox:
                text ("%d/%d" % (player.X_HealthPoints_Current_X, player.X_HealthPoints_Max_X)) xalign 0.5 size 20
                text ("%d/%d" % (player.X_AbilityPoints_Current_X, player.X_AbilityPoints_Max_X)) xalign 0.5 size 20
                text ("%d/%d" % (player.X_WillPoints_Current_X, player.X_WillPoints_Max_X)) xalign 0.5 size 20
# \/  This section is somewhat of a 'debug' section.  Primarily being used
# \/ currently to show our (de)buffs and help track for errors in the code, it
# \/ also serves as an example of how to set up statements to track the various
# \/ (de)buffs, so you can then use it for triggering pretty status icons in the
# \/ nifty UI you will undoubtedly make to replace this mess!  ^_^  It would
# \/ probably be wise to call this with a seperate screen command..
    frame xfill(False) yminimum(None) background(None) xpos 0.01 ypos 0.175:
            hbox:
                vbox:
                        text ("Buff1 -") xalign 1.0 size 12
                        text ("Buff2 -") xalign 1.0 size 12
                        text ("Debuff1 -") xalign 1.0 size 12
                        text ("Debuff2 -") xalign 1.0 size 12
                vbox:
                    hbox:
                        text (" ") size 12
                        if player.Status_Regen_EffectActive == 1:
                            text (" Regen ") size 12
                        if player.Status_Haste_EffectActive == 1:
                            text (" Haste ") size 12
                        if player.Status_Strengthen_EffectActive == 1:
                            text (" Strength ") size 12
                        if player.Status_Nimble_EffectActive == 1:
                            text (" Nimble ") size 12
                    hbox:
                        text (" ") size 12
                        if player.Status_Block_EffectActive == 1:
                            text (" Block ") size 12
                        if player.Status_Dodge_EffectActive == 1:
                            text (" Dodge ") size 12
                    hbox:
                        text (" ") size 12
                        if player.Status_Poison_EffectActive == 1:
                            text (" Poison ") size 12
                        if player.Status_Slow_EffectActive == 1:
                            text (" Slow ") size 12
                        if player.Status_Weaken_EffectActive == 1:
                            text (" Weaken ") size 12
                        if player.Status_Clumsy_EffectActive == 1:
                            text (" Clumsy ") size 12
                    hbox:
                        if player.Status_Paralyse_EffectActive == 1:
                            text (" Paralyse ") size 12
                        if player.Status_Charm_EffectActive == 1:
                            text (" Charm ") size 12
                        if player.Status_Sleep_EffectActive == 1:
                            text (" Sleep ") size 12
# /\ The end of the 'status block'
#
#####################################################################
# Really Ugly Toggle-Status Screens
#####################################################################
# \/  This section is definitely a debug section, to make sure that the items
# \/ are being properly equipped.  You'll probably want to just delete this,
# \/ unless you need it to test your work.
screen status_frame_equipment:
    frame xfill(False) yminimum(None) background(None) xpos 0.01 ypos 0.27:
            hbox:
                vbox:
                        text ("Strength+ =") xalign 1.0 size 12
                        text ("Precision+ =") xalign 1.0 size 12
                        text ("Insight+ =") xalign 1.0 size 12
                        text ("Deceit+ =") xalign 1.0 size 12
                        text ("Vigor+ =") xalign 1.0 size 12
                        text ("Spirit+ =") xalign 1.0 size 12
                        text ("Resolve+ =") xalign 1.0 size 12
                        text ("HPMax+ =") xalign 1.0 size 12
                        text ("APMax+ =") xalign 1.0 size 12
                        text ("WPMax+ =") xalign 1.0 size 12
                        text ("Armor-Phys =") xalign 1.0 size 12
                        text ("Armor-Magi =") xalign 1.0 size 12
                        text ("Armor-Will =") xalign 1.0 size 12
                        text ("Dodge =") xalign 1.0 size 12
                        text ("Initiative =") xalign 1.0 size 12
                        text ("Acc+Melee =") xalign 1.0 size 12
                        text ("Acc+Ranged =") xalign 1.0 size 12
                        text ("HP Potions =") xalign 1.0 size 12
                        text ("AP Potions =") xalign 1.0 size 12
                        text ("WP Potions =") xalign 1.0 size 12
                vbox:
                        text ("[player.Equipment_Strength]") size 12
                        text ("[player.Equipment_Precision]") size 12
                        text ("[player.Equipment_Insight]") size 12
                        text ("[player.Equipment_Deceit]") size 12
                        text ("[player.Equipment_Vigor]") size 12
                        text ("[player.Equipment_Spirit]") size 12
                        text ("[player.Equipment_Resolve]") size 12
                        text ("[player.Equipment_HealthPoints_Max]") size 12
                        text ("[player.Equipment_AbilityPoints_Max]") size 12
                        text ("[player.Equipment_WillPoints_Max]") size 12
                        text ("[player.Equipment_Armor_Physical]") size 12
                        text ("[player.Equipment_Armor_Magic]") size 12
                        text ("[player.Equipment_Armor_Will]") size 12
                        text ("[player.Equipment_Dodge]") size 12
                        text ("[player.Equipment_Initiative]") size 12
                        text ("[player.Equipment_Accuracy_Melee]") size 12
                        text ("[player.Equipment_Accuracy_Ranged]") size 12
                        text ("[player.Equipment_Consumables_Potions_HP_Restore]") size 12
                        text ("[player.Equipment_Consumables_Potions_AP_Restore]") size 12
                        text ("[player.Equipment_Consumables_Potions_WP_Restore]") size 12
                vbox:
                        text ("<-- GEAR \/") xalign 1.0 size 12
                        text ("Dam+Melee =") xalign 1.0 size 12
                        text ("Dam+Range =") xalign 1.0 size 12
                        text ("Dam+Magic =") xalign 1.0 size 12
                        text ("Dam+Will =") xalign 1.0 size 12
                        text ("W.Acc+Melee =") xalign 1.0 size 12
                        text ("W.Acc+Range =") xalign 1.0 size 12
                        text ("W.Dam Melee =") xalign 1.0 size 12
                        text ("W.Dam Range =") xalign 1.0 size 12
                        text ("W.Dam Magic =") xalign 1.0 size 12
                        text ("W.Dam Will =") xalign 1.0 size 12
                        text ("Weapon =") xalign 1.0 size 12
                        text ("W. Type =") xalign 1.0 size 12
                        text ("UpperArmor =") xalign 1.0 size 12
                        text ("LowerArmor =") xalign 1.0 size 12
                        text ("Necklace =") xalign 1.0 size 12
                        text ("Ring =") xalign 1.0 size 12
                        text ("Coins =") xalign 1.0 size 12
                vbox:
                        text (" ") size 12
                        text ("[player.Equipment_Damage_Bonus_Melee]") size 12
                        text ("[player.Equipment_Damage_Bonus_Ranged]") size 12
                        text ("[player.Equipment_Damage_Bonus_Magic]") size 12
                        text ("[player.Equipment_Damage_Bonus_Will]") size 12
                        text ("[player.Equipment_Weapon_Accuracy_Melee]") size 12
                        text ("[player.Equipment_Weapon_Accuracy_Ranged]") size 12
                        text ("[player.Equipment_Weapon_Damage_Melee_Min] - [player.Equipment_Weapon_Damage_Melee_Max]") size 12
                        text ("[player.Equipment_Weapon_Damage_Ranged_Min] - [player.Equipment_Weapon_Damage_Ranged_Max]") size 12
                        text ("[player.Equipment_Weapon_Damage_Magic_Min] - [player.Equipment_Weapon_Damage_Magic_Max]") size 12
                        text ("[player.Equipment_Weapon_Damage_Will_Min] - [player.Equipment_Weapon_Damage_Will_Max]") size 12
                        text ("[player.Equipment_Slot_Weapon_Name_Text]") size 12
                        text ("Acc - [player.Equipment_Slot_Weapon_Accuracy_Type] - Dmg - [player.Equipment_Slot_Weapon_Damage_Type]") size 12
                        text ("[player.Equipment_Slot_UpperBodyArmor_Name_Text]") size 12
                        text ("[player.Equipment_Slot_LowerBodyArmor_Name_Text]") size 12
                        text ("[player.Equipment_Slot_Necklace_Name_Text]") size 12
                        text ("[player.Equipment_Slot_Ring_Name_Text]") size 12
                        text ("[player.Equipment_Currency]") size 12
screen status_frame_stats:
    frame xfill(False) yminimum(None) background(None) xpos 0.45 ypos 0.01:
            hbox:
                vbox:
                        text ("Statistics \/") xalign 1.0 size 12
                        text ("Strength+ =") xalign 1.0 size 12
                        text ("Precision+ =") xalign 1.0 size 12
                        text ("Insight+ =") xalign 1.0 size 12
                        text ("Deceit+ =") xalign 1.0 size 12
                        text ("Vigor+ =") xalign 1.0 size 12
                        text ("Spirit+ =") xalign 1.0 size 12
                        text ("Resolve+ =") xalign 1.0 size 12
                        text ("Abilities \/") xalign 1.0 size 12
                        text ("HPMax+ =") xalign 1.0 size 12
                        text ("APMax+ =") xalign 1.0 size 12
                        text ("WPMax+ =") xalign 1.0 size 12
                        text ("Armor-Phys =") xalign 1.0 size 12
                        text ("Armor-Magi =") xalign 1.0 size 12
                        text ("Armor-Will =") xalign 1.0 size 12
                        text ("Dodge =") xalign 1.0 size 12
                        text ("Initiative =") xalign 1.0 size 12
                        text ("Acc+Melee =") xalign 1.0 size 12
                        text ("Acc+Ranged =") xalign 1.0 size 12
                        text ("Dam+Melee =") xalign 1.0 size 12
                        text ("Dam+Range =") xalign 1.0 size 12
                        text ("Dam+Magic =") xalign 1.0 size 12
                        text ("Dam+Will =") xalign 1.0 size 12
                vbox:
                        text (" ") size 12
                        text ("[player.Stats_Strength]") size 12
                        text ("[player.Stats_Precision]") size 12
                        text ("[player.Stats_Insight]") size 12
                        text ("[player.Stats_Deceit]") size 12
                        text ("[player.Stats_Vigor]") size 12
                        text ("[player.Stats_Spirit]") size 12
                        text ("[player.Stats_Resolve]") size 12
                        text (" ") size 12
                        text ("[player.Attribute_HealthPoints]") size 12
                        text ("[player.Attribute_AbilityPoints]") size 12
                        text ("[player.Attribute_WillPoints]") size 12
                        text ("[player.Attribute_Armor_Physical]") size 12
                        text ("[player.Attribute_Armor_Magic]") size 12
                        text ("[player.Attribute_Armor_Will]") size 12
                        text ("[player.Attribute_Dodge]") size 12
                        text ("[player.Attribute_Initiative]") size 12
                        text ("[player.Attribute_Accuracy_Melee]") size 12
                        text ("[player.Attribute_Accuracy_Ranged]") size 12
                        text ("[player.Attribute_Damage_Bonus_Melee]") size 12
                        text ("[player.Attribute_Damage_Bonus_Ranged]") size 12
                        text ("[player.Attribute_Damage_Bonus_Magic]") size 12
                        text ("[player.Attribute_Damage_Bonus_Will]") size 12

screen status_frame_final:
    frame xfill(False) yminimum(None) background(None) xpos 0.6 ypos 0.10:
            hbox:
                vbox:
                        text ("Final \/") xalign 1.0 size 12
                        text ("Strength+ =") xalign 1.0 size 12
                        text ("Precision+ =") xalign 1.0 size 12
                        text ("Insight+ =") xalign 1.0 size 12
                        text ("Deceit+ =") xalign 1.0 size 12
                        text ("Vigor+ =") xalign 1.0 size 12
                        text ("Spirit+ =") xalign 1.0 size 12
                        text ("Resolve+ =") xalign 1.0 size 12
                        text ("Armor-Phys =") xalign 1.0 size 12
                        text ("Armor-Magi =") xalign 1.0 size 12
                        text ("Armor-Will =") xalign 1.0 size 12
                        text ("Dodge =") xalign 1.0 size 12
                        text ("Initiative =") xalign 1.0 size 12
                        text ("Acc+Melee =") xalign 1.0 size 12
                        text ("Acc+Ranged =") xalign 1.0 size 12
                        text ("Dam+Melee =") xalign 1.0 size 12
                        text ("Dam+Range =") xalign 1.0 size 12
                        text ("Dam+Magic =") xalign 1.0 size 12
                        text ("Dam+Will =") xalign 1.0 size 12
                        text ("W.Acc+Melee =") xalign 1.0 size 12
                        text ("W.Acc+Range =") xalign 1.0 size 12
                        text ("W.Dam Melee =") xalign 1.0 size 12
                        text ("W.Dam Range =") xalign 1.0 size 12
                        text ("W.Dam Magic =") xalign 1.0 size 12
                        text ("W.Dam Will =") xalign 1.0 size 12
                        text ("Dam+Melee =") xalign 1.0 size 12
                        text ("Dam+Range =") xalign 1.0 size 12
                        text ("Dam+Magic =") xalign 1.0 size 12
                        text ("Dam+Will =") xalign 1.0 size 12
                vbox:
                        text (" ") size 12
                        text ("[player.X_Strength_X]") size 12
                        text ("[player.X_Precision_X]") size 12
                        text ("[player.X_Insight_X]") size 12
                        text ("[player.X_Deceit_X]") size 12
                        text ("[player.X_Vigor_X]") size 12
                        text ("[player.X_Spirit_X]") size 12
                        text ("[player.X_Resolve_X]") size 12
                        text ("[player.X_Armor_Physical_X]") size 12
                        text ("[player.X_Armor_Magic_X]") size 12
                        text ("[player.X_Armor_Will_X]") size 12
                        text ("[player.X_Dodge_X]") size 12
                        text ("[player.X_Initiative_X]") size 12
                        text ("[player.X_Accuracy_Melee_X]") size 12
                        text ("[player.X_Accuracy_Ranged_X]") size 12
                        text ("[player.X_Damage_Bonus_Melee_Text_X]") size 12
                        text ("[player.X_Damage_Bonus_Ranged_Text_X]") size 12
                        text ("[player.X_Damage_Bonus_Magic_Text_X]") size 12
                        text ("[player.X_Damage_Bonus_Will_Text_X]") size 12
                        text ("[player.X_Weapon_Accuracy_Melee_X]") size 12
                        text ("[player.X_Weapon_Accuracy_Ranged_X]") size 12
                        text ("[player.X_Weapon_Damage_Melee_Min_X] - [player.X_Weapon_Damage_Melee_Max_X]") size 12
                        text ("[player.X_Weapon_Damage_Ranged_Min_X] - [player.X_Weapon_Damage_Ranged_Max_X]") size 12
                        text ("[player.X_Weapon_Damage_Magic_Min_X] - [player.X_Weapon_Damage_Magic_Max_X]") size 12
                        text ("[player.X_Weapon_Damage_Will_Min_X] - [player.X_Weapon_Damage_Will_Max_X]") size 12
                        text ("[player.X_Damage_Bonus_Melee_X]") size 12
                        text ("[player.X_Damage_Bonus_Ranged_X]") size 12
                        text ("[player.X_Damage_Bonus_Magic_X]") size 12
                        text ("[player.X_Damage_Bonus_Will_X]") size 12
