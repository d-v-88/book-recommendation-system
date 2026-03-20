# Here the constant folder is used to get the file path of the yaml file. Also this won't change as the name says constant it will be constant

# In constant when we feel that a folder or file path wont change so we can place it in constant

# Here i am not hard coding the variable as well. so if in future i want top change the folder or file name i will change it from her and it will reflect in the folder/file name as well. This is called Modular coding.

# So this is like a templete we don't need to change all the code everywhere we make the templete and change in the templete itself 

import os
ROOT_DIR = os.getcwd()
# Main config file path
CONFIG_FOLDER_NAME = "config"
CONFIG_FILE_NAME = "config.yaml"
CONFIG_FILE_PATH = os.path.join(ROOT_DIR,CONFIG_FOLDER_NAME,CONFIG_FILE_NAME)