


with open("show_version.txt", "r") as f:
    output = f.read().splitlines()

for line in output:
    if "Processor board ID" in line:
        serial_number = line.split("Processor board ID ")
print(f"\nSN is : {serial_number[1]}\n")
