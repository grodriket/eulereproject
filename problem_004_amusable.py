#! /usr/bin/env python3.3

# Authors: AmusableLemur
# Complexity: O(bad)
# Output: 906609

from math import sqrt

number = 0

# Could possibly avoid checking duplicates here
for i in xrange(100, 999):
	for j in xrange(100, 999):
		n = i * j

		if str(n) == str(n)[::-1] and n > number:
			number = n

print(number)