

class network_device:
    def __init__(self, ip_addr, username, password):
        self.ip_addr = ip_addr
        self.username = username
        self.password = password
        self.serial_number = ''
        self.model = ''
        self.vendor = ''
        self.uptime = ''
        self.os_version = ''

device1 = network_device(ip_addr = '1.1.1.1', username='admin1', password='pwd1')
device2 = network_device(ip_addr = '2.1.1.1', username='admin2', password='pwd2')
device3 = network_device(ip_addr = '3.1.1.1', username='admin3', password='pwd3')

print(f"Device1 has the following attributes:\n IP address: {device1.ip_addr}\n {device1.username}\n {device1.password} ")
