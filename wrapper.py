import os
import platform
import subprocess
import yaml
from snakemake.script import snakemake
# Load config file path

def linux_copy():
    # TO-DO -> check for rsync version

    palce ='place'

def windows_copy(source, base, options, required_dependencies, log = '/LOG+:logs/robocopy.log'):
    place = 'place'
    robocopy_cmd = [
        'robocopy',
        source,
        base,
        # * Points to list contents instead of list itself
        *options,
        log,
        *required_dependencies

    ]

    print(f"Copying required items from {source} to {base} using robocopy...")
    try:
        result = subprocess.run(robocopy_cmd, capture_output=True, text=True)
        if result.returncode <= 7:
            print("Successfully copied required items.")
        else:
            print(f"Robocopy reported errors: {result.stdout}")
    except Exception as e:
        print(f"Exception during robocopy execution: {e}")
    
    return


# Extract source and destination

# Extract copy options

# Execute copy process

def main():
    config_file = snakemake.params.get('config_path')
    # Extract source and destination
    source = snakemake.config['network_source']
    options = snakemake.config['options', []]
    base_dir = snakemake.config['base_dir']
    required_dirs = snakemake.config['required_dirs', []]
    required_files = snakemake.config['required_files', []]

    # Check for os
    my_platform = platform.system()

    if my_platform == 'Linux':
    # Check if rsync package is installed
        test = 'test'
    elif my_platform == 'Windows':
        
        windows_copy(source, base_dir, options, required_files)

        for dir in required_dirs:
            windows_copy(source, base_dir, options, dir)
    else:
        print("\n Your system is not supported")


if __name__ == '__main__':
    main()
