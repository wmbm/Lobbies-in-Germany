import os
from datetime import datetime
import glob

def setup_folders(data_dir, base_directory = 'lobby_germany/PDFs/', clear_all=False):
    """
    Create directory structure for organizing petition data.

    Parameters:
    data_dir (str): The root directory where the data folders will be created.
    base_directory (str, optional): The base directory name (default is 'petitions_website/').
    state (str, optional): The state or category name to append to the base directory (default is 'all').
    clear_all (bool): Remove previously downloaded files

    Returns:
    str: The path to the created data directory.
    """

    # Create child directory
    data_path = os.path.join(data_dir, base_directory)
    if not os.path.exists(data_path):
        os.makedirs(data_path)
    
    # Get current date
    current_date = datetime.today().strftime('%Y-%m-%d')
    
    directory = base_directory + current_date + '/'
    data_path = os.path.join(data_dir, directory)
    if not os.path.exists(data_path):
        os.mkdir(data_path)

    if clear_all:
        files = glob.glob(data_path + '/*')
        for f in files:
            os.remove(f)
    return data_path