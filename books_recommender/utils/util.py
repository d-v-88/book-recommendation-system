# This function is used to read a YAML configuration file and convert it into a Python dictionary, while also handling errors using a custom exception class.

# This function is written to make the project organized, flexible, and easier to maintain. In professional projects (especially ML or backend systems), developers avoid hard-coding settings inside Python files. Instead, they store them in YAML configuration files and read them using a function like this.

# During experiments, ML engineers keep changing things to get the most accurate systems 

# Instead of changing Python code every time, they just edit the YAML file.

# In Machine Learning, we try many different values to find the best model.

import yaml
import sys
from books_recommender.exception.exception_handler import AppException



def read_yaml_file(file_path:str)->dict:
    """
    Reads a YAML file and returns the contents as a dictionary.
    file_path: str
    """
    try:
        with open(file_path, 'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise AppException(e,sys) from e