"""Here is where we run the game just to show you how the classes work"""
from characters import basic as basic_character
from weapons.level_one_weapons import Sword, Spear


# it will be best to make character classes but this is to show you how classes work
# and I'm running out of time so in the main script for now it's just going to be hard coded

player_one_squad = dict()

# assign your first character
player_one_squad["harry"] = basic_character.BasicHumanSoldier(name="harry")

# then equip him weapons he finds using the living entity functions the human class inherited
player_one_squad["harry"].pick_up_weapon(weapon=Sword())
player_one_squad["harry"].pick_up_weapon(weapon=Sword())
player_one_squad["harry"].pick_up_weapon(weapon=Spear())

# assign weapons to his hands
player_one_squad["harry"].assign_weapon(weapon=Sword())

# your character then comes across an orc who has a pike
enemy = basic_character.BasicOrc(name="Nasgul")
enemy.pick_up_weapon(weapon=Spear())
enemy.assign_weapon(weapon=Spear())

# so you see what weapons you have
print("")
print(player_one_squad["harry"].weapons)

# and what weapons you are assigned
print("")
print(player_one_squad["harry"].weapons_used)

# and you use your basic sword on him
player_one_squad["harry"].weapons_used["basic sword"].hand_attack(enemy)

# and you can see that his HP has gone down
print("")
print(enemy.hp)

