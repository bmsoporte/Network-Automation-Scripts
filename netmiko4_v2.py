from netmiko import ConnectHandler, NetmikoTimeoutException, NetmikoAuthenticationException

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

Layer3_devices = [iosv_l3_R1]

for devices in Layer3_devices:
    try:
        net_connect = ConnectHandler(**devices)
        output = net_connect.send_config_set(lines)
        print(output)
    except (NetmikoTimeoutException, NetmikoAuthenticationException) as e:
        print(f"Ocurrio un error al conectarse al dispositivo {devices['ip']}: {e}")

with open('iosv_l2_cisco_design') as f:
    lines = f.read().splitlines()
    print(lines)

Layer2_devices = [iosv_l2_S2, iosv_l2_S3]

for devices in Layer2_devices:
    try:
        net_connect = ConnectHandler(**devices)
        output = net_connect.send_config_set(lines)
        print(output)
    except (NetmikoTimeoutException, NetmikoAuthenticationException) as e:
        print(f"Ocurrio un error al conectarse al dispositivo {devices['ip']}: {e}")