import subprocess
import requests # in global Python3
import sys

print(sys.executable)


# Find UR Public IP
response = requests.get("https://api.ipify.org?format=json")
PUBLIC_ip = response.json()["ip"]


# List interface
inter = subprocess.run(
    ["/usr/bin/tshark", "-D"],
    capture_output=True,
    text=True)

print(inter.stdout)
print()

interface = input("Enter Full Name of The interface to listen: -> ")

# start Tshark interactively
process = subprocess.Popen(
    [
        "/usr/bin/tshark",
        "-i", interface, 
        "-f", "udp", 
        "-Y", "stun.type == 0x0101 && stun.att.type == 0x0020",
        "-T", "fields", 
        "-e", "stun.att.ipv4"
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
)

for line in process.stdout:
    # Blurred your PUB_IP
    if PUBLIC_ip in line:
        print("DONT MIND ME :)")
    else:
        print(line, end="")

