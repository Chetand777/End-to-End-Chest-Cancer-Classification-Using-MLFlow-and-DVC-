import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'cnnClassifier'

list_of_files = [
  ".github/workflows/.gitkeep", # to store main.yaml for cicd deployement
  f"src/{project_name}/__init__.py", # contructor helps the current folder to use as local package
  f"src/{project_name}/components/__init__.py", 
  f"src/{project_name}/utils/__init__.py",
  f"src/{project_name}/config/__init__.py",
  f"src/{project_name}/config/configuration.py",
  f"src/{project_name}/pipelines/__init__.py",
  f"src/{project_name}/entity/__init__.py",
  f"src/{project_name}/constants/__init.py",
  "config/config.yaml",
  "dvc.yaml",
  "params.yaml",
  "requirements.txt",
  "setup.py",
  "research/trials.ipynb",
  "templates/index.html"
]

for filepath in list_of_files:
  filepath = Path(filepath)
  filedir, filename = os.path.split(filepath)

  if filedir != "":
    os.makedirs(filedir, exist_ok=True)
    logging.info(f"Created directory: {filedir} for file: {filename}")

  if (not os.path.exists(filepath)) or (os.path.getatime(filepath) == 0):
    with open(filepath, 'w') as file:
      pass
      logging.info(f"Creating empty file: {filepath}")

  else:
    logging.info(f"{filename} File already exists")

