#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    if len(sys.argv) <= 1:
        print("0")
        sys.exit()

    addition = 0

    for i in range(1, len(sys.argv)):
        addition = addition + int(sys.argv[i])
    
    print("{}".format(addition))
