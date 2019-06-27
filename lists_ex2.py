

ip = input("Enter an Ip Address: ")

ip = ip.split(".")

ip[-1] = 0


binary_list = []
for string in ip:
    binary_list.append(bin(int(string)))
print(f"The Ip address is: {ip}")
print(f"In Binary this is: {binary_list}")
