#!/usr/bin/env python


with open("/home/student11/pynet_test/file.txt") as f:
    file = f.read()
    print(file)

with open("new_file.txt", "w") as f:
    f.write(file)

with open("new_file.txt", "a") as f:
    f.write("something\n")
print()

