import os

def write_file(working_directory, file_path, content):

    working_directory_abs = os.path.abspath(working_directory)
    abs_path = os.path.abspath(os.path.join(working_directory, file_path))

    # keep LLM within limits
    if not abs_path.startswith(working_directory_abs):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'


    # if not dir, make dir
    if not os.path.exists(abs_path):
        try:
            # print("no file")
            os.makedirs(os.path.dirname(abs_path), exist_ok=True)

        except Exception as e:
            return f"Error: creating directory: {e}"

    # if writing to a dir, not a file
    if os.path.exists(abs_path) and os.path.isdir(abs_path):
        return f'Error: "{file_path}" is a directory, not a file'

    # create / open file and write
    try: 
        with open(abs_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: writing to a file: {e}"
    