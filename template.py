import os
from pathlib import Path
import logging 

logging.basicConfig(level=logging.INFO, format ='[%(asctime)s]: %(message)s')


#Project name
project_name = "textSummarizer"
# Create project files and directories structure
project_paths = [
    ".github/workflows/.gitkeep",
   f"src/{project_name}/__init__.py",
   f"src/{project_name}/components/__init__.py",
   f"src/{project_name}/utils/__init__.py",
   f"src/{project_name}/utils/common.py",
   f"src/{project_name}/logging/__init__.py",
   f"src/{project_name}/config/__init__.py",
   f"src/{project_name}/config/configuration.py",
   f"src/{project_name}/pipeline/__init__.py",
   f"src/{project_name}/entity/__init__.py",
   f"src/{project_name}/constants/__init__.py",
   "config/config.yaml",
   "params.yaml",
   "app.py",
   "requirements.txt",
   "setup.py",
   "main.py",
   "Dockerfile",
   "research/trials.ipynb"
]

for filepath in project_paths:
    filepath = Path(filepath) 
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)== 0):
        with open(filepath,'w') as f:
            pass
        logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"File already exists: {filepath}, skipping creation.") 