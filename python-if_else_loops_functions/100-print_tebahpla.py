#!/usr/bin/python3

for n in range(26, 0, -1):
    if n % 2 == 0:
        z = 96
    else:
        z = 64
    print("{:s}".format(chr(n + z)), end='')
