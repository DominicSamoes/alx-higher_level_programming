#!/usr/bin/python3
for alpha in reversed(range(97, 122 + 1)):
    print("{:c}".format(alpha if (alpha % 2 == 0) else (alpha - 32)), end='')
