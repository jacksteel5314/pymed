#!/usr/bin/python3

import socket
import argparse

def make_request(hostname, port, verb):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Connect to the server
        s.connect((hostname, port))

        # send MIRO
        print("Sending MIRO...")

        s.sendall(b'MIRO')
        s.sendall(b'\0')
        s.sendall(b'\000\000\000\0')

            
        # Receive and print 16 bytes
        resp_data = s.recv(16)
        print(f"Command Generated: {b'MIRO'.hex(' ')} {verb.to_bytes(2, byteorder='big').hex(' ')} {b'0000000000'.hex(' ')}")
        print(f"Response Received: {resp_data.hex(' ')}")
        print(f"Got: Response({resp_data[4]})")
        
if __name__ == "__main__":
    # Create argument parser
    parser = argparse.ArgumentParser(description="Example client: send 'MIRO', expect 'SLAV'.")

    # Add arguments
    parser.add_argument("hostname", type=str, help="Hostname or IP address")
    parser.add_argument("port", type=int, help="Port number")
    parser.add_argument("verb", type=int, help = "Verb number")

    # Parse arguments
    args = parser.parse_args()

    # Call make_request function with provided arguments
    make_request(args.hostname, args.port, args.verb)
    
