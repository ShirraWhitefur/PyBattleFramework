# Shirra's Ren'Py Battle Framework
# https://github.com/ShirraWhitefur/PyBattleFramework
# http://creativecommons.org/licenses/by-nc/3.0/

# Status Effects file!
#  Paralyse, Charm, and Sleep, due to how they interrupt the action flow, will
# stay in battle.rpy as mostly if-else statements.
#  Notably!  Being hit with the same status effect while it's already active
# will overwrite the duration and strength of the original!
#  Checks are in place to make sure you don't get disarmed twice though, but the
# duration can be changed on those as well.
#
#  Paralyse, Charm, and Sleep do _NOT_ currently disallow you from selecting
# actions.. they just set your action to a skipped turn.  Maybe later we'll
# make a more elegant setup, but this is a framework, so.. alas!

#####################################################################
# Status Effects - Player
#####################################################################

label battle_call_Player_Status_Check_Block:
    call battle_call_Player_Status_PoisonCheck
    call battle_call_Player_Status_RegenCheck
    call battle_call_Player_Status_SlowCheck
    call battle_call_Player_Status_HasteCheck
    call battle_call_Player_Status_WeakenCheck
    call battle_call_Player_Status_StrengthenCheck
    call battle_call_Player_Status_Block
    call battle_call_Player_Status_Dodge
    call battle_call_Player_Status_EquipLoss_Weapon_Check
    call battle_call_Player_Status_EquipLoss_UpperBodyArmor_Check
    call battle_call_Player_Status_EquipLoss_LowerBodyArmor_Check
    call battle_call_Player_Status_EquipLoss_Necklace_Check
    call battle_call_Player_Status_EquipLoss_Ring_Check
    return

label battle_call_Player_Status_PoisonCheck:
    if player.Status_Poison_EffectActive == 1:
        if player.Status_Regen_Duration > 0:
            "You are currently poisoned!"
            call battle_call_Player_HP_Loss(player.Status_Poison_Strength)
            $ player.Status_Poison_Duration -= 1
            "You took [player.Status_Poison_Strength] damage from poison.  [playername!t]'s HP at [player.X_HealthPoints_Current_X].  [player.Status_Poison_Duration] rounds of poison remaining."
            return
        if player.Status_Poison_Duration == 0:
            $ player.Status_Poison_EffectActive = 0
            $ player.Status_Poison_Strength = 0
            "You feel the poison fade from your body."
    return

label battle_call_Player_Status_RegenCheck:
    if player.Status_Regen_EffectActive == 1:
        if player.Status_Regen_Duration > 0:
            "You are currently regenerating!"
            call battle_call_Player_HP_Gain(player.Status_Regen_Strength)
            $ player.Status_Regen_Duration -= 1
            "You healed [player.Status_Regen_Strength] damage due to regeneration.  [playername!t]'s HP at [player.X_HealthPoints_Current_X].  [player.Status_Regen_Duration] rounds of Regen remaining."
            return
        if player.Status_Regen_Duration == 0:
            $ player.Status_Regen_EffectActive = 0
            $ player.Status_Regen_Strength = 0
            "You feel the healing effects of Regen fade from your body."
    return

label battle_call_Player_Status_SlowCheck:
    if player.Status_Slow_EffectActive == 1:
        if player.Status_Slow_Duration > 0:
            "You are currently slowed!"
            call battle_call_Player_Dodge_Recheck
            call battle_call_Player_Initiative_Recheck
            $ player.Status_Slow_Duration -= 1
            "Your dodge and initative are [player.Status_Slow_Strength] points worse due to slow.  [player.Status_Slow_Duration] rounds of Slow remaining."
            return
        if player.Status_Slow_Duration == 0:
            $ player.Status_Slow_EffectActive = 0
            $ player.Status_Slow_Strength = 0
            call battle_call_Player_Dodge_Recheck
            call battle_call_Player_Initiative_Recheck
            "You feel yourself speeding up to normal as Slow wears off."
    return

label battle_call_Player_Status_HasteCheck:
    if player.Status_Haste_EffectActive == 1:
        if player.Status_Haste_Duration > 0:
            "You are currently hasted!"
            call battle_call_Player_Dodge_Recheck
            call battle_call_Player_Initiative_Recheck
            $ player.Status_Haste_Duration -= 1
            "Your dodge and initiative are [player.Status_Haste_Strength] points better due to haste.  [player.Status_Haste_Duration] rounds of Haste remaining."
            return
        if player.Status_Haste_Duration == 0:
            $ player.Status_Haste_EffectActive = 0
            $ player.Status_Haste_Strength = 0
            call battle_call_Player_Dodge_Recheck
            call battle_call_Player_Initiative_Recheck
            "You feel yourself slowing down to normal as Haste wears off."
    return

label battle_call_Player_Status_WeakenCheck:
    if player.Status_Weaken_EffectActive == 1:
        if player.Status_Weaken_Duration > 0:
            "You are currently weakened!"
            call battle_call_Player_Damage_Bonus_Recheck
            call battle_call_Player_Weapon_Damage_Recheck
            $ player.Status_Weaken_Duration -= 1
            "You damage is [player.Status_Weaken_Strength] points worse due to weaken.  [player.Status_Weaken_Duration] rounds of Weaken remaining."
            return
        if player.Status_Weaken_Duration == 0:
            $ player.Status_Weaken_EffectActive = 0
            $ player.Status_Weaken_Strength = 0
            call battle_call_Player_Damage_Bonus_Recheck
            call battle_call_Player_Weapon_Damage_Recheck
            "You feel your strength returning to normal as Weaken wears off."
    return

label battle_call_Player_Status_StrengthenCheck:
    if player.Status_Strengthen_EffectActive == 1:
        if player.Status_Strengthen_Duration > 0:
            "You are currently strengthed!"
            call battle_call_Player_Damage_Bonus_Recheck
            call battle_call_Player_Weapon_Damage_Recheck
            $ player.Status_Strengthen_Duration -= 1
            "You damage is [player.Status_Strengthen_Strength] points better due to strengthen.  [player.Status_Strengthen_Duration] rounds of Strengthen remaining."
            return
        if player.Status_Strengthen_Duration == 0:
            $ player.Status_Strengthen_EffectActive = 0
            $ player.Status_Strengthen_Strength = 0
            call battle_call_Player_Damage_Bonus_Recheck
            call battle_call_Player_Weapon_Damage_Recheck
            "You feel your strength returning to normal as Strengthen wears off."
    return

label battle_call_Player_Status_ClumsyCheck:
    if player.Status_Clumsy_EffectActive == 1:
        if player.Status_Clumsy_Duration > 0:
            "You are currently Clumsy!"
            call battle_call_Player_Damage_Bonus_Recheck
            call battle_call_Player_Weapon_Damage_Recheck
            $ player.Status_Clumsy_Duration -= 1
            "You ranged damage is [player.Status_Clumsy_Strength] points worse due to Clumsy.  [player.Status_Clumsy_Duration] rounds of Clumsy remaining."
            return
        if player.Status_Clumsy_Duration == 0:
            $ player.Status_Clumsy_EffectActive = 0
            $ player.Status_Clumsy_Strength = 0
            call battle_call_Player_Damage_Bonus_Recheck
            call battle_call_Player_Weapon_Damage_Recheck
            "You feel your precision returning to normal as Clumsy wears off."
    return

label battle_call_Player_Status_NimbleCheck:
    if player.Status_Nimble_EffectActive == 1:
        if player.Status_Nimble_Duration > 0:
            "You are currently Nimble!"
            call battle_call_Player_Damage_Bonus_Recheck
            call battle_call_Player_Weapon_Damage_Recheck
            $ player.Status_Nimble_Duration -= 1
            "You ranged damage is [player.Status_Nimble_Strength] points better due to Nimble.  [player.Status_Nimble_Duration] rounds of Nimble remaining."
            return
        if player.Status_Nimble_Duration == 0:
            $ player.Status_Nimble_EffectActive = 0
            $ player.Status_Nimble_Strength = 0
            call battle_call_Player_Damage_Bonus_Recheck
            call battle_call_Player_Weapon_Damage_Recheck
            "You feel your precision returning to normal as Nimble wears off."
    return

label battle_call_Player_Status_Block:
    if player.Status_Block_EffectActive == 1:
        $ player.Status_Block_EffectActive = 0
        $ player.Status_Block_Strength = 0
        call battle_call_Player_Armor_Recheck
        "You are no longer actively blocking!"
    return

label battle_call_Player_Status_Dodge:
    if player.Status_Dodge_EffectActive == 1:
        $ player.Status_Dodge_EffectActive = 0
        $ player.Status_Dodge_Strength = 0
        call battle_call_Player_Dodge_Recheck
        "You are no longer actively dodging!"
    return

label battle_call_Player_Status_EquipLoss_Weapon_Check:
    if player.Status_EquipLoss_Weapon_EffectActive == 1:
        if player.Status_EquipLoss_Weapon_Duration > 0:
            "You are currently disarmed!"
            $ player.Status_EquipLoss_Weapon_Duration -= 1
            "You will be disarmed for another [player.Status_EquipLoss_Weapon_Duration] rounds"
            return
        if player.Status_EquipLoss_Weapon_Duration == 0:
            $ player.Status_EquipLoss_Weapon_EffectActive = 0
            $ player.Equipment_Slot_Weapon_Name = player.Equipment_Slot_Weapon_Name_Temp
            call call_Player_Equipment_Slot_Equip_Weapon(player.Equipment_Slot_Weapon_Name)
            "You finally find where your weapon ended up and re-equip it."
    return

label battle_call_Player_Status_EquipLoss_UpperBodyArmor_Check:
    if player.Status_EquipLoss_UpperBodyArmor_EffectActive == 1:
        if player.Status_EquipLoss_UpperBodyArmor_Duration > 0:
            "You are currently missing your upper body armor!"
            $ player.Status_EquipLoss_UpperBodyArmor_Duration -= 1
            "You will be without your upper body armor for another [player.Status_EquipLoss_UpperBodyArmor_Duration] rounds"
            return
        if player.Status_EquipLoss_UpperBodyArmor_Duration == 0:
            $ player.Status_EquipLoss_UpperBodyArmor_EffectActive = 0
            $ player.Equipment_Slot_UpperBodyArmor_Name = player.Equipment_Slot_UpperBodyArmor_Name_Temp
            call call_Player_Equipment_Slot_Equip_UpperBodyArmor(player.Equipment_Slot_UpperBodyArmor_Name)
            "You finally find where your upper body armor ended up and re-equip it."
    return

label battle_call_Player_Status_EquipLoss_LowerBodyArmor_Check:
    if player.Status_EquipLoss_LowerBodyArmor_EffectActive == 1:
        if player.Status_EquipLoss_LowerBodyArmor_Duration > 0:
            "You are currently missing your upper body armor!"
            $ player.Status_EquipLoss_LowerBodyArmor_Duration -= 1
            "You will be without your lower body armor for another [player.Status_EquipLoss_LowerBodyArmor_Duration] rounds"
            return
        if player.Status_EquipLoss_LowerBodyArmor_Duration == 0:
            $ player.Status_EquipLoss_LowerBodyArmor_EffectActive = 0
            $ player.Equipment_Slot_LowerBodyArmor_Name = player.Equipment_Slot_LowerBodyArmor_Name_Temp
            call call_Player_Equipment_Slot_Equip_LowerBodyArmor(player.Equipment_Slot_LowerBodyArmor_Name)
            "You finally find where your upper body armor ended up and re-equip it."
    return

label battle_call_Player_Status_EquipLoss_Necklace_Check:
    if player.Status_EquipLoss_Necklace_EffectActive == 1:
        if player.Status_EquipLoss_Necklace_Duration > 0:
            "You are currently missing your upper body armor!"
            $ player.Status_EquipLoss_Necklace_Duration -= 1
            "You will be without your necklace for another [player.Status_EquipLoss_Necklace_Duration] rounds"
            return
        if player.Status_EquipLoss_Necklace_Duration == 0:
            $ player.Status_EquipLoss_Necklace_EffectActive = 0
            $ player.Equipment_Slot_Necklace_Name = player.Equipment_Slot_Necklace_Name_Temp
            call call_Player_Equipment_Slot_Equip_Necklace(player.Equipment_Slot_Necklace_Name)
            "You finally find where your upper body armor ended up and re-equip it."
    return

label battle_call_Player_Status_EquipLoss_Ring_Check:
    if player.Status_EquipLoss_Ring_EffectActive == 1:
        if player.Status_EquipLoss_Ring_Duration > 0:
            "You are currently missing your upper body armor!"
            $ player.Status_EquipLoss_Ring_Duration -= 1
            "You will be without your ring for another [player.Status_EquipLoss_Ring_Duration] rounds"
            return
        if player.Status_EquipLoss_Ring_Duration == 0:
            $ player.Status_EquipLoss_Ring_EffectActive = 0
            $ player.Equipment_Slot_Ring_Name = player.Equipment_Slot_Ring_Name_Temp
            call call_Player_Equipment_Slot_Equip_Ring(player.Equipment_Slot_Ring_Name)
            "You finally find where your upper body armor ended up and re-equip it."
    return

label battle_call_Player_Status_EquipLoss_Weapon_Remove:
    if player.Status_EquipLoss_Weapon_EffectActive == 0:
        $ player.Equipment_Slot_Weapon_Name_Temp = player.Equipment_Slot_Weapon_Name
        call call_Player_Equipment_Slot_Unequip_Weapon(player.Equipment_Slot_Weapon_Name)
    return

label battle_call_Player_Status_EquipLoss_UpperBodyArmor_Remove:
    if player.Status_EquipLoss_UpperBodyArmor_EffectActive == 0:
        $ player.Equipment_Slot_UpperBodyArmor_Name_Temp = player.Equipment_Slot_UpperBodyArmor_Name
        call call_Player_Equipment_Slot_Unequip_UpperBodyArmor(player.Equipment_Slot_UpperBodyArmor_Name)
    return

label battle_call_Player_Status_EquipLoss_LowerBodyArmor_Remove:
    if player.Status_EquipLoss_LowerBodyArmor_EffectActive == 0:
        $ player.Equipment_Slot_LowerBodyArmor_Name_Temp = player.Equipment_Slot_LowerBodyArmor_Name
        call call_Player_Equipment_Slot_Unequip_LowerBodyArmor(player.Equipment_Slot_LowerBodyArmor_Name)
    return

label battle_call_Player_Status_EquipLoss_Necklace_Remove:
    if player.Status_EquipLoss_Necklace_EffectActive == 0:
        $ player.Equipment_Slot_Necklace_Name_Temp = player.Equipment_Slot_Necklace_Name
        call call_Player_Equipment_Slot_Unequip_Necklace(player.Equipment_Slot_Necklace_Name)
    return

label battle_call_Player_Status_EquipLoss_Ring_Remove:
    if player.Status_EquipLoss_Ring_EffectActive == 0:
        $ player.Equipment_Slot_Ring_Name_Temp = player.Equipment_Slot_Ring_Name
        call call_Player_Equipment_Slot_Unequip_Ring(player.Equipment_Slot_Ring_Name)
    return

#####################################################################
# Status Effects - Enemy
#####################################################################

label battle_call_Enemy_Status_Check_Block:
    call battle_call_Enemy_Status_PoisonCheck
    call battle_call_Enemy_Status_RegenCheck
    call battle_call_Enemy_Status_SlowCheck
    call battle_call_Enemy_Status_HasteCheck
    call battle_call_Enemy_Status_WeakenCheck
    call battle_call_Enemy_Status_StrengthenCheck
    call battle_call_Enemy_Status_Block
    call battle_call_Enemy_Status_Dodge
    call battle_call_Enemy_Status_EquipLoss_Weapon_Check
    call battle_call_Enemy_Status_EquipLoss_UpperBodyArmor_Check
    call battle_call_Enemy_Status_EquipLoss_LowerBodyArmor_Check
    call battle_call_Enemy_Status_EquipLoss_Necklace_Check
    call battle_call_Enemy_Status_EquipLoss_Ring_Check
    return

label battle_call_Enemy_Status_PoisonCheck:
    if enemy.Status_Poison_EffectActive == 1:
        if enemy.Status_Regen_Duration > 0:
            "[enemy.name!t] is currently poisoned!"
            call battle_call_Enemy_HP_Loss(enemy.Status_Poison_Strength)
            $ enemy.Status_Poison_Duration -= 1
            "[enemy.name!t] took [enemy.Status_Poison_Strength] damage from poison.  [enemy.name!t]'s HP at [enemy.X_HealthPoints_Current_X].  [enemy.Status_Poison_Duration] rounds of poison remaining."
            return
        if enemy.Status_Poison_Duration == 0:
            $ enemy.Status_Poison_EffectActive = 0
            $ enemy.Status_Poison_Strength = 0
            "[enemy.name!t] feels the poison fade from their body."
    return

label battle_call_Enemy_Status_RegenCheck:
    if enemy.Status_Regen_EffectActive == 1:
        if enemy.Status_Regen_Duration > 0:
            "[enemy.name!t] is currently regenerating!"
            call battle_call_Enemy_HP_Gain(enemy.Status_Regen_Strength)
            $ enemy.Status_Regen_Duration -= 1
            "[enemy.name!t] healed [enemy.Status_Regen_Strength] damage due to regeneration.  [enemy.name!t]'s HP at [enemy.X_HealthPoints_Current_X].  [enemy.Status_Regen_Duration] rounds of Regen remaining."
            return
        if enemy.Status_Regen_Duration == 0:
            $ enemy.Status_Regen_EffectActive = 0
            $ enemy.Status_Regen_Strength = 0
            "[enemy.name!t] feels the healing effects of Regen fade from their body."
    return

label battle_call_Enemy_Status_SlowCheck:
    if enemy.Status_Slow_EffectActive == 1:
        if enemy.Status_Slow_Duration > 0:
            "[enemy.name!t] is currently slowed!"
            call battle_call_Enemy_Dodge_Recheck
            call battle_call_Enemy_Initiative_Recheck
            $ enemy.Status_Slow_Duration -= 1
            "[enemy.name!t]'s dodge and initative are [enemy.Status_Slow_Strength] points worse due to slow.  [enemy.Status_Slow_Duration] rounds of Slow remaining."
            return
        if enemy.Status_Slow_Duration == 0:
            $ enemy.Status_Slow_EffectActive = 0
            $ enemy.Status_Slow_Strength = 0
            call battle_call_Enemy_Dodge_Recheck
            call battle_call_Enemy_Initiative_Recheck
            "[enemy.name!t] feels themself speeding up to normal as Slow wears off."
    return

label battle_call_Enemy_Status_HasteCheck:
    if enemy.Status_Haste_EffectActive == 1:
        if enemy.Status_Haste_Duration > 0:
            "[enemy.name!t] is currently hasted!"
            call battle_call_Enemy_Dodge_Recheck
            call battle_call_Enemy_Initiative_Recheck
            $ enemy.Status_Haste_Duration -= 1
            "[enemy.name!t]'s dodge and initiative are [enemy.Status_Haste_Strength] points better due to haste.  [enemy.Status_Haste_Duration] rounds of Haste remaining."
            return
        if enemy.Status_Haste_Duration == 0:
            $ enemy.Status_Haste_EffectActive = 0
            $ enemy.Status_Haste_Strength = 0
            call battle_call_Enemy_Dodge_Recheck
            call battle_call_Enemy_Initiative_Recheck
            "[enemy.name!t] feels themself slowing down to normal as Haste wears off."
    return

label battle_call_Enemy_Status_WeakenCheck:
    if enemy.Status_Weaken_EffectActive == 1:
        if enemy.Status_Weaken_Duration > 0:
            "[enemy.name!t] is currently weakened!"
            call battle_call_Enemy_Damage_Bonus_Recheck
            call battle_call_Enemy_Weapon_Damage_Recheck
            $ enemy.Status_Weaken_Duration -= 1
            "[enemy.name!t]'s damage is [enemy.Status_Weaken_Strength] points worse due to weaken.  [enemy.Status_Weaken_Duration] rounds of Weaken remaining."
            return
        if enemy.Status_Weaken_Duration == 0:
            $ enemy.Status_Weaken_EffectActive = 0
            $ enemy.Status_Weaken_Strength = 0
            call battle_call_Enemy_Damage_Bonus_Recheck
            call battle_call_Enemy_Weapon_Damage_Recheck
            "[enemy.name!t] feels their strength returning to normal as Weaken wears off."
    return

label battle_call_Enemy_Status_StrengthenCheck:
    if enemy.Status_Strengthen_EffectActive == 1:
        if enemy.Status_Strengthen_Duration > 0:
            "[enemy.name!t] is currently strengthed!"
            call battle_call_Enemy_Damage_Bonus_Recheck
            call battle_call_Enemy_Weapon_Damage_Recheck
            $ enemy.Status_Strengthen_Duration -= 1
            "[enemy.name!t]'s damage is [enemy.Status_Strengthen_Strength] points better due to strengthen.  [enemy.Status_Strengthen_Duration] rounds of Strengthen remaining."
            return
        if enemy.Status_Strengthen_Duration == 0:
            $ enemy.Status_Strengthen_EffectActive = 0
            $ enemy.Status_Strengthen_Strength = 0
            call battle_call_Enemy_Damage_Bonus_Recheck
            call battle_call_Enemy_Weapon_Damage_Recheck
            "[enemy.name!t] feel their strength returning to normal as Strengthen wears off."
    return

label battle_call_Enemy_Status_Block:
    if enemy.Status_Block_EffectActive == 1:
        $ enemy.Status_Block_EffectActive = 0
        $ enemy.Status_Block_Strength = 0
        call battle_call_Enemy_Armor_Recheck
        "[enemy.name!t] is no longer actively blocking!"
    return

label battle_call_Enemy_Status_Dodge:
    if enemy.Status_Dodge_EffectActive == 1:
        $ enemy.Status_Dodge_EffectActive = 0
        $ enemy.Status_Dodge_Strength = 0
        call battle_call_Enemy_Dodge_Recheck
        "[enemy.name!t] is no longer actively dodging!"
    return

label battle_call_Enemy_Status_EquipLoss_Weapon_Check:
    if enemy.Status_EquipLoss_Weapon_EffectActive == 1:
        if enemy.Status_EquipLoss_Weapon_Duration > 0:
            "[enemy.name!t] is currently disarmed!"
            $ enemy.Status_EquipLoss_Weapon_Duration -= 1
            "[enemy.name!t] will be disarmed for another [enemy.Status_EquipLoss_Weapon_Duration] rounds"
            return
        if enemy.Status_EquipLoss_Weapon_Duration == 0:
            $ enemy.Status_EquipLoss_Weapon_EffectActive = 0
            $ enemy.Equipment_Slot_Weapon_Name = enemy.Equipment_Slot_Weapon_Name_Temp
            call call_Enemy_Equipment_Slot_Equip_Weapon(enemy.Equipment_Slot_Weapon_Name)
            "[enemy.name!t] finally finds where their weapon ended up and re-equip it."
    return

label battle_call_Enemy_Status_EquipLoss_UpperBodyArmor_Check:
    if enemy.Status_EquipLoss_UpperBodyArmor_EffectActive == 1:
        if enemy.Status_EquipLoss_UpperBodyArmor_Duration > 0:
            "[enemy.name!t] is currently missing their upper body armor!"
            $ enemy.Status_EquipLoss_UpperBodyArmor_Duration -= 1
            "[enemy.name!t] will be without their upper body armor for another [enemy.Status_EquipLoss_UpperBodyArmor_Duration] rounds"
            return
        if enemy.Status_EquipLoss_UpperBodyArmor_Duration == 0:
            $ enemy.Status_EquipLoss_UpperBodyArmor_EffectActive = 0
            $ enemy.Equipment_Slot_UpperBodyArmor_Name = enemy.Equipment_Slot_UpperBodyArmor_Name_Temp
            call call_Enemy_Equipment_Slot_Equip_UpperBodyArmor(enemy.Equipment_Slot_UpperBodyArmor_Name)
            "[enemy.name!t] finally finds where their upper body armor ended up and re-equip it."
    return

label battle_call_Enemy_Status_EquipLoss_LowerBodyArmor_Check:
    if enemy.Status_EquipLoss_LowerBodyArmor_EffectActive == 1:
        if enemy.Status_EquipLoss_LowerBodyArmor_Duration > 0:
            "[enemy.name!t] is currently missing their upper body armor!"
            $ enemy.Status_EquipLoss_LowerBodyArmor_Duration -= 1
            "[enemy.name!t] will be without their lower body armor for another [enemy.Status_EquipLoss_LowerBodyArmor_Duration] rounds"
            return
        if enemy.Status_EquipLoss_LowerBodyArmor_Duration == 0:
            $ enemy.Status_EquipLoss_LowerBodyArmor_EffectActive = 0
            $ enemy.Equipment_Slot_LowerBodyArmor_Name = enemy.Equipment_Slot_LowerBodyArmor_Name_Temp
            call call_Enemy_Equipment_Slot_Equip_LowerBodyArmor(enemy.Equipment_Slot_LowerBodyArmor_Name)
            "[enemy.name!t] finally finds where their upper body armor ended up and re-equip it."
    return

label battle_call_Enemy_Status_EquipLoss_Necklace_Check:
    if enemy.Status_EquipLoss_Necklace_EffectActive == 1:
        if enemy.Status_EquipLoss_Necklace_Duration > 0:
            "[enemy.name!t] is currently missing their upper body armor!"
            $ enemy.Status_EquipLoss_Necklace_Duration -= 1
            "[enemy.name!t] will be without their necklace for another [enemy.Status_EquipLoss_Necklace_Duration] rounds"
            return
        if enemy.Status_EquipLoss_Necklace_Duration == 0:
            $ enemy.Status_EquipLoss_Necklace_EffectActive = 0
            $ enemy.Equipment_Slot_Necklace_Name = enemy.Equipment_Slot_Necklace_Name_Temp
            call call_Enemy_Equipment_Slot_Equip_Necklace(enemy.Equipment_Slot_Necklace_Name)
            "[enemy.name!t] finally finds where their upper body armor ended up and re-equip it."
    return

label battle_call_Enemy_Status_EquipLoss_Ring_Check:
    if enemy.Status_EquipLoss_Ring_EffectActive == 1:
        if enemy.Status_EquipLoss_Ring_Duration > 0:
            "[enemy.name!t] is currently missing their upper body armor!"
            $ enemy.Status_EquipLoss_Ring_Duration -= 1
            "[enemy.name!t] will be without their ring for another [enemy.Status_EquipLoss_Ring_Duration] rounds"
            return
        if enemy.Status_EquipLoss_Ring_Duration == 0:
            $ enemy.Status_EquipLoss_Ring_EffectActive = 0
            $ enemy.Equipment_Slot_Ring_Name = enemy.Equipment_Slot_Ring_Name_Temp
            call call_Enemy_Equipment_Slot_Equip_Ring(enemy.Equipment_Slot_Ring_Name)
            "[enemy.name!t] finally finds where their upper body armor ended up and re-equip it."
    return

label battle_call_Enemy_Status_EquipLoss_Weapon_Remove:
    if enemy.Status_EquipLoss_Weapon_EffectActive == 0:
        $ enemy.Equipment_Slot_Weapon_Name_Temp = enemy.Equipment_Slot_Weapon_Name
        call call_Enemy_Equipment_Slot_Unequip_Weapon(enemy.Equipment_Slot_Weapon_Name)
    return

label battle_call_Enemy_Status_EquipLoss_UpperBodyArmor_Remove:
    if enemy.Status_EquipLoss_UpperBodyArmor_EffectActive == 0:
        $ enemy.Equipment_Slot_UpperBodyArmor_Name_Temp = enemy.Equipment_Slot_UpperBodyArmor_Name
        call call_Enemy_Equipment_Slot_Unequip_UpperBodyArmor(enemy.Equipment_Slot_UpperBodyArmor_Name)
    return

label battle_call_Enemy_Status_EquipLoss_LowerBodyArmor_Remove:
    if enemy.Status_EquipLoss_LowerBodyArmor_EffectActive == 0:
        $ enemy.Equipment_Slot_LowerBodyArmor_Name_Temp = enemy.Equipment_Slot_LowerBodyArmor_Name
        call call_Enemy_Equipment_Slot_Unequip_LowerBodyArmor(enemy.Equipment_Slot_LowerBodyArmor_Name)
    return

label battle_call_Enemy_Status_EquipLoss_Necklace_Remove:
    if enemy.Status_EquipLoss_Necklace_EffectActive == 0:
        $ enemy.Equipment_Slot_Necklace_Name_Temp = enemy.Equipment_Slot_Necklace_Name
        call call_Enemy_Equipment_Slot_Unequip_Necklace(enemy.Equipment_Slot_Necklace_Name)
    return

label battle_call_Enemy_Status_EquipLoss_Ring_Remove:
    if enemy.Status_EquipLoss_Ring_EffectActive == 0:
        $ enemy.Equipment_Slot_Ring_Name_Temp = enemy.Equipment_Slot_Ring_Name
        call call_Enemy_Equipment_Slot_Unequip_Ring(enemy.Equipment_Slot_Ring_Name)
    return
