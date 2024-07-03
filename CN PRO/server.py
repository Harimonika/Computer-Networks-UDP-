import socket 

udp_struct = (
    "<______________________________32 bits______________________________>\n"
    "--------------------------------------------------------------------\n"
    "|        Source Port (16)        |       Destination Port (16)      |\n"
    "--------------------------------------------------------------------\n"
    "|            Length (16)         |           Checksum (16)          |\n"
    "--------------------------------------------------------------------\n"
    "|                               Data                                |\n"
    "--------------------------------------------------------------------"
)

udp_header = {
    "Source Port": "A 16-bit field that identifies the sender's port number.",
    "Destination Port": "A 16-bit field that identifies the recipient's port number.",
    "Length": "A 16-bit field that specifies the length of the UDP datagram, including header and data.",
    "Checksum": "A 16-bit field used for error checking, ensuring data integrity during transmission.",
    "Data": "The actual data being transmitted in the UDP datagram."
}

# Set up the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('0.0.0.0', 12345))  

print("Server is ready to receive request...")

while True:
    data, client_address = server_socket.recvfrom(1024)
    data = data.decode()

    if data == 'Structure':
        print("Sending UDP structure information to the client...")
        server_socket.sendto(udp_struct.encode(), client_address)

    elif data in udp_header:
        print(f"Sending information about '{data}' to the client...")
        server_socket.sendto(udp_header[data].encode(), client_address)
