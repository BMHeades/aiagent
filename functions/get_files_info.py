import os



def get_files_info(working_directory, directory="."):
    
    working_directory_abs = os.path.abspath(working_directory)
    abs_path = os.path.abspath(os.path.join(working_directory, directory))

    # keep LLM within limits
    if not abs_path.startswith(working_directory_abs):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    # if not a dir
    if not os.path.isdir(abs_path):
        return f'Error: "{directory}" is not a directory'
        
    try:

        contents_info = ""

        for file in os.listdir(path=abs_path):
            file_info = f"- {file}: file_size={os.path.getsize(abs_path + '/' + file)} bytes, is_dir={os.path.isdir(abs_path + '/' + file)}\n"
            contents_info += file_info

        return contents_info

    except Exception as e:
        return f"Error listing files: {e}"



