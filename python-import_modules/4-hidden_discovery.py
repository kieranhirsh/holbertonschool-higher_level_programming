#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    to_print = dir(hidden_4)

    for i in range(len(to_print)):
        if to_print[i][0] != "_" or to_print[i][1] != "_":
            print(to_print[i])
