import getpass
import telnetlib

user = input("Enter your remote account: ")
password = getpass.getpass()

with open('myswitches') as f:
    for IP in f:
        IP = IP.strip()
        print("Configuring Switch " + IP)

        tn = telnetlib.Telnet(IP)
        tn.read_until(b"Username: ")
        tn.write(user.encode('ascii') + b"\n")

        if password:
            tn.read_until(b"Password: ")
            tn.write(password.encode('ascii') + b"\n")

        tn.write(b"enable\n")
        tn.write(b"cisco\n")  # Aquí podrías pedir otro input para el enable password
        tn.write(b"conf t\n")

        # Crear VLANs 2 a 6
        for vlan_id in range(2, 7):
            vlan_name = f"python_vlan_{vlan_id}"
            tn.write(f"vlan {vlan_id}\n".encode('ascii'))
            tn.write(f"name {vlan_name}\n".encode('ascii'))

        # Configuración de loopback
        tn.write(b"int loop 0\n")
        tn.write(b"ip address 2.2.2.2 255.255.255.0\n")

        tn.write(b"end\n")
        tn.write(b"exit\n")

        print(tn.read_all().decode('ascii'))
