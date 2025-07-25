import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    working_directory_abs = os.path.abspath(working_directory)
    abs_path = os.path.abspath(os.path.join(working_directory, file_path))

    # keep LLM within limits
    if not abs_path.startswith(working_directory_abs):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    # if path does not exist
    if not os.path.exists(abs_path):
        return f'Error: File "{file_path}" not found.'

    # if file is not .py file
    if not abs_path.endswith(".py") and not os.path.isdir(abs_path):
        return f'Error: "{file_path}" is not a Python file.'


    # run 
    try: 
        command = ['python3', abs_path] + args
        process = subprocess.run(command, capture_output = True, text = True, timeout = 30)


        output = []
        if process.stdout:
            output.append(f"STDOUT: \n{process.stdout}")

        if process.stderr:
            output.append(f"STDERR: \n{process.stderr}")
        

        if not output:
            output += "No output produced."

        # non zero return code
        if process.returncode != 0:
            output += f"Process exited with code {process.returncode}"

        return output


    except Exception as e:
        return f"Error: executing Python file: {e}"
