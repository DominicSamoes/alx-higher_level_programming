#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 1
    sum = len(sys.argv) - 1
    if sum == 0:
        print(0, "arguments.")
    elif sum == 1:
        print(1, "argument:")
        print("1: {}".format(sys.argv[i]))
    else:
        print("{} arguments:".format(sum))
        for j in range(sum):
            print("{}: {}".format(j + 1, sys.argv[j + 1]))
