import os
import platform
import yaml
from pathlib import Path
from snakemake.script import snakemake
from snakemake.shell import shell

# Load config file path

def linux_copy(source:str, base:str, options:str, required_dependencies:str, log = '/LOG') -> None:
    # TO-DO -> check for rsync version

    rsync_cmd = f'rsync {options} {source} {base} {required_dependencies} {log}'

    print(f"Copying required items from {source} to {base} using rsync...")
    try:
        shell(rsync_cmd)
        print("Successfully copied required items.")
    except Exception as e:
        print(f"Exception during rsync execution: {e}")
    return


def windows_copy(source:str, base:str, options:str, required_dependencies:str, log = '/log:logs/copy.log') -> None:

    robocopy_cmd = f'robocopy {source} {base} {required_dependencies} {log} {options}'
    print(robocopy_cmd)
    print(f"Copying required items from {source} to {base} using robocopy...")
    try:
        shell(robocopy_cmd)
        print("Successfully copied required items.")
    except Exception as e:
        print(f"Exception during robocopy execution: {e}")
    
    return


# Extract source and destination

# Extract copy options

# Execute copy process

def main():
    # Map copy functions to dict
    copy_functions = {
        'Linux': linux_copy,
        'Windows': windows_copy
    }

    # Extract from config
    source = Path(snakemake.config['network_source'])
    options = snakemake.config['options']
    print(options)
    base_dir = Path(snakemake.config['base_dir'])
    required_dirs = snakemake.config['required_dirs']
    required_files = snakemake.config['required_files']

    # Convert to single string as snakemake.shell requires
    options = " ".join(options)
    required_files = " ".join(required_files)

    # Do required path manipulation



    # Check for os
    my_platform = platform.system()

    # Retrieve relevant copy_func
    if my_platform in copy_functions:

        agnostic_copy = copy_functions[my_platform]
        agnostic_copy(source, base_dir, options, required_files)

        for dir in required_dirs:
            agnostic_copy(str(source/Path(dir)), str(base_dir/Path(dir)), options, required_dependencies='')
    else:
        print("\n Your system is not supported")


if __name__ == '__main__':
    main()
