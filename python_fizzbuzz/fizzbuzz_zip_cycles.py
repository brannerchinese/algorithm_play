#!/usr/bin/env python3
# fizzbuzz_zip_cycles.py
# Following a suggestion by Josh Bronson, 20131211

from itertools import cycle

def generate_feed(n, word):
    return [''] * (n - 1) + [word]

for fizz, buzz, num in zip(
        cycle(generate_feed(3, 'Fizz')), 
        cycle(generate_feed(5, 'Buzz')), 
        range(1, 101)):
    print(fizz + buzz or num)