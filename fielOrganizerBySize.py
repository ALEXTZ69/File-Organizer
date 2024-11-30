import os
import shutil

size_categories = {
    "Tiny": 1 * 1024,  # Up to 1 KB
    "Small": 10 * 1024,  # Up to 10 KB
    "Medium": 100 * 1024,  # Up to 100 KB
    "Large": 1 * 1024 * 1024,  # Up to 1 MB
    "Huge": 10 * 1024 * 1024,  # Up to 10 MB
    "Gigantic": 100 * 1024 * 1024,  # Up to 100 MB
    "Massive": 1 * 1024 * 1024 * 1024,  # Up to 1 GB
    "Enormous": float('inf')  # Larger than 1 GB
}

def get_size_category(size):
    for category, max_size in size_categories.items():
        if size <= max_size:
            return category
    return "Enormous"

def organize_files_by_size(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_size = os.path.getsize(file_path)
            size_category = get_size_category(file_size)
            
            # Create the folder for the size category
            folder_path = os.path.join(directory, size_category)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            
            # Move the file to the appropriate folder
            shutil.move(file_path, os.path.join(folder_path, filename))

if __name__ == "__main__":
    # Specify the Downloads folder
    my_folder = os.path.expanduser("~/Downloads")
    organize_files_by_size(my_folder)
    
    # Example of how to apply the script to another path
    # my_folder = "/path/to/another/folder"
    # organize_files_by_size(my_folder)