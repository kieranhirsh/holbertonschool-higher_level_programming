#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    import calculator_1 as calc

    if len(sys.argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)
    
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    match sys.argv[2]:
        case "+":
            print("{} {} {} = {}".format(a, sys.argv[2], b, calc.add(a, b)))
        case "-":
            print("{} {} {} = {}".format(a, sys.argv[2], b, calc.sub(a, b)))
        case "*":
            print("{} {} {} = {}".format(a, sys.argv[2], b, calc.mul(a, b)))
        case "/":
            print("{} {} {} = {}".format(a, sys.argv[2], b, calc.div(a, b)))
        case _:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
