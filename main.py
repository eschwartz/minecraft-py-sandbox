from time import sleep

from mcpi.entity import SHEEP
from mcpi.minecraft import Minecraft


def break_target():
    x, y, z = mc.getTargetBlock()

    mc.breakBlockNaturally(x, y, z)


ec2_server_ip = "3.222.216.215"
mc = Minecraft.create(address=ec2_server_ip)
flower = 38

x, y, z = mc.player.getPos()
entity = mc.spawnEntity(x + 1, y, z, SHEEP)

while True:
    x, y, z = entity.getPos()
    entity.setPos(x + 1, y, z)

    sleep(1)
