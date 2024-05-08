#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    import calculator_1 as calc

    if len(sys.argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit()

    if sys.argv[2] != "+" and sys.argv[2] != "-" and sys.argv[2] != "*" and sys.argv[2] != "/":
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit()

    if sys.argv[2] == "+":
        print("{} {} {} = {}".format(sys.argv[1], sys.argv[2], sys.argv[3], calc.add(int(sys.argv[1]), int(sys.argv[3]))))

    if sys.argv[2] == "-":
        print("{} {} {} = {}".format(sys.argv[1], sys.argv[2], sys.argv[3], calc.sub(int(sys.argv[1]), int(sys.argv[3]))))

    if sys.argv[2] == "*":
        print("{} {} {} = {}".format(sys.argv[1], sys.argv[2], sys.argv[3], calc.mul(int(sys.argv[1]), int(sys.argv[3]))))

    if sys.argv[2] == "/":
        print("{} {} {} = {}".format(sys.argv[1], sys.argv[2], sys.argv[3], calc.div(int(sys.argv[1]), int(sys.argv[3]))))
