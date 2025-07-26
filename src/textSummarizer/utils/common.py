import os 
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from beartype import beartype
from box import ConfigBox
from pathlib import Path
from typing import Any



@beartype
def read_yaml(path_to_yaml: Path) -> ConfigBox:
     
    """
    Reads a YAML file and returns its content as a ConfigBox object.
    
    Args:
        path_to_yaml (Path): Path to the YAML file.
        
    Raises:
        FileNotFoundError: If the YAML file does not exist. 
        ValueError: If the content of the YAML file is not valid.
        BoxValueError: If the content of the YAML file cannot be converted to a ConfigBox.

    Returns:
        ConfigBox: Content of the YAML file as a ConfigBox object.
    """
    
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file {path_to_yaml} read successfully.")
            return ConfigBox(content)
    except FileNotFoundError as e:
        logger.error(f"YAML file not found: {e}")
        raise
    except BoxValueError :
        raise ValueError(f"Content of the YAML file {path_to_yaml} is not valid.")
    except Exception as e:
        logger.error(f"An error occurred while reading the YAML file: {e}")
        raise e 
    
@beartype
def create_directories(paths: list[Path], verbose = True):
    """
    Creates directories if they do not exist.
    
    Args:
        paths (list[Path]): List of directory paths to create.
        
    Raises:
        Exception: If an error occurs while creating the directories.
    """
    
    for path in paths:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory: {path}")


@beartype
def get_size(path: Path) -> str:
    """
    Returns the size of a file or directory in a human-readable format.
    
    Args:
        path (Path): Path to the file or directory.
        
    Returns:
        str: Size of the file or directory in a human-readable format.
    """
    
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"{size_in_kb} KB" if size_in_kb > 0 else "0 KB"