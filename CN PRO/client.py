import socket

server_ip = '127.0.0.1'
server_port = 12345

udp_header_fields = [
    "Source Port",
    "Destination Port",
    "Length",
    "Checksum",
    "Data"
]
print("---------------UDP Packet Structure---------------------")
print("UDP header fields:")
for i, field in enumerate(udp_header_fields, start=1):
    print(f"{i}. {field}")
print(f"{len(udp_header_fields) + 1}. Structure")

while True:
    user_choice = input("Enter number to retrieve information ('0' to exit): ")

    if user_choice == '0':
        break

    elif user_choice.isdigit() and 1 <= int(user_choice) <= len(udp_header_fields):

        field_index = int(user_choice) - 1
        user_input = udp_header_fields[field_index]

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client_socket.sendto(user_input.encode(), (server_ip, server_port))

        data, _ = client_socket.recvfrom(4096)
        print(f"'{user_input}': {data.decode()}")

        client_socket.close()

    elif user_choice == str(len(udp_header_fields) + 1):
        user_input = 'Structure'

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client_socket.sendto(user_input.encode(), (server_ip, server_port))

        data, _ = client_socket.recvfrom(4096)
        print(data.decode())

        client_socket.close()
    else:
        print("Invalid input. Please enter a valid number...")
