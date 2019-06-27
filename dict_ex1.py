


network_device = {
    "ip_addr": "1.1.1.1",
    "user": "bob",
    "password": "pass",
    "vendor": "cisco",
    "model": "isr4k"
    }

for item in network_device:
    print(f"{item} : {network_device[item]}")

network_device.update(password = "hello", secret = "what")

try:
    network_device.get(device_type)
except NameError:
    print("Default value is cisco_ios")
