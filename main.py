from time import sleep

from mcpi.entity import SHEEP, PARROT, LLAMA
from mcpi.minecraft import Minecraft


def break_target():
    x, y, z = mc.getTargetBlock()

    mc.breakBlockNaturally(x, y, z)


ec2_server_ip = "3.222.216.215"
mc = Minecraft.create(address=ec2_server_ip)
flower = 38

while True:
    x, y, z = mc.player.getPos()
    try:
        bot = mc.spawnEntity(x + 1, y, z, LLAMA)
        if bot.id:
            print(f"Created animal {bot.id}")
            break
    except:
        pass

sleep(3)

x, y, z = bot.getPos()

while True:
    bot.setPos(x, y, z)

    # break block in front / below
    mc.breakBlockNaturally(x + 1, y - 1, z)
    # break block above that
    mc.breakBlockNaturally(x + 1, y, z)
    mc.breakBlockNaturally(x + 1, y + 1, z)

    # Move down/forward one
    bot.setPos(x + 1, y - 1, z)
    x, y, z = bot.getPos()


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
