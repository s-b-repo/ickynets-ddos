import time
import threading
import socket
import asyncio
import sys

urlset = input("Enter the site or ip =): ")
proxynames = input("Enter the proxy list name" "proxy.txt""): ")

null = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Content-Length': '0' * 1000000
}




# Function to display the menu and handle user input
print("Payload Menu:")
print("1. null")
print("2. Payload 2")
print("3. Payload 3")
print("4. Payload 4")
print("5. Payload 5")
print("6. Payload 6")
print("7. Payload 7")
print("8. Payload 8")
print("9. Payload 9")
print("10. Payload 10")

# Ask for user input
user_input = input("Enter the payload number you want or 'custom' for a custom payload: ")

# Check if the user wants a custom payload
if user_input.lower() == 'custom':
    custom_payload = input("Enter your custom payload: ")
    selected_payload = custom_payload
else:
    # Create a dictionary to simulate switch-case
    payload_mapping = {
        '1': 'null',
        '2': 'Payload 2',
        '3': 'Payload 3',
        '4': 'Payload 4',
        '5': 'Payload 5',
        '6': 'Payload 6',
        '7': 'Payload 7',
        '8': 'Payload 8',
        '9': 'Payload 9',
        '10': 'Payload 10'
    }

    # Use the dictionary to get the corresponding payload
    selected_payload = payload_mapping.get(user_input, "Invalid payload")

# Print the result
print(f"The selected payload is: {selected_payload}")

ftp = {'21'}
ssh = {'22'}
telnet = {'23'}
dns = {'53'}
http = {'80'}
https = {'443'}
rdp = {'3389'}

# Function to display the menu and handle user input
print("port Menu:")
print("1. port21 ftp")
print("2. port22 ssh")
print("3. port23 telnet")
print("4. port43 dns")
print("5. port80 http")
print("6. port443 https")
print("7. port3389 rdp")

# Ask for user input
user_input = input("Enter the port number you want or 'custom' for a custom port number: ")

# Check if the user wants a custom port
if user_input.lower() == 'custom':
    custom_payload = input("Enter your custom port: ")
    selected_port = custom_port
else:
    # Create a dictionary to simulate switch-case
    port_mapping = {
        '1': 'ftp',
        '2': 'ssh',
        '3': 'telnet',
        '4': 'dns',
        '5': 'http',
        '6': 'https',
        '7': 'rdp',
    }

    # Use the dictionary to get the corresponding port
    selected_port = port_mapping.get(user_input, "Invalid port")

# Print the result
print(f"The selected proxy type is: {selected_proxy}")

http = {'http'}
sock4 = {'socks4'}
sock5 = {'socks5'}

# Function to display the menu and handle user input
print("proxy Menu:")
print("1. http")
print("2. socks4")
print("3. socks5 ")


# Ask for user input
user_input = input("Enter the proxy  you want or 'custom' for a custom proxy: ")

# Check if the user wants a custom proxy
if user_input.lower() == 'custom':
    custom_payload = input("Enter your custom proxy: ")
    selected_port = custom_port
else:
    # Create a dictionary to simulate switch-case
    port_mapping = {
        '1': 'http',
        '2': 'socks4',
        '3': 'socks5'
    }

    # Use the dictionary to get the corresponding proxy
    selected_port = port_mapping.get(user_input, "Invalid proxy")

# Print the result
print(f"The selected proxy is: {selected_proxy}")




async def replace_and_run(original_program_path, replacements):
    with open(original_program_path, 'r') as file:
        original_program = file.read()

    # Replace the variables with the desired values
    modified_program = original_program
    for variable_name, replacement_value in replacements.items():
        modified_program = modified_program.replace(variable_name, str(replacement_value))

    # Write the modified program to a temporary file
    temp_file_path = '/temp_program.py'
    with open(temp_file_path, 'w') as file:
        file.write(modified_program)

    # Execute the modified program asynchronously
    process = await asyncio.create_subprocess_exec(sys.executable, temp_file_path)
    await process.communicate()

# Entry point of the program
if __name__ == "__main__":
    replacements = {
        "https://example.com": selected_sock,
        "payload": custom_payload,
        "socks4": proxy_type_you_want_to_use,
        "portnumber": selected_port,
       "proxies.txt": proxynames
    }
    asyncio.run(replace_and_run('/zerohandler.py', replacements))
