import os
from config import *

def get_file_content(working_directory, file_path):
    working_directory_abs = os.path.abspath(working_directory)
    abs_path = os.path.abspath(os.path.join(working_directory, file_path))

    # keep LLM within limits
    if not abs_path.startswith(working_directory_abs):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working file_path'

    # if not a file
    if not os.path.isfile(abs_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        text = get_text(abs_path)
        if len(text) >= CHAR_LIMIT:
            text += f'\n[...File "{file_path}" truncated at 10000 characters]'

        return text

    except Exception as e:
        return f"Error listing files: {e}"


def get_text(path):
    with open(path) as f:
        return f.read(CHAR_LIMIT)