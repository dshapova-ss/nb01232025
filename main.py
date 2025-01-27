import shutil
from pathlib import Path
import logging
import os

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

# Define paths and vars
base_dir = Path.home() / "automation_test"
source_path = base_dir / "source"
destination_path = base_dir / "destiny"

# Create source directory
source_path.mkdir(parents=True, exist_ok=True)

# Create a text file with "hello nebo mentor!" content
(txt_file := source_path / "nebo_text.txt").write_text("hello nebo mentor!")

# Ensure destination directory exists
destination_path.mkdir(parents=True, exist_ok=True)

logging.info("checking directories before copytree")
contents = os.listdir(destination_path)
logging.info(contents)
logging.info("end of directory")

# Copy source directory contents to destination directory
shutil.copytree(source_path, destination_path, dirs_exist_ok=True)

#checking directory after
logging.info("checking directories after copytree")
contents = os.listdir(destination_path)
logging.info(contents)
logging.info("end of directory")

logging.info(f"Files copied successfully from {source_path} to {destination_path}.")
