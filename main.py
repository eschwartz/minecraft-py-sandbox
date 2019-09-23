from time import sleep

from mcpi.entity import SHEEP, PARROT, LLAMA, ENDERMAN, OCELOT
from mcpi.minecraft import Minecraft


def break_target():
    x, y, z = mc.getTargetBlock()

    mc.breakBlockNaturally(x, y, z)


ec2_server_ip = "3.222.216.215"
mc = Minecraft.create(address=ec2_server_ip)
flower = 38
while True:
    x, y, z = mc.player.getPos()
    print(f"X: {x}, Y: {y}, Z: {z}")
    try:
        bot = mc.spawnEntity(x + 1, y, z, PARROT)
        bot.freeze()
        if bot.id:
            print(f"Created animal {bot.id}")
            break
    except:
        pass

sleep(3)


# Current status:
#   entities move on their own, making them hard to control,
#       need to set tick rate too high or they move away. But then hard to track
#
# Idea:
#   Bukkit side: add `spawnBot` endpoint.
#       creates entity same as spawnEntity, but tracks in a hashmap of `{ <entId>: Bot(loc=Loc), }`
#       then adds event to constantly teleport entity to same location.
#       `setPos` endpoint then modifies that hashmap.
#
#   or, we need something with a custom entity, and dig into that entity code to
#   see what can be hacked

print('starting loop')


x, y, z = bot.getPos()
print(f"{x}, {y}, {z}")


# This one works pretty well. But could use a `setBlock(dirt)` in case
# we run into a cave.
# I would like to understand why they die if I don't clear enough bricks
while True:
    x, y, z = bot.getPos()
    # break block in front / below
    print(f"{x}, {y}, {z}")

    # break three blocks for next stair
    mc.breakBlockNaturally(x, y - 1, z)
    mc.breakBlockNaturally(x, y - 1, z + 1)
    mc.breakBlockNaturally(x, y - 1, z - 1)
    mc.breakBlockNaturally(x, y + 1, z)
    mc.breakBlockNaturally(x, y + 1, z + 1)
    mc.breakBlockNaturally(x, y + 1, z - 1)
    mc.breakBlockNaturally(x, y + 2, z)
    mc.breakBlockNaturally(x, y + 2, z + 1)
    mc.breakBlockNaturally(x, y + 2, z - 1)
    mc.breakBlockNaturally(x + 1, y, z)
    mc.breakBlockNaturally(x + 1, y, z + 1)
    mc.breakBlockNaturally(x + 1, y, z - 1)
    mc.breakBlockNaturally(x + 1, y - 1, z)
    mc.breakBlockNaturally(x + 1, y - 1, z + 1)
    mc.breakBlockNaturally(x + 1, y - 1, z - 1)
    sleep(0.2)

    # move down stair
    bot.setPos(x + 1, y - 1, z)
    sleep(0.2)

    # place torch
    mc.setBlock(x - 1, y - 1, z + 1, 50)
    mc.setBlock(x - 1, y - 1, z - 1, 50)
    sleep(0.2)

    # place blocks
    mc.setBlock(x - 2, y - 2, z, 1)
    mc.setBlock(x - 2, y - 2, z + 1, 1)
    mc.setBlock(x - 2, y - 2, z - 1, 1)


# while True:
#     x, y, z = mc.player.getPos()
#     sX, sY, sZ = bot.getPos()
#     print(f"Player: {x}, {y}, {z}  -  Sheep: {sX}, {sY}, {sZ}")
#     bot.setPos(x + 1, y, z)
#
#     # break block in front
#     mc.breakBlockNaturally(x + 1, y - 1, z)


# while True:
#     x, y, z = entity.getPos()
#     print(f"Sheep: {x}, {y}, {z}")
#
#     entity.setPos(x + 1, y, z)
#
#     print(f"Player: {mc.player.getPos()}")
#
#     sleep(0.5)
