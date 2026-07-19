import getpass
import telnetlib

HOST = "192.168.171.11"
user = input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.write(b"cisco\n")
tn.write(b"conf t\n")

# Loop para crear VLANs 2 a 6
for vlan_id in range(2, 7):
    vlan_name = f"python_vlan_{vlan_id}"
    tn.write(f"vlan {vlan_id}\n".encode('ascii'))
    tn.write(f"name {vlan_name}\n".encode('ascii'))

# Configuración de interfaz de loopback como ejemplo
tn.write(b"int loop 0\n")
tn.write(b"ip address 2.2.2.2 255.255.255.0\n")

tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
