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
entId = mc.spawnEntity(x + 1, y, z, SHEEP)

while True:
    x, y, z = mc.conn.sendReceive(b"entity.getPos", entId).split(',')
    x, y, z = [float(x), float(y), float(z)]

    mc.conn.send(b"entity.setPos", entId, str(x + 1), str(y), str(z))

    sleep(1)
