import getpass
import telnetlib

user = input("Enter your remote account: ")
password = getpass.getpass("Enter your login password: ")
enable_password = getpass.getpass("Enter your enable password: ")

with open('myswitches') as f:
    for IP in f:
        HOST = IP.strip()
        print("Configuring Switch " + HOST)

        try:
            tn = telnetlib.Telnet(HOST, timeout=10)  # timeout evita bloqueos largos
            tn.read_until(b"Username: ")
            tn.write(user.encode('ascii') + b"\n")

            if password:
                tn.read_until(b"Password: ")
                tn.write(password.encode('ascii') + b"\n")

            tn.write(b"enable\n")
            tn.write(enable_password.encode('ascii') + b"\n")
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

        except Exception as e:
            print(f"❌ Error al conectar con {HOST}: {e}")
