from mine import *

mc = Minecraft()

print(mc.player.getTilePos())

#mc.player.setPos(500, 15, 500)

print(mc.getBlock(500, 5, 500))
mc.setBlock(500, 5, 500, 78)
mc.setBlock(500, 5, 499, 79)
mc.setBlock(500, 5, 498, 80)

