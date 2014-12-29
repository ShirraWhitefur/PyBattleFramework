#####################################################################
# Equipment
#####################################################################
#  For now, these will have to be per slot.  Because reasons that totally have
# to do with rubber hose, and not my lack of coding skill.  Really.
#
#    call call_Equipment_Slot_Equip_UpperBodyArmor(battle.EquipGearName)
#    call call_Equipment_Slot_Unquip_UpperBodyArmor(player.Equipment_Slot_UpperBodyArmor_Name)
# and if out of combat..
#    call battle_call_Player_HP_AP_WP_Current_to_Max_Set
# afterwards, to bring your totals in line.

# Init to replicate the ename initial setup from battle_init.rpy
init:
    $ eweaponname = "FailedWeapon"

#  This one is best right at very game start, putting your initially selected
# gear (or no gear) into the player's slots, and getting the equipment system
# set up and started.  Alternatively, if you're starting them with no gear, you
# might want to just use call_Player_Equipment_Slot_Strip_All instead?
label call_Player_Equipment_Slot_Initialize_All:
    $ player.Equipment_HealthPoints_Max = 0
    $ player.Equipment_AbilityPoints_Max = 0
    $ player.Equipment_WillPoints_Max = 0
    $ player.Equipment_Accuracy_Melee = 0
    $ player.Equipment_Accuracy_Ranged = 0
    $ player.Equipment_Armor_Physical = 0
    $ player.Equipment_Armor_Magic = 0
    $ player.Equipment_Armor_Will = 0
    $ player.Equipment_Damage_Bonus_Melee_Max = 0
    $ player.Equipment_Damage_Bonus_Ranged_Max = 0
    $ player.Equipment_Damage_Bonus_Magic_Max = 0
    $ player.Equipment_Damage_Bonus_Will_Max = 0
    $ player.Equipment_Dodge = 0
    $ player.Equipment_Initiative = 0
    call call_Player_Equipment_Slot_Equip_Weapon(player.Equipment_Slot_Weapon_Name)
    call call_Player_Equipment_Slot_Equip_UpperBodyArmor(player.Equipment_Slot_UpperBodyArmor_Name)
    call call_Player_Equipment_Slot_Equip_LowerBodyArmor(player.Equipment_Slot_LowerBodyArmor_Name)
    call call_Player_Equipment_Slot_Equip_Necklace(player.Equipment_Slot_Necklace_Name)
    call call_Player_Equipment_Slot_Equip_Ring(player.Equipment_Slot_Ring_Name)
    call battle_call_Player_Full_Recheck
    return

#  So, your player just woke up after being captured by slavers?  Lets get rid
# of all that pesky equipment!
label call_Player_Equipment_Slot_Strip_All:
    $ player.Equipment_HealthPoints_Max = 0
    $ player.Equipment_AbilityPoints_Max = 0
    $ player.Equipment_WillPoints_Max = 0
    $ player.Equipment_Accuracy_Melee = 0
    $ player.Equipment_Accuracy_Ranged = 0
    $ player.Equipment_Armor_Physical = 0
    $ player.Equipment_Armor_Magic = 0
    $ player.Equipment_Armor_Will = 0
    $ player.Equipment_Damage_Bonus_Melee_Max = 0
    $ player.Equipment_Damage_Bonus_Ranged_Max = 0
    $ player.Equipment_Damage_Bonus_Magic_Max = 0
    $ player.Equipment_Damage_Bonus_Will_Max = 0
    $ player.Equipment_Dodge = 0
    $ player.Equipment_Initiative = 0
    $ player.Equipment_Weapon_Accuracy_Melee = no_weapon.Equipment_Weapon_Accuracy_Melee
    $ player.Equipment_Weapon_Accuracy_Ranged = no_weapon.Equipment_Weapon_Accuracy_Ranged
    $ player.Equipment_Weapon_Damage_Melee_Max = no_weapon.Equipment_Weapon_Damage_Melee_Max
    $ player.Equipment_Weapon_Damage_Melee_Min = no_weapon.Equipment_Weapon_Damage_Melee_Min
    $ player.Equipment_Weapon_Damage_Ranged_Max = no_weapon.Equipment_Weapon_Damage_Ranged_Max
    $ player.Equipment_Weapon_Damage_Ranged_Min = no_weapon.Equipment_Weapon_Damage_Ranged_Min
    $ player.Equipment_Weapon_Damage_Magic_Max = no_weapon.Equipment_Weapon_Damage_Magic_Max
    $ player.Equipment_Weapon_Damage_Magic_Min = no_weapon.Equipment_Weapon_Damage_Magic_Min
    $ player.Equipment_Weapon_Damage_Will_Max = no_weapon.Equipment_Weapon_Damage_Will_Max
    $ player.Equipment_Weapon_Damage_Will_Min = no_weapon.Equipment_Weapon_Damage_Will_Min
    $ player.Equipment_Slot_Weapon_Name = "no_weapon"
    $ player.Equipment_Slot_Weapon_Name_Text = no_weapon.Equipment_Slot_Weapon_Name_Text
    $ player.Equipment_Slot_Weapon_Accuracy_Type = no_weapon.Equipment_Slot_Weapon_Accuracy_Type
    $ player.Equipment_Slot_Weapon_Damage_Type = no_weapon.Equipment_Slot_Weapon_Damage_Type
    $ player.Equipment_Slot_UpperBodyArmor_Name = "no_upper_armor"
    $ player.Equipment_Slot_UpperBodyArmor_Name_Text = no_upper_armor.Equipment_Slot_UpperBodyArmor_Name_Text
    $ player.Equipment_Slot_LowerBodyArmor_Name = "no_lower_armor"
    $ player.Equipment_Slot_LowerBodyArmor_Name_Text = no_lower_armor.Equipment_Slot_LowerBodyArmor_Name_Text
    $ player.Equipment_Slot_Necklace_Name = "no_necklace"
    $ player.Equipment_Slot_Necklace_Name_Text = no_necklace.Equipment_Slot_Necklace_Name_Text
    $ player.Equipment_Slot_Ring_Name = "no_ring"
    $ player.Equipment_Slot_Ring_Name_Text = no_ring.Equipment_Slot_Ring_Name_Text
    call battle_call_Player_Full_Recheck
    return

label call_Player_Equipment_Slot_Equip_Weapon(weaponname):
    $ player.Equipment_HealthPoints_Max += weaponname.Equipment_HealthPoints_Max
    $ player.Equipment_AbilityPoints_Max += weaponname.Equipment_AbilityPoints_Max
    $ player.Equipment_WillPoints_Max += weaponname.Equipment_WillPoints_Max
    $ player.Equipment_Accuracy_Melee += weaponname.Equipment_Accuracy_Melee
    $ player.Equipment_Accuracy_Ranged += weaponname.Equipment_Accuracy_Ranged
    $ player.Equipment_Armor_Physical += weaponname.Equipment_Armor_Physical
    $ player.Equipment_Armor_Magic += weaponname.Equipment_Armor_Magic
    $ player.Equipment_Armor_Will += weaponname.Equipment_Armor_Will
    $ player.Equipment_Damage_Bonus_Melee_Max += weaponname.Equipment_Damage_Bonus_Melee_Max
    $ player.Equipment_Damage_Bonus_Ranged_Max += weaponname.Equipment_Damage_Bonus_Ranged_Max
    $ player.Equipment_Damage_Bonus_Magic_Max += weaponname.Equipment_Damage_Bonus_Magic_Max
    $ player.Equipment_Damage_Bonus_Will_Max += weaponname.Equipment_Damage_Bonus_Will_Max
    $ player.Equipment_Dodge += weaponname.Equipment_Dodge
    $ player.Equipment_Initiative += weaponname.Equipment_Initiative
    $ player.Equipment_Weapon_Accuracy_Melee = weaponname.Equipment_Weapon_Accuracy_Melee
    $ player.Equipment_Weapon_Accuracy_Ranged = weaponname.Equipment_Weapon_Accuracy_Ranged
    $ player.Equipment_Weapon_Damage_Melee_Max = weaponname.Equipment_Weapon_Damage_Melee_Max
    $ player.Equipment_Weapon_Damage_Melee_Min = weaponname.Equipment_Weapon_Damage_Melee_Min
    $ player.Equipment_Weapon_Damage_Ranged_Max = weaponname.Equipment_Weapon_Damage_Ranged_Max
    $ player.Equipment_Weapon_Damage_Ranged_Min = weaponname.Equipment_Weapon_Damage_Ranged_Min
    $ player.Equipment_Weapon_Damage_Magic_Max = weaponname.Equipment_Weapon_Damage_Magic_Max
    $ player.Equipment_Weapon_Damage_Magic_Min = weaponname.Equipment_Weapon_Damage_Magic_Min
    $ player.Equipment_Weapon_Damage_Will_Max = weaponname.Equipment_Weapon_Damage_Will_Max
    $ player.Equipment_Weapon_Damage_Will_Min = weaponname.Equipment_Weapon_Damage_Will_Min
    $ player.Equipment_Slot_Weapon_Name = weaponname.Equipment_Slot_Weapon_Name
    $ player.Equipment_Slot_Weapon_Name_Text = weaponname.Equipment_Slot_Weapon_Name_Text
    $ player.Equipment_Slot_Weapon_Accuracy_Type = weaponname.Equipment_Slot_Weapon_Accuracy_Type
    $ player.Equipment_Slot_Weapon_Damage_Type = weaponname.Equipment_Slot_Weapon_Damage_Type
    call battle_call_Player_Full_Recheck
    return

label call_Player_Equipment_Slot_Unquip_Weapon(weaponname):
    $ player.Equipment_HealthPoints_Max -= weaponname.Equipment_HealthPoints_Max
    $ player.Equipment_AbilityPoints_Max -= weaponname.Equipment_AbilityPoints_Max
    $ player.Equipment_WillPoints_Max -= weaponname.Equipment_WillPoints_Max
    $ player.Equipment_Accuracy_Melee -= weaponname.Equipment_Accuracy_Melee
    $ player.Equipment_Accuracy_Ranged -= weaponname.Equipment_Accuracy_Ranged
    $ player.Equipment_Armor_Physical -= weaponname.Equipment_Armor_Physical
    $ player.Equipment_Armor_Magic -= weaponname.Equipment_Armor_Magic
    $ player.Equipment_Armor_Will -= weaponname.Equipment_Armor_Will
    $ player.Equipment_Damage_Bonus_Melee_Max -= weaponname.Equipment_Damage_Bonus_Melee_Max
    $ player.Equipment_Damage_Bonus_Ranged_Max -= weaponname.Equipment_Damage_Bonus_Ranged_Max
    $ player.Equipment_Damage_Bonus_Magic_Max -= weaponname.Equipment_Damage_Bonus_Magic_Max
    $ player.Equipment_Damage_Bonus_Will_Max -= weaponname.Equipment_Damage_Bonus_Will_Max
    $ player.Equipment_Dodge -= weaponname.Equipment_Dodge
    $ player.Equipment_Initiative -= weaponname.Equipment_Initiative
    $ player.Equipment_Weapon_Accuracy_Melee = no_weapon.Equipment_Weapon_Accuracy_Melee
    $ player.Equipment_Weapon_Accuracy_Ranged = no_weapon.Equipment_Weapon_Accuracy_Ranged
    $ player.Equipment_Weapon_Damage_Melee_Max = no_weapon.Equipment_Weapon_Damage_Melee_Max
    $ player.Equipment_Weapon_Damage_Melee_Min = no_weapon.Equipment_Weapon_Damage_Melee_Min
    $ player.Equipment_Weapon_Damage_Ranged_Max = no_weapon.Equipment_Weapon_Damage_Ranged_Max
    $ player.Equipment_Weapon_Damage_Ranged_Min = no_weapon.Equipment_Weapon_Damage_Ranged_Min
    $ player.Equipment_Weapon_Damage_Magic_Max = no_weapon.Equipment_Weapon_Damage_Magic_Max
    $ player.Equipment_Weapon_Damage_Magic_Min = no_weapon.Equipment_Weapon_Damage_Magic_Min
    $ player.Equipment_Weapon_Damage_Will_Max = no_weapon.Equipment_Weapon_Damage_Will_Max
    $ player.Equipment_Weapon_Damage_Will_Min = no_weapon.Equipment_Weapon_Damage_Will_Min
    $ player.Equipment_Slot_Weapon_Name = "no_weapon"
    $ player.Equipment_Slot_Weapon_Name_Text = no_weapon.Equipment_Slot_Weapon_Name_Text
    $ player.Equipment_Slot_Weapon_Accuracy_Type = no_weapon.Equipment_Slot_Weapon_Accuracy_Type
    $ player.Equipment_Slot_Weapon_Damage_Type = no_weapon.Equipment_Slot_Weapon_Damage_Type
    call battle_call_Player_Full_Recheck
    return

label call_Player_Equipment_Slot_Equip_UpperBodyArmor(upperbodyarmorname):
    $ player.Equipment_HealthPoints_Max += upperbodyarmorname.Equipment_HealthPoints_Max
    $ player.Equipment_AbilityPoints_Max += upperbodyarmorname.Equipment_AbilityPoints_Max
    $ player.Equipment_WillPoints_Max += upperbodyarmorname.Equipment_WillPoints_Max
    $ player.Equipment_Accuracy_Melee += upperbodyarmorname.Equipment_Accuracy_Melee
    $ player.Equipment_Accuracy_Ranged += upperbodyarmorname.Equipment_Accuracy_Ranged
    $ player.Equipment_Armor_Physical += upperbodyarmorname.Equipment_Armor_Physical
    $ player.Equipment_Armor_Magic += upperbodyarmorname.Equipment_Armor_Magic
    $ player.Equipment_Armor_Will += upperbodyarmorname.Equipment_Armor_Will
    $ player.Equipment_Damage_Bonus_Melee_Max += upperbodyarmorname.Equipment_Damage_Bonus_Melee_Max
    $ player.Equipment_Damage_Bonus_Ranged_Max += upperbodyarmorname.Equipment_Damage_Bonus_Ranged_Max
    $ player.Equipment_Damage_Bonus_Magic_Max += upperbodyarmorname.Equipment_Damage_Bonus_Magic_Max
    $ player.Equipment_Damage_Bonus_Will_Max += upperbodyarmorname.Equipment_Damage_Bonus_Will_Max
    $ player.Equipment_Dodge += upperbodyarmorname.Equipment_Dodge
    $ player.Equipment_Initiative += upperbodyarmorname.Equipment_Initiative
    $ player.Equipment_Slot_UpperBodyArmor_Name = upperbodyarmorname.Equipment_Slot_Necklace_Name
    $ player.Equipment_Slot_UpperBodyArmor_Name_Text = upperbodyarmorname.Equipment_Slot_UpperBodyArmor_Name_Text
    call battle_call_Player_Full_Recheck
    return

label call_Player_Equipment_Slot_Unequip_UpperBodyArmor(upperbodyarmorname):
    $ player.Equipment_HealthPoints_Max -= upperbodyarmorname.Equipment_HealthPoints_Max
    $ player.Equipment_AbilityPoints_Max -= upperbodyarmorname.Equipment_AbilityPoints_Max
    $ player.Equipment_WillPoints_Max -= upperbodyarmorname.Equipment_WillPoints_Max
    $ player.Equipment_Accuracy_Melee -= upperbodyarmorname.Equipment_Accuracy_Melee
    $ player.Equipment_Accuracy_Ranged -= upperbodyarmorname.Equipment_Accuracy_Ranged
    $ player.Equipment_Armor_Physical -= upperbodyarmorname.Equipment_Armor_Physical
    $ player.Equipment_Armor_Magic -= upperbodyarmorname.Equipment_Armor_Magic
    $ player.Equipment_Armor_Will -= upperbodyarmorname.Equipment_Armor_Will
    $ player.Equipment_Damage_Bonus_Melee_Max -= upperbodyarmorname.Equipment_Damage_Bonus_Melee_Max
    $ player.Equipment_Damage_Bonus_Ranged_Max -= upperbodyarmorname.Equipment_Damage_Bonus_Ranged_Max
    $ player.Equipment_Damage_Bonus_Magic_Max -= upperbodyarmorname.Equipment_Damage_Bonus_Magic_Max
    $ player.Equipment_Damage_Bonus_Will_Max -= upperbodyarmorname.Equipment_Damage_Bonus_Will_Max
    $ player.Equipment_Dodge -= upperbodyarmorname.Equipment_Dodge
    $ player.Equipment_Initiative -= upperbodyarmorname.Equipment_Initiative
    $ player.Equipment_Slot_UpperBodyArmor_Name = "no_upper_armor"
    $ player.Equipment_Slot_UpperBodyArmor_Name_Text = no_upper_armor.Equipment_Slot_UpperBodyArmor_Name_Text
    call battle_call_Player_Full_Recheck
    return

label call_Player_Equipment_Slot_Equip_LowerBodyArmor(lowerbodyarmorname):
    $ player.Equipment_HealthPoints_Max += lowerbodyarmorname.Equipment_HealthPoints_Max
    $ player.Equipment_AbilityPoints_Max += lowerbodyarmorname.Equipment_AbilityPoints_Max
    $ player.Equipment_WillPoints_Max += lowerbodyarmorname.Equipment_WillPoints_Max
    $ player.Equipment_Accuracy_Melee += lowerbodyarmorname.Equipment_Accuracy_Melee
    $ player.Equipment_Accuracy_Ranged += lowerbodyarmorname.Equipment_Accuracy_Ranged
    $ player.Equipment_Armor_Physical += lowerbodyarmorname.Equipment_Armor_Physical
    $ player.Equipment_Armor_Magic += lowerbodyarmorname.Equipment_Armor_Magic
    $ player.Equipment_Armor_Will += lowerbodyarmorname.Equipment_Armor_Will
    $ player.Equipment_Damage_Bonus_Melee_Max += lowerbodyarmorname.Equipment_Damage_Bonus_Melee_Max
    $ player.Equipment_Damage_Bonus_Ranged_Max += lowerbodyarmorname.Equipment_Damage_Bonus_Ranged_Max
    $ player.Equipment_Damage_Bonus_Magic_Max += lowerbodyarmorname.Equipment_Damage_Bonus_Magic_Max
    $ player.Equipment_Damage_Bonus_Will_Max += lowerbodyarmorname.Equipment_Damage_Bonus_Will_Max
    $ player.Equipment_Dodge += lowerbodyarmorname.Equipment_Dodge
    $ player.Equipment_Initiative += lowerbodyarmorname.Equipment_Initiative
    $ player.Equipment_Slot_LowerBodyArmor_Name = lowerbodyarmorname.Equipment_Slot_Necklace_Name
    $ player.Equipment_Slot_LowerBodyArmor_Name_Text = lowerbodyarmorname.Equipment_Slot_LowerBodyArmor_Name_Text
    call battle_call_Player_Full_Recheck
    return

label call_Player_Equipment_Slot_Unequip_LowerBodyArmor(lowerbodyarmorname):
    $ player.Equipment_HealthPoints_Max -= lowerbodyarmorname.Equipment_HealthPoints_Max
    $ player.Equipment_AbilityPoints_Max -= lowerbodyarmorname.Equipment_AbilityPoints_Max
    $ player.Equipment_WillPoints_Max -= lowerbodyarmorname.Equipment_WillPoints_Max
    $ player.Equipment_Accuracy_Melee -= lowerbodyarmorname.Equipment_Accuracy_Melee
    $ player.Equipment_Accuracy_Ranged -= lowerbodyarmorname.Equipment_Accuracy_Ranged
    $ player.Equipment_Armor_Physical -= lowerbodyarmorname.Equipment_Armor_Physical
    $ player.Equipment_Armor_Magic -= lowerbodyarmorname.Equipment_Armor_Magic
    $ player.Equipment_Armor_Will -= lowerbodyarmorname.Equipment_Armor_Will
    $ player.Equipment_Damage_Bonus_Melee_Max -= lowerbodyarmorname.Equipment_Damage_Bonus_Melee_Max
    $ player.Equipment_Damage_Bonus_Ranged_Max -= lowerbodyarmorname.Equipment_Damage_Bonus_Ranged_Max
    $ player.Equipment_Damage_Bonus_Magic_Max -= lowerbodyarmorname.Equipment_Damage_Bonus_Magic_Max
    $ player.Equipment_Damage_Bonus_Will_Max -= lowerbodyarmorname.Equipment_Damage_Bonus_Will_Max
    $ player.Equipment_Dodge -= lowerbodyarmorname.Equipment_Dodge
    $ player.Equipment_Initiative -= lowerbodyarmorname.Equipment_Initiative
    $ player.Equipment_Slot_LowerBodyArmor_Name = "no_lower_armor"
    $ player.Equipment_Slot_LowerBodyArmor_Name_Text = no_lower_armor.Equipment_Slot_LowerBodyArmor_Name_Text
    call battle_call_Player_Full_Recheck
    return

label call_Player_Equipment_Slot_Equip_Necklace(necklacename):
    $ player.Equipment_HealthPoints_Max += necklacename.Equipment_HealthPoints_Max
    $ player.Equipment_AbilityPoints_Max += necklacename.Equipment_AbilityPoints_Max
    $ player.Equipment_WillPoints_Max += necklacename.Equipment_WillPoints_Max
    $ player.Equipment_Accuracy_Melee += necklacename.Equipment_Accuracy_Melee
    $ player.Equipment_Accuracy_Ranged += necklacename.Equipment_Accuracy_Ranged
    $ player.Equipment_Armor_Physical += necklacename.Equipment_Armor_Physical
    $ player.Equipment_Armor_Magic += necklacename.Equipment_Armor_Magic
    $ player.Equipment_Armor_Will += necklacename.Equipment_Armor_Will
    $ player.Equipment_Damage_Bonus_Melee_Max += necklacename.Equipment_Damage_Bonus_Melee_Max
    $ player.Equipment_Damage_Bonus_Ranged_Max += necklacename.Equipment_Damage_Bonus_Ranged_Max
    $ player.Equipment_Damage_Bonus_Magic_Max += necklacename.Equipment_Damage_Bonus_Magic_Max
    $ player.Equipment_Damage_Bonus_Will_Max += necklacename.Equipment_Damage_Bonus_Will_Max
    $ player.Equipment_Dodge += necklacename.Equipment_Dodge
    $ player.Equipment_Initiative += necklacename.Equipment_Initiative
    $ player.Equipment_Slot_Necklace_Name = necklacename.Equipment_Slot_Necklace_Name
    $ player.Equipment_Slot_Necklace_Name_Text = necklacename.Equipment_Slot_Necklace_Name_Text
    call battle_call_Player_Full_Recheck
    return

label call_Player_Equipment_Slot_Unequip_Necklace(necklacename):
    $ player.Equipment_HealthPoints_Max -= necklacename.Equipment_HealthPoints_Max
    $ player.Equipment_AbilityPoints_Max -= necklacename.Equipment_AbilityPoints_Max
    $ player.Equipment_WillPoints_Max -= necklacename.Equipment_WillPoints_Max
    $ player.Equipment_Accuracy_Melee -= necklacename.Equipment_Accuracy_Melee
    $ player.Equipment_Accuracy_Ranged -= necklacename.Equipment_Accuracy_Ranged
    $ player.Equipment_Armor_Physical -= necklacename.Equipment_Armor_Physical
    $ player.Equipment_Armor_Magic -= necklacename.Equipment_Armor_Magic
    $ player.Equipment_Armor_Will -= necklacename.Equipment_Armor_Will
    $ player.Equipment_Damage_Bonus_Melee_Max -= necklacename.Equipment_Damage_Bonus_Melee_Max
    $ player.Equipment_Damage_Bonus_Ranged_Max -= necklacename.Equipment_Damage_Bonus_Ranged_Max
    $ player.Equipment_Damage_Bonus_Magic_Max -= necklacename.Equipment_Damage_Bonus_Magic_Max
    $ player.Equipment_Damage_Bonus_Will_Max -= necklacename.Equipment_Damage_Bonus_Will_Max
    $ player.Equipment_Dodge -= necklacename.Equipment_Dodge
    $ player.Equipment_Initiative -= necklacename.Equipment_Initiative
    $ player.Equipment_Slot_Necklace_Name = "no_necklace"
    $ player.Equipment_Slot_Necklace_Name_Text = no_necklace.Equipment_Slot_Necklace_Name_Text
    call battle_call_Player_Full_Recheck
    return

label call_Player_Equipment_Slot_Equip_Ring(ringname):
    $ player.Equipment_HealthPoints_Max += ringname.Equipment_HealthPoints_Max
    $ player.Equipment_AbilityPoints_Max += ringname.Equipment_AbilityPoints_Max
    $ player.Equipment_WillPoints_Max += ringname.Equipment_WillPoints_Max
    $ player.Equipment_Accuracy_Melee += ringname.Equipment_Accuracy_Melee
    $ player.Equipment_Accuracy_Ranged += ringname.Equipment_Accuracy_Ranged
    $ player.Equipment_Armor_Physical += ringname.Equipment_Armor_Physical
    $ player.Equipment_Armor_Magic += ringname.Equipment_Armor_Magic
    $ player.Equipment_Armor_Will += ringname.Equipment_Armor_Will
    $ player.Equipment_Damage_Bonus_Melee_Max += ringname.Equipment_Damage_Bonus_Melee_Max
    $ player.Equipment_Damage_Bonus_Ranged_Max += ringname.Equipment_Damage_Bonus_Ranged_Max
    $ player.Equipment_Damage_Bonus_Magic_Max += ringname.Equipment_Damage_Bonus_Magic_Max
    $ player.Equipment_Damage_Bonus_Will_Max += ringname.Equipment_Damage_Bonus_Will_Max
    $ player.Equipment_Dodge += ringname.Equipment_Dodge
    $ player.Equipment_Initiative += ringname.Equipment_Initiative
    $ player.Equipment_Slot_Ring_Name = ringname.Equipment_Slot_Necklace_Name
    $ player.Equipment_Slot_Ring_Name_Text = ringname.Equipment_Slot_Ring_Name_Text
    call battle_call_Player_Full_Recheck
    return

label call_Player_Equipment_Slot_Unequip_Recklace(ringname):
    $ player.Equipment_HealthPoints_Max -= ringname.Equipment_HealthPoints_Max
    $ player.Equipment_AbilityPoints_Max -= ringname.Equipment_AbilityPoints_Max
    $ player.Equipment_WillPoints_Max -= ringname.Equipment_WillPoints_Max
    $ player.Equipment_Accuracy_Melee -= ringname.Equipment_Accuracy_Melee
    $ player.Equipment_Accuracy_Ranged -= ringname.Equipment_Accuracy_Ranged
    $ player.Equipment_Armor_Physical -= ringname.Equipment_Armor_Physical
    $ player.Equipment_Armor_Magic -= ringname.Equipment_Armor_Magic
    $ player.Equipment_Armor_Will -= ringname.Equipment_Armor_Will
    $ player.Equipment_Damage_Bonus_Melee_Max -= ringname.Equipment_Damage_Bonus_Melee_Max
    $ player.Equipment_Damage_Bonus_Ranged_Max -= ringname.Equipment_Damage_Bonus_Ranged_Max
    $ player.Equipment_Damage_Bonus_Magic_Max -= ringname.Equipment_Damage_Bonus_Magic_Max
    $ player.Equipment_Damage_Bonus_Will_Max -= ringname.Equipment_Damage_Bonus_Will_Max
    $ player.Equipment_Dodge -= ringname.Equipment_Dodge
    $ player.Equipment_Initiative -= ringname.Equipment_Initiative
    $ player.Equipment_Slot_Ring_Name = "no_ring"
    $ player.Equipment_Slot_Ring_Name_Text = no_ring.Equipment_Slot_Ring_Name_Text
    call battle_call_Player_Full_Recheck
    return

#####################################################################
# Equipment - For the enemy.
#####################################################################

label call_Enemy_Equipment_Slot_Initialize_All:
    $ enemy.Equipment_HealthPoints_Max = 0
    $ enemy.Equipment_AbilityPoints_Max = 0
    $ enemy.Equipment_WillPoints_Max = 0
    $ enemy.Equipment_Accuracy_Melee = 0
    $ enemy.Equipment_Accuracy_Ranged = 0
    $ enemy.Equipment_Armor_Physical = 0
    $ enemy.Equipment_Armor_Magic = 0
    $ enemy.Equipment_Armor_Will = 0
    $ enemy.Equipment_Damage_Bonus_Melee_Max = 0
    $ enemy.Equipment_Damage_Bonus_Ranged_Max = 0
    $ enemy.Equipment_Damage_Bonus_Magic_Max = 0
    $ enemy.Equipment_Damage_Bonus_Will_Max = 0
    $ enemy.Equipment_Dodge = 0
    $ enemy.Equipment_Initiative = 0
    nar "enemy.Equipment_Slot_Weapon_Name = [enemy.Equipment_Slot_Weapon_Name]"
#    call call_Enemy_Equipment_Slot_Equip_Weapon(enemy.Equipment_Slot_Weapon_Name)
    $ eweaponname = enemy.Equipment_Slot_Weapon_Name
    call call_Enemy_Equipment_Slot_Equip_Weapon
    call call_Enemy_Equipment_Slot_Equip_UpperBodyArmor(enemy.Equipment_Slot_UpperBodyArmor_Name)
    call call_Enemy_Equipment_Slot_Equip_LowerBodyArmor(enemy.Equipment_Slot_LowerBodyArmor_Name)
    call call_Enemy_Equipment_Slot_Equip_Necklace(enemy.Equipment_Slot_Necklace_Name)
    call call_Enemy_Equipment_Slot_Equip_Ring(enemy.Equipment_Slot_Ring_Name)
    call battle_call_Enemy_Full_Recheck
    return

#  So, your enemy just woke up after being captured by slavers?  Lets get rid
# of all that pesky equipment!
label call_Enemy_Equipment_Slot_Strip_All:
    $ enemy.Equipment_HealthPoints_Max = 0
    $ enemy.Equipment_AbilityPoints_Max = 0
    $ enemy.Equipment_WillPoints_Max = 0
    $ enemy.Equipment_Accuracy_Melee = 0
    $ enemy.Equipment_Accuracy_Ranged = 0
    $ enemy.Equipment_Armor_Physical = 0
    $ enemy.Equipment_Armor_Magic = 0
    $ enemy.Equipment_Armor_Will = 0
    $ enemy.Equipment_Damage_Bonus_Melee_Max = 0
    $ enemy.Equipment_Damage_Bonus_Ranged_Max = 0
    $ enemy.Equipment_Damage_Bonus_Magic_Max = 0
    $ enemy.Equipment_Damage_Bonus_Will_Max = 0
    $ enemy.Equipment_Dodge = 0
    $ enemy.Equipment_Initiative = 0
    $ enemy.Equipment_Weapon_Accuracy_Melee = no_weapon.Equipment_Weapon_Accuracy_Melee
    $ enemy.Equipment_Weapon_Accuracy_Ranged = no_weapon.Equipment_Weapon_Accuracy_Ranged
    $ enemy.Equipment_Weapon_Damage_Melee_Max = no_weapon.Equipment_Weapon_Damage_Melee_Max
    $ enemy.Equipment_Weapon_Damage_Melee_Min = no_weapon.Equipment_Weapon_Damage_Melee_Min
    $ enemy.Equipment_Weapon_Damage_Ranged_Max = no_weapon.Equipment_Weapon_Damage_Ranged_Max
    $ enemy.Equipment_Weapon_Damage_Ranged_Min = no_weapon.Equipment_Weapon_Damage_Ranged_Min
    $ enemy.Equipment_Weapon_Damage_Magic_Max = no_weapon.Equipment_Weapon_Damage_Magic_Max
    $ enemy.Equipment_Weapon_Damage_Magic_Min = no_weapon.Equipment_Weapon_Damage_Magic_Min
    $ enemy.Equipment_Weapon_Damage_Will_Max = no_weapon.Equipment_Weapon_Damage_Will_Max
    $ enemy.Equipment_Weapon_Damage_Will_Min = no_weapon.Equipment_Weapon_Damage_Will_Min
    $ enemy.Equipment_Slot_Weapon_Name = "no_weapon"
    $ enemy.Equipment_Slot_Weapon_Name_Text = no_weapon.Equipment_Slot_Weapon_Name_Text
    $ enemy.Equipment_Slot_Weapon_Accuracy_Type = no_weapon.Equipment_Slot_Weapon_Accuracy_Type
    $ enemy.Equipment_Slot_Weapon_Damage_Type = no_weapon.Equipment_Slot_Weapon_Damage_Type
    $ enemy.Equipment_Slot_UpperBodyArmor_Name = "no_upper_armor"
    $ enemy.Equipment_Slot_UpperBodyArmor_Name_Text = no_upper_armor.Equipment_Slot_UpperBodyArmor_Name_Text
    $ enemy.Equipment_Slot_LowerBodyArmor_Name = "no_lower_armor"
    $ enemy.Equipment_Slot_LowerBodyArmor_Name_Text = no_lower_armor.Equipment_Slot_LowerBodyArmor_Name_Text
    $ enemy.Equipment_Slot_Necklace_Name = "no_necklace"
    $ enemy.Equipment_Slot_Necklace_Name_Text = no_necklace.Equipment_Slot_Necklace_Name_Text
    $ enemy.Equipment_Slot_Ring_Name = "no_ring"
    $ enemy.Equipment_Slot_Ring_Name_Text = no_ring.Equipment_Slot_Ring_Name_Text
    call battle_call_Enemy_Full_Recheck
    return

#label call_Enemy_Equipment_Slot_Equip_Weapon(weaponname):
label call_Enemy_Equipment_Slot_Equip_Weapon:
# swapped over partially to eweaponname instead of weaponname -just- to avoid any potential conflicts.
    nar "eweaponname = [eweaponname]"
    nar "[no_weapon.Equipment_Slot_Weapon_Name] [no_weapon.Equipment_HealthPoints_Max]"
# Copy from Script, picking out the enemy before the jump..
#    $ ename = Orc_Hero
# Copy from label battle_call_Enemy_Data_Import:
#    $ enemy = ename
#    $ enemy.name = ename.name
#    $ enemy.battle_selected_action = "battle_Enemy_Wait"
#    $ enemy.Attack_List = ename.Attack_List
#    And that -works why-, when this doesn't?
    $ enemy = eweaponname
    $ enemy.Equipment_Slot_Weapon_Name = eweaponname.Equipment_Slot_Weapon_Name
#
    $ enemy.Equipment_HealthPoints_Max += eweaponname.Equipment_HealthPoints_Max
    $ enemy = ename
#
    $ enemy.Equipment_AbilityPoints_Max += eweaponname.Equipment_AbilityPoints_Max
    $ enemy.Equipment_WillPoints_Max += weaponname.Equipment_WillPoints_Max
    $ enemy.Equipment_Accuracy_Melee += weaponname.Equipment_Accuracy_Melee
    $ enemy.Equipment_Accuracy_Ranged += weaponname.Equipment_Accuracy_Ranged
    $ enemy.Equipment_Armor_Physical += weaponname.Equipment_Armor_Physical
    $ enemy.Equipment_Armor_Magic += weaponname.Equipment_Armor_Magic
    $ enemy.Equipment_Armor_Will += weaponname.Equipment_Armor_Will
    $ enemy.Equipment_Damage_Bonus_Melee_Max += weaponname.Equipment_Damage_Bonus_Melee_Max
    $ enemy.Equipment_Damage_Bonus_Ranged_Max += weaponname.Equipment_Damage_Bonus_Ranged_Max
    $ enemy.Equipment_Damage_Bonus_Magic_Max += weaponname.Equipment_Damage_Bonus_Magic_Max
    $ enemy.Equipment_Damage_Bonus_Will_Max += weaponname.Equipment_Damage_Bonus_Will_Max
    $ enemy.Equipment_Dodge += weaponname.Equipment_Dodge
    $ enemy.Equipment_Initiative += weaponname.Equipment_Initiative
    $ enemy.Equipment_Weapon_Accuracy_Melee = weaponname.Equipment_Weapon_Accuracy_Melee
    $ enemy.Equipment_Weapon_Accuracy_Ranged = weaponname.Equipment_Weapon_Accuracy_Ranged
    $ enemy.Equipment_Weapon_Damage_Melee_Max = weaponname.Equipment_Weapon_Damage_Melee_Max
    $ enemy.Equipment_Weapon_Damage_Melee_Min = weaponname.Equipment_Weapon_Damage_Melee_Min
    $ enemy.Equipment_Weapon_Damage_Ranged_Max = weaponname.Equipment_Weapon_Damage_Ranged_Max
    $ enemy.Equipment_Weapon_Damage_Ranged_Min = weaponname.Equipment_Weapon_Damage_Ranged_Min
    $ enemy.Equipment_Weapon_Damage_Magic_Max = weaponname.Equipment_Weapon_Damage_Magic_Max
    $ enemy.Equipment_Weapon_Damage_Magic_Min = weaponname.Equipment_Weapon_Damage_Magic_Min
    $ enemy.Equipment_Weapon_Damage_Will_Max = weaponname.Equipment_Weapon_Damage_Will_Max
    $ enemy.Equipment_Weapon_Damage_Will_Min = weaponname.Equipment_Weapon_Damage_Will_Min
    $ enemy.Equipment_Slot_Weapon_Name = weaponname.Equipment_Slot_Weapon_Name
    $ enemy.Equipment_Slot_Weapon_Name_Text = weaponname.Equipment_Slot_Weapon_Name_Text
    $ enemy.Equipment_Slot_Weapon_Accuracy_Type = weaponname.Equipment_Slot_Weapon_Accuracy_Type
    $ enemy.Equipment_Slot_Weapon_Damage_Type = weaponname.Equipment_Slot_Weapon_Damage_Type
    call battle_call_Enemy_Full_Recheck
    return

label call_Enemy_Equipment_Slot_Unquip_Weapon(weaponname):
    $ enemy.Equipment_HealthPoints_Max -= weaponname.Equipment_HealthPoints_Max
    $ enemy.Equipment_AbilityPoints_Max -= weaponname.Equipment_AbilityPoints_Max
    $ enemy.Equipment_WillPoints_Max -= weaponname.Equipment_WillPoints_Max
    $ enemy.Equipment_Accuracy_Melee -= weaponname.Equipment_Accuracy_Melee
    $ enemy.Equipment_Accuracy_Ranged -= weaponname.Equipment_Accuracy_Ranged
    $ enemy.Equipment_Armor_Physical -= weaponname.Equipment_Armor_Physical
    $ enemy.Equipment_Armor_Magic -= weaponname.Equipment_Armor_Magic
    $ enemy.Equipment_Armor_Will -= weaponname.Equipment_Armor_Will
    $ enemy.Equipment_Damage_Bonus_Melee_Max -= weaponname.Equipment_Damage_Bonus_Melee_Max
    $ enemy.Equipment_Damage_Bonus_Ranged_Max -= weaponname.Equipment_Damage_Bonus_Ranged_Max
    $ enemy.Equipment_Damage_Bonus_Magic_Max -= weaponname.Equipment_Damage_Bonus_Magic_Max
    $ enemy.Equipment_Damage_Bonus_Will_Max -= weaponname.Equipment_Damage_Bonus_Will_Max
    $ enemy.Equipment_Dodge -= weaponname.Equipment_Dodge
    $ enemy.Equipment_Initiative -= weaponname.Equipment_Initiative
    $ enemy.Equipment_Weapon_Accuracy_Melee = no_weapon.Equipment_Weapon_Accuracy_Melee
    $ enemy.Equipment_Weapon_Accuracy_Ranged = no_weapon.Equipment_Weapon_Accuracy_Ranged
    $ enemy.Equipment_Weapon_Damage_Melee_Max = no_weapon.Equipment_Weapon_Damage_Melee_Max
    $ enemy.Equipment_Weapon_Damage_Melee_Min = no_weapon.Equipment_Weapon_Damage_Melee_Min
    $ enemy.Equipment_Weapon_Damage_Ranged_Max = no_weapon.Equipment_Weapon_Damage_Ranged_Max
    $ enemy.Equipment_Weapon_Damage_Ranged_Min = no_weapon.Equipment_Weapon_Damage_Ranged_Min
    $ enemy.Equipment_Weapon_Damage_Magic_Max = no_weapon.Equipment_Weapon_Damage_Magic_Max
    $ enemy.Equipment_Weapon_Damage_Magic_Min = no_weapon.Equipment_Weapon_Damage_Magic_Min
    $ enemy.Equipment_Weapon_Damage_Will_Max = no_weapon.Equipment_Weapon_Damage_Will_Max
    $ enemy.Equipment_Weapon_Damage_Will_Min = no_weapon.Equipment_Weapon_Damage_Will_Min
    $ enemy.Equipment_Slot_Weapon_Name = "no_weapon"
    $ enemy.Equipment_Slot_Weapon_Name_Text = no_weapon.Equipment_Slot_Weapon_Name_Text
    $ enemy.Equipment_Slot_Weapon_Accuracy_Type = no_weapon.Equipment_Slot_Weapon_Accuracy_Type
    $ enemy.Equipment_Slot_Weapon_Damage_Type = no_weapon.Equipment_Slot_Weapon_Damage_Type
    call battle_call_Enemy_Full_Recheck
    return

label call_Enemy_Equipment_Slot_Equip_UpperBodyArmor(upperbodyarmorname):
    $ enemy.Equipment_HealthPoints_Max += upperbodyarmorname.Equipment_HealthPoints_Max
    $ enemy.Equipment_AbilityPoints_Max += upperbodyarmorname.Equipment_AbilityPoints_Max
    $ enemy.Equipment_WillPoints_Max += upperbodyarmorname.Equipment_WillPoints_Max
    $ enemy.Equipment_Accuracy_Melee += upperbodyarmorname.Equipment_Accuracy_Melee
    $ enemy.Equipment_Accuracy_Ranged += upperbodyarmorname.Equipment_Accuracy_Ranged
    $ enemy.Equipment_Armor_Physical += upperbodyarmorname.Equipment_Armor_Physical
    $ enemy.Equipment_Armor_Magic += upperbodyarmorname.Equipment_Armor_Magic
    $ enemy.Equipment_Armor_Will += upperbodyarmorname.Equipment_Armor_Will
    $ enemy.Equipment_Damage_Bonus_Melee_Max += upperbodyarmorname.Equipment_Damage_Bonus_Melee_Max
    $ enemy.Equipment_Damage_Bonus_Ranged_Max += upperbodyarmorname.Equipment_Damage_Bonus_Ranged_Max
    $ enemy.Equipment_Damage_Bonus_Magic_Max += upperbodyarmorname.Equipment_Damage_Bonus_Magic_Max
    $ enemy.Equipment_Damage_Bonus_Will_Max += upperbodyarmorname.Equipment_Damage_Bonus_Will_Max
    $ enemy.Equipment_Dodge += upperbodyarmorname.Equipment_Dodge
    $ enemy.Equipment_Initiative += upperbodyarmorname.Equipment_Initiative
    $ enemy.Equipment_Slot_UpperBodyArmor_Name = upperbodyarmorname.Equipment_Slot_Necklace_Name
    $ enemy.Equipment_Slot_UpperBodyArmor_Name_Text = upperbodyarmorname.Equipment_Slot_UpperBodyArmor_Name_Text
    call battle_call_Enemy_Full_Recheck
    return

label call_Enemy_Equipment_Slot_Unequip_UpperBodyArmor(upperbodyarmorname):
    $ enemy.Equipment_HealthPoints_Max -= upperbodyarmorname.Equipment_HealthPoints_Max
    $ enemy.Equipment_AbilityPoints_Max -= upperbodyarmorname.Equipment_AbilityPoints_Max
    $ enemy.Equipment_WillPoints_Max -= upperbodyarmorname.Equipment_WillPoints_Max
    $ enemy.Equipment_Accuracy_Melee -= upperbodyarmorname.Equipment_Accuracy_Melee
    $ enemy.Equipment_Accuracy_Ranged -= upperbodyarmorname.Equipment_Accuracy_Ranged
    $ enemy.Equipment_Armor_Physical -= upperbodyarmorname.Equipment_Armor_Physical
    $ enemy.Equipment_Armor_Magic -= upperbodyarmorname.Equipment_Armor_Magic
    $ enemy.Equipment_Armor_Will -= upperbodyarmorname.Equipment_Armor_Will
    $ enemy.Equipment_Damage_Bonus_Melee_Max -= upperbodyarmorname.Equipment_Damage_Bonus_Melee_Max
    $ enemy.Equipment_Damage_Bonus_Ranged_Max -= upperbodyarmorname.Equipment_Damage_Bonus_Ranged_Max
    $ enemy.Equipment_Damage_Bonus_Magic_Max -= upperbodyarmorname.Equipment_Damage_Bonus_Magic_Max
    $ enemy.Equipment_Damage_Bonus_Will_Max -= upperbodyarmorname.Equipment_Damage_Bonus_Will_Max
    $ enemy.Equipment_Dodge -= upperbodyarmorname.Equipment_Dodge
    $ enemy.Equipment_Initiative -= upperbodyarmorname.Equipment_Initiative
    $ enemy.Equipment_Slot_UpperBodyArmor_Name = "no_upper_armor"
    $ enemy.Equipment_Slot_UpperBodyArmor_Name_Text = no_upper_armor.Equipment_Slot_UpperBodyArmor_Name_Text
    call battle_call_Enemy_Full_Recheck
    return

label call_Enemy_Equipment_Slot_Equip_LowerBodyArmor(lowerbodyarmorname):
    $ enemy.Equipment_HealthPoints_Max += lowerbodyarmorname.Equipment_HealthPoints_Max
    $ enemy.Equipment_AbilityPoints_Max += lowerbodyarmorname.Equipment_AbilityPoints_Max
    $ enemy.Equipment_WillPoints_Max += lowerbodyarmorname.Equipment_WillPoints_Max
    $ enemy.Equipment_Accuracy_Melee += lowerbodyarmorname.Equipment_Accuracy_Melee
    $ enemy.Equipment_Accuracy_Ranged += lowerbodyarmorname.Equipment_Accuracy_Ranged
    $ enemy.Equipment_Armor_Physical += lowerbodyarmorname.Equipment_Armor_Physical
    $ enemy.Equipment_Armor_Magic += lowerbodyarmorname.Equipment_Armor_Magic
    $ enemy.Equipment_Armor_Will += lowerbodyarmorname.Equipment_Armor_Will
    $ enemy.Equipment_Damage_Bonus_Melee_Max += lowerbodyarmorname.Equipment_Damage_Bonus_Melee_Max
    $ enemy.Equipment_Damage_Bonus_Ranged_Max += lowerbodyarmorname.Equipment_Damage_Bonus_Ranged_Max
    $ enemy.Equipment_Damage_Bonus_Magic_Max += lowerbodyarmorname.Equipment_Damage_Bonus_Magic_Max
    $ enemy.Equipment_Damage_Bonus_Will_Max += lowerbodyarmorname.Equipment_Damage_Bonus_Will_Max
    $ enemy.Equipment_Dodge += lowerbodyarmorname.Equipment_Dodge
    $ enemy.Equipment_Initiative += lowerbodyarmorname.Equipment_Initiative
    $ enemy.Equipment_Slot_LowerBodyArmor_Name = lowerbodyarmorname.Equipment_Slot_Necklace_Name
    $ enemy.Equipment_Slot_LowerBodyArmor_Name_Text = lowerbodyarmorname.Equipment_Slot_LowerBodyArmor_Name_Text
    call battle_call_Enemy_Full_Recheck
    return

label call_Enemy_Equipment_Slot_Unequip_LowerBodyArmor(lowerbodyarmorname):
    $ enemy.Equipment_HealthPoints_Max -= lowerbodyarmorname.Equipment_HealthPoints_Max
    $ enemy.Equipment_AbilityPoints_Max -= lowerbodyarmorname.Equipment_AbilityPoints_Max
    $ enemy.Equipment_WillPoints_Max -= lowerbodyarmorname.Equipment_WillPoints_Max
    $ enemy.Equipment_Accuracy_Melee -= lowerbodyarmorname.Equipment_Accuracy_Melee
    $ enemy.Equipment_Accuracy_Ranged -= lowerbodyarmorname.Equipment_Accuracy_Ranged
    $ enemy.Equipment_Armor_Physical -= lowerbodyarmorname.Equipment_Armor_Physical
    $ enemy.Equipment_Armor_Magic -= lowerbodyarmorname.Equipment_Armor_Magic
    $ enemy.Equipment_Armor_Will -= lowerbodyarmorname.Equipment_Armor_Will
    $ enemy.Equipment_Damage_Bonus_Melee_Max -= lowerbodyarmorname.Equipment_Damage_Bonus_Melee_Max
    $ enemy.Equipment_Damage_Bonus_Ranged_Max -= lowerbodyarmorname.Equipment_Damage_Bonus_Ranged_Max
    $ enemy.Equipment_Damage_Bonus_Magic_Max -= lowerbodyarmorname.Equipment_Damage_Bonus_Magic_Max
    $ enemy.Equipment_Damage_Bonus_Will_Max -= lowerbodyarmorname.Equipment_Damage_Bonus_Will_Max
    $ enemy.Equipment_Dodge -= lowerbodyarmorname.Equipment_Dodge
    $ enemy.Equipment_Initiative -= lowerbodyarmorname.Equipment_Initiative
    $ enemy.Equipment_Slot_LowerBodyArmor_Name = "no_lower_armor"
    $ enemy.Equipment_Slot_LowerBodyArmor_Name_Text = no_lower_armor.Equipment_Slot_LowerBodyArmor_Name_Text
    call battle_call_Enemy_Full_Recheck
    return

label call_Enemy_Equipment_Slot_Equip_Necklace(necklacename):
    $ enemy.Equipment_HealthPoints_Max += necklacename.Equipment_HealthPoints_Max
    $ enemy.Equipment_AbilityPoints_Max += necklacename.Equipment_AbilityPoints_Max
    $ enemy.Equipment_WillPoints_Max += necklacename.Equipment_WillPoints_Max
    $ enemy.Equipment_Accuracy_Melee += necklacename.Equipment_Accuracy_Melee
    $ enemy.Equipment_Accuracy_Ranged += necklacename.Equipment_Accuracy_Ranged
    $ enemy.Equipment_Armor_Physical += necklacename.Equipment_Armor_Physical
    $ enemy.Equipment_Armor_Magic += necklacename.Equipment_Armor_Magic
    $ enemy.Equipment_Armor_Will += necklacename.Equipment_Armor_Will
    $ enemy.Equipment_Damage_Bonus_Melee_Max += necklacename.Equipment_Damage_Bonus_Melee_Max
    $ enemy.Equipment_Damage_Bonus_Ranged_Max += necklacename.Equipment_Damage_Bonus_Ranged_Max
    $ enemy.Equipment_Damage_Bonus_Magic_Max += necklacename.Equipment_Damage_Bonus_Magic_Max
    $ enemy.Equipment_Damage_Bonus_Will_Max += necklacename.Equipment_Damage_Bonus_Will_Max
    $ enemy.Equipment_Dodge += necklacename.Equipment_Dodge
    $ enemy.Equipment_Initiative += necklacename.Equipment_Initiative
    $ enemy.Equipment_Slot_Necklace_Name = necklacename.Equipment_Slot_Necklace_Name
    $ enemy.Equipment_Slot_Necklace_Name_Text = necklacename.Equipment_Slot_Necklace_Name_Text
    call battle_call_Enemy_Full_Recheck
    return

label call_Enemy_Equipment_Slot_Unequip_Necklace(necklacename):
    $ enemy.Equipment_HealthPoints_Max -= necklacename.Equipment_HealthPoints_Max
    $ enemy.Equipment_AbilityPoints_Max -= necklacename.Equipment_AbilityPoints_Max
    $ enemy.Equipment_WillPoints_Max -= necklacename.Equipment_WillPoints_Max
    $ enemy.Equipment_Accuracy_Melee -= necklacename.Equipment_Accuracy_Melee
    $ enemy.Equipment_Accuracy_Ranged -= necklacename.Equipment_Accuracy_Ranged
    $ enemy.Equipment_Armor_Physical -= necklacename.Equipment_Armor_Physical
    $ enemy.Equipment_Armor_Magic -= necklacename.Equipment_Armor_Magic
    $ enemy.Equipment_Armor_Will -= necklacename.Equipment_Armor_Will
    $ enemy.Equipment_Damage_Bonus_Melee_Max -= necklacename.Equipment_Damage_Bonus_Melee_Max
    $ enemy.Equipment_Damage_Bonus_Ranged_Max -= necklacename.Equipment_Damage_Bonus_Ranged_Max
    $ enemy.Equipment_Damage_Bonus_Magic_Max -= necklacename.Equipment_Damage_Bonus_Magic_Max
    $ enemy.Equipment_Damage_Bonus_Will_Max -= necklacename.Equipment_Damage_Bonus_Will_Max
    $ enemy.Equipment_Dodge -= necklacename.Equipment_Dodge
    $ enemy.Equipment_Initiative -= necklacename.Equipment_Initiative
    $ enemy.Equipment_Slot_Necklace_Name = "no_necklace"
    $ enemy.Equipment_Slot_Necklace_Name_Text = no_necklace.Equipment_Slot_Necklace_Name_Text
    call battle_call_Enemy_Full_Recheck
    return

label call_Enemy_Equipment_Slot_Equip_Ring(ringname):
    $ enemy.Equipment_HealthPoints_Max += ringname.Equipment_HealthPoints_Max
    $ enemy.Equipment_AbilityPoints_Max += ringname.Equipment_AbilityPoints_Max
    $ enemy.Equipment_WillPoints_Max += ringname.Equipment_WillPoints_Max
    $ enemy.Equipment_Accuracy_Melee += ringname.Equipment_Accuracy_Melee
    $ enemy.Equipment_Accuracy_Ranged += ringname.Equipment_Accuracy_Ranged
    $ enemy.Equipment_Armor_Physical += ringname.Equipment_Armor_Physical
    $ enemy.Equipment_Armor_Magic += ringname.Equipment_Armor_Magic
    $ enemy.Equipment_Armor_Will += ringname.Equipment_Armor_Will
    $ enemy.Equipment_Damage_Bonus_Melee_Max += ringname.Equipment_Damage_Bonus_Melee_Max
    $ enemy.Equipment_Damage_Bonus_Ranged_Max += ringname.Equipment_Damage_Bonus_Ranged_Max
    $ enemy.Equipment_Damage_Bonus_Magic_Max += ringname.Equipment_Damage_Bonus_Magic_Max
    $ enemy.Equipment_Damage_Bonus_Will_Max += ringname.Equipment_Damage_Bonus_Will_Max
    $ enemy.Equipment_Dodge += ringname.Equipment_Dodge
    $ enemy.Equipment_Initiative += ringname.Equipment_Initiative
    $ enemy.Equipment_Slot_Ring_Name = ringname.Equipment_Slot_Necklace_Name
    $ enemy.Equipment_Slot_Ring_Name_Text = ringname.Equipment_Slot_Ring_Name_Text
    call battle_call_Enemy_Full_Recheck
    return

label call_Enemy_Equipment_Slot_Unequip_Recklace(ringname):
    $ enemy.Equipment_HealthPoints_Max -= ringname.Equipment_HealthPoints_Max
    $ enemy.Equipment_AbilityPoints_Max -= ringname.Equipment_AbilityPoints_Max
    $ enemy.Equipment_WillPoints_Max -= ringname.Equipment_WillPoints_Max
    $ enemy.Equipment_Accuracy_Melee -= ringname.Equipment_Accuracy_Melee
    $ enemy.Equipment_Accuracy_Ranged -= ringname.Equipment_Accuracy_Ranged
    $ enemy.Equipment_Armor_Physical -= ringname.Equipment_Armor_Physical
    $ enemy.Equipment_Armor_Magic -= ringname.Equipment_Armor_Magic
    $ enemy.Equipment_Armor_Will -= ringname.Equipment_Armor_Will
    $ enemy.Equipment_Damage_Bonus_Melee_Max -= ringname.Equipment_Damage_Bonus_Melee_Max
    $ enemy.Equipment_Damage_Bonus_Ranged_Max -= ringname.Equipment_Damage_Bonus_Ranged_Max
    $ enemy.Equipment_Damage_Bonus_Magic_Max -= ringname.Equipment_Damage_Bonus_Magic_Max
    $ enemy.Equipment_Damage_Bonus_Will_Max -= ringname.Equipment_Damage_Bonus_Will_Max
    $ enemy.Equipment_Dodge -= ringname.Equipment_Dodge
    $ enemy.Equipment_Initiative -= ringname.Equipment_Initiative
    $ enemy.Equipment_Slot_Ring_Name = "no_ring"
    $ enemy.Equipment_Slot_Ring_Name_Text = no_ring.Equipment_Slot_Ring_Name_Text
    call battle_call_Enemy_Full_Recheck
    return
