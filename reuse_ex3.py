from pprint import pprint

def open_file(filename):
    with open(filename) as f:
        return f.read()

def parse_list(ip_brief):
        my_dict = {}
        my_dict1 = {}
        ip_addr = ""
        status = ""
        line_protocol = ""
        for line in ip_brief.splitlines():
            if "Interface" in line:
                _, ip_addr, _, _, status, line_protocol = line.split()
            else:
                name, ip, _, _, stat, operation = line.split()
                my_dict1 = ({ip_addr:ip, line_protocol:operation, status:stat})
                my_dict.update({name:my_dict1})
        return my_dict



filename = "show_ip_int_brief.txt"
data = open_file(filename)
print(data)
headers = parse_list(data)
pprint(headers)
            
