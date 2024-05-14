#!/usr/bin/python3

result = 0

for i in range(1, 4):
    try:
        if i > a:
            raise Exception('Too far')
        else:
            result += (b ** a) / i
    except Exception:
        result += a + b