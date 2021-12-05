"""

	author	:  Dio
  	created	:  2021-11-29 13:22:15

"""
pyramid_height = int(input("Masukkan tinggi pyramid: "))

for i in range(1, pyramid_height + 1):
    print("* "*i)

print()

for i in range(pyramid_height, 0, -1):
    print("* "*i)

print()

for i in range(1, pyramid_height + 1):
    print(" " * ((pyramid_height - i) * 2) + "* "*i)

print()

for i in range(1, pyramid_height + 1):
    print(" " * (pyramid_height - i) + "* "*i)

print()

for i in range(pyramid_height, 0, -1):
    print(" " * (pyramid_height - i) + "* "*i)