# This is where any Screen/UI elements for battle will end up.

#  This is called with your player name and enemy name, appearing on the left and
# right upper corners.

screen fight(pname,ename):
    use stats_frame(pname)
    use stats_frame2(ename)

screen stats_frame(pname):
    frame xfill(False) yminimum(None) background(None) xalign 0.02 yalign 0.05:
        hbox: # (name, "HP", bar) from (level, hp, maxhp)
            vbox: # name from ("HP", bar)
                text (pname) size 20
                vbox: # name from ("HP", bar)
                    hbox: # "HP" from bar
                        text ("HP") size 20
                        bar value player.X_HealthPoints_Current_X range player.X_HealthPoints_Max_X xmaximum 150
                    hbox: # "HP" from bar
                        text ("AP") size 20
                        bar value player.X_AbilityPoints_Current_X range player.X_AbilityPoints_Max_X xmaximum 150
                vbox: # \/ This section is kinda 'debug'.  Heck, most of the frame is.  Comment out the blocks you don't need!
                    hbox:
                        if player.Status_Regen_EffectActive == 1:
                            text (" Regen ") size 20
                        if player.Status_Haste_EffectActive == 1:
                            text (" Haste ") size 20
                        if player.Status_Strengthen_EffectActive == 1:
                            text (" Strength ") size 20
                    hbox:
                        if player.Status_Poison_EffectActive == 1:
                            text (" Poison ") size 20
                        if player.Status_Slow_EffectActive == 1:
                            text (" Slow ") size 20
                        if player.Status_Weaken_EffectActive == 1:
                            text (" Weaken ") size 20
                    hbox:
                        if player.Status_Paralyse_EffectActive == 1:
                            text (" Paralyse ") size 20
                        if player.Status_Charm_EffectActive == 1:
                            text (" Charm ") size 20
                        if player.Status_Sleep_EffectActive == 1:
                            text (" Sleep ") size 20
                    hbox:
                        if player.Status_Block_EffectActive == 1:
                            text (" Block ") size 20
                        if player.Status_Dodge_EffectActive == 1:
                            text (" Dodge ") size 20
                      # /\ The end of the 'status block'
            vbox: # Level from (hp/maxhp)
# Removed a level note here, because I don't use levels.  Left it around in case it's needed.
#               text ("Lv. %d" % level) xalign 0.5 size 20
                text (" ") xalign 0.5 size 20
                text ("%d/%d" % (player.X_HealthPoints_Current_X, player.X_HealthPoints_Max_X)) xalign 0.5 size 20
                text ("%d/%d" % (player.X_AbilityPoints_Current_X, player.X_AbilityPoints_Max_X)) xalign 0.5 size 20

screen stats_frame2(ename):
    frame xfill(False) yminimum(None) background(None) xalign 0.98 yalign 0.05:
        hbox: # (name, "HP", bar) from (level, hp, maxhp)
            vbox: # name from ("HP", bar)
                text (ename) size 20
                vbox: # name from ("HP", bar)
                    hbox: # "HP" from bar
                        text ("HP") size 20
                        bar value enemy.X_HealthPoints_Current_X range enemy.X_HealthPoints_Max_X xmaximum 150
                    hbox: # "HP" from bar
                        text ("AP") size 20
                        bar value enemy.X_AbilityPoints_Current_X range enemy.X_AbilityPoints_Max_X xmaximum 150
                vbox: # \/ This section is kinda 'debug'.  Heck, most of the frame is.  Comment out the blocks you don't need!
                    hbox:
                        if enemy.Status_Regen_Strength > 0:
                            text (" Regen ") size 20
                        if enemy.Status_Haste_Strength > 0:
                            text (" Haste ") size 20
                        if enemy.Status_Strengthen_Strength > 0:
                            text (" Strength ") size 20
                    hbox:
                        if enemy.Status_Poison_Strength > 0:
                            text (" Poison ") size 20
                        if enemy.Status_Slow_Strength > 0:
                            text (" Slow ") size 20
                        if enemy.Status_Weaken_Strength > 0:
                            text (" Weaken ") size 20
                    hbox:
                        if enemy.Status_Paralyse_Duration > 0:
                            text (" Paralyse ") size 20
                        if enemy.Status_Charm_Duration > 0:
                            text (" Charm ") size 20
                        if enemy.Status_Sleep_Duration > 0:
                            text (" Sleep ") size 20
                      # /\ The end of the 'status block'
            vbox: # Level from (hp/maxhp)
# Removed a level note here, because I don't use levels.  Left it around in case it's needed.
#               text ("Lv. %d" % level) xalign 0.5 size 20
                text (" ") xalign 0.5 size 20
                text ("%d/%d" % (enemy.X_HealthPoints_Current_X, enemy.X_HealthPoints_Max_X)) xalign 0.5 size 20
                text ("%d/%d" % (enemy.X_AbilityPoints_Current_X, enemy.X_AbilityPoints_Max_X)) xalign 0.5 size 20
