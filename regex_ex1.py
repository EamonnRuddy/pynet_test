#!/usr/bin/env python
import re

with open("show_int_fa4.txt") as f:
    output = f.read()

patterns = {
    "Input": r"(\d+) packets input, (\d+) bytes",
    "Output": r"(\d+) packets output, (\d+) bytes",
}

for label, pattern in patterns.items():
    match = re.search(pattern, output)
    if match:
        print(f"\n{label}: ")
        print(f"Packets: {match.group(1)}")
        print(f"Bytes: {match.group(2)}\n")
