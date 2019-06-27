


ip_address = input("Enter a IP Address: ")
octects = ip_address.split(".")
octects[-1] = 0

binary_list = []
for item in octects:
    binary_list.append(bin(int(item)))



print("{:12} {:12} {:12} {:12}".format(octects[0], octects[1], octects[2], octects[3]))
print("{:12} {:12} {:12} {:12}".format(binary_list[0], binary_list[1], binary_list[2], binary_list[3]))
