import shutil
import os
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

source_path = Path("/home/runner/work/nb01232025/nb01232025").resolve()
destination_path = Path("/home/runner/work/nb01232025").resolve()

shutil.copytree(
    source_path,
    destination_path
)

logging.info(f"Files copied successfully from {source_path} to {destination_path}.")
