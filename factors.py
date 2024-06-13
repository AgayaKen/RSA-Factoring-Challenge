#!/usr/bin/env python3

import sys

def factorize(n):
    factors = []
    for i in range(2, n // 2 + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    return factors

def main():
    if len(sys.argv) != 2:
        print("Usage: {} <file>".format(sys.argv[0]))
        sys.exit(1)

    input_file = sys.argv[1]

    try:
        with open(input_file, 'r') as f:
            for line in f:
                number = int(line.strip())
                factors = factorize(number)
                if len(factors) >= 2:
                    p, q = factors[0], factors[1]
                    print("{}={}*{}".format(number, p, q))
    except FileNotFoundError:
        print("File not found:", input_file)
        sys.exit(1)

if __name__ == "__main__":
    main()

