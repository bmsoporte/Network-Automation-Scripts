from netmiko import ConnectHandler

iosv_l3_R1 = {
    'device_type': 'cisco_ios',
    'ip': '172.16.10.2',
    'username': 'cisco',
    'password': 'cisco'
}

iosv_l2_S2 = {
    'device_type': 'cisco_ios',
    'ip': '172.16.10.11',
    'username': 'cisco',
    'password': 'cisco'
}

iosv_l2_S3 = {
    'device_type': 'cisco_ios',
    'ip': '172.16.10.12',
    'username': 'cisco',
    'password': 'cisco'
}

with open('iosv_l3_cisco_design') as f:
    lines = f.read().splitlines()
    print(lines)

all_devices = [iosv_l3_R1]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print(output)

with open('iosv_l2_cisco_design') as f:
    lines = f.read().splitlines()
    print(lines)

all_devices = [iosv_l2_S2, iosv_l2_S3]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print(output)