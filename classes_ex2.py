

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
    def print_ip(self):
        print(f"Device IP is: {self.ip_addr}")
    def user_pass(self):
        print(f"Device username: {self.username}\n Device password: {self.password}")
    def set_vendor(self, vendor):
        self.vendor = vendor
        print(f"Setting vendor to {self.vendor}")

device1 = network_device(ip_addr = '1.1.1.1', username='admin1', password='pwd1')
device2 = network_device(ip_addr = '2.1.1.1', username='admin2', password='pwd2')
device3 = network_device(ip_addr = '3.1.1.1', username='admin3', password='pwd3')

device1.print_ip()
device1.user_pass()
device1.set_vendor("Cumulus")
#print(f"Device1 has the following attributes:\n IP address: {device1.ip_addr}\n {device1.username}\n {device1.password} ")
