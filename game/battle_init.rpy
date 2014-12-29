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
    $ battle = Character("BattleSettings")
    $ battle.roundcount = 0
    $ ename = "FailName"
#####################################################################
# Enemy Init Section
#####################################################################
    $ enemy = Character("Current Foe")
    $ enemy.name = "FailedEnemy"
    $ enemy.battle_selected_action = "battle_Enemy_Wait"
    $ enemy.Attack_List = "Attack_List_Goblin"
# Base Stats - From these, when they're actually added and used, we'll get our base attributes.
#
# Base attributes, to be derived from Stats.. when we add the stats in.
#
# Equipment.. which may be derived.. if we add in equipment properly.
#
#  Equipment - Consumables.  Consider it a 'stock', and will handle the
# potions, grenades, and other one use items and non-rechargables (like wands.)
    $ enemy.Equipment_Consumables_Potions_HP_Restore = 0
#  This block handles status effects, including the check to see if it's on.
# EffectActive is probably going to be used mostly for the Screen/Frame/UI
# stuff.
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
# Enemy's Calculated Attributes
    $ enemy.X_HealthPoints_Current_X = 50
    $ enemy.X_HealthPoints_Max_X = 50
    $ enemy.X_AbilityPoints_Current_X = 30
    $ enemy.X_AbilityPoints_Max_X = 30
    $ enemy.X_WillPoints_Max_X = 0
    $ enemy.X_WillPoints_Current_X = 0
    $ enemy.X_PlaceholderStrength_X = 0
    $ enemy.X_Accuracy_Melee_X = 0
    $ enemy.X_Accuracy_Ranged_X = 0
    $ enemy.X_Armor_Physical_X = 0
    $ enemy.X_Armor_Magic_X = 0
    $ enemy.X_Armor_Will_X = 0
    $ enemy.X_Damage_Melee_Max_X = 0
    $ enemy.X_Damage_Melee_Min_X = 0
    $ enemy.X_Damage_Ranged_Max_X = 0
    $ enemy.X_Damage_Ranged_Min_X = 0
    $ enemy.X_Damage_Magic_Max_X = 0
    $ enemy.X_Damage_Magic_Min_X = 0
    $ enemy.X_Damage_Will_Max_X = 0
    $ enemy.X_Damage_Will_Min_X = 0
    $ enemy.X_Dodge_X = 0
    $ enemy.X_Initiative_X = 0

