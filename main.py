from time import sleep

from mcpi.minecraft import Minecraft

mc = Minecraft.create()
flower = 38

while True:
    x, y, z = mc.getTargetBlock()

    mc.breakBlockNaturally(x, y, z)
    print(f"{x}, {y}, {z}")
    sleep(0.2)