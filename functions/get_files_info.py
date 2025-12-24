import os

def get_files_info(working_directory, directory="."):
    working_abs_path = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_abs_path, directory))

    valid_target_dir = os.path.commonpath([working_abs_path, target_dir]) == working_abs_path

    if not valid_target_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'
    
    dir_contents = []
    try:
        for file in os.listdir(target_dir):
            target_loc = os.path.join(target_dir, file)
            dir_contents.append(f"- {file}: file_size={os.path.getsize(target_loc)} bytes, is_dir={os.path.isdir(target_loc)}")
    except Exception as e:
        return "Error: Listing operation went wrong"
    
    return "\n".join(dir_contents)
