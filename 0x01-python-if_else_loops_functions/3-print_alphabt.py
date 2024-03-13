#!/usr/bin/python3

for lower_alpha in range(97, 123):
    if lower_alpha == 101 or lower_alpha == 113:
        continue
#    if lower_alpha == 113:
#        continue
    print("{}".format(chr(lower_alpha)), end='')
