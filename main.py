from time import sleep

from mcpi.entity import SHEEP, PARROT
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
        parrot = mc.spawnEntity(x + 1, y, z, PARROT)
        if parrot.id:
            print(f"Created sheep {parrot.id}")
            break
    except:
        pass

while True:
    x, y, z = mc.player.getPos()
    sX, sY, sZ = parrot.getPos()
    print(f"Player: {x}, {y}, {z}  -  Sheep: {sX}, {sY}, {sZ}")
    parrot.setPos(x + 1, y, z)

    # break block in front
    mc.breakBlockNaturally(x + 1, y - 1, z)


# while True:
#     x, y, z = entity.getPos()
#     print(f"Sheep: {x}, {y}, {z}")
#
#     entity.setPos(x + 1, y, z)
#
#     print(f"Player: {mc.player.getPos()}")
#
#     sleep(0.5)
