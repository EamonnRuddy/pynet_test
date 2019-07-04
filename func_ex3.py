
def func_1(filename):
    with open(filename, "r") as f:
        output = f.read().splitlines()
    return output

def func_2(txt):
    for line in txt:
        if "Processor board ID" in line:
            serial_number = line.split("Processor board ID ")
    return serial_number[1]


txt = func_1("show_version.txt")
#print(f"Text string is: {txt}")
print()
serial_no = func_2(txt)
print(f"Serial Number is : {serial_no}" )
