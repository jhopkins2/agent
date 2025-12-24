import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    try: 
        working_abs_path = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_abs_path, file_path))

        valid_target_file = os.path.commonpath([working_abs_path, target_file]) == working_abs_path

        if not valid_target_file:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
        if not os.path.isfile(file_path):
            f'Error: File not found or is not a regular file: "{file_path}"'

        with open(target_file, "r") as f:
            content = f.read(MAX_CHARS)
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
    except Exception as e:
        return f"Reading file={file_path} Error: {e}"

    return content

