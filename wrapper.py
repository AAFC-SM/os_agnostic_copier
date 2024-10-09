import os
import platform
import subprocess
import yaml
from snakemake.script import snakemake
from snakemake.shell import shell

# Load config file path

def linux_copy(source, base, options, required_dependencies, log = '/LOG'):
    # TO-DO -> check for rsync version
    rsync_cmd = [
        'rsync',
        *options,
        source,
        base,
        log
    ]

def windows_copy(source, base, options, required_dependencies, log = '/LOG+:logs/copy.log'):

    options

    robocopy_cmd = [
        'robocopy',
        source,
        base,
        # * Points to list contents instead of list itself
        *options,
        log,
        *required_dependencies

    ]
    robocopy_cmd = f'robocopy {source} {base} {options} {log} {required_dependencies}'

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
    config_file = snakemake.params.get('config_path')

    # Extract from config
    source = snakemake.config['network_source']
    options = snakemake.config['options', []]
    base_dir = snakemake.config['base_dir']
    required_dirs = snakemake.config['required_dirs', []]
    required_files = snakemake.config['required_files', []]

    # Convert to single string as snakemake.shell requires
    options = " ".join(options)
    required_files = " ".join(required_files)

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
