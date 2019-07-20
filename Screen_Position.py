import ctypes
from time import sleep
from ctypes import c_long, c_ulong
gHandle = ctypes.windll.kernel32.GetStdHandle(c_long(-11))
def move (y, x):
   value = x + (y << 16)
   ctypes.windll.kernel32.SetConsoleCursorPosition(gHandle, c_ulong(value))

x = 0
y = 0

for n in range(5000):
	move(y, x)
	print("█")
	sleep(0.01)
	x = x + 1
	if x > 78:
		x = 0
	y = y + 1
	if y > 23:
		y = 0

input()