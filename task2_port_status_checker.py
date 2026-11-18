import socket

host = input("Enter system IP address or hostname (example: scanme.nmap.org): ")
port = int(input("Enter port number (1-65535): "))

if not 1 <= port <= 65535:
    print("Invalid port number.")
else:
    try:
        result = socket.create_connection((host, port), timeout=3)
        result.close()
        print(f"Port {port} on {host} is OPEN.")
    except (socket.timeout, ConnectionRefusedError, OSError):
        print(f"Port {port} on {host} is CLOSED or unreachable.")
