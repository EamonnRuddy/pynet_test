
def func_1(filename):
    with open(filename, "r") as f:
        output = f.read().splitlines()
    return output

def func_2(txt):
    for line in txt:
        if "Processor board ID" in line:
            serial_number = line.split("Processor board ID ")
    return serial_number[1]

def func_vendor(txt):
    for line in txt:
        if "processor" in line:
            vendor = line.split(" ")
    return vendor[0]

def func_model(txt):
    for line in txt:
        if "processor" in line:
            model = line.split(" ")
    return model[1]

def func_os(txt):
    for line in txt:
        if "System image file is" in line:
            _, os = line.split(":")
    return os

def func_uptime(txt):
    for line in txt:
        if "uptime is" in line:
            _, uptime = line.split("is ")
    return uptime


txt = func_1("show_version.txt")
network_device = {}
print()
network_device["serial_no"] = func_2(txt)
network_device["vendor"] = func_vendor(txt)
network_device["model"] = func_model(txt)
network_device["os"] = func_os(txt)
network_device["uptime"] = func_uptime(txt)

print(network_device)
print()
