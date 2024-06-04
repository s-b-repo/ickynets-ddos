import time
import threading
import socket
import asyncio
import sys

urlset = input("Enter the site or ip =): ")
proxynames = input("Enter the proxy list name" "proxy.txt""): ")

# Function to display the menu and handle user input
async def payload():
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
user_input = input("Enter the payload you want or 'custom' for a custom payload: ")

# Check if the user wants a custom port
if user_input.lower() == 'custom':
    custom_port = input("Enter your custom payload: ")
    selected_port = custom_payload
else:
    # Create a dictionary to simulate switch-case
    port_mapping = {
 '"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",    "Content-Length": "0" * 1000000': null,
        '22': payload,
        '23': payload,
        '80': payload,
        '443': payload
    }

    # Use the dictionary to get the corresponding port
    selected_payload = port_mapping.get(user_input, "Invalid payload")

# Print the result
print(f"The selected port is: {selected_payload}")


# Define the ports as variables
port21 = '21'
port22 = '22'
port23 = '23'
port80 = '80'
port443 = '443'

# Ask for user input
user_input = input("Enter the port you want or 'custom' for a custom port: ")

# Check if the user wants a custom port
if user_input.lower() == 'custom':
    custom_port = input("Enter your custom port number: ")
    selected_port = custom_port
else:
    # Create a dictionary to simulate switch-case
    port_mapping = {
        '21': port21,
        '22': port22,
        '23': port23,
        '80': port80,
        '443': port443
    }

    # Use the dictionary to get the corresponding port
    selected_port = port_mapping.get(user_input, "Invalid port")

# Print the result
print(f"The selected port is: {selected_port}")




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
        "portnumber": selected_port,
       "proxies.txt": proxynames
    }
    asyncio.run(replace_and_run('/program.py', replacements))
