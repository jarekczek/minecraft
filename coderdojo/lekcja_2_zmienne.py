from mine import *

mc = Minecraft()

# Tu są zmienne. Znak # wprowadza komentarz, można go pominąć.
x = 100
y = 20

# Zmienna b: rodzaj bloku.
b = 44

mc.setBlock(x, y, 100, b)
mc.setBlock(x, y+1, 100, b)
mc.setBlock(x, y+2, 100, b)
mc.setBlock(x, y+3, 100, b)
mc.setBlock(x, y+4, 100, b)

# Wypisanie pozycji gracza.
print(mc.player.getTilePos())

# Teleportacja.
mc.player.setPos(100, y, 100)
