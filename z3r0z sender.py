import asyncio
import threading
import socket
import sys

async def replace_and_run(original_program_path, variable_name, replacement_value):
    with open(original_program_path, 'r') as file:
        original_program = file.read()

    # Replace the variable with the desired value
    modified_program = original_program.replace(variable_name, str(replacement_value))

    # Write the modified program to a temporary file
    temp_file_path = '/temp_program.py'
    with open(temp_file_path, 'w') as file:
        file.write(modified_program)

    # Execute the modified program asynchronously
    process = await asyncio.create_subprocess_exec(sys.executable, temp_file_path)
    await process.communicate()

# Example usage:
asyncio.run(replace_and_run('path/to/program.py', 'variable_name', 'replacement_value', 'variable_name', 'replacement_value', 'variable_name', 'replacement_value', 'variable_name', 'replacement_value'))
#
