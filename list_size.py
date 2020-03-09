"""Demonstration that adding something to a list doesn't always increase the size of a list."""

import sys
x = []
sizes = {len(x): sys.getsizeof(x)}

for i in range(0, 100):
    x.append(1)
    # sizes.append(sys.getsizeof(x))
    sizes[len(x)] = sys.getsizeof(x)

for pair in sizes:
    print(f"X has length {pair} and a size of {sizes[pair]}")
