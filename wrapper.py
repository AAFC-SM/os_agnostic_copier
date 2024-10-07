import os
import subprocess
import yaml
from snakemake.script import snakemake
# Load config file path
config_file = snakemake.params.get('config_path')

with open(config_file, 'r') as file:
    config = yaml.load(file)


# Extract source and destination

# Detect os

# Execute copy process
