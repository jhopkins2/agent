import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    try:
        working_abs_path = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_abs_path, file_path))

        valid_file_directory = os.path.commonpath([working_abs_path, target_file]) == working_abs_path

        if not valid_file_directory:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not target_file.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        
        command = ["python", target_file]

        if args:
            command.extend(args)
        
        result = subprocess.run(command, capture_output=True, text=True, timeout=30, cwd=working_abs_path)

        output = ""
        if result.returncode != 0:
            output = output + f"Process exited with code {result.returncode}\n"

        if not result.stdout and not result.stderr:
            output = output + "No output produced\n"
        
        if result.stdout:
            output = output + f"STDOUT: {result.stdout}\n"
        
        if result.stderr:
            output = output + f"STDERR: {result.stderr}\n"

    except Exception as e:
        return f"Error: executing Python file: {e}"

    return output
        
