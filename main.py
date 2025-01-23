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

shutil.copytree(
    Path(input("Enter the source folder path: ")).resolve(),
    Path(input("Enter the destination folder path: ")).resolve()
)

logging.info("Files copied successfully.")
