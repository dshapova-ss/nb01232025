import shutil
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

# Use user directory as a base to ensure OS compatibility
base_dir = Path.home() / "automation_test"
source_path = base_dir / "source"
destination_path = base_dir / "destiny"

# Create source directory and some files for demonstration purposes
source_path.mkdir(parents=True, exist_ok=True)
(destination_path).mkdir(parents=True, exist_ok=True)

shutil.copytree(
    source_path,
    destination_path,
    dirs_exist_ok=True
)

# Program result without sensitive info 
base_dir_str = str(base_dir).replace(str(Path.home()), "~")
logging.info(f"Files copied successfully from {source_path} to {destination_path}.")
