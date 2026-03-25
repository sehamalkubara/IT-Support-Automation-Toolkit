import os

host = "8.8.8.8"
print("Testing Connectivity to Google DNS...")

response = os.system(f"ping -n 4 {host}")

if response == 0:
    print("Network is reachable.")
else:
    print("Network issue detected.")
