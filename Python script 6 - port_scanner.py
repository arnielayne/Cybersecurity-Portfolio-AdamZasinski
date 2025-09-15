# This script is a simple port scanner that checks for open ports on a target IP.
# It scans ports from 1 to 1024 and tells which ones are open.

import socket  # Used to create sockets for checking ports.

target = input("Podaj adres IP do zeskanowania: ")  # Ask the user for the IP address to scan.

for port in range(1, 1025):  # Loop through ports 1 to 1024.
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP socket.
    result = sock.connect_ex((target, port))  # Try to connect to the port.
    if result == 0:  # If connection succeeds (result 0), the port is open.
        print(f"Port {port} jest otwarty")  # Print that the port is open.
    sock.close()  # Close the socket after each check.