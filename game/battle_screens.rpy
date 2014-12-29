# This is where any Screen/UI elements for battle will end up.

#  This is called with your player name and enemy name, appearing on the left and
# right upper corners.
screen fight(pname,ename):
    use stats_frame(pname)
    use stats_frame2(ename)

screen stats_frame(pname):
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
                    hbox:
                        if player.Status_Paralyse_EffectActive == 1:
                            text (" Paralyse ") size 12
                        if player.Status_Charm_EffectActive == 1:
                            text (" Charm ") size 12
                        if player.Status_Sleep_EffectActive == 1:
                            text (" Sleep ") size 12
# /\ The end of the 'status block'


#  If you don't like the (very bad) 'mirrored' effect, remove the xalign's, then
# tinker with the xpos's until you get it on screen in the spot you want!
# Didn't invert the bar's because.. need custom images for it not to look wrong.
# If you -do- want inverted bars, bar_invert 1 is where you start, followed by
# http://www.renpy.org/doc/html/style_properties.html#bar-style-properties for
# the rest of your properties to define the left and right bar displayables.
screen stats_frame2(ename):
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

