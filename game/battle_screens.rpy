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
                        bar value player.hp_c range player.hp_m xmaximum 150
                    hbox: # "HP" from bar
                        text ("AP") size 20
                        bar value player.ap_c range player.ap_m xmaximum 150
                vbox: # \/ This section is kinda 'debug'.  Heck, most of the frame is.  Comment out the blocks you don't need!
                    hbox:
                        if player.status_regen_strength > 0:
                            text (" Regen ") size 20
                        if player.status_haste_strength > 0:
                            text (" Haste ") size 20
                        if player.status_strengthen_strength > 0:
                            text (" Strength ") size 20
                    hbox:
                        if player.status_poison_strength > 0:
                            text (" Poison ") size 20
                        if player.status_slow_strength > 0:
                            text (" Slow ") size 20
                        if player.status_weaken_strength > 0:
                            text (" Weaken ") size 20
                    hbox:
                        if player.status_paralyse_duration > 0:
                            text (" Paralyse ") size 20
                        if player.status_charm_duration > 0:
                            text (" Charm ") size 20
                        if player.status_sleep_duration > 0:
                            text (" Sleep ") size 20
                      # /\ The end of the 'status block'
            vbox: # Level from (hp/maxhp)
# Removed a level note here, because I don't use levels.  Left it around in case it's needed.
#               text ("Lv. %d" % level) xalign 0.5 size 20
                text (" ") xalign 0.5 size 20
                text ("%d/%d" % (player.hp_c, player.hp_m)) xalign 0.5 size 20
                text ("%d/%d" % (player.ap_c, player.ap_m)) xalign 0.5 size 20

screen stats_frame2(ename):
    frame xfill(False) yminimum(None) background(None) xalign 0.98 yalign 0.05:
        hbox: # (name, "HP", bar) from (level, hp, maxhp)
            vbox: # name from ("HP", bar)
                text (ename) size 20
                vbox: # name from ("HP", bar)
                    hbox: # "HP" from bar
                        text ("HP") size 20
                        bar value enemy.hp_c range enemy.hp_m xmaximum 150
                    hbox: # "HP" from bar
                        text ("AP") size 20
                        bar value enemy.ap_c range enemy.ap_m xmaximum 150
                vbox: # \/ This section is kinda 'debug'.  Heck, most of the frame is.  Comment out the blocks you don't need!
                    hbox:
                        if enemy.status_regen_strength > 0:
                            text (" Regen ") size 20
                        if enemy.status_haste_strength > 0:
                            text (" Haste ") size 20
                        if enemy.status_strengthen_strength > 0:
                            text (" Strength ") size 20
                    hbox:
                        if enemy.status_poison_strength > 0:
                            text (" Poison ") size 20
                        if enemy.status_slow_strength > 0:
                            text (" Slow ") size 20
                        if enemy.status_weaken_strength > 0:
                            text (" Weaken ") size 20
                    hbox:
                        if enemy.status_paralyse_duration > 0:
                            text (" Paralyse ") size 20
                        if enemy.status_charm_duration > 0:
                            text (" Charm ") size 20
                        if enemy.status_sleep_duration > 0:
                            text (" Sleep ") size 20
                      # /\ The end of the 'status block'
            vbox: # Level from (hp/maxhp)
# Removed a level note here, because I don't use levels.  Left it around in case it's needed.
#               text ("Lv. %d" % level) xalign 0.5 size 20
                text (" ") xalign 0.5 size 20
                text ("%d/%d" % (enemy.hp_c, enemy.hp_m)) xalign 0.5 size 20
                text ("%d/%d" % (enemy.ap_c, enemy.ap_m)) xalign 0.5 size 20
