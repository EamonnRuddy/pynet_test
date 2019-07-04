from pprint import pprint

def open_file(filename):
    with open(filename) as f:
        return f.read()

def parse_list(ip_brief):
        my_dict = {}
        my_dict1 = {}
        for line in ip_brief.splitlines():
            if "Protocol" in line:
                continue
            else:
                name, ip, _, mac, _, _ = line.split()
                my_dict1.update({ip:mac})
                my_dict.update({mac:ip})
        print("IP Address to Mac mapping")
        print("--"*20)
        pprint(my_dict1)
        print("\n")
        print("Mac to IP address mapping")
        print("--"*20)
        pprint(my_dict)



filename = "show_arp.txt"
data = open_file(filename)
print(data)
headers = parse_list(data)
            
