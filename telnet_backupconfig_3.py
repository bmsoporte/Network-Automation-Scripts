import getpass
import telnetlib
import time

user = input("Enter your remote account: ")
password = getpass.getpass("Enter your login password: ")
enable_password = getpass.getpass("Enter your enable password: ")

with open('myswitches') as f:
    for IP in f:
        HOST = IP.strip()
        print("Respaldando configs en " + HOST)

        try:
            tn = telnetlib.Telnet(HOST, timeout=10)

            # Detectar si pide usuario o solo contraseña
            idx, match, text = tn.expect(
                [b"Username", b"User", b"Password", b">", b"#"],
                timeout=5
            )

            # Si pide usuario
            if idx in [0, 1]:
                tn.write(user.encode('ascii') + b"\n")
                tn.expect([b"Password", b"password"], timeout=5)
                tn.write(password.encode('ascii') + b"\n")

            # Si pide solo contraseña
            elif idx == 2:
                tn.write(password.encode('ascii') + b"\n")

            # Detectar prompt EXEC o PRIVILEGED
            idx, match, text = tn.expect([b">", b"#"], timeout=5)

            # Si estamos en modo EXEC (SW1>)
            if idx == 0:
                tn.write(b"enable\n")
                tn.expect([b"Password", b"password"], timeout=5)
                tn.write(enable_password.encode('ascii') + b"\n")
                tn.expect([b"#"], timeout=5)

            # Ya estamos en modo privilegiado
            tn.write(b"terminal length 0\n")
            tn.expect([b"#"], timeout=5)

            tn.write(b"show running-config\n")
            time.sleep(2)
            tn.write(b"exit\n")

            readoutput = tn.read_all().decode('ascii', errors='ignore')

            with open(f"switch_{HOST}.txt", "w") as saveoutput:
                saveoutput.write(readoutput)

        except Exception as e:
            print(f"❌ Error al conectar con {HOST}: {e}")
