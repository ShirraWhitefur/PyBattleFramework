#  Realize that we need to initialize a whole mess of variables for this system to work nicely
# and that any enemy is going to need his own full set.  Likely, we'll be putting each enemy's
# init set into his own file though, to keep things tidy.
#  Also, anything with .* style variables on it is being set up as a character because.. well
# it's the only way I could make it work.  So yes.  Battle is a character.

# The following init python section is from Asceai on the forums - ' http://lemmasoft.renai.us/forums/viewtopic.php?p=323010#p323010 '
init python:
    def WeightedChoice(choices):
        """
        @param choices: A list of (choice, weight) tuples. Returns a random
        choice (using renpy.random as the random number generator)
        """
        totalweight = 0.0
        for choice, weight in choices:
            totalweight += weight
        randval = renpy.random.random() * totalweight
        for choice, weight in choices:
            if randval <= weight:
                return choice
            else:
                randval -= weight

init:
    $ player = DynamicCharacter("playername", color=(192, 64, 64, 255))
    $ playername = "Fail"
    $ playernametemp = playername
    $ player.hp_c = 200
    $ player.hp_m = 200
    $ player.ap_c = 100
    $ player.ap_m = 100
    $ player.damage_melee_max = 12
    $ player.damage_melee_min = 2
    $ player.armor = 2
    $ player.accuracy_melee = 15
    $ player.dodge = 14
    $ player.initiative_mod = 15
    $ player.exp = 0
    $ player.items_potions_hp = 3
    $ player.items_potions_ap = 2
    $ player.roll_attack = 0
    $ player.roll_damage = 0
    $ player.roll_damage_final = 0
    $ player.roll_initiative = 0
    $ player.battle_selected_action = "battle_Player_Wait"
    $ player.status_poison_duration = 0
    $ player.status_poison_strength = 0
    $ player.status_regen_duration = 0
    $ player.status_regen_strength = 0
    $ player.status_slow_duration = 0
    $ player.status_slow_strength = 0
    $ player.status_haste_duration = 0
    $ player.status_haste_strength = 0
    $ player.status_weaken_duration = 0
    $ player.status_weaken_strength = 0
    $ player.status_strengthen_duration = 0
    $ player.status_strengthen_strength = 0
    $ player.status_paralyse_duration = 0
    $ player.status_charm_duration = 0
    $ player.status_sleep_duration = 0
    $ player.initiative_mod_temp = 0
    $ player.dodge_temp = 0
    $ player.damage_melee_max_temp = 0
    $ player.damage_melee_min_temp = 0
    $ enemy = Character("Current Foe")
    $ enemy.name = "FailedGoblin"
    $ enemy.hp_c = 50
    $ enemy.hp_m = 50
    $ enemy.ap_c = 30
    $ enemy.ap_m = 30
    $ enemy.attack_list = "Attack_List_Goblin"
    $ enemy.damage_melee_max = 5
    $ enemy.damage_melee_min = 1
    $ enemy.armor = 3
    $ enemy.accuracy_melee = 7
    $ enemy.dodge = 6
    $ enemy.initiative_mod = 1
    $ enemy.items_potions_hp = 0
    $ enemy.roll_attack = 0
    $ enemy.roll_damage = 0
    $ enemy.roll_damage_final = 0
    $ enemy.roll_initiative = 0
    $ enemy.battle_selected_action = "battle_Enemy_Wait"
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
    $ ename = "Fail"
    $ battle = Character("BattleSettings")
    $ battle.roundcount = 0
